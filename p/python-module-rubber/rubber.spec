%define oname rubber
Name: python-module-%oname
Version: 0.1.8
Release: alt1
Summary: Elasticsearch client with Django support
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/rubber
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools

%description
rubber is a Python client for Elasticsearch.

Its main features are:
  - rubber is easy to use
  - rubber does not try to hide or wrap Elasticsearch syntax.
  - rubber integrates nicely with Django:
  - automatically saves your models to Elasticsearch
  - provides a Manager-style object on your django models
    for querying
  - rubber is unit-testing friendly: you don't need an elasticsearch
    instance to run your tests

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc README.md
%python_sitelibdir/%{oname}*

%changelog
* Tue Jun 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt1
- Initial build for Sisyphus

