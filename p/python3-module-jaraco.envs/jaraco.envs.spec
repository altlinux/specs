%define _unpackaged_files_terminate_build 1
%define pypi_name jaraco.envs

%def_with check

Name: python3-module-%pypi_name
Version: 2.4.0
Release: alt2
Summary: Classes for orchestrating Python virtual environments
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jaraco.envs/
Vcs: https://github.com/jaraco/jaraco.envs.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%py3_requires virtualenv
%py3_requires tox
# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
%pypi_name provides classes for orchestrating Python virtual environments.

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
%python3_sitelibdir/jaraco/__pycache__/envs.cpython-*.py*
%python3_sitelibdir/jaraco/envs.py
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Fri Apr 21 2023 Stanislav Levin <slev@altlinux.org> 2.4.0-alt2
- Mapped PyPI name to distro's one.

* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 2.4.0-alt1
- 2.3.0 -> 2.4.0.

* Tue Apr 05 2022 Stanislav Levin <slev@altlinux.org> 2.3.0-alt1
- 2.2.0 -> 2.3.0.

* Tue Jan 11 2022 Stanislav Levin <slev@altlinux.org> 2.2.0-alt1
- 2.1.1 -> 2.2.0.

* Fri Mar 26 2021 Stanislav Levin <slev@altlinux.org> 2.1.1-alt1
- Initial build for Sisyphus.
