%define _unpackaged_files_terminate_build 1
%define pypi_name oldest-supported-numpy
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2023.8.3
Release: alt1
Summary: Oldest NumPy that supports a given Python version and platform
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/oldest-supported-numpy
Vcs: https://github.com/scipy/oldest-supported-numpy
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# devel files are shipped with subpackage
Requires: libnumpy-py3-devel
# tests/testing are shipped with subpackage
Requires: python3-module-numpy-tests
Requires: python3-module-numpy-testing
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This is a meta-package which can be used in pyproject.toml files to
automatically provide as a build-time dependency the oldest version of NumPy
that supports the given Python version and platform. In case of platforms for
which NumPy has prebuilt wheels, the provided version also has a prebuilt NumPy
wheel.

The reason to use the oldest available NumPy version as a build-time dependency
is because of ABI compatibility. Binaries compiled with old NumPy versions are
binary compatible with newer NumPy versions, but not vice versa. This
meta-package exists to make dealing with this more convenient, without having to
duplicate the same list manually in all packages requiring it.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile tests/requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# test_valid_numpy_is_installed checks if oldest-supported-numpy pulls
# correct numpy, but we allow any version
%pyproject_run_pytest -ra -Wignore -k 'not test_valid_numpy_is_installed'

%files
%doc README.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Aug 07 2023 Stanislav Levin <slev@altlinux.org> 2023.8.3-alt1
- 2022.11.19 -> 2023.8.3.

* Wed Jun 21 2023 Stanislav Levin <slev@altlinux.org> 2022.11.19-alt1
- Initial build for Sisyphus.
