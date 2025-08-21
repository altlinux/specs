%define oname hdf5storage

%def_with check

Name: python3-module-%oname
Version: 0.2.1
Release: alt1

Summary: Utilities to read/write Python types to/from HDF5 files, including MATLAB v7.3 MAT files
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/hdf5storage
Vcs: https://github.com/jclds139/hdf5storage

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-h5py
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-scipy
BuildRequires: python3-module-matplotlib
%endif

%py3_provides %oname
%py3_requires numpy h5py


%description
This Python package provides high level utilities to read/write a
variety of Python types to/from HDF5 (Heirarchal Data Format) formatted
files. This package also provides support for MATLAB MAT v7.3 formatted
files, which are just HDF5 files with a different extension and some
extra meta-data.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%ifarch i586
%pyproject_run_pytest -k "not test_read_empty"
%else
%pyproject_run_pytest -v
%endif

%files
%doc README.*
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Wed Aug 20 2025 Anton Vyatkin <toni@altlinux.org> 0.2.1-alt1
- New version 0.2.1.

* Sat Jun 14 2025 Anton Vyatkin <toni@altlinux.org> 0.2.0-alt2
- Change upstream remotes.
- Fixed FTBFS (numpy2).

* Sat Apr 20 2024 Anton Vyatkin <toni@altlinux.org> 0.2-alt1.1
- Fixed FTBFS.

* Thu Mar 23 2023 Anton Vyatkin <toni@altlinux.org> 0.2-alt1
- new version 0.2

* Thu Nov 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.14-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.14-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.14-alt1
- Updated to upstream version 0.1.14.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.git20150209.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1.git20150209.1
- NMU: Use buildreq for BR.

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150209
- Initial build for Sisyphus

