%define oname mozdevice
Name: python-module-%oname
Version: 0.44
Release: alt1
Summary: Mozilla-authored device management
License: MPL
Group: Development/Python
Url: https://pypi.python.org/pypi/mozdevice/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-mozfile python-module-mozlog
BuildPreReq: python-module-moznetwork python-module-mozprocess

%py_provides %oname

%description
Mozilla-authored device management.

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
* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.44-alt1
- Initial build for Sisyphus

