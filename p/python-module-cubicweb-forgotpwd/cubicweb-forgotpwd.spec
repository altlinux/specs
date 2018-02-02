%define _unpackaged_files_terminate_build 1
%define oname cubicweb-forgotpwd
Name: python-module-%oname
Version: 0.7.1
Release: alt1.1
Summary: Password recovery component for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-forgotpwd/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/33/4d/20de2827f8b094dfd7872ec5758753cbb6011037534852f3df473200fbf3/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-pycrypto python-module-Pillow

Requires: cubicweb
%py_requires Crypto PIL

%description
The forgotpwd cube provides an easy way to generate a new password for
 an user, eg the common "I forgot my password" functionnality.

It is non-obstrusive and easy to plug.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README PKG-INFO
%python_sitelibdir/*
%_datadir/cubicweb/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1
- automated PyPI update

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1
- Version 0.6.2

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

