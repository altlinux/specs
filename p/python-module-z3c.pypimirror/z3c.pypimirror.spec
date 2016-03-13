%define oname z3c.pypimirror

%def_with python3

Name: python-module-%oname
Version: 1.0.16
Release: alt3.1
Summary: A module for building a complete or a partial PyPI mirror
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.pypimirror/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zc.lockfile BeautifulSoup

%description
This package provides a mirror for the PyPI simple interface,
http://cheeseshop.python.org/simple/.

%package -n python3-module-%oname
Summary: A module for building a complete or a partial PyPI mirror
Group: Development/Python3
%py3_requires zc.lockfile BeautifulSoup

%description -n python3-module-%oname
This package provides a mirror for the PyPI simple interface,
http://cheeseshop.python.org/simple/.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.pypimirror
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zc.buildout zope.testing interlude

%description -n python3-module-%oname-tests
This package provides a mirror for the PyPI simple interface,
http://cheeseshop.python.org/simple/.

This package contains tests for z3c.pypimirror.

%package tests
Summary: Tests for z3c.pypimirror
Group: Development/Python
Requires: %name = %version-%release
%py_requires zc.buildout zope.testing interlude

%description tests
This package provides a mirror for the PyPI simple interface,
http://cheeseshop.python.org/simple/.

This package contains tests for z3c.pypimirror.

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
%if_with python3
pushd ../python3
%python3_install
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
install -p -m644 src/z3c/pypimirror/util.py \
	%buildroot%python3_sitelibdir/z3c/pypimirror
popd
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
install -p -m644 src/z3c/pypimirror/util.py \
	%buildroot%python_sitelibdir/z3c/pypimirror

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.16-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.16-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.16-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.16-alt2
- Added necessary requirements
- Excluded *.pth

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.16-alt1
- Initial build for Sisyphus

