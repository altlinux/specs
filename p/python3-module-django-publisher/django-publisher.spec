%define oname django-publisher

Name: python3-module-%oname
Version: 0.0.3
Release: alt2

Summary: Django external publishing app
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-publisher/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Django external publishing app.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Django external publishing app.

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
%exclude %python3_sitelibdir/*/tests.*

%files tests
%python3_sitelibdir/*/tests.*


%changelog
* Tue Dec 17 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.3-alt2
- build for python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.0.3-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.3-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1
- Initial build for Sisyphus

