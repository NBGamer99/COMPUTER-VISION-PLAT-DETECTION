<div align="center" id="top">
  <a href="">
    <img src="./assets/OpenCV_logo_no_text.png" alt="Logo" width="150px">
  </a>

  <h3 align="center">THE BEAUTY OF COMPUTER VISION
</h3>

  <p align="center">
    Computer Vision Shenanigans ...
    <br />
    <br />
    <a href="#contribute">Contribute</a>
    ·
    <a href="https://github.com/NBGamer99/VisionOrdinateur/issues">Report Bug</a>
  </p>

  ![License](https://camo.githubusercontent.com/3dbcfa4997505c80ef928681b291d33ecfac2dabf563eb742bb3e269a5af909c/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f496c65726961796f2f6d61726b646f776e2d6261646765733f7374796c653d666f722d7468652d6261646765)
  ![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
  ![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white)
  ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)

</div>



<br>
<center>

<img src="./assets/meme.png" alt="drawimemeng" width="400"/>

</center>

<!-- omit in toc -->
## > Would it work on my machine ?

Probably ?! idk as long as these following conditions are meet.
  * A Working computer
  * And hands
  * At least 1gb of free storage
  * python 3.9.1 (can be downloaded from [here](https://www.python.org/downloads/release/python-391/))
  * Have patient (it might take minutes, hours or maybe years)


<!-- omit in toc -->
### 1. Open your terminal in the project working directory :
![](./assets/Screen%20Shot%202022-12-08%20at%2011.59.28%20PM.png)
Make sure you are operating in the project folder.

<!-- omit in toc -->
## 2. Create a Virtual Environment :

```bash
$ python3 -m venv env
```
This will create a Python self contained virtual environment that contains a specific version of Python and any associated libraries and dependencies.This allows for the creation of isolated environments for different projects or purposes, without affecting your overall system Python installation. elimenating any possibiltie for conflecting files and packages.

After running the previous command a folder by the name **env** should appear.

![](./assets/Screen%20Shot%202022-12-09%20at%2012.00.49%20AM.png)

In order to not fall in any compatibilities issues it's highly recommended to update your pip and setuptools by running the following :

```bash
$ pip install pip -U
$ pip install setuptools -U
```

<!-- omit in toc -->
## 3. Activate your virtual environment :

To activate your virtual environment run the following commands that corresponds to your OS.
- **Windows** :
  - cmd
	```cmd
	$ env\Scripts\activate.bat
	```
  - powershell
	```powershell
	$ env\Scripts\activate.ps
	```
- Mac/Linux:
	```bash
	$ source ./env/bin/activate
	```
This will activate our virtual environment by adding an **env** next to our terminal command line.

![](./assets/Screen%20Shot%202022-12-09%20at%2012.00.49%20AM.png)

To deactivate it run the following command

```bash
$ deactivate
```

<!-- omit in toc -->
## 4. Installing the required libraries :

Open-CV / easyocr / imutils / matplotlib

now we will install the required libraries needed for our project to run which python made easy using pip on a requirements.txt file.

```bash
$ pip install -r requirements.txt
```

> 💡 Tip of the day
> if you are working on your own vitual environement and you want to extract all the libraries you used in your isolated environment run the following.
> ``` pip freeze > requirements.txt```
> this should list all your packages and their versions in a requirements.txt

<!-- omit in toc -->
## 5. Congratulations new skill acquired 🥳

<!-- <div style="color:white;"><a style="text-decoration: none !important;color:white;">https://www.youtube.com/watch?v=dQw4w9WgXcQ</a></div> -->
Now you are a certified average python venv user.

<!-- omit in toc -->
## > Code Documentations 👨‍💻
This Project consists of two parts :

- [Cars Plates Detections 🚘](#cars-plates-detections-)
- [Video Detection 🤖](#video-detection-)

### Cars Plates Detections 🚘

In this first project you will find two files a Jupyter Notebook and a python main file, both are implementing what we have learned in our previous lessons regarding the **High-pass filter** and it's utilization in edge detection,by implementing the [Marr–Hildreth](https://en.wikipedia.org/wiki/Marr%E2%80%93Hildreth_algorithm) algorithm we can extract car plates from pictures.
The Mar-Hildreth code is done by **Afaf & Mouna**.

### Video Detection 🤖

This one is just straight forward, we try to use image processing and classification to detect objects from an already trained data.




<h2 id="contribute">Contributions</h2>

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

- Fork the repo
- Create a new branch (`git checkout -b feature/AmazingFeature`)
- Make your changes and add them (`git add .`)
- Commit and push your changes (`git commit -m 'Add some AmazingFeature' && git push origin feature/AmazingFeature`)
- Create a new pull request 🤩
- And that's it 😊
- Don't forget to star ⭐ the repo if you like it 😊

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact Information

- Devs : mesrarhamza48@gmail.com && ynabouzi.me@gmail.com
---
**Note:** The object detection algorithms are here to aid students and learners. Please use it responsibly, following your educational institution's rules and applicable regulations related to mathematical optimization and algorithms.
