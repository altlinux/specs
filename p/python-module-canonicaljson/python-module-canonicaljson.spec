%def_without check
%def_with python3

%define modulename canonicaljson
Name: python-module-canonicaljson
Version: 1.0.0
Release: alt1

Summary: Canonical JSONs

Url: https://github.com/matrix-org/python-canonicaljson
License: ASL 2.0
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/matrix-org/python-canonicaljson/archive/v%version.tar.gz
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
* Encodes objects and arrays as RFC 7159 JSON.
* Sorts object keys so that you get the same result each time.
* Has no inignificant whitespace to make the output as small as possible.
* Escapes only the characters that must be escaped,
  U+0000 to U+0019 / U+0022 / U+0056, to keep the output as small as possible.
* Uses the shortest escape sequence for each escaped character.
* Encodes the JSON as UTF-8.
* Can encode frozendict immutable dictionaries.


%package -n python3-module-canonicaljson
Summary: Sign JSON with Ed25519 signatures
Group: Development/Python3

%description -n python3-module-canonicaljson
Features:
* Encodes objects and arrays as RFC 7159 JSON.
* Sorts object keys so that you get the same result each time.
* Has no inignificant whitespace to make the output as small as possible.
* Escapes only the characters that must be escaped,
  U+0000 to U+0019 / U+0022 / U+0056, to keep the output as small as possible.
* Uses the shortest escape sequence for each escaped character.
* Encodes the JSON as UTF-8.
* Can encode frozendict immutable dictionaries.


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
%files -n python3-module-canonicaljson
%doc README.rst
%python3_sitelibdir/*
%endif


%changelog
* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Sisyphus

