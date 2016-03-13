%define oname z3c.profiler

%def_with python3

Name: python-module-%oname
Version: 0.10.0
Release: alt3.1
Summary: Profiler skin for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.profiler/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires z3c.layer.pagelet z3c.macro z3c.pagelet z3c.template
%py_requires z3c.zrtresource zope.app.wsgi zope.browserpage
%py_requires zope.component zope.componentvocabulary zope.configuration
%py_requires zope.contentprovider zope.i18n zope.i18nmessageid
%py_requires zope.contentprovider zope.i18n zope.i18nmessageid
%py_requires zope.interface zope.login zope.principalregistry
%py_requires zope.schema zope.security zope.securitypolicy zope.testing
%py_requires zope.traversing zope.viewlet

%description
This package provides a profiler skin which allows you to profile pages.

%package -n python3-module-%oname
Summary: Profiler skin for Zope3
Group: Development/Python3
%py3_requires z3c.layer.pagelet z3c.macro z3c.pagelet z3c.template
%py3_requires z3c.zrtresource zope.app.wsgi zope.browserpage
%py3_requires zope.component zope.componentvocabulary zope.configuration
%py3_requires zope.contentprovider zope.i18n zope.i18nmessageid
%py3_requires zope.contentprovider zope.i18n zope.i18nmessageid
%py3_requires zope.interface zope.login zope.principalregistry
%py3_requires zope.schema zope.security zope.securitypolicy zope.testing
%py3_requires zope.traversing zope.viewlet

%description -n python3-module-%oname
This package provides a profiler skin which allows you to profile pages.

%package -n python3-module-%oname-tests
Summary: Tests for Profiler skin for Zope3
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires z3c.etestbrowser zope.app.testing

%description -n python3-module-%oname-tests
This package provides a profiler skin which allows you to profile pages.

This package contains tests for Profiler skin for Zope3.

%package tests
Summary: Tests for Profiler skin for Zope3
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.etestbrowser zope.app.testing

%description tests
This package provides a profiler skin which allows you to profile pages.

This package contains tests for Profiler skin for Zope3.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt1
- Initial build for Sisyphus

