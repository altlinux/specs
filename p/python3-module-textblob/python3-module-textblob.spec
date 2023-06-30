%define pypi_name textblob
%def_disable check

Name: python3-module-%pypi_name
Version: 0.17.1
Release: alt1

Summary: TextBlob is a Python3 library for processing textual data
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%pypi_name

Vcs: https://github.com/sloria/TextBlob
Source: https://pypi.io/packages/source/t/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 >= 0.1.19
BuildRequires: python3-module-wheel python3-module-setuptools

%description
TextBlob is a Python3 library for processing textual data. It provides a
simple API for diving into common natural language processing (NLP) tasks
such as part-of-speech tagging, noun phrase extraction, sentiment
analysis, classification, translation, and more.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
py.test3

%files
%python3_sitelibdir_noarch/*
%doc README* CHANGELOG* NOTICE AUTHORS*

%changelog
* Fri Jun 30 2023 Yuri N. Sedunov <aris@altlinux.org> 0.17.1-alt1
- first build for Sisyphus




