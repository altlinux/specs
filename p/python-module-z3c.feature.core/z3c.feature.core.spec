%define ocore z3c.feature
%define oname %ocore.core

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt4.1
Summary: Core Features to use with z3c.builder.core
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.feature.core/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

Requires: python-module-%ocore = %EVR
%py_requires z3c.builder.core zope.schema zope.interface z3c.form
%py_requires zc.buildout zope.app.pagetemplate

%description
Core Features to use with z3c.builder.core

This package provides the ZBoiler Core Features.

%package -n python3-module-%oname
Summary: Core Features to use with z3c.builder.core
Group: Development/Python3
Requires: python3-module-%ocore = %EVR
%py3_requires z3c.builder.core zope.schema zope.interface z3c.form
%py3_requires zc.buildout zope.app.pagetemplate

%description -n python3-module-%oname
Core Features to use with z3c.builder.core

This package provides the ZBoiler Core Features.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.builder.core
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing z3c.coverage zope.testing zope.component
%py3_requires zope.configuration

%description -n python3-module-%oname-tests
Core Features to use with z3c.builder.core

This package contains tests for z3c.builder.core.

%package tests
Summary: Tests for z3c.builder.core
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing z3c.coverage zope.testing zope.component
%py_requires zope.configuration

%description tests
Core Features to use with z3c.builder.core

This package contains tests for z3c.builder.core.

%package -n python-module-%ocore
Summary: Core package of %ocore
Group: Development/Python
Conflicts: %name < %EVR

%description -n python-module-%ocore
Core package of %ocore.

%package -n python3-module-%ocore
Summary: Core package of %ocore
Group: Development/Python3

%description -n python3-module-%ocore
Core package of %ocore.

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
touch %buildroot%python_sitelibdir/z3c/feature/__init__.py

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%else
install -d %buildroot%python3_sitelibdir/z3c/feature
%endif
touch %buildroot%python3_sitelibdir/z3c/feature/__init__.py

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/test*
%exclude %python_sitelibdir/z3c/feature/__init__.py*

%files tests
%python_sitelibdir/*/*/*/test*

%files -n python-module-%ocore
%python_sitelibdir/z3c/feature/__init__.py*

%files -n python3-module-%ocore
%python3_sitelibdir/z3c/feature/__init__.py
%python3_sitelibdir/z3c/feature/__pycache__/__init__.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/*/test*
%exclude %python3_sitelibdir/z3c/feature/__init__.py
%exclude %python3_sitelibdir/z3c/feature/__pycache__/__init__.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%python3_sitelibdir/*/*/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt4
- Added module for Python 3

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt3
- Moved %ocore into separate package

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt2.1
- Rebuild with Python-2.7

* Fri Jul 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus

