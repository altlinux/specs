%define _unpackaged_files_terminate_build 1
%define pypi_name icontract
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.7.1
Release: alt1
Summary: Design-by-contract in Python3 with informative violation messages and inheritance
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/icontract/
Vcs: https://github.com/Parquery/icontract.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# not packaged
%add_pyproject_deps_check_filter deal
%add_pyproject_deps_check_filter dpcontracts
%pyproject_builddeps_metadata_extra dev
# skipped by default filter
BuildRequires: python3-module-mypy
%endif

%description
Icontract provides design-by-contract to Python3 with informative
violation messages and inheritance.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# see for details: precommit.py
export ICONTRACT_SLOW=true
%pyproject_run_unittest discover -v

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Feb 07 2025 Stanislav Levin <slev@altlinux.org> 2.7.1-alt1
- 2.6.6 -> 2.7.1.

* Wed Jun 19 2024 Dmitry Lyalyaev <fruktime@altlinux.org> 2.6.6-alt1
- Initial build for ALT Linux
