# StyleTTS 2: Towards Human-Level Text-to-Speech through Style Diffusion and Adversarial Training with Large Speech Language Models

## Pre-requisites
1. Python >= 3.7
2. Clone this repository:
```bash
git https://github.com/NamPham-Trivita/StyleTTS2-Trivita
cd StyleTTS2-Trivita
```
3. Install python requirements: 
```bash
pip install -r requirements.txt
```
On Windows add:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 -U
```
Also install phonemizer and espeak if you want to run the demo:
```bash
pip install phonemizer
sudo apt-get install espeak-ng
```
4. Download and extract the [PhoAudioBook](https://huggingface.co/datasets/thivux/phoaudiobook/), unzip to the data folder and upsample the data to 24 kHz. The text aligner and pitch extractor are pre-trained on 24 kHz data, but you can easily change the preprocessing and re-train them using your own preprocessing.

## Training
First stage training:
```bash
accelerate launch train_first.py --config_path ./Configs/config.yml
```
Second stage training:
```bash
python train_second.py --config_path ./Configs/config.yml
```
You can run both consecutively and it will train both the first and second stages. The model will be saved in the format "epoch_1st_%05d.pth" and "epoch_2nd_%05d.pth". Checkpoints and Tensorboard logs will be saved at `log_dir`.  

Fine-tuning models:
```bash
python train_finetune_accelerate.py --config_path ./Configs/config.yml
```
For finetuneing from pre-trained models, you can specify the pre-trained model paths in the config file.

The **data list format** needs to be `filename.wav|transcription|speaker`, see [test.txt](https://github.com/NamPham-Trivita/StyleTTS2-Trivita/blob/main/Data/test.txt) as an example. The speaker labels are needed for multi-speaker models because we need to sample reference audio for style diffusion model training. 

## Explanation of folders

I use phonemes of [Viphoneme](https://github.com/v-nhandt21/Viphoneme).  
But I customized it to make it compatible with my dataset. I fix it a little bit. It is in the **viphoneme** folder.


