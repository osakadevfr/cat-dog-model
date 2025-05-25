Here's the formatted Markdown:

```markdown
# 🐶 Small Cat or Dog Classifier 🐱  

A tiny image classifier that looks at a photo and tells you:  

- 🐕 *"This is a dog."*  
- 🐈 *"This is a cat."*  
- 🐟❓ *"This is a cat."*  
  *(Even when it’s definitely not. Cats are the default guess. Sorry, fish.)*  

Surprised?  
**You shouldn’t be.**  

---  

## 🧠 Training Details  

- ⏱️ ~20–30 minutes on CPU  
- 📸 28,000 dog images  
- 🐱 11,000 cat images  
- 🛠️ Built with TensorFlow  
- ❌ No CUDA, no GPU — just raw RX 580 suffering  

---  

## 🛠️ How to Use  

### Run the GUI  
```bash  
python gui.py  
```  

You’ll get a window. Drop in an image. Watch it try.  

### Re-train the model (hi nerds)
Firstly make a cat folder.
Then make a dog folder.

Place your images.
then:
  
```bash  
python main.py  
```  

Tweak the resolution or image count inside `main.py` if you feel brave.  

Done.
---  

## 📂 Image Sources  

- **Cats:** [Kaggle Cat Breeds](https://www.kaggle.com/) (MIT License)  
- **Dogs:** [Stanford Dogs Dataset](http://vision.stanford.edu/aditya86/ImageNetDogs/)  

---  

## 💀 Disclaimer  

This model isn’t smart.  
It just saw a LOT of cats and dogs.  
Use at your own risk. Laugh at your own results.  

---  

## 🔓 License  

Do whatever you want with it. Seriously. Fork it, improve it, meme it, make it bark.  
