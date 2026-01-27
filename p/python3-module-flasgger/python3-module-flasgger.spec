%define pypi_name flasgger

Name: python3-module-%pypi_name
Version: 0.9.7.1
Release: alt1

Summary: Extract swagger specs from your Flask project
License: MIT
Group: Development/Python3
URL: https://github.com/flasgger/flasgger/

BuildArch: noarch

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
Flasgger is a Flask extension to extract OpenAPI-Specification from all Flask
views registered in your API.

Flasgger also comes with SwaggerUI embedded so you can access
http://localhost:5000/apidocs and visualize and interact with your API resources.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jan 20 2025 Vitaly Lipatov <lav@altlinux.ru> 0.9.7.1-alt1
- initial build for ALT Sisyphus
