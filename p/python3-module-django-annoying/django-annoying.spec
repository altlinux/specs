%define _unpackaged_files_terminate_build 1
%define oname django-annoying

Name: python3-module-%oname
Version: 0.10.3
Release: alt2

Summary: Django application that tries to eliminate annoying things in the Django framework
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-annoying/
BuildArch: noarch

# https://github.com/skorokithakis/django-annoying.git
Source0: https://pypi.python.org/packages/2b/8f/42d3203498a9e5487467a09548a758c2e6449f92fe17c497fdd51f6c7f95/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3


%description
This django application eliminates certain annoyances in the Django
framework.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This django application eliminates certain annoyances in the Django
framework.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%files
%doc PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Tue Dec 17 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.10.3-alt2
- build for python2 disabled

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt1.git20140525.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20140525
- Initial build for Sisyphus

