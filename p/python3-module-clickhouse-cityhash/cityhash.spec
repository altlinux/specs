%define _unpackaged_files_terminate_build 1
%define oname clickhouse-cityhash


Name:       python3-module-%oname
Version:    1.0.2.4
Release:    alt2

License:    %mit
Group:      Development/Python3
Summary:    Python bindings for CityHash

Url:        https://github.com/xzkostyan/python-cityhash
Source:     %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Cython

BuildRequires: gcc-c++


%description
A fork of Python wrapper around CityHash with downgraded version of algorithm.
This fork used as 3-rd party library for hashing data in ClickHouse protocol.
Unfortunately ClickHouse server comes with built-in old version of this algorithm.

%package    tests
Group:      Development/Python3
Summary:    Python bindings for CityHash

%add_python3_req_skip cityhash
Requires:   python3-module-%oname = %EVR

%description tests
A fork of Python wrapper around CityHash with downgraded version of algorithm.
This fork used as 3-rd party library for hashing data in ClickHouse protocol.
Unfortunately ClickHouse server comes with built-in old version of this algorithm.

Package contains tests for %name.

%prep
%setup

%build
%python3_build

%install
%python3_install

install -d %buildroot%python3_sitelibdir/clickhouse_cityhash/tests
cp -fR tests/ %buildroot%python3_sitelibdir/clickhouse_cityhash/

%files
%doc LICENSE README.*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/clickhouse_cityhash/tests/

%files tests
%python3_sitelibdir/clickhouse_cityhash/tests/


%changelog
* Wed Dec 20 2023 Grigory Ustinov <grenka@altlinux.org> 1.0.2.4-alt2
- Add build dependency on Cython.

* Mon Dec 12 2022 Grigory Ustinov <grenka@altlinux.org> 1.0.2.4-alt1
- Build new version.

* Thu Aug 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2.3-alt1
- Initial build for Sisyphus

