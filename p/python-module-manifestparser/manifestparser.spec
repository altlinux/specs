%define oname manifestparser
Name: python-module-%oname
Version: 0.8
Release: alt1
Summary: Library to create and manage test manifests
License: MPL
Group: Development/Python
Url: https://pypi.python.org/pypi/manifestparser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-modules-json

%py_provides %oname

%description
Library to create and manage test manifests.

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
* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1
- Initial build for Sisyphus

