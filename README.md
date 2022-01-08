<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

<p align="center">
  <a href="#">
     <img src="https://ik.imagekit.io/kummiktgaiq/ppg/logo_OE3b6z79V.png?updatedAt=1635261532682" alt="PPG Logo" width="50%">
  </a>
</p>

<h3 align="center">PPG - Python Package Generator</h3>

<p align="center">
  Sleek, intuitive, and powerful tool for faster and easier PyQt/PySide App development.
  <br>
  <a href="#docs"><strong>Explore PPG docs »</strong></a>
  <br>
</p>


## Table of contents

- [Quick start](#quick-start)
- [Status](#status)
- [What's Changed](#whats-Changed)
- [Getting started](#getting-started)
- [CLI Usage](#using-the-cli)
- [The Life Cycle of a component](#the-life-cycle-of-a-component)
- [Creators](#creators)
- [Copyright and license](#copyright-and-license)


## Quick start

Several quick start options are available:

- [Download the latest release](https://github.com/runesc/PPG/releases/)
- Clone the repo: `git clone https://github.com/runesc/ppg.git`
- Install with Pip: `pip install ppg`

Read the [Getting started](#getting-started) section for information, templates, examples, and more.

## Status

![Build](https://img.shields.io/badge/build-1.0.0--stable-green)
![Compiling](https://img.shields.io/badge/compiling-pass-green)
![GitHub issues](https://img.shields.io/github/issues/runesc/Refresh-UI)
![GitHub forks](https://img.shields.io/github/forks/runesc/PPG)
![GitHub stars](https://img.shields.io/github/stars/runesc/PPG)
![GitHub licence](	https://img.shields.io/github/license/runesc/PPG)
![Twitter](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Frunesc%2FPPG)

## What's Changed
- Fixed *`build_settings`* in *`ApplicationContext`* ✅
- Fixed *`ppg freeze`* ✅
- Fixed *`shiboken6`* hook ✅
- Modified *`project_template`* in *`ppg/builtin_commands/project_template`* ✅
- Modified **LifeCycle** class, new methods were added like:
  - *`component_will_mount`* **Renamed**
  - *`allow_bg`* **New**
  - *`render_`*
  - *`resizeEvent`* **Updated**
  - *`component_did_mount`* **Renamed**
  - *`set_CSS`*  **Renamed**
  - *`responsive_UI`* **Renamed**
  - *`destroyComponent`* **New**
  - *`find`* **New**
  - *`calc`* **New**
  For more info check the [docs](#Documentation). ✅
- **New!** Now you can create components or views just typing *`ppg create component`* 🎉
- Fixed component template does not import selected widget ✅
- Modified Icons updated

## Getting started
This section is a step-by-step overview of using the PPG tool for creating apps.

#### Overview
- [Setup](#setup)
- [Create a project](#create-a-project)
- [Running the app](#running-the-app)
- [Compile your app](#compile-your-app)

#### Setup
There are different ways to install PPG but before installing it, we recommend creating a virtual environment with virtualenv or conda. We do not recommend installing it directly on your computer to avoid compatibility problems in future projects.

##### Using Conda
Run the following command to create your virtual environment:

```bash
conda create -n YOUR_ENV_NAME python=3.X -y
```

Activate your virtual enviroment.
```bash
conda activate YOUR_ENV_NAME
```

##### Using Virtualenv 

```bash
python -m venv venv
```

Activate your virtual enviroment.
```bash
# On Mac/Linux:
source venv/bin/activate
# On Windows:
call venv\scripts\activate.bat
```

##### Installing PPG
Now we need to install PPG.

```bash
# Using Pypi
pip install ppg

# Using github repository
pip install https://github.com/runesc/PPG.git

# From source code
curl -L -O https://github.com/runesc/PPG.git
unzip PPG.zip
cd PPG/
python setup.py install
```

Great! You already have PPG installed, now you need to choose the Qt binding that you prefer in our case we will use PySide6.

#### Create a project
Creating a project is the easiest part of PPG, you just have to answer a few questions and that's it.

```bash
# Just write
ppg init
# Console displays: 
PPG init v1.0.0

App name [MyApp] : MyDemoApp
Version [1.0.0] : 1.0.0
Author [ppg] : you
Please select your Qt binding [default: 'PySide6']: 1) PyQt5 or 2) PyQt6 or 3) PySide2 or 4) PySide6 [4] : 4
Mac bundle identifier (eg. com.you.mydemoapp, optional):
Created the src/ directory. If you have PySide6 installed, you can now
do:

    ppg run

```

#### Running the app
<div class="alert alert-warning" role="alert">
  Before running the app, we recommend that you have the qt binding that you will use installed.
</div>


As you can see, two folders *`src/`* and *`requirements/`* have been created later on we will see in detail what those folders do for now, focus on executing the application

```bash
# Just write
ppg run
```
It's like magic!🎉🌌 You already have a template where you can start expressing your ideas with code.

#### Compile your app
We want to turn the source code of our app into a standalone executable that can be run on your users' computers. In the context of Python applications, this process is called "freezing".

Use the following command to turn the app's source code into a standalone executable:

```bash
# Just write
ppg freeze
```
This creates the folder *`target/YourApp/`*. You can copy this directory to any other computer (with the same OS as yours) and run the app there.

Now we have generated a binary that can run on any PC as long as they use the same operating system (if you compile on Windows you can't run the app on Linux or MacOS) but we need an elegant way to distribute our apps because we can't send the app in zip and ask the user to unzip it and run for that we can choose an installer (*`setup.exe`* on Windows, *`.dmg`* on MacOS or *`.deb/.rpm/.pkg.tar.xz`* on Linux.

<div class="alert alert-warning" role="alert">
  If you use Windows first install <a href="http://nsis.sourceforge.net/Main_Page">NSIS</a> and add to the path.
</div>

To be able to generate an installer you just have to write the following command:

```bash
# Create a installer
ppg installer
```


## Using the CLI
PPG CLI is a command line interface tool used to initialize, develop, structure, and maintain Qt applications directly from a command shell.

#### Overview
- [ppg init](#ppg-init)
- [ppg start](#ppg-start)
- [ppg create](#ppg-create)
- [ppg freeze](#ppg-freeze)
- [ppg installer](##ppg-installer)
- [ppg sign](##ppg-sign)
- [ppg sign_installer](#ppg-sign_installer)
- [ppg test](#ppg-test)
- [ppg clean](#ppg-clean)

#### ppg init
Create an Python/Qt workspace.

```bash
ppg init
```

##### Description
Create and initialize a new Python/Qt application that is the default project for a new workspace.

Provides interactive prompts for initial configuration, such as binding to use, version, app name and more. All prompts can be allowed to be safely set by default.

The new workspace folder is named *`src/`* specified and contains configuration files.

By default, the files for a new starter application are placed in the *`src/`* folder.

The configuration of the new application appears in the section of *`build/settings`* where the configuration file of the workspace *`base.json`* is located

#### ppg start
Builds and serves your app.
```bash
ppg start
```

#### ppg create
Create a new component or view.

```bash
ppg create <element>
```
##### Description
Add a new component to the workspace and configure the project to use it, it can be an empty widget (*`QWidget`*) or a simple component like a *`QPushButton`*.

The CLI provides a simple interface where you can select the type of widget you want to work with and the type of component that will be created (*`view`* or *`component`*) and it is saved in its respective folder (*`components/`*/ or *`views/`*/).

##### Arguments
| Argument      | Description | Value type    |
| :---          | :---        | :---          |
| `<component>`|Select the type of component to be used (**view** or **component**).| `string`|


#### ppg freeze
Compile the source code and transform it into an executable file

```bash
ppg freeze [options]
```

##### Description
Creates an executable file that can be used on any PC that uses the same operating system for which it was compiled.

##### Options
| Argument      | Description | Value type    |  Default value    |
| :---          | :---        | :---          | :---          |
| `--debug`| It shows a log in the compilation and when executing the app it shows the status in a terminal.| `boolean`|`false`|

#### ppg installer
<div class="alert alert-warning" role="alert">
  <a href="http://nsis.sourceforge.net/Main_Page">NSIS</a> required if compiling on Windows.
</div>

Create a user-friendly installer that can be distributed in a classic way.

```bash
ppg installer
```

#### ppg sign
Signs the executable file with a `.pfx` certificate so that it cannot be detected by antivirus as malware. (the signed certificate must be placed in `src/sign/windows/certificate.pfx`)
```bash
ppg sign
```
#### ppg sign_installer
Signs the installer file with a `.pfx` certificate so that it cannot be detected by antivirus as malware. (the signed certificate must be placed in `src/sign/windows/certificate.pfx`)
```bash
ppg sign_installer
```
#### ppg test
Automatically run the unit tests you put in `src/unittest/python`
```bash
ppg test
```
#### ppg clean
Clean up the waste and configuration files that are generated when compiling an application.

```bash
ppg clean
```

## The Life Cycle of a component

Before starting to design applications with ppg it is very important to understand the life cycle of a component.

The life cycle is a fundamental part in app development since it allows to have a better control and code structure when implementing an app, it is found in each component generated by the CLI and in the main class of each project. We recommend including it in your custom components for better integration.




## Creators

**Luis Alfredo Reyes**

- <https://twitter.com/Fredo_Dev>
- <https://github.com/runesc>




## Copyright and license

Code and documentation copyright 2020–2021 the [PPG](#) Code released under the [GPL v3 License](#). Docs released under [Creative Commons](https://creativecommons.org/licenses/by/3.0/).
