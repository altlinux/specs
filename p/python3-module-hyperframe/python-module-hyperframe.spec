%def_without check

%define modulename hyperframe
Name: python3-module-hyperframe
Version: 6.0.1
Release: alt1

Summary: HTTP/2 framing layer for Python

Url: https://github.com/python-hyper/hyperframe
License: MIT
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.io/packages/source/h/%modulename/%modulename-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
This library contains the HTTP/2 framing code used in the `hyper`_ project. It
provides a pure-Python codebase that is capable of decoding a binary stream
into HTTP/2 frames.

This library is used directly by `hyper`_ and a number of other projects to
provide HTTP/2 frame decoding logic.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*


%changelog
* Wed Apr 21 2021 Vitaly Lipatov <lav@altlinux.ru> 6.0.1-alt1
- new version (6.0.1) with rpmgs script
- build python3 module standalone

* Sun Jun 09 2019 Vitaly Lipatov <lav@altlinux.ru> 5.2.0-alt1
- new version 5.2.0 (with rpmrb script)

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 5.1.0-alt1.qa1
- NMU: applied repocop patch

* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 5.1.0-alt1
- initial build for ALT Sisyphus
