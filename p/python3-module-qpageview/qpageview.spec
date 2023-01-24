Name: python3-module-qpageview
Version: 0.6.2
Release: alt1

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
# will failed with LANG=C
export LANG=en_US.UTF8
%python3_check test

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Wed Jan 25 2023 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt1
- initial build for ALT Sisyphus

