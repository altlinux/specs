%define oname django-facebook-realtime

Name: python3-module-%oname
Version: 0.1.1.20130208
Release: alt2

Summary: A reusable app to interact with facebook real-time updates 
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-facebook-realtime/
BuildArch: noarch

# https://github.com/rmaceissoft/django-facebook-realtime.git
Source: %name-%version.tar
Patch0: port-on-new-django.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
Django app for adding/removing/listing facebook realtime subscriptions
and retrieving facebook realtime updates.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Django app for adding/removing/listing facebook realtime subscriptions
and retrieving facebook realtime updates.

This package contains tests for %oname.

%prep
%setup
%patch0 -p1

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Thu Dec 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.1.20130208-alt2
- build for python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.1.20130208-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1.20130208-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1.20130208-alt1
- Initial build for Sisyphus

