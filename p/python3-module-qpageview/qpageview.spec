Name: python3-module-qpageview
Version: 1.0.3
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
BuildRequires: python3-module-hatchling

%add_python3_req_skip PyQt6.QtPdf

%description
page-based viewer widget for Qt5/PyQt5.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst
%python3_sitelibdir/qpageview/
%python3_sitelibdir/%{pyproject_distinfo qpageview}/

%changelog
* Sun Mar 08 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- new version 1.0.3
- switch to pyproject build (hatchling)
- skip PyQt6.QtPdf dependency (not in Sisyphus)

* Fri Oct 25 2024 Stanislav Levin <slev@altlinux.org> 0.6.2-alt2
- Disabled check (see #50996).

* Wed Jan 25 2023 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt1
- initial build for ALT Sisyphus
