%define _unpackaged_files_terminate_build 1
%define rname clickhouse_test

# To run the build test the clickhouse-server package is needed.
%ifarch x86_64 aarch64
%def_with tests
%else
%def_without tests
%endif

Name: test-with-clickhouse
Version: 0.1.3
Release: alt1

Group: Development/Python3
Summary: A wrapper to run tests against ClickHouse server
Url: http://git.altlinux.org/people/manowar/packages/python3-module-clickhouse-test.git
License: GPLv2+

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools) python3(wheel)

%if_with tests
BuildRequires: python3(pytest)
BuildRequires: clickhouse-server /proc
BuildRequires: python3(clickhouse_driver)
%endif

%description
A wrapper to run tests against ClickHouse server.

%package -n python3-module-%rname
Group: Development/Python3
Summary: A wrapper to run tests against ClickHouse server
BuildArch: noarch

%description -n python3-module-%rname
A wrapper to run tests against ClickHouse server.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%if_with tests
%pyproject_run_pytest
%endif

%files -n python3-module-%rname
%python3_sitelibdir_noarch/%rname
%python3_sitelibdir_noarch/%rname-%version.dist-info

%changelog
* Thu Apr 18 2024 Paul Wolneykien <manowar@altlinux.org> 0.1.3-alt1
- Add support to test UDFs and with UDFs.
- Add configuration parameters to the ClickHouseTestServer()
  constructor.

* Thu Apr 04 2024 Paul Wolneykien <manowar@altlinux.org> 0.1.2-alt2
- Disable build test on arches where clickhouse-server is not
  available.

* Mon Oct 16 2023 Paul Wolneykien <manowar@altlinux.org> 0.1.2-alt1
- Improved logging control.
- Fix: Make CLICKHOUSE_SERVER_CLEANUP=0 disable cleanup.

* Wed Oct 11 2023 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt1
- Add support for CLICKHOUSE_SERVER_CLEANUP.

* Tue Oct 10 2023 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus.
