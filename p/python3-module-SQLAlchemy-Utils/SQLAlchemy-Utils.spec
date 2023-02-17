%define oname SQLAlchemy-Utils

Name: python3-module-%oname
Version: 0.40.0
Release: alt1

Summary: Various utility functions for SQLAlchemy

License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/kvesteri/sqlalchemy-utils

Source: %name-%version.tar
BuildArch: noarch
%py3_provides %oname

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-SQLAlchemy >= 1.3

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE *.rst
%python3_sitelibdir/sqlalchemy_utils
%python3_sitelibdir/SQLAlchemy_Utils-%version-py%_python3_version.egg-info

%changelog
* Fri Feb 17 2023 Grigory Ustinov <grenka@altlinux.org> 0.40.0-alt1
- Automatically updated to 0.40.0.

* Mon Dec 26 2022 Grigory Ustinov <grenka@altlinux.org> 0.39.0-alt1
- Automatically updated to 0.39.0.

* Sun Aug 07 2022 Grigory Ustinov <grenka@altlinux.org> 0.38.3-alt1
- Build new version.

* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 0.32.1-alt2
- Drop python2 support.

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 0.32.1-alt1
- Initial build for Sisyphus.

