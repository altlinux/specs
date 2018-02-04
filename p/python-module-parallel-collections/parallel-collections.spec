%define oname parallel-collections

Name: python-module-%oname
Version: 0.2.3
Release: alt1.git20141027.1
Summary: Parallel implementations of collections with support for map/reduce style operations
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/python-parallel-collections/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gterzian/Python-Parallel-Collections.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-futures python-modules-wsgiref
BuildPreReq: python-module-nose

%py_provides parallel

%description
This package provides a convenient interface to perform
map/filter/reduce style operation on standard Python data structures and
generators in multiple processes. The parallelism is achieved using the
Python 2.7 backport of the concurrent.futures package. If you can define
your problem in terms of map/reduce/filter operations, it will run on
several parallel Python processes on your machine, taking advantage of
multiple cores. Otherwise these datastructures are equivalent to their
non-parallel peers found in the standard library.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%add_python_req_skip parallel_collections

%description tests
This package provides a convenient interface to perform
map/filter/reduce style operation on standard Python data structures and
generators in multiple processes. The parallelism is achieved using the
Python 2.7 backport of the concurrent.futures package. If you can define
your problem in terms of map/reduce/filter operations, it will run on
several parallel Python processes on your machine, taking advantage of
multiple cores. Otherwise these datastructures are equivalent to their
non-parallel peers found in the standard library.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
nosetests

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.3-alt1.git20141027.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1.git20141027
- Initial build for Sisyphus

