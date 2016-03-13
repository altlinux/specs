%define oname z3c.csvvocabulary

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt2.1
Summary: A package to create vocabularies based on CSV files
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.csvvocabulary/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.i18nmessageid zope.schema

%description
This package provides a very simple vocabulary implementation using CSV
files. The advantage of CSV files is that they provide an external point
to specify data, which allows a non-developer to adjust the data
themselves.

%package -n python3-module-%oname
Summary: A package to create vocabularies based on CSV files
Group: Development/Python3
%py3_requires zope.i18nmessageid zope.schema

%description -n python3-module-%oname
This package provides a very simple vocabulary implementation using CSV
files. The advantage of CSV files is that they provide an external point
to specify data, which allows a non-developer to adjust the data
themselves.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.csvvocabulary
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
This package provides a very simple vocabulary implementation using CSV
files. The advantage of CSV files is that they provide an external point
to specify data, which allows a non-developer to adjust the data
themselves.

This package contains tests for z3c.csvvocabulary.

%package tests
Summary: Tests for z3c.csvvocabulary
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package provides a very simple vocabulary implementation using CSV
files. The advantage of CSV files is that they provide an external point
to specify data, which allows a non-developer to adjust the data
themselves.

This package contains tests for z3c.csvvocabulary.

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1
- Version 2.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

