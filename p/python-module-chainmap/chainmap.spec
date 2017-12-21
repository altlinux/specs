%define oname chainmap

%def_with python3

Name: python-module-%oname
Version: 1.0.2
Release: alt1
Summary: Backport/clone of ChainMap for py26, py32, and pypy3.
License: Python Software Foundation License
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/chainmap

Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
%endif

%description
This module is a polyfill, implementing ChainMap for reasonably-recent versions
of Python that do not have collections.ChainMap - namely, Python 2.6, Python 3.2,
and PyPy3 releases based on Python 3.2.
(It will also work as expected on Python 2.7, PyPy, and Python 3.3 and higher,
but it is not needed there since those versions' collections modules
contains a ChainMap implementation.)

The code for this package is closely derived from the Python 3.5 source code at hg.python.org,
(especially the collections and reprlib modules).
Several changes have been made to ensure Python 2.6 compatibility,
and tests and packaging have been added.

%if_with python3
%package -n python3-module-%oname
Summary: Backport/clone of ChainMap for py26, py32, and pypy3.
Group: Development/Python3

%description -n python3-module-%oname
This module is a polyfill, implementing ChainMap for reasonably-recent versions
of Python that do not have collections.ChainMap - namely, Python 2.6, Python 3.2,
and PyPy3 releases based on Python 3.2.
(It will also work as expected on Python 2.7, PyPy, and Python 3.3 and higher,
but it is not needed there since those versions' collections modules
contains a ChainMap implementation.)

The code for this package is closely derived from the Python 3.5 source code at hg.python.org,
(especially the collections and reprlib modules).
Several changes have been made to ensure Python 2.6 compatibility,
and tests and packaging have been added.
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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export PYTHONPATH=$PWD
py.test -vv
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
py.test3 -vv
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.2-alt1
- Initial build for ALT.
