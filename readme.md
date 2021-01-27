<img src="square-logo.svg" width=255 height=255 align="right">

#  Rasa Form Examples

This repository contains a collection of tutorials that will help you understand forms. Each example is self contained and is part of a series of videos on our youtube channel. Note that all the demos here are built with Rasa 2.2 in mind. 

## Installation 

To run all the examples here you'll need to install Rasa, preferably in a virtualenv in the root directory. 

```
python -m pip install rasa==2.2
```

If you'd also like to use Rasa X, you can install this via; 

```
python -m pip install rasa-x --upgrade -i https://pypi.rasa.com/simple
```

## `01-custom-actions`

It helps to understand custom actions and slots before we talk about forms. In this simple bot we show how they work by keeping track of a users name. 

## `02-slots`

It helps to understand custom actions and slots before we talk about forms. In this simple bot we show how they work by keeping track of a users name. 

## `03-simple-forms`

If we want to query multiple things from the user, it may be best to use forms instead of custom actions. Luckily for us, we can use our `RulePolicy` to help us out.

## `04-checking-form-input`

What if we want to validate the input of our form? We don't want to have a name that's an empty string after all! 

## `05-entities-and-forms`

The user might give the response in a sentence, in which case we'll want to detect entities instead of grabbing the full text.

## `06-expanding-forms`

The user might give the response in a sentence, in which case we'll want to detect entities instead of grabbing the full text.