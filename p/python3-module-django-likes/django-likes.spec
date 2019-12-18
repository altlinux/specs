%define oname django-likes

Name: python3-module-%oname
Version: 2.0.1
Release: alt1

Summary: Django app providing view interface to django-secretballot
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-likes/
BuildArch: noarch

# https://github.com/praekelt/django-likes.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
This app utilizes django-secretballot to provide Facebook or Google+1
style item liking of Django model objects. Authenticated or anonymous
users are allowed to like any given object only once.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This app utilizes django-secretballot to provide Facebook or Google+1
style item liking of Django model objects. Authenticated or anonymous
users are allowed to like any given object only once.

This package contains tests for %oname.

%prep
%setup

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
* Wed Dec 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.1-alt1
- Version updated to 2.0.1
- build for python2 disabled

* Sun May 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20131108.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20131108
- Initial build for Sisyphus

