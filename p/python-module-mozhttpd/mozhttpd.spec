%define oname mozhttpd

%def_disable check

Name: python-module-%oname
Version: 0.7
Release: alt1
Summary: Python webserver intended for use with Mozilla testing
License: MPL
Group: Development/Python
Url: https://pypi.python.org/pypi/mozhttpd/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-moznetwork

%py_provides %oname

%description
Python webserver intended for use with Mozilla testing.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc PKG-INFO
%_bindir/*
%python_sitelibdir/*

%changelog
* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Initial build for Sisyphus

