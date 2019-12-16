%define oname django-taggit

Name: python3-module-%oname
Version: 1.2.0
Release: alt1

Summary: Simple tagging for django
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-taggit
BuildArch: noarch

# https://github.com/alex/django-taggit.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-isort


%description
django-taggit is a reusable Django application for simple tagging.

%package tests
Summary: Tests for %name
Group: Development/Python3
Requires: %name = %EVR

%description tests
django-taggit is a reusable Django application for simple tagging.

This package contains tests for %name.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc AUTHORS LICENSE *.rst docs/*
%python3_sitelibdir/*

%files tests



%changelog
* Mon Dec 16 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.2.0-alt1
- Version updated to 1.2.0
- build for python2 disabled

* Wed Dec 26 2018 Grigory Ustinov <grenka@altlinux.org> 0.23.0-alt1
- Build new version.

* Sun May 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.12.2-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.12.2-alt1.git20140921.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.12.2-alt1.git20140921.1
- NMU: Use buildreq for BR.

* Tue Sep 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.2-alt1.git20140921
- Initial build for Sisyphus

