%define oname django-order

Name: python3-module-%oname
Version: 0.0.7
Release: alt2

Summary: Django app allowing users to manually order objects via admin
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-order/
BuildArch: noarch

# https://github.com/praekelt/django-order.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Provides an additional order tool within admin with which objects can be
ordered by any number of arbitrary settings defined fields. A
user_order_by queryset method allows for retrieval of objects as they
were ordered by users via admin.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Provides an additional order tool within admin with which objects can be
ordered by any number of arbitrary settings defined fields. A
user_order_by queryset method allows for retrieval of objects as they
were ordered by users via admin.

This package contains tests for %oname.

%prep
%setup

sed -i 's|core.urlresolvers|urls|' order/utils.py

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
* Wed Dec 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.7-alt2
- build for python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.0.7-alt1.git20110915.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.7-alt1.git20110915.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1.git20110915
- Initial build for Sisyphus

