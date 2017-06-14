%def_without check
%def_with python3

%define modulename signedjson
Name: python-module-signedjson
Version: 1.0.0
Release: alt1

Summary: Sign JSON with Ed25519 signatures

Url: https://github.com/matrix-org/python-signedjson
License: ASL 2.0
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/matrix-org/python-signedjson/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools

BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

#setup_python_module %modulename

%description
Features:
* More than one entity can sign the same object.
* Each entity can sign the object with more than one key making it easier
  to rotate keys
* ED25519 can be replaced with a different algorithm.
* Unprotected data can be added to the object under the "unsigned" key.


%package -n python3-module-signedjson
Summary: Sign JSON with Ed25519 signatures
Group: Development/Python3

%description -n python3-module-signedjson
Features:
* More than one entity can sign the same object.
* Each entity can sign the object with more than one key making it easier
  to rotate keys
* ED25519 can be replaced with a different algorithm.
* Unprotected data can be added to the object under the "unsigned" key.


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
%files -n python3-module-signedjson
%doc README.rst
%python3_sitelibdir/*
%endif


%changelog
* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Sisyphus

