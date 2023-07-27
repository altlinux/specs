%define pypi_name requests-credssp

%def_with check

Name:    python3-module-%pypi_name
Version: 2.0.0
Release: alt1

Summary: An authentication handler for using CredSSP with Python Requests

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/requests-credssp
VCS:     https://github.com/jborean93/requests-credssp

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
BuildRequires: python3-module-pytest-cov
%endif

%description
This package allows for HTTPS CredSSP authentication using the requests library.
CredSSP is a Microsoft authentication that allows your credentials
to be delegated to a server giving you double hop authentication.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE *.md
%python3_sitelibdir/requests_credssp
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Jul 27 2023 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus.
