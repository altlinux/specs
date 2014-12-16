%define oname mozprofile
Name: python-module-%oname
Version: 0.22
Release: alt1
Summary: Library to create and modify Mozilla application profiles
License: MPLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/mozprofile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-modules-sqlite3
BuildPreReq: python-module-manifestparser python-module-mozfile
BuildPreReq: python-module-mozlog python-module-mozhttpd

%py_provides %oname
%py_requires mozhttpd

%description
Library to create and modify Mozilla application profiles.

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
* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.22-alt1
- Initial build for Sisyphus

