---
title: GenomeCRISPR
author: Nourdine Bah
numbersections: true
numbersubsections: true
---

# How to install and run the script

We assume that you are on `bash`, and that you have `unzip` and `python3` already installed on your system.
We also assume that `black`, `pylint` and `pytest` python packages are installed.

## Extract the content of the `zip` archive

First, extract the content of the `zip` archive by running:

```
$ unzip genomecrispr.zip
```

This should create a folder called `genomecrispr` in your current directory.

## Create package archive and generate documentation

Change directory to go to the `genomecrispr` folder and build the package by running:

```
$ cd genomecrispr
$ make build
```

The archive should be now visible in the `dist` directory:

```
$ ls dist
genomecrispr-0.0.0-py3-none-any.whl  genomecrispr-0.0.0.tar.gz
```

If you have `sphinx` and `sphinx-rtd-theme` installed, you can generated the documentation by running:

```
$ make doc
```

The generated documentation should be in `genomecrispr/docs/build/html`.
You can now leave the `genomecrispr` directory and go back to where you were:

```
$ cd ../
```

## Create a `virtualenv` environment

If you don't have `virtualenv` already on your system, please install it by running:

```
$ pip install virtualenv
```

Then, create a virtual environment called `venv` and source it by running:

```
$ virtualenv venv
$ . venv/bin/activate
```

You are now in the virtual environment.

## Install the package

Now, install the package by running:

```
(venv) $ pip install genomecrispr/dist/genomecrispr-0.0.0.tar.gz
```

The package is now installed.
You can display information about the script by running:

```
screen --help
```

## Run the script

To run the script on a file you can run:

```
screen <PATH_OF_THE_FILE_CONTAINING_GENES> <BASE_PATH_OF_THE_RESULTS>
```

To run the solution on CDKs:

```
screen genomecrispr/cdks.txt results_cdks
```

## Leave the virtual environment

When you are done, you can leave the virtual environment by running:

```
deactivate
```

