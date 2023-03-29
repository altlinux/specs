%define _unpackaged_files_terminate_build 1
%define pypi_name hatch-requirements-txt

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.0
Release: alt1

Summary: Hatchling plugin to read project dependencies from requirements.txt
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/hatch-requirements-txt/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(hatchling)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-datadir)
BuildRequires: python3(coincidence)
BuildRequires: python3(handy-archives)
BuildRequires: python3(dist-meta)
BuildRequires: python3(pkginfo)
%endif

BuildArch: noarch

%py3_provides %pypi_name

%description
Hatchling plugin to read project dependencies from requirements.txt

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE README.rst
%python3_sitelibdir/hatch_requirements_txt/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 29 2023 Anton Zhukharev <ancieg@altlinux.org> 0.4.0-alt1
- New version.

* Mon Feb 13 2023 Anton Zhukharev <ancieg@altlinux.org> 0.3.0-alt1
- 0.1.1 -> 0.3.0

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 0.1.1-alt1
- initial build for Sisyphus

