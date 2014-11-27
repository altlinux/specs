%define oname cubicweb-forgotpwd
Name: python-module-%oname
Version: 0.6.1
Release: alt1
Summary: Password recovery component for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-forgotpwd/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-pycrypto python-module-Pillow

Requires: cubicweb
%py_requires Crypto PIL

%description
The forgotpwd cube provides an easy way to generate a new password for
 an user, eg the common "I forgot my password" functionnality.

It is non-obstrusive and easy to plug.

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
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

