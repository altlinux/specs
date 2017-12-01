%def_without check
%def_with python3

%define modulename patch
Name: python-module-patch
Version: 1.16
Release: alt1

Summary: Library to parse and apply unified diffs

Url: https://pypi.python.org/pypi/patch/
License: Python Software Foundation License
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# NOSource-url: https://pypi.io/packages/source/p/%modulename/%modulename-%version.tar.gz
# Source-url: https://github.com/techtonik/python-patch/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

#setup_python_module %modulename

%description
Library to parse and apply unified diffs.


%package -n python3-module-patch
Summary: Library to parse and apply unified diffs
Group: Development/Python3

%description -n python3-module-patch
Library to parse and apply unified diffs.


%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build

%install
install -D -m755 patch.py %buildroot%python_sitelibdir/patch.py
install -D -m755 patch.py %buildroot%python3_sitelibdir/patch.py
%__subst "s|^#!/usr/bin/env python$|#!/usr/bin/python3|g" %buildroot%python3_sitelibdir/patch.py

%files
%doc README.md doc/
%python_sitelibdir/*

%if_with python3
%files -n python3-module-patch
%doc README.md doc/
%python3_sitelibdir/*
%endif


%changelog
* Fri Dec 01 2017 Vitaly Lipatov <lav@altlinux.ru> 1.16-alt1
- initial build for ALT Sisyphus

