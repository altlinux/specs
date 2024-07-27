%define pypi_name tacacs_plus

%def_with check

Name: python3-module-%pypi_name
Version: 2.6
Release: alt1

Summary: A client for TACACS+ authentication
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/tacacs_plus
VCS: https://github.com/ansible/tacacs_plus

BuildArch: noarch

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-six
%endif

%description
A Python-based TACACS+ client that supports authentication,
authorization and accounting.

%prep
%setup -n %pypi_name-%version

sed -i '/addopts/d' setup.cfg

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.*
%_bindir/tacacs_client
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/tests

%changelog
* Mon Jul 22 2024 Anton Vyatkin <toni@altlinux.org> 2.6-alt1
- Initial build for Sisyphus.
