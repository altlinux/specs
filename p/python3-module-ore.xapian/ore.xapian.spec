%define oname ore.xapian

%def_without tests

Name: python3-module-%oname
Version: 0.5.0
Release: alt3

Summary: A Xapian Content Indexing/Searching Framework for Zope3
License: GPL
Group: Development/Python3
Url: http://pypi.python.org/pypi/ore.xapian/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_provides %oname
%py3_requires ore


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

%if_with tests
%package tests
Summary: Tests for ore.xapian
Group: Development/Python3
Requires: %name = %version-%release

%description tests
The package provides a content indexing framework for a multi-threaded
python application. It utilizes xapian for its indexing library, and the
zope component architecture for flexibility. It operates primarily as a
framework wrapper for xapian core search facilities.

This package contains tests for ore.xapian.
%endif

%package -n python3-module-ore
Summary: Core package of ore
Group: Development/Python3
%py3_provides ore

%description -n python3-module-ore
Core package of ore.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

install -p -m644 src/ore/__init__.py \
    %buildroot%python3_sitelibdir/ore/

# install -d %buildroot%python3_sitelibdir/ore

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/ore/__init__.py
%exclude %python3_sitelibdir/ore/__pycache__/__init__.*

%if_with tests
%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%files -n python3-module-ore
%python3_sitelibdir/ore/__init__.py
%python3_sitelibdir/ore/__pycache__/__init__.*


%changelog
* Mon Dec 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.5.0-alt3
- build for python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.5.0-alt2.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt2.1.1.1
- (AUTO) subst_x86_64.

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

