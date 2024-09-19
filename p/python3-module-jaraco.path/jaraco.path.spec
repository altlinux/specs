%define _unpackaged_files_terminate_build 1
%define pypi_name jaraco.path
%define ns_name jaraco
%define mod_name path

%def_with check

Name: python3-module-%pypi_name
Version: 3.7.1
Release: alt1
Summary: Miscellaneous path functions
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jaraco.path/
VCS: https://github.com/jaraco/jaraco.path
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
%pypi_name provides miscellaneous path functions.

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
%pyproject_run_pytest -ra -Wignore

%files
%doc README.rst
%dir %python3_sitelibdir/%ns_name/
%python3_sitelibdir/%ns_name/__pycache__/
%python3_sitelibdir/%ns_name/__pycache__/%mod_name.*
%python3_sitelibdir/%ns_name/%mod_name.py
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Thu Sep 19 2024 Stanislav Levin <slev@altlinux.org> 3.7.1-alt1
- 3.7.0 -> 3.7.1.

* Fri Jul 21 2023 Stanislav Levin <slev@altlinux.org> 3.7.0-alt1
- 3.6.0 -> 3.7.0.

* Tue Jun 20 2023 Stanislav Levin <slev@altlinux.org> 3.6.0-alt1
- 3.5.0 -> 3.6.0.

* Fri Apr 21 2023 Stanislav Levin <slev@altlinux.org> 3.5.0-alt1
- 3.4.1 -> 3.5.0.

* Tue Feb 21 2023 Stanislav Levin <slev@altlinux.org> 3.4.1-alt1
- 3.4.0 -> 3.4.1.

* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 3.4.0-alt1
- 3.3.1 -> 3.4.0.

* Fri Mar 26 2021 Stanislav Levin <slev@altlinux.org> 3.3.1-alt1
- Initial build for Sisyphus.
