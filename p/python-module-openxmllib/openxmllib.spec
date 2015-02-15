%define oname openxmllib
Name: python-module-%oname
Version: 1.0.7
Release: alt1
Summary: Provides resources to handle OpenXML documents
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/openxmllib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-lxml
BuildPreReq: python-module-nose

%py_provides %oname
%py_requires lxml

%description
openxmllib is a set of tools that deals with the new ECMA 376 office
file formats known as OpenXML.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc HISTORY README TODO
%_bindir/*
%python_sitelibdir/*

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt1
- Initial build for Sisyphus

