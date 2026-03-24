%define _unpackaged_files_terminate_build 1
%define pypi_name apispec
%define mod_name apispec

%def_with check

Name: python3-module-%pypi_name
Version: 6.10.0
Release: alt1
Summary: A pluggable API specification generator
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/apispec/
Vcs: https://github.com/marshmallow-code/apispec/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core

%if_with check
BuildRequires: python3-module-yaml
BuildRequires: python3-module-marshmallow
BuildRequires: python3-module-openapi-spec-validator
%endif

%description
%summary.
Currently supports the OpenAPI Specification (f.k.a. the Swagger specification).

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.rst LICENSE docs/
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Mar 24 2026 Alexey Rodygin <alehandro@altlinux.org> 6.10.0-alt1
- Updated to new version 6.10.0.

* Tue Jan 13 2026 Alexey Rodygin <alehandro@altlinux.org> 6.8.4-alt1
- Initial build for ALT Linux
