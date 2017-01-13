%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname zope.catalog

%def_with python3

Name: python-module-%oname
Version: 4.1.0
#Release: alt3.1
Summary: Cataloging and Indexing Framework for the Zope Toolkit
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.catalog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/ea/f4/87706b8d3e207589117ab9eee792ead2639388e80df149b3a48ca7479a00/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope ZODB3 zope.annotation zope.intid zope.component
%py_requires zope.container zope.index zope.interface persistent
%py_requires zope.lifecycleevent zope.location zope.schema

%description
Catalogs provide management of collections of related indexes with a
basic search algorithm.

%package -n python3-module-%oname
Summary: Cataloging and Indexing Framework for the Zope Toolkit
Group: Development/Python3
%py3_requires zope ZODB3 zope.annotation zope.intid zope.component
%py3_requires zope.container zope.index zope.interface persistent
%py3_requires zope.lifecycleevent zope.location zope.schema

%description -n python3-module-%oname
Catalogs provide management of collections of related indexes with a
basic search algorithm.

%package -n python3-module-%oname-tests
Summary: Tests for zope.catalog
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing zope.site

%description -n python3-module-%oname-tests
Catalogs provide management of collections of related indexes with a
basic search algorithm.

This package contains tests for zope.catalog.

%package tests
Summary: Tests for zope.catalog
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.site

%description tests
Catalogs provide management of collections of related indexes with a
basic search algorithm.

This package contains tests for zope.catalog.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
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
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.0-alt3.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3
- Version 4.0.0

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.a1
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a1
- Version 4.0.0a1

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.2-alt1
- Version 3.8.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.8.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt1
- Initial build for Sisyphus

