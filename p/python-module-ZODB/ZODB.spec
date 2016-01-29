%define oname ZODB

%def_with python3
#def_disable check

Name: python-module-%oname
Version: 4.2.1
Release: alt3.dev0.git20150714
Summary: Zope Object Database: object database and persistence
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/ZODB
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/ZODB.git
Source: %name-%version.tar
BuildArch: noarch
BuildRequires: python-module-BTrees python-module-pytest python-module-transaction python-module-zc.lockfile python-module-zdaemon python-module-zope.testing

BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-Zope2-tests
#BuildPreReq: python-module-zope.interface python-module-persistent
#BuildPreReq: python-module-BTrees
#BuildPreReq: python-module-zconfig
#BuildPreReq: python-module-transaction
BuildPreReq: python-module-six
#BuildPreReq: python-module-zc.lockfile
#BuildPreReq: python-module-zdaemon
BuildPreReq: python-module-zodbpickle
BuildPreReq: python-module-manuel-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-zope.interface python3-module-persistent
#BuildPreReq: python3-module-BTrees
#BuildPreReq: python3-module-zconfig
#BuildPreReq: python3-module-transaction
BuildPreReq: python3-module-six
#BuildPreReq: python3-module-zc.lockfile
#BuildPreReq: python3-module-zdaemon
BuildPreReq: python3-module-zodbpickle
BuildPreReq: python3-module-manuel-tests
BuildRequires: python3-module-BTrees python3-module-pytest python3-module-transaction python3-module-zc.lockfile python3-module-zdaemon python3-module-zope.testing
%endif

%py_provides %oname
%py_requires transaction BTrees persistent zc.lockfile ZConfig zdaemon
%py_requires zope.event zope.interface zope.proxy zodbpickle

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
%py_requires zope.testing
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
%py3_provides %oname
%py3_requires transaction BTrees persistent zc.lockfile ZConfig zdaemon
%py3_requires zope.event zope.interface zope.proxy

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
%py3_requires zope.testing
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
python setup.py test
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
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

