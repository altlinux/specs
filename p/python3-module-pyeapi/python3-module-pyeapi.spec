%define pypi_name pyeapi

%def_with check

Name:    python3-module-%pypi_name
Version: 1.0.2
Release: alt1

Summary: Python client for Arista eAPI
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/arista-eosplus/pyeapi

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-netaddr
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
The Python library for Arista's eAPI command API implementation provides a
client API work using eAPI and communicating with EOS nodes. The Python library
can be used to communicate with EOS either locally (on-box) or remotely
(off-box). It uses a standard INI-style configuration file to specify one or
more nodes and connection properties.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest test/unit

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Nov 14 2023 Alexander Burmatov <thatman@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus.
