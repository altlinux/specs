%define _unpackaged_files_terminate_build 1
%define module_name dominate
%def_with check

Name: python3-module-%module_name
Version: 2.9.1
Release: alt1
Summary: Library for creating and manipulating HTML documents using an elegant DOM API
License: LGPL-3.0
Group: Development/Python3
Url: https://github.com/Knio/dominate
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

%description
Dominate is a Python library for creating and manipulating HTML documents using
an elegant DOM API. It allows you to write HTML pages in pure Python very
concisely, which eliminates the need to learn another template language, and
lets you take advantage of the more powerful features of Python.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/%module_name
%python3_sitelibdir/%module_name-%version.dist-info
%doc LICENSE.txt README.md

%changelog
* Sat Jan 20 2024 Alexander Makeenkov <amakeenk@altlinux.org> 2.9.1-alt1
- Updated to version 2.9.1.

* Fri Oct 07 2022 Alexander Makeenkov <amakeenk@altlinux.org> 2.7.0-alt1
- Updated to version 2.7.0

* Sun Mar 08 2020 Alexander Makeenkov <amakeenk@altlinux.org> 2.5.1-alt1
- New version

* Sat Feb 29 2020 Alexander Makeenkov <amakeenk@altlinux.org> 2.5.0-alt1
- New version
- Move tests in separate package

* Wed Oct 02 2019 Alexander Makeenkov <amakeenk@altlinux.org> 2.4.0-alt1
- Initial build for ALT
