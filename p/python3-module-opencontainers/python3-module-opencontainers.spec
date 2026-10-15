%define pypi_name opencontainers

%def_with check

Name: python3-module-opencontainers
Version: 0.0.15
Release: alt1

Summary: Python module for Open Container Initiative (OCI) specifications

License: MPL-2.0
Group: Development/Python3
URL: https://github.com/vsoch/oci-python
# Source-url: %__pypi_url %pypi_name
Source: %pypi_name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
%endif

%description
Python module for Open Container Initiative (OCI) specifications.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 -c 'import opencontainers'

%files
%doc README*
%python3_sitelibdir/opencontainers/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 0.0.15-alt1
- initial build for Sisyphus
