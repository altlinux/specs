%define pypi_name napalm-ce
%define mod_name napalm_ce

%def_with check

Name:    python3-module-%pypi_name
Version: 0.2.0
Release: alt1

Summary: NAPALM driver for Huawei CloudEngine switch
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/napalm-automation-community/napalm-ce

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-napalm
BuildRequires: python3-module-netmiko
BuildRequires: python3-module-pylama
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
This is a NAPALM community driver for the Huawei CloudEngine Switch.

%prep
%setup -n %pypi_name-%version
sed -i "s/netmiko.ssh_exception/netmiko.exceptions/" napalm_ce/ce.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -s -k 'not (test_get_config_filtered or test_get_interfaces or test_get_facts)'

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Dec 08 2023 Alexander Burmatov <thatman@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus.
