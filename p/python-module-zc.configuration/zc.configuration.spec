%define oname zc.configuration

%def_with python3

Name: python-module-%oname
Version: 1.1
Release: alt3.1
Summary: Extensions to zope.configuration
License: ZPLv1.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.configuration/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.testing zope.configuration

%description
The zc.configuration package used to provide the exclude directive for
inhibiting configuration. It was included in the zope.configuration and
this package currently provides a backward-compatibility imports and
tests that ensure that it will work for people who are already using
zc.configuration and not the newer zope.configuration.

This package may contain more configuration extensions in future, but
currently, it's not useful anymore as the only feature it provided, the
exclude directive was merged into the original zope.configuration
package.

%package -n python3-module-%oname
Summary: Extensions to zope.configuration
Group: Development/Python3
%py3_requires zope.testing zope.configuration

%description -n python3-module-%oname
The zc.configuration package used to provide the exclude directive for
inhibiting configuration. It was included in the zope.configuration and
this package currently provides a backward-compatibility imports and
tests that ensure that it will work for people who are already using
zc.configuration and not the newer zope.configuration.

This package may contain more configuration extensions in future, but
currently, it's not useful anymore as the only feature it provided, the
exclude directive was merged into the original zope.configuration
package.

%package -n python3-module-%oname-demo
Summary: demo for zc.configuration
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-demo
The zc.configuration package used to provide the exclude directive for
inhibiting configuration. It was included in the zope.configuration and
this package currently provides a backward-compatibility imports and
tests that ensure that it will work for people who are already using
zc.configuration and not the newer zope.configuration.

This package may contain more configuration extensions in future, but
currently, it's not useful anymore as the only feature it provided, the
exclude directive was merged into the original zope.configuration
package.

This package contains demo for zc.configuration.

%package -n python3-module-%oname-tests
Summary: Tests for zc.configuration
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
The zc.configuration package used to provide the exclude directive for
inhibiting configuration. It was included in the zope.configuration and
this package currently provides a backward-compatibility imports and
tests that ensure that it will work for people who are already using
zc.configuration and not the newer zope.configuration.

This package may contain more configuration extensions in future, but
currently, it's not useful anymore as the only feature it provided, the
exclude directive was merged into the original zope.configuration
package.

This package contains tests for zc.configuration.

%package tests
Summary: Tests for zc.configuration
Group: Development/Python
Requires: %name = %version-%release

%description tests
The zc.configuration package used to provide the exclude directive for
inhibiting configuration. It was included in the zope.configuration and
this package currently provides a backward-compatibility imports and
tests that ensure that it will work for people who are already using
zc.configuration and not the newer zope.configuration.

This package may contain more configuration extensions in future, but
currently, it's not useful anymore as the only feature it provided, the
exclude directive was merged into the original zope.configuration
package.

This package contains tests for zc.configuration.

%package demo
Summary: demo for zc.configuration
Group: Development/Python
Requires: %name = %version-%release

%description demo
The zc.configuration package used to provide the exclude directive for
inhibiting configuration. It was included in the zope.configuration and
this package currently provides a backward-compatibility imports and
tests that ensure that it will work for people who are already using
zc.configuration and not the newer zope.configuration.

This package may contain more configuration extensions in future, but
currently, it's not useful anymore as the only feature it provided, the
exclude directive was merged into the original zope.configuration
package.

This package contains demo for zc.configuration.

%prep
%setup

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
%exclude %python_sitelibdir/*/*/tests.*
%exclude %python_sitelibdir/*/*/demo

%files tests
%python_sitelibdir/*/*/tests.*

%files demo
%python_sitelibdir/*/*/demo

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/demo

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-demo
%python3_sitelibdir/*/*/demo
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

