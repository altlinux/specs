%define _unpackaged_files_terminate_build 1
%define module_name qasync
%def_with check

Name: python3-module-%module_name
Version: 0.28.0
Release: alt1
Summary: Python library for using asyncio in Qt-based applications
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/qasync
VCS: https://github.com/CabbageDevelopment/qasync

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-uv-build

%if_with check
BuildRequires: python3-module-PyQt6
BuildRequires: python3-module-pyside6
%endif

%description
qasync allows coroutines to be used in PyQt/PySide applications
by providing an implementation of the PEP 3156 event loop.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
export QT_QPA_PLATFORM=offscreen
%pyproject_run_pytest

%files
%python3_sitelibdir/%module_name
%python3_sitelibdir/%{pyproject_distinfo %module_name}
%exclude %python3_sitelibdir/%module_name/_windows.py
%doc LICENSE

%changelog
* Sat Jun 13 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.28.0-alt1
- Updated to version 0.28.0.

* Tue Dec 03 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.27.1-alt1
- Initial build for ALT.
