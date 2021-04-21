%def_without check

%define modulename hpack

Name: python3-module-hpack
Version: 4.0.0
Release: alt1

Summary: Pure-Python HPACK header compression

Url: https://github.com/python-hyper/hpack
License: MIT
Group: Development/Python3

# Source-url: https://pypi.io/packages/source/h/%modulename/%modulename-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
This module contains a pure-Python HTTP/2 header encoding (HPACK) logic for use
in Python programs that implement HTTP/2. It also contains a compatibility
layer that automatically enables the use of ``nghttp2`` if it's available.

%prep
%setup
# hack encoding issue
echo > README.rst
echo > HISTORY.rst

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*

%changelog
* Wed Apr 21 2021 Vitaly Lipatov <lav@altlinux.ru> 4.0.0-alt1
- new version (4.0.0) with rpmgs script
- build python3 module separately

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1.qa1
- NMU: applied repocop patch

* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- initial build for ALT Sisyphus
