%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname z3c.formwidget.query

%def_with python3

Name: python-module-%oname
Version: 0.12
#Release: alt1.1
Summary: A source query widget for z3c.form
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.formwidget.query/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/ab/38/7d93a07b58b50a773d7e360217d90839b061c1c8731f8a4aa20cb5b27e96/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires z3c.formwidget z3c.form zope.app.form zope.interface
%py_requires zope.schema zope.component zope.i18nmessageid

%description
This package implements a widget that lets users enter a query and
select from the results.

The widget works with zope.schema.Choice-fields supplying a query
source, optionally in conjunction with a collection field which then
allows multiple selections.

%package -n python3-module-%oname
Summary: A source query widget for z3c.form
Group: Development/Python3
%py3_requires z3c.formwidget z3c.form zope.app.form zope.interface
%py3_requires zope.schema zope.component zope.i18nmessageid

%description -n python3-module-%oname
This package implements a widget that lets users enter a query and
select from the results.

The widget works with zope.schema.Choice-fields supplying a query
source, optionally in conjunction with a collection field which then
allows multiple selections.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.formwidget.query
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.testing

%description -n python3-module-%oname-tests
This package implements a widget that lets users enter a query and
select from the results.

The widget works with zope.schema.Choice-fields supplying a query
source, optionally in conjunction with a collection field which then
allows multiple selections.

This package contains tests for z3c.formwidget.query.

%package tests
Summary: Tests for z3c.formwidget.query
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.testing

%description tests
This package implements a widget that lets users enter a query and
select from the results.

The widget works with zope.schema.Choice-fields supplying a query
source, optionally in conjunction with a collection field which then
allows multiple selections.

This package contains tests for z3c.formwidget.query.

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
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10-alt1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1
- Version 0.10
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1
- Version 0.9

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Version 0.7

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt3.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt3
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt2
- Fixed requirements

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1
- Initial build for Sisyphus

