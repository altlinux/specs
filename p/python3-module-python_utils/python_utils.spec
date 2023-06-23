%define _unpackaged_files_terminate_build 1
%define pypi_name python-utils
%define mod_name python_utils

%def_with check

Name: python3-module-%mod_name
Version: 3.7.0
Release: alt1
Summary: A module with some convenient utilities not included with the standard Python install
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/python-utils/
Vcs: https://github.com/WoLpH/python-utils
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# mapping from PyPI name
Provides: python3-module-%pypi_name = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra tests
%endif

%description
Python Utils is a collection of small Python functions and classes which
make common patterns shorter and easier. It is by no means a complete
collection but it has served me quite a bit in the past and I will keep
extending it.

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
%pyproject_run_pytest -ra -o=addopts=-Wignore

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}/

%changelog
* Fri Jun 23 2023 Stanislav Levin <slev@altlinux.org> 3.7.0-alt1
- 3.6.1 -> 3.7.0.

* Mon Jun 19 2023 Stanislav Levin <slev@altlinux.org> 3.6.1-alt1
- 3.1.0 -> 3.6.1.

* Fri Mar 11 2022 Stanislav Levin <slev@altlinux.org> 3.1.0-alt1
- 2.5.6 -> 3.1.0.

* Mon Apr 26 2021 Stanislav Levin <slev@altlinux.org> 2.5.6-alt1
- 2.2.0 -> 2.5.6.

* Wed Apr 15 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.2.0-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 22 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.0-alt1
- Updated to upstream version 2.2.0.
- Enabled build for python-3.

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.2-alt1.git20150209
- Version 1.6.2

* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1.git20141015
- Initial build for Sisyphus

