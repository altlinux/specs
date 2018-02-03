%define oname dexml

%def_with python3

Name: python-module-%oname
Version: 0.5.1
Release: alt1.git20150420.1.1
Summary: A dead-simple Object-XML mapper for Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/dexml/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rfk/dexml.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
The dexml module takes the obvious mapping between XML tags and Python
objects and lets you capture that as cleanly as possible. Loosely
inspired by Django's ORM, you write simple class definitions to define
the expected structure of your XML document.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The dexml module takes the obvious mapping between XML tags and Python
objects and lets you capture that as cleanly as possible. Loosely
inspired by Django's ORM, you write simple class definitions to define
the expected structure of your XML document.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A dead-simple Object-XML mapper for Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The dexml module takes the obvious mapping between XML tags and Python
objects and lets you capture that as cleanly as possible. Loosely
inspired by Django's ORM, you write simple class definitions to define
the expected structure of your XML document.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The dexml module takes the obvious mapping between XML tags and Python
objects and lets you capture that as cleanly as possible. Loosely
inspired by Django's ORM, you write simple class definitions to define
the expected structure of your XML document.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test.*

%files tests
%python_sitelibdir/*/test.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.1-alt1.git20150420.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.1-alt1.git20150420.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20150420
- New snapshot

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20121026
- Initial build for Sisyphus

