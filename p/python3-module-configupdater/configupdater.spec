%define _unpackaged_files_terminate_build 1
%define pypi_name configupdater

%def_with check

Name: python3-module-%pypi_name
Version: 3.2
Release: alt1
Summary: Parser like ConfigParser but for updating configuration files
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/configupdater
Vcs: https://github.com/pyscaffold/configupdater
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
The sole purpose of ConfigUpdater is to easily update an INI config file with no
changes to the original file except the intended ones. This means comments, the
ordering of sections and key/value-pairs as wells as their cases are kept as in
the original file. Thus ConfigUpdater provides complementary functionality to
Python's ConfigParser which is primarily meant for reading config files and
writing new ones.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc README.rst
%python3_sitelibdir/configupdater/
%python3_sitelibdir/ConfigUpdater-%version.dist-info/

%changelog
* Fri Mar 01 2024 Stanislav Levin <slev@altlinux.org> 3.2-alt1
- 3.1.1 -> 3.2.

* Tue Aug 09 2022 Stanislav Levin <slev@altlinux.org> 3.1.1-alt1
- 3.1 -> 3.1.1.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 3.1-alt1
- Initial build for Sisyphus.
