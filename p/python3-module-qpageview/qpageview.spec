Name: python3-module-qpageview
Version: 0.6.2
Release: alt2

Summary: page-based viewer widget for Qt5/PyQt5

Url: https://github.com/frescobaldi/qpageview
License: GPLv3
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/frescobaldi/qpageview/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro
BuildRequires: gcc-c++

%py3_use PyQt5

%description
page-based viewer widget for Qt5/PyQt5.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
# upstream doesn't provide tests suite

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Fri Oct 25 2024 Stanislav Levin <slev@altlinux.org> 0.6.2-alt2
- Disabled check (see #50996).

* Wed Jan 25 2023 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt1
- initial build for ALT Sisyphus

