%define pypi_name requests-ntlm

%def_with check

Name:    python3-module-%pypi_name
Version: 1.3.0
Release: alt1

Summary: NTLM authentication support for Requests

License: ISC
Group:   Development/Python3
URL:     https://pypi.org/project/requests-ntlm
VCS:     https://github.com/requests/requests-ntlm

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-spnego
BuildRequires: python3-module-requests
BuildRequires: python3-module-flask
%endif

%description
%summary.

%prep
%setup
sed -i -e 's/requests.packages.\(urllib3.response\)/\1/' requests_ntlm/requests_ntlm.py

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
# These tests require network
%tox_check_pyproject -- --ignore=tests/functional/test_functional.py -k\
                        'not TestRequestsNtlm'

%files
%doc LICENSE *.rst
%python3_sitelibdir/requests_ntlm
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jul 01 2024 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt1
- Automatically updated to 1.3.0.

* Thu Jul 27 2023 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus.
