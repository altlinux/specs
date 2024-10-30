%define _unpackaged_files_terminate_build 1
%define pypi_name makefun
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.15.6
Release: alt2

Summary: Dynamically create python functions with a proper signature
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/makefun/
Vcs: https://github.com/smarie/python-makefun

BuildArch: noarch

Source0: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

%description
Small library to dynamically create python functions.

%prep
%setup
%autopatch -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.md docs
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Oct 25 2024 Grigory Ustinov <grenka@altlinux.org> 1.15.6-alt2
- Fixed building scheme for backport to stable branches.

* Mon Sep 30 2024 Anton Zhukharev <ancieg@altlinux.org> 1.15.6-alt1
- Updated to 1.15.6.

* Wed Jul 17 2024 Anton Zhukharev <ancieg@altlinux.org> 1.15.4-alt1
- Updated to 1.15.4.

* Fri Jul 05 2024 Anton Zhukharev <ancieg@altlinux.org> 1.15.3-alt1
- Updated to 1.15.3.

* Fri Nov 10 2023 Anton Zhukharev <ancieg@altlinux.org> 1.15.2-alt1
- Updated to 1.15.2.

* Tue Aug 01 2023 Anton Zhukharev <ancieg@altlinux.org> 1.15.1-alt1
- Updated to 1.15.1.

* Wed Sep 28 2022 Anton Zhukharev <ancieg@altlinux.org> 1.15.0-alt1
- 1.14.0 -> 1.15.0
- clean up spec
- fix description

* Sat Jul 23 2022 Anton Zhukharev <ancieg@altlinux.org> 1.14.0-alt1
- initial build for Sisyphus

