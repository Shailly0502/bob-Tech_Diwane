## Add your idea files to this directory. Please don't rename this directory.


### _A solution is provided for the Problem Statement titled as Automated Cheque Processing,in Bank of Baroda Hackathon 2022 hosted on TechGig._

## Provided Problem Statement(Automated Cheque Processing)

Bank handles large volumes of cheques in the clearing process. The process involves many technical verifications including signature verification. Some of these steps are manual and require human intervention to complete the process. The current process requires the high human capital deployment and longer processing time.

## Expected Solution

Using rule-based and AI/ML/ICR/ OCR (Optical Character Recognition) capabilities for automation and doing technical and signature verification of the cheques.
* Automation of the clearing process using AI/ML/ICR/OCR techniques
* Automatic Data Entry & Technical verification
* Signature Verification
* Support Multilingual
* Reduce Human Efforts
* Reduce Processing time
* Detecting Potential Frauds

## Proposed Solution

### Demo Video


### Workflow

* A cheque image is taken as an input & scanned. Then this scanned image is transformed into many different small part where every part contain seperate useful information like signature,amount,account number,payee name,bank name,etc. 
* These parts are extracted by drawing boxes on those parts of the scanned cheque image that contain useful information, with help of __OpenCV__ and __Geometry.__
* With the help of __Azure APIs__ these small different parts of the scanned images are sent to __OCR(Optical Character Recognition)__ for  processing information written in these small images.
* OCR model returns a list of detections and then among that list, there are both useful information and additional informations. Among complete list, detections of only required information are considered(this is  known as __text cleaning or extracting of useful information__).

_Please make a note that Useful information here mean that only that information that is relevant or required for cheque verification and processing._

__Useful information includes:__   _Payee Name, Amount in words, Amount in numbers, Date, IFSC Code, Bank Name, Account Number, MICR Code, Signature._

![cheque image](https://github.com/Shailly0502/Tech-Diwane/blob/f6b6ac386f94a1ac83bbad23283a2805e63eccee/cheque.jpeg)
  
* _To ensure the genuinity or correctiveness of cheque, extracted Amount in words is converted into numerical form and then that numerical form is compared with Amount in numbers, if it matches then, cheque information is correct and then further process is done_.

 __Transaction Type detection__: _If 'self' or 'myself' is written in payee name then that transaction is NEFT otherwise it is a RTGS Transaction._

* After cleaning or extracting useful detection from OCR list, the extracted information of the payer is used to compare with it's existing record information in database __so as to verify if payer is genuine or not__ and _this process is known as __Verification Process__ & is the most crucial part of the whole process._

* For complete verification of payer, verification of different extracted information takes place with the help of ML modules.

  * __Signature Verification__ is done with the help of __signver module__ that contains __sub-modules__ such that:
 
    * _Cleaner module_ returns a list of cleaned signature images (removal of background lines and text), given a list of signature images.
    * _Extactor module_ returns a list of vector representations, given a list of image tensors/np arrays.
    * _Matcher module_ returns a distance measure given a pair of signatures (where one signature image is the image of payee's signature extracted from input cheque image and other image is the image present in payee's existing records in the database). _If both images match, then signature is verified otherwise signature on input cheque is a forgery or fake signature of payee._

   #### _Diagrametic Representation of signver module_

  ![signature verification](https://raw.githubusercontent.com/fastforwardlabs/signver/main/docs/images/signature_pipeline.png)
  
   * Extracted __Account Number__ is verified by checking if any information of payer with this extracted account number exists.
   * Extracted __MICR Code__ is verifed by checking if leaf number is less than leaf left.
   * __Amount Verification__ is done to check if account contains sufficient amount such that transaction of mentioned amount could take place in future after successful verification of cheque details because _If sufficient amount is present in account then only transaction will take place._

 _Only after the successful verification, any processes or transactions(as instructed on cheque like transferring of money to the intended user bank account) takes place._

* __After successful cheque processing, the details of the sender gets further updated in the database as per the transaction took place successfully.__

![cheque verification](https://github.com/Shailly0502/Tech-Diwane/blob/69f23f6342bee3c180b161ec4146ce7174276da8/astha.png)

#### _Diagrametic Representation of Complete Workflow_

### Database

Information of different payers are stored in the database. 
It includes:
* Cheque ID
* Account Number
* MICR
* Current Amount
* Signature Image

![database image](https://github.com/Shailly0502/Tech-Diwane/blob/b4fef312819a8182b7e3c97a19e105d2d96ccf4f/database.png)

### Features

* Supports Multilingual _(Hindi,English)_
* MICR Verification.
* Checks the correctiveness of cheque information by matching amount in words match with amount in number so as to ensure correctiveness of mentioned information of cheque.
* Checks if a transaction is NEFT or RTGS(Transaction type detection).
* Reduce Human Efforts _(By automating process of verification and data updation after processing)
* Reduce Processing time _(Machine take less time than humans so it fastens the cheque processing time )
* Detecting Potential Frauds _(Through verification processing)_

### How to use our code?

1. Clone this repository into your system. 
   ##### git clone https://github.com/Shailly0502/bob-Tech_Diwane.git
  
2. After cloning, inside source folder ,compile and run all files except main.py file.
3. After that, run main.py file where it will ask to give path of the image of cheque on terminal so enter the path of image.



### Contact Us

![Linkedin](https://github.com/Shailly0502/Tech-Diwane/blob/75e855a19f318370ebc02275ceed6d05cb649e4a/linkedin.png=250*250) <a href=""> Anubhav Yadav </a> <br>
<a href=""> Shailly Raj </a> <br>
![Amisha Singh](https://github.com/Shailly0502/Tech-Diwane/blob/75e855a19f318370ebc02275ceed6d05cb649e4a/linkedin.png) <a href ="https://www.linkedin.com/in/amisha-s-a56329200"> Amisha Singh </a> <br>
![Astha Goel](https://github.com/Shailly0502/Tech-Diwane/blob/75e855a19f318370ebc02275ceed6d05cb649e4a/linkedin.png) <a href="https://www.linkedin.com/in/goel-astha"> Astha Goel </a>
