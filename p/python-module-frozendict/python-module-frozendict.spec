%def_without check
%def_with python3

%define modulename frozendict
Name: python-module-frozendict
Version: 1.2
Release: alt1

Summary: An immutable dictionary

Url: https://pypi.python.org/pypi/frozendict
License: MIT
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.io/packages/source/f/%modulename/%modulename-%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools

BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

#setup_python_module %modulename

%description
frozendict is an immutable wrapper around dictionaries that implements
the complete mapping interface. It can be used as a drop-in replacement
for dictionaries where immutability is desired.


%package -n python3-module-frozendict
Summary: An immutable dictionary
Group: Development/Python3

%description -n python3-module-frozendict
frozendict is an immutable wrapper around dictionaries that implements
the complete mapping interface. It can be used as a drop-in replacement
for dictionaries where immutability is desired.


%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-frozendict
%doc README.rst
%python3_sitelibdir/*
%endif


%changelog
* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- initial build for ALT Sisyphus

