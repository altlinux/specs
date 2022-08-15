%define _unpackaged_files_terminate_build 1
%define pypi_name hatch-vcs

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.0
Release: alt2

Summary: Hatch plugin for versioning with your preferred VCS
License: MIT
Group: Development/Python3
# Source-git: https://github.com/ofek/hatch-vcs.git
Url: https://pypi.org/project/hatch-vcs

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(hatchling)

%if_with check
# dependencies=
BuildRequires: python3(setuptools-scm)
BuildRequires: python3(hatchling)

BuildRequires: python3(pytest)
%endif

BuildArch: noarch

# PEP503 name
%py3_provides %pypi_name

# lazy import
%py3_requires setuptools_scm

%description
%pypi_name provides a plugin for Hatch that uses your preferred version control
system (like Git) to determine project versions.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject -- -vra tests

%files
%doc README.md
%python3_sitelibdir/hatch_vcs/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 0.2.0-alt2
- Fixed FTBFS (setuptools_scm 7).

* Mon Apr 04 2022 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus.
