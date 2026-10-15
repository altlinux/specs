%define pypi_name duo_client

%def_with check

Name: python3-module-duo-client
Version: 5.7.0
Release: alt1

Summary: Reference client for Duo Security APIs

License: BSD-3-Clause
Group: Development/Python3
URL: https://github.com/duosecurity/duo_client_python
# Source-url: %__pypi_url %pypi_name
Source: %pypi_name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-freezegun
BuildRequires: python3-module-pytz
%endif

%description
Reference client for Duo Security APIs.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
# test_logo needs a resource file missing from sdist; ssl hostname tests depend on the python version
%__python3 -m pytest -v tests --deselect tests/admin/test_logo.py::TestLogo::test_update_logo --deselect tests/test_https_wrapper.py::TestSSLContextCreation::test_server_hostname --deselect tests/test_https_wrapper.py::TestSSLContextCreation::test_server_hostname_with_port

%files
%doc README*
%python3_sitelibdir/duo_client/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 5.7.0-alt1
- initial build for Sisyphus
