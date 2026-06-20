%define _unpackaged_files_terminate_build 1
%define pypi_name covdefaults

%def_with check

Name: python3-module-%pypi_name
Version: 2.3.0
Release: alt2

Summary: A coverage plugin to provide sensible default settings
License: MIT
Group: Development/Python3

Url: https://pypi.org/project/covdefaults/
Vcs: https://github.com/asottile/covdefaults

BuildArch: noarch

Source: %name-%version.tar
Patch: support-coverage-7.7.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-coverage
%endif

%description
%summary.

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.md
%python3_sitelibdir/*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sat Jun 20 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.3.0-alt2
- fixed FTBFS

* Wed Jul 26 2023 Anton Zhukharev <ancieg@altlinux.org> 2.3.0-alt1
- Updated to 2.3.0.

* Mon Feb 13 2023 Anton Zhukharev <ancieg@altlinux.org> 2.2.2-alt1
- 2.2.0 -> 2.2.2

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 2.2.0-alt1
- initial build for Sisyphus

