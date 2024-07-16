%define _unpackaged_files_terminate_build 1
%define pypi_name numcodecs
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.13.0
Release: alt1
Summary: Buffer compression and transformation codecs for use
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/numcodecs/
Vcs: https://github.com/zarr-developers/numcodecs
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: libblosc-devel
BuildRequires: libzstd-devel
BuildRequires: liblz4-devel
BuildRequires: libnumpy-py3-devel
%if_with check
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_metadata_extra msgpack
BuildRequires: python3-module-numpy-testing
%endif

%description
Numcodecs is a Python package providing buffer compression
and transformation codecs for use in data storage and communication applications.

%package tests
Summary: Tests for %pypi_name
Group: Development/Python3

%description tests
Numcodecs is a Python package providing buffer compression
and transformation codecs for use in data storage and communication applications.

This package contains tests for %pypi_name.

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
%pyproject_run -- \
    pytest --import-mode append -ra -o=addopts=-Wignore --pyargs %mod_name

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%mod_name/tests/

%files tests
%python3_sitelibdir/%mod_name/tests/

%changelog
* Mon Jul 15 2024 Stanislav Levin <slev@altlinux.org> 0.13.0-alt1
- 0.12.1 -> 0.13.0.

* Wed Mar 06 2024 Stanislav Levin <slev@altlinux.org> 0.12.1-alt1
- 0.11.0 -> 0.12.1.

* Fri Jun 23 2023 Stanislav Levin <slev@altlinux.org> 0.11.0-alt2
- Added compatibility with numpy 1.25.0.
- Modernized packaging.

* Sun Jan 15 2023 Grigory Ustinov <grenka@altlinux.org> 0.11.0-alt1
- Automatically updated to 0.11.0.

* Mon Aug 23 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.0-alt1
- Initial build for ALT.
