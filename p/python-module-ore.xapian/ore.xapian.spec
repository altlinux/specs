%define oname ore.xapian
Name: python-module-%oname
Version: 0.5.0
Release: alt1.1
Summary: A Xapian Content Indexing/Searching Framework for Zope3
License: GPL
Group: Development/Python
Url: http://pypi.python.org/pypi/ore.xapian/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_provides %oname
%py_requires ore

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


%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

install -p -m644 src/ore/__init__.py \
	%buildroot%python_sitelibdir/ore/

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

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt1.1
- Rebuild with Python-2.7

* Fri Jun 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus

