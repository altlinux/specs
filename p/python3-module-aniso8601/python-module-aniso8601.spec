%define oname aniso8601

Summary: Another ISO 8601 parser for Python
Name: python3-module-%oname
Version: 4.0.1
Release: alt2
Url: https://bitbucket.org/nielsenb/aniso8601
Source: https://pypi.python.org/packages/source/a/%oname/%oname-%version.tar.gz
License: BSD
Group: Development/Python3

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
This is a Python library for parsing date strings
in ISO 8601 format into datetime format.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst LICENSE
%python3_sitelibdir/*
#%exclude %python3_sitelibdir/*/tests

#%files -n python3-module-%oname-tests
#%python3_sitelibdir/*/tests

%changelog
* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt2
- Drop python2 support.

* Thu Dec 13 2018 Alexey Shabalin <shaba@altlinux.org> 4.0.1-alt1
- initial build

