%define _unpackaged_files_terminate_build 1
%define oname clickhouse-driver

Name:       python3-module-%oname
Version:    0.2.5
Release:    alt1
License:    MIT
Group:      Development/Python3
Summary:    ClickHouse Python Driver with native interface support.
Url:        https://github.com/mymarilyn/clickhouse-driver
Source:     %name-%version.tar
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-tzlocal
BuildRequires: python3-module-pytz

Requires: python3-module-clickhouse-cityhash
Requires: python3-module-numpy
Requires: python3-module-tzlocal

%add_python3_req_skip pandas pandas.api.types

%add_python3_self_prov_path %buildroot%python3_sitelibdir/clickhouse_driver/tests/

%description
ClickHouse Python Driver with native (TCP) interface support.

%package    tests
Group:      Development/Python3
Summary:    ClickHouse Python Driver with native interface support.
Requires:   python3-module-%oname = %EVR

%description tests
ClickHouse Python Driver with native (TCP) interface support.

Package contains tests for %name.

%prep
%setup

%build
%pyproject_build

# install module for sphinx to temporary directory 
%__python3 setup.py install --skip-build --root=_build --force
export PYTHONPATH=$PWD/_build/%python3_sitelibdir
%make -C docs/ man SPHINXBUILD=sphinx-build-3

%install
%pyproject_install

cp -fR tests/ %buildroot%python3_sitelibdir/clickhouse_driver/
mkdir -p %buildroot/%_man1dir
install -pm0644 docs/*/man/*.1 %buildroot/%_man1dir/

%files
%doc LICENSE README.* CONTRIBUTING.rst
%python3_sitelibdir/*
%_man1dir/*.1.*
%exclude %python3_sitelibdir/clickhouse_driver/tests/

%files tests
%python3_sitelibdir/clickhouse_driver/tests/

%changelog
* Wed Mar 29 2023 Danil Shein <dshein@altlinux.org> 0.2.5-alt1
- NMU: 0.2.4 -> 0.2.5
  + fix FTBFS
  + migarte to pyproject_installer

* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 0.2.4-alt2.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Wed Nov 02 2022 Paul Wolneykien <manowar@altlinux.org> 0.2.4-alt2
- Fix: Added python3-module-tzlocal to the package requirements.

* Tue Jun 28 2022 Anton Farygin <rider@altlinux.ru> 0.2.4-alt1
- 0.2.3 -> 0.2.4

* Mon Feb 21 2022 Anton Farygin <rider@altlinux.ru> 0.2.3-alt1
- 0.2.2 -> 0.2.3

* Tue Dec 14 2021 Anton Farygin <rider@altlinux.ru> 0.2.2-alt2
- make pandas requires optional

* Wed Sep 29 2021 Anton Farygin <rider@altlinux.ru> 0.2.2-alt1
- 0.2.2

* Mon Aug 16 2021 Anton Farygin <rider@altlinux.ru> 0.2.1-alt1
- 0.2.1

* Thu Feb 11 2021 Anton Farygin <rider@altlinux.org> 0.2.0-alt1
- 0.2.0

* Fri Oct 02 2020 Anton Farygin <rider@altlinux.ru> 0.1.5-alt1
- 0.1.5

* Fri Jun 19 2020 Anton Farygin <rider@altlinux.ru> 0.1.4-alt1
- 0.1.4

* Fri Feb 21 2020 Anton Farygin <rider@altlinux.ru> 0.1.2-alt1
- 0.1.2

* Fri Oct 04 2019 Anton Farygin <rider@altlinux.ru> 0.1.1-alt1
- 0.1.1
- built and install man page 

* Thu Aug 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.0-alt1
- Version updated to 0.1.0

* Wed Jun 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.20-alt1
- Initial build for Sisyphus
