%define oname DateTime

%def_with python3

Name: python-module-%oname
Version: 3.0rel
Release: alt2
Summary: Encapsulation of date/time values
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/DateTime/
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
This package provides a DateTime data type, as known from Zope 2. Unless
you need to communicate with Zope 2 APIs, you're probably better off
using Python's built-in datetime module.

%if_with python3
%package -n python3-module-%oname
Summary: Encapsulation of date/time values (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
This package provides a DateTime data type, as known from Zope 2. Unless
you need to communicate with Zope 2 APIs, you're probably better off
using Python's built-in datetime module.

%package -n python3-module-%oname-tests
Summary: Tests for DateTime (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package provides a DateTime data type, as known from Zope 2. Unless
you need to communicate with Zope 2 APIs, you're probably better off
using Python's built-in datetime module.

This package contains tests for DateTime.
%endif

%package tests
Summary: Tests for DateTime
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a DateTime data type, as known from Zope 2. Unless
you need to communicate with Zope 2 APIs, you're probably better off
using Python's built-in datetime module.

This package contains tests for DateTime.

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
	2to3 -w -n $i
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
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Tue May 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0rel-alt2
- Added module for Python 3

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0rel-alt1
- Version 3.0 (release)

* Thu Dec 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0b3-alt1
- Version 3.0b3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0b1-alt1.1
- Rebuild with Python-2.7

* Tue May 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0b1-alt1
- Initial build for Sisyphus

