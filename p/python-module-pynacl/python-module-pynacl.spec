%def_without check
%def_with python3

%define modulename pynacl
Name: python-module-pynacl
Version: 1.1.2
Release: alt1.1

Summary: Python binding to the Networking and Cryptography (NaCl) library

Url: https://github.com/pyca/pynacl
License: ASL 2.0
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/pyca/pynacl/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools

BuildRequires:  libsodium-devel
BuildRequires: python-module-cffi

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildRequires: python3-module-cffi
%endif

#setup_python_module %modulename

%description
PyNaCl is a Python binding to the Networking and Cryptography library,
a crypto library with the stated goal of improving usability, security
and speed.


%package -n python3-module-pynacl
Summary: Python binding to the Networking and Cryptography (NaCl) library
Group: Development/Python3

%description -n python3-module-pynacl
PyNaCl is a Python binding to the Networking and Cryptography library,
a crypto library with the stated goal of improving usability, security
and speed.


%prep
%setup
# Remove bundled libsodium, to be sure
rm -vrf src/libsodium/

%if_with python3
cp -fR . ../python3
%endif

%build
export SODIUM_INSTALL=system
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
%files -n python3-module-pynacl
%doc README.rst
%python3_sitelibdir/*
%endif


%changelog
* Mon Feb 12 2018 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1.1
- NMU: autorebuild with libsodium-1.0.16

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- initial build for ALT Sisyphus

