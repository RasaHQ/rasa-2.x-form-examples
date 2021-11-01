<img src="square-logo.svg" width=255 height=255 align="right">

#  Rasa 2.x Form Examples

## Archived 

This repository contains a collection of tutorials that will help you understand forms. Each example is self contained and is part of a series of videos on our youtube channel. Note that all the demos here are built with Rasa 2.3 in mind. These examples won't work for Rasa 3.x onward. 

## Installation 

To run all the examples here you'll need to install Rasa, preferably in a virtualenv in the root directory. 

```
python -m pip install rasa==2.3
```

If you'd also like to use Rasa X, you can install this via; 

```
python -m pip install rasa-x --upgrade -i https://pypi.rasa.com/simple
```

## 1. Custom Actions

It helps to understand custom actions and slots before we talk about forms. In this simple bot we show how they work by keeping track of a users name. 

Code can be found in the `01-actions` folder.

## 2. Slots 

It helps to understand custom actions and slots before we talk about forms. In this simple bot we show how they work by keeping track of a users name. 

Code can be found in the `02-slots` folder.

## 3. Simple Forms

If we want to query multiple things from the user, it may be best to use forms instead of custom actions. Luckily for us, we can use our `RulePolicy` to help us out.

Code can be found in the `03-simple-forms` folder. 

## 4. Asking Questions 

You can customise how questions are asked in a form. You can write templates in a domain.yml file or use custom actions.

## 5. Form Validation 

What if we want to validate the input of our form? We don't want to have a name that's an empty string after all! 

Code can be found in the `04-checking-form-input` folder.

## 5. Entities and Forms

The user might give the response in a sentence, in which case we'll want to detect entities instead of grabbing the full text.

Code can be found in the `05-entities-and-forms` folder.

## 6. Expanding Forms

The user might give the response in a sentence, in which case we'll want to detect entities instead of grabbing the full text.

Code can be found in the `06-expanding-forms` folder.

## 7. Elaborate Name Form Example

In this final example we'll show an elaborate example of a form that can ask for names.
