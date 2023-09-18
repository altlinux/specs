%define oname mysql-replication

%def_without check

Name: python3-module-%oname
Version: 0.44.0
Release: alt1

Summary: Pure Python Implementation of MySQL replication protocol build on top of PyMYSQL

License: Apache-2.0
Group: Development/Python3
URL: https://pypi.org/project/mysql-replication
VCS: https://github.com/julien-duponchelle/python-mysql-replication

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
Pure Python Implementation of MySQL replication protocol build on top of PyMYSQL.
This allow you to receive event like insert, update, delete with their datas
and raw SQL queries.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc CHANGELOG README.md
%python3_sitelibdir/pymysqlreplication
%python3_sitelibdir/mysql_replication-%version.dist-info
%exclude %python3_sitelibdir/pymysqlreplication/tests

%changelog
* Mon Sep 18 2023 Grigory Ustinov <grenka@altlinux.org> 0.44.0-alt1
- Automatically updated to 0.44.0.

* Mon Jul 24 2023 Grigory Ustinov <grenka@altlinux.org> 0.43.0-alt1
- Automatically updated to 0.43.0.

* Mon Jul 17 2023 Grigory Ustinov <grenka@altlinux.org> 0.42.2-alt1
- Automatically updated to 0.42.2.

* Tue Jun 13 2023 Grigory Ustinov <grenka@altlinux.org> 0.41.1-alt1
- Automatically updated to 0.41.1.

* Thu May 18 2023 Grigory Ustinov <grenka@altlinux.org> 0.40-alt1
- Automatically updated to 0.40.

* Mon Mar 13 2023 Grigory Ustinov <grenka@altlinux.org> 0.31-alt1
- Automatically updated to 0.31.

* Thu May 26 2022 Grigory Ustinov <grenka@altlinux.org> 0.30-alt1
- Build new version.

* Sun Jan 24 2021 Vitaly Lipatov <lav@altlinux.ru> 0.22-alt1
- initial build for ALT Sisyphus
