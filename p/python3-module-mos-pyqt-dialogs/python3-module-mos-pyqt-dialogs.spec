%define pypi_name mos-pyqt-dialogs
%define mod_name mos_pyqt_dialogs
%define commit c89b9397350c8ca9b9d0c5dbc97b7aa1153c48e5

Name: python3-module-%pypi_name
Version: 1.1.0
Release: alt1

Summary: Qt dialogs and common functions for PyQt projects

License: GPL-3.0-only
Group: Development/Python3
Url: https://hub.mos.ru/mos/src/mos-pyqt-dialogs

BuildArch: noarch

# Source-url: https://hub.mos.ru/mos/src/mos-pyqt-dialogs/-/archive/%commit/mos-pyqt-dialogs-%commit.tar.gz
Source: %name-%version.tar
Patch: %name-1.1.0-alt-fix-imports.patch

BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%description
Common dialog windows (alert, question, password, wait box) and helper
functions (current graphical user, log trimming) for PyQt5 and PyQt6
applications on Linux. The functions can also work in console mode.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{mod_name}-*.dist-info/
%doc README.md

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for Sisyphus
