%define _unpackaged_files_terminate_build 1
%define pypi_name coincidence

%def_with check

Name: python3-module-%pypi_name
Version: 0.6.3
Release: alt3

Summary: Helper functions for pytest
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/coincidence/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(whey)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_timeout)
BuildRequires: python3(pytest-datadir)
BuildRequires: python3(tox)
BuildRequires: python3(tox-envlist)
BuildRequires: python3(consolekit)
BuildRequires: python3(dist-meta)
BuildRequires: python3(handy-archives)
BuildRequires: python3(pyproject-parser)
BuildRequires: python3(shippinglabel)
%endif

BuildArch: noarch

%description
%summary

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Nov 14 2022 Stanislav Levin <slev@altlinux.org> 0.6.3-alt3
- Fixed FTBFS (pytest 7.2).

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 0.6.3-alt2
- enable tests

* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 0.6.3-alt1
- initial build for Sisyphus

