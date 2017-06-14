%def_without check
%def_with python3

%define modulename daemonize
Name: python-module-daemonize
Version: 2.4.7
Release: alt1

Summary: Library for writing system daemons in Python

Url: https://github.com/thesharp/daemonize
License: MIT
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/thesharp/daemonize/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools

BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

#setup_python_module %modulename

%description
daemonize is a library for writing system daemons in Python.

%package -n python3-module-daemonize
Summary: Library for writing system daemons in Python
Group: Development/Python3

%description -n python3-module-daemonize
daemonize is a library for writing system daemons in Python.

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
%files -n python3-module-daemonize
%doc README.rst
%python3_sitelibdir/*
%endif


%changelog
* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 2.4.7-alt1
- initial build for ALT Sisyphus

