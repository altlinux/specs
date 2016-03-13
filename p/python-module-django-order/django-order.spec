%define oname django-order

%def_with python3

Name: python-module-%oname
Version: 0.0.7
Release: alt1.git20110915.1
Summary: Django app allowing users to manually order objects via admin
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-order/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/django-order.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Provides an additional order tool within admin with which objects can be
ordered by any number of arbitrary settings defined fields. A
user_order_by queryset method allows for retrieval of objects as they
were ordered by users via admin.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Provides an additional order tool within admin with which objects can be
ordered by any number of arbitrary settings defined fields. A
user_order_by queryset method allows for retrieval of objects as they
were ordered by users via admin.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Django app allowing users to manually order objects via admin
Group: Development/Python3

%description -n python3-module-%oname
Provides an additional order tool within admin with which objects can be
ordered by any number of arbitrary settings defined fields. A
user_order_by queryset method allows for retrieval of objects as they
were ordered by users via admin.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Provides an additional order tool within admin with which objects can be
ordered by any number of arbitrary settings defined fields. A
user_order_by queryset method allows for retrieval of objects as they
were ordered by users via admin.

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.7-alt1.git20110915.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1.git20110915
- Initial build for Sisyphus

