%define oname robotframework-elasticsearch
Name: python-module-%oname
Version: 1.0
Release: alt1.git20141223
Summary: ElasticSearch library for Robot Framework
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/robotframework-elasticsearch/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pagesjaunes/robotframework-elasticsearch.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-modules-json
BuildPreReq: python-module-robotframework
BuildPreReq: python-module-elasticsearch

%py_provides ElasticSearchLib
%py_requires robotframework elasticsearch

%description
This lib provides basic keywords to interact with elasticsearch in a
RobotFramework testsuite. It allows to query, count, create or delete an
index.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.md doc/*
%python_sitelibdir/*

%changelog
* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20141223
- Initial build for Sisyphus

