%def_without check
%def_with python3

%define modulename pymacaroons-pynacl
Name: python-module-pymacaroons-pynacl
Version: 0.13.0
Release: alt1

Summary: Library providing non-opaque cookies for authorization

Url: https://github.com/ecordell/pymacaroons
License: MIT
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/ecordell/pymacaroons/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools

BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

#setup_python_module %modulename

%description
This is a Python re-implementation of the libmacaroons C library.
Macaroons, like cookies, are a form of bearer credential. Unlike
opaque tokens, macaroons embed caveats that define specific authorization
requirements for the target service, the service that issued the root macaroon
and which is capable of verifying the integrity of macaroons it receives.

Macaroons allow for delegation and attenuation of authorization. They are
simple and fast to verify, and decouple authorization policy from the
enforcement of that policy.


%package -n python3-module-pymacaroons-pynacl
Summary: Library providing non-opaque cookies for authorization
Group: Development/Python3

%description -n python3-module-pymacaroons-pynacl
This is a Python re-implementation of the libmacaroons C library.
Macaroons, like cookies, are a form of bearer credential. Unlike
opaque tokens, macaroons embed caveats that define specific authorization
requirements for the target service, the service that issued the root macaroon
and which is capable of verifying the integrity of macaroons it receives.


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
%doc README.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-pymacaroons-pynacl
%doc README.md
%python3_sitelibdir/*
%endif


%changelog
* Wed Feb 06 2019 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- new version 0.13.0 (with rpmrb script)

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1.qa1
- NMU: applied repocop patch

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt1
- initial build for ALT Sisyphus

