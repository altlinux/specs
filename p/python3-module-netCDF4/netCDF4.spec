%define _unpackaged_files_terminate_build 1
%define pypi_name netCDF4
%def_with check

Name: python3-module-%pypi_name
Version: 1.7.2
Release: alt1

Summary: Python/numpy interface to netCDF library (versions 3 and 4)
License: BSD / MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/netCDF4/
Vcs: https://github.com/Unidata/netcdf4-python.git

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata

Provides: python3-module-%{pep503_name %pypi_name} = %EVR

BuildRequires(pre): rpm-build-pyproject
BuildRequires: libnetcdf-devel
BuildRequires: zlib-devel
BuildRequires: libjpeg-devel
BuildRequires: libcurl-devel
BuildRequires: libnumpy-py3-devel
BuildRequires: libhdf5-devel
# For generating documentation.
BuildRequires: python3-module-pdoc3

%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra tests
BuildRequires: netcdf-tools
BuildRequires: python3-module-numpy-testing
%endif

Conflicts: python-module-%pypi_name
Obsoletes: python-module-%pypi_name

%py3_provides %pypi_name

%description
netCDF version 4 has many features not found in earlier versions of the
library and is implemented on top of HDF5. This module can read and
write files in both the new netCDF 4 and the old netCDF 3 format, and
can create files that are readable by HDF5 clients. The API modelled
after Scientific.IO.NetCDF, and should be familiar to users of that
module.

Most new features of netCDF 4 are implemented, such as multiple
unlimited dimensions, groups and zlib data compression. All the new
numeric data types (such as 64 bit and unsigned integer types) are
implemented. Compound and variable length (vlen) data types are
supported, but the enum and opaque data types are not. Mixtures of
compound and vlen data types (compound types containing vlens, and vlens
containing compound types) are not supported.

%package docs
Summary: Documentation for %pypi_name
Group: Development/Documentation
BuildArch: noarch

%description docs
netCDF version 4 has many features not found in earlier versions of the
library and is implemented on top of HDF5. This module can read and
write files in both the new netCDF 4 and the old netCDF 3 format, and
can create files that are readable by HDF5 clients. The API modelled
after Scientific.IO.NetCDF, and should be familiar to users of that
module.

Most new features of netCDF 4 are implemented, such as multiple
unlimited dimensions, groups and zlib data compression. All the new
numeric data types (such as 64 bit and unsigned integer types) are
implemented. Compound and variable length (vlen) data types are
supported, but the enum and opaque data types are not. Mixtures of
compound and vlen data types (compound types containing vlens, and vlens
containing compound types) are not supported.

This package contains documentation for %pypi_name.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%pyproject_run -- pdoc3 --html --output-dir ./docs/ netCDF4

%install
%pyproject_install

%check
pushd test
export NO_NET=1

export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 run_all.py
popd

%files
%doc LICENSE
%_bindir/*
%python3_sitelibdir/netCDF4/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%files docs
%doc docs/netCDF4/index.html

%changelog
* Wed Aug 13 2025 Anton Vyatkin <toni@altlinux.org> 1.7.2-alt1
- New version 1.7.2.

* Thu Jul 24 2025 Anton Vyatkin <toni@altlinux.org> 1.7.1-alt3
- Fixed FTBFS.

* Wed May 14 2025 Ivan Khanas <xeno@altlinux.org> 1.7.1-alt2
- Fix FTBFS: change %%files with distinfo macro.

* Thu Apr 10 2025 Ivan Khanas <xeno@altlinux.org> 1.7.1-alt1
- New version.
- Migrate to pyproject macros.
- Fix documentation packaging.

* Mon Apr 19 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.6-alt2
- Rebuilt with new libhdf5.

* Thu Mar 18 2021 Grigory Ustinov <grenka@altlinux.org> 1.5.6-alt1
- Build new version.

* Thu Jan 21 2021 Grigory Ustinov <grenka@altlinux.org> 1.5.5.1-alt1
- Build new version.

* Fri Sep 04 2020 Grigory Ustinov <grenka@altlinux.org> 1.2.9-alt4
- Drop python2 support.

* Thu Apr 11 2019 Grigory Ustinov <grenka@altlinux.org> 1.2.9-alt3
- Rebuild for python3.7.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.9-alt2.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.9-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.9-alt2
- Rebuilt with new libnetcdf11.

* Thu Aug 24 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.9-alt1
- Updated to upstream version 1.2.9.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.9-alt1.git20150728.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.9-alt1.git20150728.1
- NMU: Use buildreq for BR.

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.9-alt1.git20150728
- New snapshot

* Mon Jul 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.9-alt1.git20150722
- Version 1.1.9

* Thu Apr 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.8-alt1.git20150416
- Version 1.1.8

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.5-alt1.git20150303
- Version 1.1.5

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.git20141218
- Version 1.1.3

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.git20141116
- Initial build for Sisyphus

