%define oname anykeystore

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt1.1
Summary: A key-value store supporting multiple backends
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/anykeystore/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
A generic interface wrapping multiple different backends to provide a
consistent key-value storage API. This library is intended to be used by
other libraries that require some form of generic storage.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A generic interface wrapping multiple different backends to provide a
consistent key-value storage API. This library is intended to be used by
other libraries that require some form of generic storage.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A key-value store supporting multiple backends
Group: Development/Python3

%description -n python3-module-%oname
A generic interface wrapping multiple different backends to provide a
consistent key-value storage API. This library is intended to be used by
other libraries that require some form of generic storage.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A generic interface wrapping multiple different backends to provide a
consistent key-value storage API. This library is intended to be used by
other libraries that require some form of generic storage.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

