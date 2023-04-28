%define _unpackaged_files_terminate_build 1
%define pypi_name jaraco.path

%def_with check

Name: python3-module-%pypi_name
Version: 3.5.0
Release: alt1
Summary: Cross platform hidden file detection
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jaraco.path/
VCS: https://github.com/jaraco/jaraco.path
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%py3_provides %pypi_name
# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
%pypi_name provides cross platform hidden file detection.

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
%python3_sitelibdir/jaraco/__pycache__/path.cpython-*.py*
%python3_sitelibdir/jaraco/path.py
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Fri Apr 21 2023 Stanislav Levin <slev@altlinux.org> 3.5.0-alt1
- 3.4.1 -> 3.5.0.

* Tue Feb 21 2023 Stanislav Levin <slev@altlinux.org> 3.4.1-alt1
- 3.4.0 -> 3.4.1.

* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 3.4.0-alt1
- 3.3.1 -> 3.4.0.

* Fri Mar 26 2021 Stanislav Levin <slev@altlinux.org> 3.3.1-alt1
- Initial build for Sisyphus.
