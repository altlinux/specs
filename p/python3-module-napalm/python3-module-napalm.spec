%define pypi_name napalm

%def_with check

Name:    python3-module-%pypi_name
Version: 4.1.0
Release: alt1

Summary: Network Automation and Programmability Abstraction Layer with Multivendor support
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/napalm-automation/napalm

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-json-report
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-netmiko
BuildRequires: python3-module-netutils
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-lxml
BuildRequires: python3-module-netaddr
BuildRequires: python3-module-yaml
BuildRequires: python3-module-pyeapi
BuildRequires: python3-module-junos-eznc
BuildRequires: python3-module-requests
BuildRequires: python3-module-mock
BuildRequires: python3-module-ddt
BuildRequires: python3-module-ttp
BuildRequires: python3-module-ttp_templates
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar
Patch1: fix-broken-imports.patch

%description
NAPALM (Network Automation and Programmability Abstraction Layer withi
Multivendor support) is a Python library that implements a set of functions to
interact with different router vendor devices using a unified API.

%prep
%setup -n %pypi_name-%version
%patch1 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
rm -fr test/junos/
%pyproject_run_pytest

%files
%doc *.md
%_bindir/%pypi_name
%_bindir/cl_napalm_test
%_bindir/cl_napalm_validate
%_bindir/cl_napalm_configure
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Nov 13 2023 Alexander Burmatov <thatman@altlinux.org> 4.1.0-alt1
- Initial build for Sisyphus.
