%define oname z3c.discriminator

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt3.1
Summary: Provides a formalism for marking adapter specifications as discriminators
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.discriminator/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.configuration zope.interface

%description
z3c.discriminator provides a formalism for marking adapter
specifications as discriminators in the sense that they will be used
only for adapter lookup, not instantiation.

%package -n python3-module-%oname
Summary: Provides a formalism for marking adapter specifications as discriminators
Group: Development/Python3
%py3_requires zope.configuration zope.interface

%description -n python3-module-%oname
z3c.discriminator provides a formalism for marking adapter
specifications as discriminators in the sense that they will be used
only for adapter lookup, not instantiation.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.discriminator
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.component.testing zope.testing

%description -n python3-module-%oname-tests
z3c.discriminator provides a formalism for marking adapter
specifications as discriminators in the sense that they will be used
only for adapter lookup, not instantiation.

This package contains tests for z3c.discriminator.

%package tests
Summary: Tests for z3c.discriminator
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.component.testing zope.testing

%description tests
z3c.discriminator provides a formalism for marking adapter
specifications as discriminators in the sense that they will be used
only for adapter lookup, not instantiation.

This package contains tests for z3c.discriminator.

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
%doc *.txt docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

