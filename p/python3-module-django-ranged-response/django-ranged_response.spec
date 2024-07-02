%define _unpackaged_files_terminate_build 1
%define pypi_name django-ranged-response
%define mod_name ranged_response

Name: python3-module-%pypi_name
Version: 0.2.0
Release: alt1

Summary: Modified Django FileResponse that adds Content-Range headers

License: BSD
Group: Development/Python3
Url: https://pypi.org/project/django-ranged-response/

BuildArch: noarch

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)


%description
Modified Django FileResponse that adds Content-Range headers.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
%python3_prune

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/


%changelog
* Fri Jun 28 2024 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1
- initial build for Sisyphus

