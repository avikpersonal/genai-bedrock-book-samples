---

# Chapter Name: Introduction to Amazon Bedrock
##### Chapter: 19
##### Github name: genai-bedrock-book-samples
##### Folder: chapter19
##### Book Name: A Definitive Guide to Generative AI with Amazon Bedrock

---


## Prerequisite

* [AWS Console access](https://aws.amazon.com/console/)
* [IAM](https://aws.amazon.com/iam/) access role to execute AWS CloudFormation template
* [IAM](https://aws.amazon.com/iam/) access Creating Amazon SageMaker domain, Amazon SageMaker domain user, AWS Lambda, and AWS IAM roles & policies

## AWS region for implementation Amazon SageMaker domain 

us-east-1 

## Account allowlisting
To run this source code, your account must be included on the Amazon Bedrock allowlist. Please ensure that your account is activated and allowlisted before executing this source code.

---

### **Section 1**: Jupyter Notebook & GitHub
**Purpose**: Executing Jupyter Notebooks and Cloning Example Source Code.

---

Executing Jupyter Notebooks and cloning example source code enables hands-on learning and practical engagement with concepts. By running code directly, users can better understand the mechanics of each example, experiment with modifications, and troubleshoot in real time, deepening their knowledge and enhancing their skill development.

## Executing Jupyter Notebooks

1. In the AWS Management Console search bar, type **"sagemaker"**. Then, select **Amazon SageMaker**.

![Console-Home-us-east-1](../image/1_Console-Home-us-east-1.png)

2. In the Amazon SageMaker Console, click **Domains** in the left-side navigation menu.

![2_How-it-works-Amazon-SageMaker-us-east-1](../image/2_How-it-works-Amazon-SageMaker-us-east-1.png)

3. You will view **genai-bedrock-book-sagemaker-basic** as **Domain**. 

4. Click **genai-bedrock-book-sagemaker-basic** in the **Domains** section. Click **User profiles**.

![3_Domains-Amazon-SageMaker-us-east-1](../image/3_Domains-Amazon-SageMaker-us-east-1.png)

5. Click **Launch**. Click **Studio**.

![4_Domain-GenAIDomain-Domains-Amazon-SageMaker-us-east-1](../image/4_Domain-GenAIDomain-Domains-Amazon-SageMaker-us-east-1.png)

6. Wait for the **Amazon SageMaker Studio** to come online. It will take **~2-3 mins** to open **Amazon SageMaker Studio**.

![5_Creating-application-SageMaker-Studio](../image/5_Creating-application-SageMaker-Studio.png)

7. This takes you to **Amazon SageMaker Studio**. Click **Studio Clasic**.

![6a_sagenmaker_pic](../image/6a_sagenmaker_pic.png)

8. Click **Run** in the **Amazon SageMaker Studio**. 

![6b_sagemaker_pic](../image/6b_sagemaker_pic.png)

9. Click **Open** in the **Amazon SageMaker Studio**. 

![b6_sagemaker_pic](../image/b6_sagemaker_pic.png)

10. This takes you to **Amazon SageMaker Studio**.

![6_lab-JupyterLab](../image/6_lab-JupyterLab.png)

11. Click **File**. Choose **New**. Choose **Terminal**.

![6d_sagemaker_terminal](../image/6d_sagemaker_terminal.png)

## Clone the GitHub repository 

1. Execute the following git command.

```
git clone < Git Repository Name>

```

> [!NOTE]
> Git Repository Name: Please refer book Appendix section. 

2. Click **File Browser** in the left side panel of **Amazon SageMaker Studio** to view all code files. 

![6e_sagemaker_file](../image/6e_sagemaker_file.png)

3. Click *chapter19*. Open **simple_multimodal_data_prep.ipynb** file. 

4. Use *Image* as **Data Science 3.0**. *Kernel* as **Python 3**. *Instance* as **ml.t3.medium**.

![7_lab-JupyterLab_2](../image/7_lab-JupyterLab_2.png)

5. Read and follow all the steps of **simple_multimodal_data_prep.ipynb** file. 

### File Name: simple_multimodal_data_prep.ipynb
### Purpose: 
        1. Processing a dataset of images, saving them to a specified directory while generating and storing metadata descriptions.
        2. Generates multimodal embeddings by accepting an image or text description, processes the input, and invokes a model via the Bedrock runtime client, returning the resulting embeddings.
        3. Adds multimodal embeddings to each dictionary in image_metadata_list.

6. Click *chapter19*. Open **simple_multimodal_knwl_bases_building.ipynb** file. 

7. Use *Image* as **Data Science 3.0**. *Kernel* as **Python 3**. *Instance* as **ml.t3.medium**.

![7_lab-JupyterLab_2](../image/7_lab-JupyterLab_2.png)

8. Read and follow all the steps of **simple_multimodal_knwl_bases_building.ipynb** file. 

### File Name: simple_multimodal_knwl_bases_building.ipynb
### Purpose: 
        1. Create collection on serverless opensearch
        2. Create a network policy for collection
        3. Create a security policy for encryption using an AWS-owned key
        4. Create a access policy for collection to define permissions for the collection and index
        5. Call the create_access_policy method to define permissions for the collection and index
        6. Create a vector search collection in OpenSearch Serverless
        7. Collection will take some time to be "ACTIVE". So, checking when the collection is "ACTIVE" for the next steps
        8. Index Creation on the collection
        9. Search capability with a simple text prompts
        10. Search capability features a combination of text and image prompts

> [!CAUTION]
> If you are running this in your own account, please be aware that costs may be incurred. The exact expenses depend on factors such as the frequency of your calls to Bedrock, the length of tokens or the size of images in your calls, and the specific models you utilize. For detailed pricing information for each model, please refer to the Amazon Bedrock console. Even, you will get specific note before every exercises. 

## Clean up

If you dont want to continue with this hands on exercise further, Please follow the **Delete** the AWS CloudFormation stack to avoid incurring future charges and to clean up unused roles and policies, delete the resources you created as part of the execution of the AWS CloudFormation stack. 