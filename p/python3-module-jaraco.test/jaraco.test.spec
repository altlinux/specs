%define _unpackaged_files_terminate_build 1
%define pypi_name jaraco.test

%def_with check

Name: python3-module-%pypi_name
Version: 5.4.0
Release: alt3
Summary: Testing support by jaraco
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jaraco.test
VCS: https://github.com/jaraco/jaraco.test.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
# required by jaraco/test/cpython.py
Requires: python3-test

# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra testing
# required by jaraco/test/cpython.py
BuildRequires: python3-test
%endif

%description
%summary.

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
%pyproject_run_pytest -vra -oconsider_namespace_packages=True

%files
%doc README.rst
%python3_sitelibdir/jaraco/test/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Thu May 16 2024 Stanislav Levin <slev@altlinux.org> 5.4.0-alt3
- Added missing runtime dependency on python3-test.

* Mon May 06 2024 Stanislav Levin <slev@altlinux.org> 5.4.0-alt2
- Fixed FTBFS (Pytest 8.1.1).

* Thu Mar 21 2024 Stanislav Levin <slev@altlinux.org> 5.4.0-alt1
- 5.3.0 -> 5.4.0.

* Fri Apr 21 2023 Stanislav Levin <slev@altlinux.org> 5.3.0-alt2
- Mapped PyPI name to distro's one.

* Wed Feb 01 2023 Stanislav Levin <slev@altlinux.org> 5.3.0-alt1
- Initial build for Sisyphus.
