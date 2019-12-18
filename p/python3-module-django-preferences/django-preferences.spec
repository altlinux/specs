%define _unpackaged_files_terminate_build 1
%define oname django-preferences

Name: python3-module-%oname
Version: 1.0.0
Release: alt1

Summary: Django app allowing users to set app specific preferences through the admin interface
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-preferences/
BuildArch: noarch

# https://github.com/praekelt/django-preferences.git
Source0: %name-%version.tar.gz

BuildRequires(pre): rpm-build-python3


%description
Provides singleton admin views for Preferences objects and a simple
interface to preference values. Singleton views ensure only one
preference intance per site is available for each Preferences class.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Provides singleton admin views for Preferences objects and a simple
interface to preference values. Singleton views ensure only one
preference intance per site is available for each Preferences class.

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
* Wed Dec 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt1
- Version updated to 1.0.0
- build for python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.6-alt1.git20120612.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20120612
- Initial build for Sisyphus

