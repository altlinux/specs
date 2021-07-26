%define oname SQLAlchemy-Utils

Name: python3-module-%oname
Version: 0.32.1
Release: alt2

Summary: Various utility functions for SQLAlchemy.
License: BSD
Group: Development/Python3
Url: https://github.com/kvesteri/sqlalchemy-utils

Source: %oname-%version.tar
BuildArch: noarch
%py3_provides %oname

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-six
BuildRequires: python3-module-SQLAlchemy >= 1.0

%description
%summary

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %version-%release

%description tests
%summary

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*
#exclude %python3_sitelibdir/*/tests

#files -n python3-module-%oname-tests
#python3_sitelibdir/*/tests

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 0.32.1-alt2
- Drop python2 support.

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 0.32.1-alt1
- Initial build for Sisyphus.

