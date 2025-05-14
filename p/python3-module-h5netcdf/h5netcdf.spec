%define _unpackaged_files_terminate_build 1
%define pypi_name h5netcdf

%def_with check

Name: python3-module-%pypi_name
Version: 1.6.1
Release: alt2

Summary: Pythonic interface to netCDF4 via h5py
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/h5netcdf
VCS: https://github.com/shoyer/h5netcdf
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject

%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra test
BuildRequires: python3-module-numpy-testing
%endif

%py3_provides %pypi_name
%py3_requires h5py

%description
A Python interface for the netCDF4 file-format that reads and writes
HDF5 files API directly via h5py, without relying on the Unidata netCDF
library.

This is an experimental project. It currently passes basic tests for
reading and writing netCDF4 files with Python, but it has not been
tested for compatibility with other netCDF4 interfaces.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build

export SETUPTOOLS_SCM_PRETEND_VERSION="%version"
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE *.rst
%python3_sitelibdir/h5netcdf/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed May 14 2025 Ivan Khanas <xeno@altlinux.org> 1.6.1-alt2
- Maintainer`s work.

* Fri Apr 11 2025 Ivan Khanas <xeno@altlinux.org> 1.6.1-alt1
- New version.
- Migrate to pyproject macros.

* Tue Jan 23 2024 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt1
- Automatically updated to 1.3.0.

* Tue Jun 13 2023 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt1
- Automatically updated to 1.2.0.

* Tue Nov 29 2022 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1
- Automatically updated to 1.1.0.

* Mon Oct 31 2022 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt1
- Automatically updated to 1.0.2.
- Build with check.

* Wed Mar 24 2021 Grigory Ustinov <grenka@altlinux.org> 0.10.0-alt1
- Build new version.
- Fixed Build Requires (Fixed FTBFS).

* Fri Nov 15 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.7.4-alt1
- Version updated to 0.7.4
- python2 disabled

* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 0.5.0-alt2
- Added missing dep on `numpy.testing`.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.0-alt1
- Updated to upstream version 0.5.0.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1.dev0-alt1.git20150531.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1.dev0-alt1.git20150531
- Initial build for Sisyphus

