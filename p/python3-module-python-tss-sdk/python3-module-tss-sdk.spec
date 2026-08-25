%define pypi_name python-tss-sdk

%def_without check

Name: python3-module-%pypi_name
Version: 1.2.3
Release: alt2

Summary: A Python SDK for Delinea Secret Server
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/python-tss-sdk
VCS: https://github.com/DelineaXPM/python-tss-sdk

BuildArch: noarch

Source: %pypi_name-%version.tar
# https://github.com/DelineaXPM/python-tss-sdk/pull/99
Patch0: python-tss-sdk-1.2.3-fix-build-support-flit-core-4.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core

%description
The Delinea Secret Server Python SDK contains classes that interact with
Secret Server via the REST API.

%prep
%setup -n %pypi_name-%version
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install
rm -rf %buildroot%python3_sitelibdir/delinea/__init__.py
rm -rf %buildroot%python3_sitelibdir/delinea/__pycache__
rm -rf %buildroot%python3_sitelibdir/delinea/secrets/__init__.py
rm -rf %buildroot%python3_sitelibdir/delinea/secrets/__pycache__/

%files
%doc README.*
%dir %python3_sitelibdir/delinea
%dir %python3_sitelibdir/delinea/secrets/
%dir %python3_sitelibdir/delinea/secrets/__pycache__/
%python3_sitelibdir/delinea/secrets/__pycache__/
%python3_sitelibdir/delinea/secrets/server.py
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Aug 25 2026 Stanislav Levin <slev@altlinux.org> 1.2.3-alt2
- NMU: fixed FTBFS (flit-core 4).

* Thu Jul 25 2024 Anton Vyatkin <toni@altlinux.org> 1.2.3-alt1
- Initial build for Sisyphus
