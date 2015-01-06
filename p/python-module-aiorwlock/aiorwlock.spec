%define oname aiorwlock

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt1.git20141223
Summary: Synchronization primitive RWLock for asyncio (PEP 3156) 
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/aiorwlock/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aio-libs/aiorwlock.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-asyncio python-module-nose
BuildPreReq: python-module-flake8
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio python3-module-nose
BuildPreReq: python3-module-flake8
%endif

%py_provides %oname
%py_requires asyncio

%description
Read write lock for asyncio . A RWLock maintains a pair of associated
locks, one for read-only operations and one for writing. The read lock
may be held simultaneously by multiple reader tasks, so long as there
are no writers. The write lock is exclusive.

Whether or not a read-write lock will improve performance over the use
of a mutual exclusion lock depends on the frequency that the data is
read compared to being modified. For example, a collection that is
initially populated with data and thereafter infrequently modified,
while being frequently searched is an ideal candidate for the use of a
read-write lock. However, if updates become frequent then the data
spends most of its time being exclusively locked and there is little, if
any increase in concurrency.

%package -n python3-module-%oname
Summary: Synchronization primitive RWLock for asyncio (PEP 3156) 
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
Read write lock for asyncio . A RWLock maintains a pair of associated
locks, one for read-only operations and one for writing. The read lock
may be held simultaneously by multiple reader tasks, so long as there
are no writers. The write lock is exclusive.

Whether or not a read-write lock will improve performance over the use
of a mutual exclusion lock depends on the frequency that the data is
read compared to being modified. For example, a collection that is
initially populated with data and thereafter infrequently modified,
while being frequently searched is an ideal candidate for the use of a
read-write lock. However, if updates become frequent then the data
spends most of its time being exclusively locked and there is little, if
any increase in concurrency.

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i 's|flake8|python3-flake8|' ../python3/Makefile
sed -i 's|nosetests|nosetests3|' ../python3/Makefile
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
python setup.py test
%make flake
%make vtest
%endif
%if_with python3
pushd ../python3
python3 setup.py test
%make flake
%make vtest
popd
%endif

%if_with python2
%files
%doc *.rst examples
%python_sitelibdir/*
%exclude %python_sitelibdir/tests
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141223
- Initial build for Sisyphus

