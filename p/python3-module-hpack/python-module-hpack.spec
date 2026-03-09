%define pypi_name hpack

Name: python3-module-hpack
Version: 4.1.0
Release: alt1

Summary: Pure-Python HPACK header compression

Url: https://github.com/python-hyper/hpack
License: MIT
Group: Development/Python3

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%description
This module contains a pure-Python HTTP/2 header encoding (HPACK) logic for use
in Python programs that implement HTTP/2. It also contains a compatibility
layer that automatically enables the use of ``nghttp2`` if it's available.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/hpack/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Mar 10 2026 Vitaly Lipatov <lav@altlinux.ru> 4.1.0-alt1
- new version 4.1.0
- switch to pyproject_build

* Wed Apr 21 2021 Vitaly Lipatov <lav@altlinux.ru> 4.0.0-alt1
- new version (4.0.0) with rpmgs script
- build python3 module separately

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1.qa1
- NMU: applied repocop patch

* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- initial build for ALT Sisyphus
