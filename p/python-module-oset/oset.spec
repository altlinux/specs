%define oname oset

%def_with python3

Name: python-module-%oname
Version: 0.1.3
Release: alt1.1.1
Summary: Ordered Set
License: Python
Group: Development/Python
Url: https://pypi.python.org/pypi/oset
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
Set that remembers original insertion order.

Implementation based on a doubly linked link and an internal dictionary.
This design gives OrderedSet the same big-Oh running times as regular
sets including O(1) adds, removes, and lookups as well as O(n)
iteration.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Set that remembers original insertion order.

Implementation based on a doubly linked link and an internal dictionary.
This design gives OrderedSet the same big-Oh running times as regular
sets including O(1) adds, removes, and lookups as well as O(n)
iteration.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Ordered Set
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Set that remembers original insertion order.

Implementation based on a doubly linked link and an internal dictionary.
This design gives OrderedSet the same big-Oh running times as regular
sets including O(1) adds, removes, and lookups as well as O(n)
iteration.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Set that remembers original insertion order.

Implementation based on a doubly linked link and an internal dictionary.
This design gives OrderedSet the same big-Oh running times as regular
sets including O(1) adds, removes, and lookups as well as O(n)
iteration.

This package contains tests for %oname.
%endif

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
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.3-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.3-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus

