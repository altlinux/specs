%define oname z3c.boiler

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt3.1
Summary: A utility to help jump start Zope 3 projects
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.boiler/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zc.buildout z3c.builder.core z3c.feature.core
%py_requires z3c.feature.zope

%description
This package provides the ZBoiler Zope Features.

The ZBoiler package provides a small script to generate the boilerplate
of a project from a simple, high-level feature XML file.

%package -n python3-module-%oname
Summary: A utility to help jump start Zope 3 projects
Group: Development/Python3
%py3_requires zc.buildout z3c.builder.core z3c.feature.core
%py3_requires z3c.feature.zope

%description -n python3-module-%oname
This package provides the ZBoiler Zope Features.

The ZBoiler package provides a small script to generate the boilerplate
of a project from a simple, high-level feature XML file.

%package -n python3-module-%oname-tests
Summary: Tests for ZBoiler Zope Features
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing z3c.coverage

%description -n python3-module-%oname-tests
This package provides the ZBoiler Zope Features.

The ZBoiler package provides a small script to generate the boilerplate
of a project from a simple, high-level feature XML file.

This package contains tests for ZBoiler Zope Features.

%package tests
Summary: Tests for ZBoiler Zope Features
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing z3c.coverage

%description tests
This package provides the ZBoiler Zope Features.

The ZBoiler package provides a small script to generate the boilerplate
of a project from a simple, high-level feature XML file.

This package contains tests for ZBoiler Zope Features.

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
%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus

