%define oname cubicweb-preview
Name: python-module-%oname
Version: 1.1.1
Release: alt1
Summary: Enables adding a preview button in your forms
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-preview/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb

Requires: cubicweb

%description
Enables adding a preview button in your forms.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%python_sitelibdir/*
%_datadir/cubicweb/*

%changelog
* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Version 1.1.1

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

