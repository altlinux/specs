%def_without check

Name: python3-module-signedjson
Version: 1.1.1
Release: alt1

Summary: Sign JSON with Ed25519 signatures

Url: https://github.com/matrix-org/python-signedjson
License: ASL 2.0
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/matrix-org/python-signedjson/archive/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro
BuildRequires: python3-base python3-module-setuptools python3-module-setuptools_scm

%add_python3_req_skip importlib_metadata

%py3_use canonicaljson >= 1.0.0
%py3_use unpaddedbase64 >= 1.0.1
%py3_use pynacl >= 0.3.0
%py3_use typing-extensions >= 3.5
# As of Python 3.8, this functionality has been added to the Python standard library.
#py3_use importlib-metadata

%description
Features:
* More than one entity can sign the same object.
* Each entity can sign the object with more than one key making it easier
  to rotate keys
* ED25519 can be replaced with a different algorithm.
* Unprotected data can be added to the object under the "unsigned" key.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build_debug

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Fri Jan 22 2021 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- new version 1.1.1 (with rpmrb script)

* Thu Feb 20 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version 1.1.0 (with rpmrb script)

* Thu Feb 20 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- build new python3 package

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1.qa1
- NMU: applied repocop patch

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Sisyphus

