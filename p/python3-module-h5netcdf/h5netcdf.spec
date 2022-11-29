%define _unpackaged_files_terminate_build 1
%define oname h5netcdf

%def_with check

Name: python3-module-%oname
Version: 1.1.0
Release: alt1

Summary: Pythonic interface to netCDF4 via h5py
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/h5netcdf
# https://github.com/shoyer/h5netcdf.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-h5py python3-module-netCDF4
BuildRequires: python3-module-Cython
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-cftime
%endif

%py3_provides %oname
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

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
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

