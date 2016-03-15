%define oname ore.xapian

%def_without python3

Name: python-module-%oname
Version: 0.5.0
Release: alt2.1.1
Summary: A Xapian Content Indexing/Searching Framework for Zope3
License: GPL
Group: Development/Python
Url: http://pypi.python.org/pypi/ore.xapian/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
#BuildPreReq: python-devel python-module-setuptools
%if_with python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires ore

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools rpm-build-python3

%description
The package provides a content indexing framework for a multi-threaded
python application. It utilizes xapian for its indexing library, and the
zope component architecture for flexibility. It operates primarily as a
framework wrapper for xapian core search facilities.

features:

  * processes all indexing operations asynchronously.
  * mechanisms for indexing/resolving content from multiple data stores.
  * easy to customize indexing behavior via adaptation.
  * transaction aware modifications, aggregates operations for content
    within a transaaction scope.

%package -n python3-module-%oname
Summary: A Xapian Content Indexing/Searching Framework for Zope3
Group: Development/Python3
%py3_provides %oname
%py3_requires ore

%description -n python3-module-%oname
The package provides a content indexing framework for a multi-threaded
python application. It utilizes xapian for its indexing library, and the
zope component architecture for flexibility. It operates primarily as a
framework wrapper for xapian core search facilities.

features:

  * processes all indexing operations asynchronously.
  * mechanisms for indexing/resolving content from multiple data stores.
  * easy to customize indexing behavior via adaptation.
  * transaction aware modifications, aggregates operations for content
    within a transaaction scope.

%package -n python3-module-%oname-tests
Summary: Tests for ore.xapian
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
The package provides a content indexing framework for a multi-threaded
python application. It utilizes xapian for its indexing library, and the
zope component architecture for flexibility. It operates primarily as a
framework wrapper for xapian core search facilities.

This package contains tests for ore.xapian.

%package tests
Summary: Tests for ore.xapian
Group: Development/Python
Requires: %name = %version-%release

%description tests
The package provides a content indexing framework for a multi-threaded
python application. It utilizes xapian for its indexing library, and the
zope component architecture for flexibility. It operates primarily as a
framework wrapper for xapian core search facilities.

This package contains tests for ore.xapian.

%package -n python-module-ore
Summary: Core package of ore
Group: Development/Python
%py_provides ore

%description -n python-module-ore
Core package of ore.

%package -n python3-module-ore
Summary: Core package of ore
Group: Development/Python3
%py3_provides ore

%description -n python3-module-ore
Core package of ore.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif
install -p -m644 src/ore/__init__.py \
	%buildroot%python_sitelibdir/ore/

%if_with python3
pushd ../python3
%python3_install
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
install -p -m644 src/ore/__init__.py \
	%buildroot%python3_sitelibdir/ore/
popd
%else
install -d %buildroot%python3_sitelibdir/ore
install -p -m644 src/ore/__init__.py \
	%buildroot%python3_sitelibdir/ore/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/tests.*
%exclude %python_sitelibdir/ore/__init__.*

%files tests
%python_sitelibdir/*/*/tests.*

%files -n python-module-ore
%dir %python_sitelibdir/ore
%python_sitelibdir/ore/__init__.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/ore/__init__.py
%exclude %python3_sitelibdir/ore/__pycache__/__init__.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%files -n python3-module-ore
%python3_sitelibdir/ore/__init__.py
%python3_sitelibdir/ore/__pycache__/__init__.*

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt2.1
- NMU: Use buildreq for BR.

* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt2
- Added python3-module-ore

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt1.1
- Rebuild with Python-2.7

* Fri Jun 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus

