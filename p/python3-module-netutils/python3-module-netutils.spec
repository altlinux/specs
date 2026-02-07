%define pypi_name netutils

%def_with check

Name:    python3-module-%pypi_name
Version: 1.17.1
Release: alt1

Summary: Python library that is a collection of functions and objects for common network automation tasks
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/networktocode/netutils

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-toml
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-crypt-r
%endif

%add_python3_req_skip distutils.version

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
A Python library that is a collection of functions that are used in the common
network automation tasks. Tasks such as converting a BGP ASN to and from dotted
format, normalizing an interface name, or "type 5" encrypting a password.
The intention is to centralize these functions while keeping the library light.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -k "not (test_is_fqdn_resolvable or test_fqdn_to_ip)"

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Feb 07 2026 Grigory Ustinov <grenka@altlinux.org> 1.17.1-alt1
- Automatically updated to 1.17.1.

* Sun Oct 12 2025 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt2.1
- Fixed FTBFS.

* Mon Nov 20 2023 Alexander Burmatov <thatman@altlinux.org> 1.6.0-alt2
- Skip distutils requires.

* Tue Nov 14 2023 Alexander Burmatov <thatman@altlinux.org> 1.6.0-alt1
- Initial build for Sisyphus.
