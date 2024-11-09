# File Name: simple_bedrock_application.py
### Location: Chapter 3
### Purpose: 
"""
    1. Bedrock Client Initialization:
        Sets up a Bedrock client (boto3_bedrock_runtime_client) for model invocation.
    2. Model Invocation:
        invoke_bedrock_model: Invokes the selected Bedrock model and returns the response, handling JSON decoding and potential client errors.
        handle_client_error: Manages AWS-specific errors, such as AccessDeniedException, showing an appropriate message.
    3. Model Response Functions:
        get_response_bedrock_claude: Invokes the Claude model, formatting parameters like temperature and top_p for inference and returns the text content.
        get_response_bedrock_titan: Similar to the Claude function but customized for the Titan model.
    4. Model Selection and Prompt Input:
        call_bedrock_function: Decides which model-specific function to call based on the selected model ID.
        get_model_id: Maps user-friendly model names to Bedrock model IDs.
    5. Streamlit User Interface (UI):
        The UI includes a title, parameter sliders (temperature, top_p, top_k, max tokens), and a text area for prompt input.
        Adds a CSS-styled vertical line for visual separation between parameter and input sections.
        Sets default prompt text for user guidance.
        Upon submitting, a loading spinner is shown while the selected model processes the prompt. The response is displayed in a large text area.
"""

import streamlit as st
import json
import boto3
import botocore

# Initialize the Bedrock client at the top
boto3_bedrock_runtime_client = boto3.client('bedrock-runtime')

def invoke_bedrock_model(body, model_id):
    """Handles the Bedrock model invocation and returns the response."""
    try:
        # Attempt to invoke the model with the specified parameters
        response = boto3_bedrock_runtime_client.invoke_model(
            body=body,
            modelId=model_id,
            accept="application/json",
            contentType="application/json"
        )
        # Process the response and decode the JSON content
        response_body = response["body"].read().decode("utf-8")
        return json.loads(response_body)
    except botocore.exceptions.ClientError as error:
        # Handle client-specific errors (e.g., permission or configuration issues)
        handle_client_error(error)

def handle_client_error(error):
    """Handles ClientError exceptions for Bedrock invocation."""
    error_code = error.response['Error'].get('Code', 'Unknown')
    if error_code == 'AccessDeniedException':
        # Display specific error message for Access Denied
        st.error(f"Access Denied: {error.response['Error'].get('Message', 'No message available')}")
    else:
        # Display a generic error message and re-raise the error for further inspection
        st.error(f"An error occurred: {error}")
        raise

def get_response_bedrock_claude(model_id, user_input_prompt, user_temperature, user_top_p, user_top_k, user_max_tokens):
    """Prepares and invokes the Claude model with the specified parameters."""
    messages_info = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": user_max_tokens,
        "temperature": user_temperature,
        "top_p": user_top_p,
        "top_k": user_top_k,
        "messages": [
            {
                "role": "user",
                "content": [{"type": "text", "text": user_input_prompt}]
            }
        ]
    }
    body = json.dumps(messages_info)
    response_json = invoke_bedrock_model(body, model_id)
    return response_json.get("content", [{}])[0].get("text", "")

def get_response_bedrock_titan(model_id, user_input_prompt, user_temperature, user_top_p, user_top_k, user_max_tokens):
    """Prepares and invokes the Titan model with the specified parameters."""
    body = json.dumps({
        "inputText": user_input_prompt,
        "textGenerationConfig": {
            "topP": user_top_p,
            "temperature": user_temperature
        }
    })
    response_json = invoke_bedrock_model(body, model_id)
    return response_json.get("results", [{}])[0].get("outputText", "")

def call_bedrock_function(model_id, user_input_prompt, user_temperature, user_top_p, user_top_k, user_max_tokens):
    """Selects the appropriate function based on the model ID."""
    if model_id == "amazon.titan-text-express-v1":
        return get_response_bedrock_titan(model_id, user_input_prompt, user_temperature, user_top_p, user_top_k, user_max_tokens)
    return get_response_bedrock_claude(model_id, user_input_prompt, user_temperature, user_top_p, user_top_k, user_max_tokens)

def get_model_id(model_name):
    """Returns the model ID based on the selected model name."""
    return "amazon.titan-text-express-v1" if model_name == "Titan Text G1 - Express v1" else "anthropic.claude-3-haiku-20240307-v1:0"

# Streamlit UI
st.title("Generative AI Streamlit Application")

# Add custom CSS for the vertical line
st.markdown(
    """
    <style>
    /* Style for vertical line */
    .vertical-line {
        border-left: 1px solid #ddd;
        height: 100%;
        margin: 0 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Default value for prompts
default_prompts = [
    """Generate a story for kids within 1000 words."""
]

# Create two columns for side-by-side layout
left, middle, right = st.columns([2, 1, 4])

# Section for parameters in the left column
with left:
    st.header("Inference parameters")
    user_temperature = st.slider("Temperature:", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
    user_top_p = st.slider("Top P:", min_value=0.0, max_value=1.0, value=0.9, step=0.1)
    user_top_k = st.slider("Top K:", min_value=1, max_value=100, value=20, step=5)
    user_max_tokens = st.slider("Max Tokens:", min_value=500, max_value=1500, value=1000, step=500)
    
# Insert a vertical line between the two columns
st.markdown('<div class="vertical-line"></div>', unsafe_allow_html=True)

# Section for model selection and prompt input in the right column
with right:
    user_input_prompt = default_prompts
    dropdown_option = st.selectbox("Choose LLM model to explore:", ["Titan Text G1 - Express v1", "Claude 3 Haiku"])
    model_id = get_model_id(dropdown_option)
    # Larger input box using st.text_area
    user_input_prompt = st.text_area("Enter your prompt: (Feel free to replace this default prompt with your own.)", value=user_input_prompt[0].strip(), height=150)

    if st.button("Submit"):
        with st.spinner("Evaluating..."):
            # Invokes the selected model and retrieves the response
            response_content = call_bedrock_function(model_id, user_input_prompt, user_temperature, user_top_p, user_top_k, user_max_tokens)
            st.text_area("Generated Output", response_content, height=250)
