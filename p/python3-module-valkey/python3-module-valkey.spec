%define pypi_name valkey

%def_without check

Name:    python3-module-%pypi_name
Version: 6.1.0
Release: alt1

Summary: Valkey Python client based on a fork of redis-py
License: MIT
Group:   Development/Python3
URL:     https://github.com/valkey-io/valkey-py

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
The Python interface to the Valkey key-value store.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed May 28 2025 Alexander Burmatov <thatman@altlinux.org> 6.1.0-alt1
- Initial build for Sisyphus.
