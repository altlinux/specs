%define oname ZODB

%def_with python3
#def_disable check

Name: python-module-%oname
Version: 5.3.0
Release: alt1.1
Summary: Zope Object Database: object database and persistence
License: ZPL
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/ZODB

# https://github.com/zopefoundation/ZODB.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires: python-dev python-module-setuptools
BuildRequires: python2.7(persistent) python2.7(BTrees) python2.7(ZConfig) python2.7(transaction)
BuildRequires: python2.7(six) python2.7(zc.lockfile) python2.7(zope.interface) python2.7(zodbpickle)
BuildRequires: python-module-manuel-tests python2.7(zope.testing) python2.7(zope.testrunner)
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3(persistent) python3(BTrees) python3(ZConfig) python3(transaction)
BuildRequires: python3(six) python3(zc.lockfile) python3(zope.interface) python3(zodbpickle)
BuildRequires: python3-module-manuel-tests python3(zope.testing) python3(zope.testrunner)
BuildRequires: python3-module-pytest
%endif

%py_provides %oname %oname.TimeStamp
%py_requires persistent.TimeStamp zc.lockfile zdaemon zope.event zope.interface zope.proxy zodbpickle

%description
The Zope Object Database provides an object-oriented database for Python
that provides a high-degree of transparency. Applications can take
advantage of object database features with few, if any, changes to
application logic. ZODB includes features such as a plugable storage
interface, rich transaction support, and undo.

%package tests
Summary: Tests for Zope Object Database
Group: Development/Python
Requires: %name = %EVR
#%py_requires zope.testing
%add_python_req_skip fstest

%description tests
The Zope Object Database provides an object-oriented database for Python
that provides a high-degree of transparency. Applications can take
advantage of object database features with few, if any, changes to
application logic. ZODB includes features such as a plugable storage
interface, rich transaction support, and undo.

This package contains tests for Zope Object Database.

%package docs
Summary: Documentation for Zope Object Database
Group: Development/Documentation
BuildArch: noarch

%description docs
The Zope Object Database provides an object-oriented database for Python
that provides a high-degree of transparency. Applications can take
advantage of object database features with few, if any, changes to
application logic. ZODB includes features such as a plugable storage
interface, rich transaction support, and undo.

This package contains documentation for Zope Object Database.

%package -n python3-module-%oname
Summary: Zope Object Database: object database and persistence
Group: Development/Python3
%py3_provides %oname %oname.TimeStamp
%py3_requires persistent.TimeStamp zodbpickle zdaemon zope.event zope.proxy

%description -n python3-module-%oname
The Zope Object Database provides an object-oriented database for Python
that provides a high-degree of transparency. Applications can take
advantage of object database features with few, if any, changes to
application logic. ZODB includes features such as a plugable storage
interface, rich transaction support, and undo.

%package -n python3-module-%oname-tests
Summary: Tests for Zope Object Database
Group: Development/Python3
Requires: python3-module-%oname = %EVR
#%py3_requires zope.testing
%add_python3_req_skip fstest

%description -n python3-module-%oname-tests
The Zope Object Database provides an object-oriented database for Python
that provides a high-degree of transparency. Applications can take
advantage of object database features with few, if any, changes to
application logic. ZODB includes features such as a plugable storage
interface, rich transaction support, and undo.

This package contains tests for Zope Object Database.

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
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
py.test
%if_with python3
pushd ../python3
py.test3
popd
%endif

%files
%doc *.txt *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests*
%exclude %python_sitelibdir/*/*/manual_tests

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests*
%python_sitelibdir/*/*/manual_tests

%files docs
%doc doc/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests*
%exclude %python3_sitelibdir/*/*/manual_tests
%exclude %python3_sitelibdir/*/*/*/tests*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests*
%python3_sitelibdir/*/*/manual_tests
%python3_sitelibdir/*/*/*/tests*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 5.3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.3.0-alt1
- Updated to upstream version 5.3.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2.1-alt4.dev0.git20150714.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.2.1-alt4.dev0.git20150714.1
- NMU: Use buildreq for BR.

* Fri Jan 29 2016 Sergey Alembekov <rt@altlinux.ru> 4.2.1-alt4.dev0.git20150714
- remove useless requires

* Fri Jan 29 2016 Sergey Alembekov <rt@altlinux.ru> 4.2.1-alt3.dev0.git20150714
- remove useless build requires

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt2.dev0.git20150714
- Enabled check

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.dev0.git20150714
- Version 4.2.1.dev0

* Mon Jan 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1.git20150111
- Version 4.1.0

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1.dev.git20141226
- Version 4.1.0dev

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.dev.git20140724
- Version 4.0.1dev
- Enabled testing

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Initial build for Sisyphus

