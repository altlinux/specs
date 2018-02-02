%define oname manuel

%def_with python3

Name: python-module-%oname
Version: 1.8.0
Release: alt1.1.1
Summary: Manuel lets you build tested documentation
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/manuel/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-six python-module-zope.testing
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildPreReq: python3-module-six python3-module-zope.testing
BuildPreReq: python-tools-2to3
%endif

%py_requires six

%description
Manuel lets you build tested documentation.

%if_with python3
%package -n python3-module-%oname
Summary: Manuel lets you build tested documentation (Python 3)
Group: Development/Python3
%py3_requires six

%description -n python3-module-%oname
Manuel lets you build tested documentation.

%package -n python3-module-%oname-tests
Summary: Tests for Manuel (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
Manuel lets you build tested documentation.

This package contains tests for Manuel.
%endif

%package tests
Summary: Tests for Manuel
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
Manuel lets you build tested documentation.

This package contains tests for Manuel.

%package docs
Summary: Documentation for Manuel
Group: Development/Documentation

%description docs
Manuel lets you build tested documentation.

This package contains documentation for Manuel.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
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
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/test*

%files tests
%python_sitelibdir/%oname/test*

%files docs
%doc docs/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/test*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.8.0-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.8.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1
- Version 1.8.0

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt2
- Use 'find... -exec...' instead of 'for ... $(find...'

* Mon Apr 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt1
- Version 1.7.2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.5.0-alt2.1
- Rebuild with Python-3.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.0-alt1.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus

