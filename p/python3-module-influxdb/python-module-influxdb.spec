%define oname influxdb

%def_with check

Name: python3-module-%oname
Version: 5.3.1
Release: alt4

Summary: Python client for InfluxDB

License: MIT
Group: Development/Python3
Url: https://github.com/influxdata/influxdb-python

Source: %name-%version.tar
Patch: remove-nose.patch
Patch1: remove-distutils-for-python-3.12.patch
Patch2: python-influxdb-new-pandas.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-msgpack
BuildRequires: python3-module-requests-mock
BuildRequires: python3-module-pytz
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-pandas-tests
%endif

%add_python3_req_skip pandas

%description
InfluxDB-Python is a client for interacting with InfluxDB.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1
sed -e 's/^import mock/from unittest import mock/' \
    -e 's/^from mock import/from unittest.mock import/' \
    -e 's/assertRaisesRegexp/assertRaisesRegex/' \
    -i influxdb/tests/*.py influxdb/tests/*/*.py

sed -i "s/freq='H'/freq='h'/g" influxdb/tests/dataframe_client_test.py

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -k 'not test_write_points_from_dataframe_with_tags_and_nan_json and not testWarnBulkSizeNoEffect'

%files
%python3_sitelibdir/*
%doc docs/source examples README.rst
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%changelog
* Sat Jul 27 2024 Anton Vyatkin <toni@altlinux.org> 5.3.1-alt4
- Fixed FTBFS.

* Thu Jan 25 2024 Anton Vyatkin <toni@altlinux.org> 5.3.1-alt3
- Fixed FTBFS.

* Tue Oct 17 2023 Grigory Ustinov <grenka@altlinux.org> 5.3.1-alt2
- Dropped dependency on distutils.

* Fri Apr 21 2023 Anton Vyatkin <toni@altlinux.org> 5.3.1-alt1
- New version 5.3.1.

* Tue Aug 17 2021 Vitaly Lipatov <lav@altlinux.ru> 5.2.2-alt4
- make pandas requirement optional

* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 5.2.2-alt3
- Rename package, spec cleanup.

* Wed Feb 05 2020 Vitaly Lipatov <lav@altlinux.ru> 5.2.2-alt2
- rebuild without python2 subpackage

* Thu Mar 21 2019 Alexey Shabalin <shaba@altlinux.org> 5.2.2-alt1
- 5.2.2
- add python3 package

* Sat Mar 17 2018 Terechkov Evgenii <evg@altlinux.org> 5.0.0-alt1
- 5.0.0

* Sun Oct 22 2017 Terechkov Evgenii <evg@altlinux.org> 4.1.1-alt1
- Initial build for ALT Linux Sisyphus
