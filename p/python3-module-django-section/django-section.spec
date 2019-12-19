%define oname django-section

Name: python3-module-%oname
Version: 0.0.3
Release: alt3

Summary: Django app for determining site section by request
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-section/
BuildArch: noarch

# https://github.com/praekelt/django-section.git
Source: %name-%version.tar
Patch0: port-on-new-django.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-django-snippetscream


%description
Django app for determining site section by request.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Django app for determining site section by request.

This package contains tests for %oname.

%prep
%setup
%patch0 -p1

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
* Thu Dec 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.3-alt3
- porting on python3

* Sun May 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.0.3-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.3-alt1.git20110908.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20110908
- Initial build for Sisyphus

