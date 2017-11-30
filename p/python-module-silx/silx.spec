%define _unpackaged_files_terminate_build 1
%define oname silx

%def_with python3

Name: python-module-%oname
Version: 0.6.1
Release: alt1
Summary: Software library for X-Ray data analysis
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/silx

# https://github.com/silx-kit/silx.git
Source: %name-%version.tar

BuildRequires: gcc-c++ libgomp-devel
BuildRequires: python-devel python-module-setuptools
BuildRequires: libnumpy-devel python2.7(sphinx) python2.7(h5py)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: libnumpy-py3-devel python3(sphinx) python3(h5py)
%endif

%add_python_req_skip pyopencl

%description
The silx project aims at providing a collection of Python packages
to support the development of data assessment,
reduction and analysis applications at synchrotron radiation facilities.
It aims at providing reading/writing different file formats,
data reduction routines and a set of Qt widgets to browse and visualize data.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The silx project aims at providing a collection of Python packages
to support the development of data assessment,
reduction and analysis applications at synchrotron radiation facilities.
It aims at providing reading/writing different file formats,
data reduction routines and a set of Qt widgets to browse and visualize data.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Software library for X-Ray data analysis
Group: Development/Python3
%add_python3_req_skip pyopencl pyopencl.array pyopencl.elementwise

%description -n python3-module-%oname
The silx project aims at providing a collection of Python packages
to support the development of data assessment,
reduction and analysis applications at synchrotron radiation facilities.
It aims at providing reading/writing different file formats,
data reduction routines and a set of Qt widgets to browse and visualize data.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The silx project aims at providing a collection of Python packages
to support the development of data assessment,
reduction and analysis applications at synchrotron radiation facilities.
It aims at providing reading/writing different file formats,
data reduction routines and a set of Qt widgets to browse and visualize data.

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
%doc CHANGELOG.rst README.rst
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
%doc CHANGELOG.rst README.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/test
%endif

%changelog
* Thu Nov 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.1-alt1
- Initial build for ALT.
