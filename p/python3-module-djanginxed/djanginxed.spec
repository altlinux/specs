%define oname djanginxed

Name: python3-module-%oname
Version: 0.0.5
Release: alt2

Summary: Django Nginx Memcached integration
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/djanginxed/
BuildArch: noarch

# https://github.com/shaunsephton/djanginxed.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Provides a view decorator caching content in Memcached for easy
retrieval via Nginx. The cache is keyed by md5 of full request path
(which includes GET parameters).

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Provides a view decorator caching content in Memcached for easy
retrieval via Nginx. The cache is keyed by md5 of full request path
(which includes GET parameters).

This package contains tests for %oname.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*


%changelog
* Thu Dec 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.5-alt2
- build for python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.5-alt1.git20110216.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.5-alt1.git20110216.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1.git20110216
- Initial build for Sisyphus

