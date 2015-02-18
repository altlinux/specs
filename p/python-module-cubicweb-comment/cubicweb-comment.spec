%define oname cubicweb-comment
Name: python-module-%oname
Version: 1.11.0
Release: alt1
Summary: Commenting system for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-comment/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-markdown

Requires: cubicweb

%description
The comment cube provides threadable comments feature.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README
%python_sitelibdir/*
%_datadir/cubicweb/*

%changelog
* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.0-alt1
- Version 1.11.0

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.0-alt1
- Initial build for Sisyphus

