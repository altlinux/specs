%define oname zope.mkzeoinstance

%def_with python3

Name: python-module-%oname
Version: 3.9.6
Release: alt1.1
Summary: Make standalone ZEO database server instances
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.mkzeoinstance/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope ZODB3

%description
This package provides a single script, mkzeoinstance, which creates a
standalone ZEO server instance.

%package -n python3-module-%oname
Summary: Make standalone ZEO database server instances
Group: Development/Python3
%py3_requires zope ZODB3

%description -n python3-module-%oname
This package provides a single script, mkzeoinstance, which creates a
standalone ZEO server instance.

%package -n python3-module-%oname-tests
Summary: Tests for mkzeoinstance
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package provides a single script, mkzeoinstance, which creates a
standalone ZEO server instance.

This package contains tests for mkzeoinstance.

%package tests
Summary: Tests for mkzeoinstance
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a single script, mkzeoinstance, which creates a
standalone ZEO server instance.

This package contains tests for mkzeoinstance.

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
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.9.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.6-alt1
- Version 3.9.6

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.5-alt2
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.5-alt1
- Version 3.9.5

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9.4-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.4-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.4-alt1
- Initial build for Sisyphus

