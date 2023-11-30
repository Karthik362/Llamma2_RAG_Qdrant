# Chaabi_Assignment

To run in google colab:
Use the Assignment.ipynb file

Setup:

Upload bigBasketProducts.zip file by compressing the csv file as zip. ( This is for faster upload )

Use Gpu T4 which is provided freely as runtime. 

Inference:

Some references are attached at the end of the notebook

Run every cell in the colab notebook and add a cell :-

  rag_pipeline(prompt) 
  
To get the result.

Some example queries :

'query': 'What are some highly rated products that are used in the kitchen?'

'result': " Based on the provided text, some highly rated products used in the kitchen include the Kitchen Essentials brand's utensils, which enable fast and natural oil-free cooking, and the Classic Essentials Kitchen Tool Set, which is made from high-quality, food-grade stainless steel and is designed for easy handling and safe usage when cooking or serving food. Additionally, the Kitchen Essential product is also highly rated for its superior heat conductivity and lasting durability, making it ideal for heating milk and making tea on a daily basis."

'query': 'Provide some Home cleaning products?'

'result': '\n\nHerbal Strategi Just Mop - Herbal Floor Cleaner, Disinfectant, Insect Repellent is a revolutionary product which is free from harsh chemicals. This is a natural disinfectant. This Herbal Strategi product contains natural oils and plant extracts. This natural disinfectant is a versatile cleaning product. It not just cleanses stains, but also does kill germs and act as repellent to the insects. The refreshing lemon grass fragrance is a boon to this product.\n\nColin Cleaner Glass and Household has vinegar as the main ingredient known for its strong cleansing action. It removes the dust from your surfaces and makes them spick and span. It is not too harsh on the skin and this formula doesn’t even bother your nose. It makes cleaning all kinds of glass surfaces and appliances a breeze.The Sponge Wipe is a one swipe cleaner for kitchen countertops, tables, and other kitchen appliances.'

To run using Flask :
Use app.py , untitled.py , Templates folder .
Setup :

pip install Flask \
  torch \
  transformers==4.31.0 \
  sentence-transformers==2.2.2 \
  pinecone-client==2.2.2 \
  datasets==2.14.0 \
  accelerate==0.21.0 \
  einops==0.6.1 \
  langchain==0.0.240 \
  xformers==0.0.20 \
  bitsandbytes==0.41.0

Run :
python app.py
