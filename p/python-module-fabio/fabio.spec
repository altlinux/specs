%define _unpackaged_files_terminate_build 1
%define oname fabio

%def_with python3
# check disabled because it relies a lot on network
%def_disable check

Name: python-module-%oname
Version: 0.5.0
Release: alt1
Summary: Image IO for fable
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/fabio

# https://github.com/silx-kit/fabio.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: libnumpy-devel python-module-Cython
BuildRequires: python2.7(lxml)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: libnumpy-py3-devel python3-module-Cython
BuildRequires: python3(lxml)
%endif

%description
FabIO is an I/O library for images produced by 2D X-ray detectors and written in Python.
FabIO support images detectors from a dozen of companies (including Mar, Dectris, ADSC, Hamamatsu, Oxford, ...),
for a total of 20 different file formats (like CBF, EDF, TIFF, ...) and offers an unified interface to their
headers (as a python dictionary) and datasets (as a numpy ndarray of integers or floats).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
FabIO is an I/O library for images produced by 2D X-ray detectors and written in Python.
FabIO support images detectors from a dozen of companies (including Mar, Dectris, ADSC, Hamamatsu, Oxford, ...),
for a total of 20 different file formats (like CBF, EDF, TIFF, ...) and offers an unified interface to their
headers (as a python dictionary) and datasets (as a numpy ndarray of integers or floats).

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Image IO for fable
Group: Development/Python3
%add_python3_req_skip UserDict

%description -n python3-module-%oname
FabIO is an I/O library for images produced by 2D X-ray detectors and written in Python.
FabIO support images detectors from a dozen of companies (including Mar, Dectris, ADSC, Hamamatsu, Oxford, ...),
for a total of 20 different file formats (like CBF, EDF, TIFF, ...) and offers an unified interface to their
headers (as a python dictionary) and datasets (as a numpy ndarray of integers or floats).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
FabIO is an I/O library for images produced by 2D X-ray detectors and written in Python.
FabIO support images detectors from a dozen of companies (including Mar, Dectris, ADSC, Hamamatsu, Oxford, ...),
for a total of 20 different file formats (like CBF, EDF, TIFF, ...) and offers an unified interface to their
headers (as a python dictionary) and datasets (as a numpy ndarray of integers or floats).

This package contains tests for %oname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test

%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc README.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/test

%files tests
%python_sitelibdir/%oname/test

%if_with python3
%files -n python3-module-%oname
%doc README.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/test
%endif

%changelog
* Fri Dec 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.0-alt1
- Initial build for ALT.
