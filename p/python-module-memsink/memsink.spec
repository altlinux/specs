%define oname memsink
Name: python-module-%oname
Version: 0.0.1
Release: alt1.git20131003.1
Summary: Experimental copy-on-invalidate memory protocol
License: ASLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/memsink/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dw/memsink.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools

%py_provides %oname

%description
This package implements an experimental way for CPython extension
modules to communicate buffer lifetimes to each other.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.md
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.1-alt1.git20131003.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20131003
- Initial build for Sisyphus

