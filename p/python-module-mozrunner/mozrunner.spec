%define oname mozrunner
Name: python-module-%oname
Version: 6.6
Release: alt1.1
Summary: Reliable start/stop/configuration of Mozilla Applications (Firefox, Thunderbird, etc.)
License: MPLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/mozrunner/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-mozcrash python-module-mozdevice
BuildPreReq: python-module-mozfile python-module-mozinfo
BuildPreReq: python-module-mozlog python-module-mozprocess
BuildPreReq: python-module-mozprofile

%py_provides %oname

%description
Reliable start/stop/configuration of Mozilla Applications (Firefox,
Thunderbird, etc.).

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 6.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.6-alt1
- Initial build for Sisyphus

