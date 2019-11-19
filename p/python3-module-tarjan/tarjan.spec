%define oname tarjan

Name: python3-module-%oname
Version: 0.2.1.3
Release: alt2

Summary: Implementation of Tarjan's algorithm: resolve cyclic deps
License: AGPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/tarjan/
# https://github.com/bwesterb/py-tarjan.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname


%description
Tarjan's algorithm takes as input a directed (possibly cyclic!) graph
and returns as output its strongly connected components in a topological
order.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Tarjan's algorithm takes as input a directed (possibly cyclic!) graph
and returns as output its strongly connected components in a topological
order.

This package contains tests for %oname.


%prep
%setup

sed -i 's|@VERSION@|%version|' setup.py

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 setup.py test

%files
%doc *.md doc/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Tue Nov 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.1.3-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.1.3-alt1.git20140805.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1.3-alt1.git20140805.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1.3-alt1.git20140805
- Initial build for Sisyphus

