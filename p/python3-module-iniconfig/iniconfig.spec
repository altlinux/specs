%define _unpackaged_files_terminate_build 1
%define pypi_name iniconfig

%def_with check

Name: python3-module-%pypi_name
Version: 2.1.0
Release: alt1
Summary: A small and simple INI-file parser
License: MIT
Group: Development/Tools
Url: https://pypi.org/project/iniconfig/
VCS: https://github.com/pytest-dev/iniconfig
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary

%prep
%setup
%patch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_hatch pyproject.toml test
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc CHANGELOG README.rst
%python3_sitelibdir/iniconfig/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Mar 20 2025 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- 2.0.0 -> 2.1.0.

* Tue Jan 24 2023 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1
- 1.1.1 -> 2.0.0.

* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 1.1.1-alt1
- 1.0.0 -> 1.1.1.
- Built Python3 package from its ows src.

* Thu Aug 08 2019 Stanislav Levin <slev@altlinux.org> 1.0.0-alt2
- Fixed testing against Pytest 5.

* Sat Mar 16 2019 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- Initial build.

