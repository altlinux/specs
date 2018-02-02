%define oname djanginxed

%def_with python3

Name: python-module-%oname
Version: 0.0.5
Release: alt1.git20110216.1.1
Summary: Django Nginx Memcached integration
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/djanginxed/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/shaunsephton/djanginxed.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Provides a view decorator caching content in Memcached for easy
retrieval via Nginx. The cache is keyed by md5 of full request path
(which includes GET parameters).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Provides a view decorator caching content in Memcached for easy
retrieval via Nginx. The cache is keyed by md5 of full request path
(which includes GET parameters).

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Django Nginx Memcached integration
Group: Development/Python3

%description -n python3-module-%oname
Provides a view decorator caching content in Memcached for easy
retrieval via Nginx. The cache is keyed by md5 of full request path
(which includes GET parameters).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Provides a view decorator caching content in Memcached for easy
retrieval via Nginx. The cache is keyed by md5 of full request path
(which includes GET parameters).

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.5-alt1.git20110216.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.5-alt1.git20110216.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1.git20110216
- Initial build for Sisyphus

