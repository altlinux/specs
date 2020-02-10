%define oname oset

Name: python3-module-%oname
Version: 0.1.3
Release: alt2

Summary: Ordered Set
License: Python
Group: Development/Python3
Url: https://pypi.python.org/pypi/oset
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%py3_provides %oname


%description
Set that remembers original insertion order.

Implementation based on a doubly linked link and an internal dictionary.
This design gives OrderedSet the same big-Oh running times as regular
sets including O(1) adds, removes, and lookups as well as O(n)
iteration.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Set that remembers original insertion order.

Implementation based on a doubly linked link and an internal dictionary.
This design gives OrderedSet the same big-Oh running times as regular
sets including O(1) adds, removes, and lookups as well as O(n)
iteration.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test -v

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*


%changelog
* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1.3-alt2
- Build for python2 removal.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.3-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.3-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus

