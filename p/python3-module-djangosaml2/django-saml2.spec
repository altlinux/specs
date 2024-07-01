%define _unpackaged_files_terminate_build 1
%define pypi_name djangosaml2
%define mod_name djangosaml2

Name: python3-module-%pypi_name
Version: 1.9.3
Release: alt1

Summary: pysaml2 integration for Django

License: BSD
Group: Development/Python3
Url: https://pypi.org/project/djangosaml2/

BuildArch: noarch

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)


%description
A Django application that builds a Fully Compliant SAML2 Service Provider on top of PySAML2 library.
Djangosaml2 protects your project with a SAML2 SSO Authentication.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
%python3_prune

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/


%changelog
* Fri Jun 28 2024 Vitaly Lipatov <lav@altlinux.ru> 1.9.3-alt1
- initial build for Sisyphus

