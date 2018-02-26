%define oname manuel

%def_with python3

Name: python-module-%oname
Version: 1.5.0
Release: alt2
Summary: Manuel lets you build tested documentation
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/manuel/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
%endif

%description
Manuel lets you build tested documentation.

%if_with python3
%package -n python3-module-%oname
Summary: Manuel lets you build tested documentation (Python 3)
Group: Development/Python3

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
for i in $(find ./ -name '*.py'); do
	2to3 -w $i
done
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

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/test*

%files tests
%python_sitelibdir/%oname/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/test*
%endif

%changelog
* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.0-alt1.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus

