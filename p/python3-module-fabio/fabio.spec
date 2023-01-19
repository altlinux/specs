%define _unpackaged_files_terminate_build 1

%define oname fabio

# check disabled because it relies a lot on network
%def_disable check

Name: python3-module-%oname
Version: 2022.12.1
Release: alt1
Summary: Image IO for fable
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/fabio

# https://github.com/silx-kit/fabio.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: libnumpy-py3-devel python3-module-Cython
BuildRequires: python3(lxml)

%add_python3_req_skip UserDict
%py3_requires argparse gzip six

%description
FabIO is an I/O library for images produced by 2D X-ray detectors and written in Python.
FabIO support images detectors from a dozen of companies (including Mar, Dectris, ADSC, Hamamatsu, Oxford, ...),
for a total of 20 different file formats (like CBF, EDF, TIFF, ...) and offers an unified interface to their
headers (as a python dictionary) and datasets (as a numpy ndarray of integers or floats).

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
FabIO is an I/O library for images produced by 2D X-ray detectors and written in Python.
FabIO support images detectors from a dozen of companies (including Mar, Dectris, ADSC, Hamamatsu, Oxford, ...),
for a total of 20 different file formats (like CBF, EDF, TIFF, ...) and offers an unified interface to their
headers (as a python dictionary) and datasets (as a numpy ndarray of integers or floats).

This package contains tests for %oname.

%prep
%setup

# remove some third-party bundled stuff
rm -rf fabio/third_party/_local

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc README.rst
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test

%files tests
%python3_sitelibdir/%oname/test

%changelog
* Thu Jan 19 2023 Grigory Ustinov <grenka@altlinux.org> 2022.12.1-alt1
- Automatically updated to 2022.12.1.

* Fri Jun 03 2022 Grigory Ustinov <grenka@altlinux.org> 0.14.0-alt1
- Automatically updated to 0.14.0.

* Tue Feb 08 2022 Grigory Ustinov <grenka@altlinux.org> 0.13.0-alt1
- Automatically updated to 0.13.0.

* Thu Aug 12 2021 Grigory Ustinov <grenka@altlinux.org> 0.12.0-alt1
- Automatically updated to 0.12.0.

* Tue Nov 10 2020 Vitaly Lipatov <lav@altlinux.ru> 0.10.2-alt2
- drop BR: libnumpy-devel (it was python2 only package)

* Wed Sep 16 2020 Grigory Ustinov <grenka@altlinux.org> 0.10.2-alt1
- Automatically updated to 0.10.2.

* Thu Apr 11 2019 Grigory Ustinov <grenka@altlinux.org> 0.9.0-alt2
- Rebuild for python3.7.

* Mon Apr 08 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.0-alt1
- Updated to latest upstream release (Closes: #36539)
- Disabled build for python-2.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Dec 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.0-alt1
- Initial build for ALT.
