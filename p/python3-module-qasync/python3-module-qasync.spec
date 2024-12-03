%define _unpackaged_files_terminate_build 1
%define module_name qasync

Name: python3-module-%module_name
Version: 0.27.1
Release: alt1
Summary: Python library for using asyncio in Qt-based applications
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/qasync
VCS: https://github.com/CabbageDevelopment/qasync

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry

%description
qasync allows coroutines to be used in PyQt/PySide applications
by providing an implementation of the PEP 3156 event loop.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%module_name
%python3_sitelibdir/%{pyproject_distinfo %module_name}
%exclude %python3_sitelibdir/%module_name/_windows.py
%doc LICENSE

%changelog
* Tue Dec 03 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.27.1-alt1
- Initial build for ALT.
