<h2 align="center">   Entity Recognition on images using OCR </h2>

<hr>

<div align="center">
  <img src="https://user-images.githubusercontent.com/88481845/215395503-1ccca3ad-bb5a-4a9a-99fd-f7101d40d5e5.jpg">
</div>

<hr>

An entity can be a word or series of words that consistently refer to the same thing. Every detected entity is classified into a prelabelled category. For example, a NER model might detect the word “London” in a text and classify it as a ‘Geography’.
But we need to find the entities from the images. So for this purpose, we need to extract text from the images, so for extracting text we are a technique called OCR.


<h1> What is Optimal character recognition(OCR)? </h1>

OCR stands for Optical Character Recognition. It is widespread technology to recognize text inside images, such as scanned documents and photos. OCR is used to convert any kind of image containing text like(typed handwritten or printed) into machine-readable text format.

![optimal-recognition](https://user-images.githubusercontent.com/88481845/215395624-3a231b77-e0f6-49d9-9b14-f64007a03216.jpg)

For extracting the text we are using open-source software called tesseract which can be implemented using the Pytesseract package.

# Techniques used
        1. Open CV
        2. Spacy
        3. Nltk 
        4. OCR 
        5. Regex
        6. Pandas

<hr>

# How does Pytesseract work?

Pytesseract detects the images in five different stages where we can collect complete text step by step

Step: 1 -> detect complete page
Step: 2 -> detect individual blocks of the image
Step : 3 -> detect paragraphs
Step: 4 -> detect Line
Step: 5 -> detect words 

For detecting entities, we collected individual words from images using step 5 and created a rectangle box on the top of each word using geometric transformations

<img src="https://user-images.githubusercontent.com/88481845/215395862-8602e160-f2a8-4257-8b68-0518aaf2cb3c.png" width="75%">

Same procedure we applied for entire data and collected individual words and saved it in a CSV file. 

For detecting the entities we need class labels for each word, so for creating custom entity recognition on images we used a technique called BIO, where B - Token begins an entity, I - Token is inside an entity, O - Token is outside an entity. Using five different labels we made unstructured data into a structured format.

Now for training the custom entity recognition, we selected a spacy pre-trained model, so we convert the data into a spacy format like complete image data and its corresponding words and labels into dictionary type, This process, we applied for entire data and divide the data into the training part and the testing part.
For training purposes, we used 50 epochs where at the end of the training we got 94% accuracy for the model, 91% precision, and 90.6% recall. We test around 20 images using our trained model and check the results, 

<img src="https://user-images.githubusercontent.com/88481845/215396079-320d8f05-7a7c-439c-90c4-08b7f4f10752.png" width="75%">

<hr>

# Outputs

Few Predicted Images :

<img src="https://user-images.githubusercontent.com/88481845/215396164-3d93e05c-7fd5-4646-a01c-5e73a3dd9903.png" width="75%">

<img src="https://user-images.githubusercontent.com/88481845/215396197-f9d5e3d5-e2a6-49aa-afdd-7a9c58a219e0.png" width="75%">


## Useful Information

### References
- [ Entity Recognition on images using OCR](https://www.bluetickconsultants.com/enity-recognition-on-images-using-ocr.html)

## Other Projects

To view all other open source projects visit
  - [ Open Source Projects ](https://www.bluetickconsultants.com/open-source.html) 
  - [ Open Source Repositories ](https://github.com/orgs/bluetickconsultants/repositories)

## Author

[Bluetick Consultants LLP](https://www.bluetickconsultants.com/)
  #### contact us at admin@bluetickconsultants.com

<img src="https://user-images.githubusercontent.com/88481845/215745914-16aa10a5-f24b-4fa9-b1be-432454487788.png" width="50%">

