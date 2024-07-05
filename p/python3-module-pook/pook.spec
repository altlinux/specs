%define  oname pook

# tests rely on lots of network
%def_without check

Name:    python3-module-%oname
Version: 2.0.0
Release: alt1

Summary: HTTP traffic mocking and testing made easy in Python

License: MIT
Group:   Development/Python3
URL:     https://github.com/h2non/pook

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-furl
BuildRequires: python3-module-xmltodict
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-requests
BuildRequires: python3-module-urllib3
BuildRequires: python3-module-httpx
BuildRequires: python3-module-pytest-httpbin
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -k 'not test_engines' --ignore="tests/unit/interceptors" --ignore="tests/integration"

%files
%doc LICENSE *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Fri Jul 05 2024 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Automatically updated to 2.0.0.

* Tue Apr 02 2024 Grigory Ustinov <grenka@altlinux.org> 1.4.3-alt1
- Automatically updated to 1.4.3.

* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 1.1.1-alt2
- Fixed FTBFS.

* Fri Jan 13 2023 Grigory Ustinov <grenka@altlinux.org> 1.1.1-alt1
- Automatically updated to 1.1.1.

* Thu Jan 12 2023 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1
- Automatically updated to 1.1.0.

* Fri Jun 24 2022 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus.
