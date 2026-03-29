%define _unpackaged_files_terminate_build 1
%define pypi_name hypothesis-openapi
%define mod_name hypothesis_openapi

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.0
Release: alt1.1

Summary: Hypothesis plugin for generating valid Open API documents
License: MIT
Group: Development/Python3
Url: https://github.com/Stranger6667/hypothesis-openapi
VCS: https://github.com/Stranger6667/hypothesis-openapi.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-coverage
BuildRequires: python3-module-hypothesis
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-referencing
%endif

%description
Hypothesis plugin for generating valid Open API documents.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.3.0-alt1.1
- Demodernized packaging.

* Tue Mar 03 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 0.3.0-alt1
- New version (0.3.0).
- Updated dependencies management.

* Thu Oct 03 2024 Martynenko Evgeniy <enimalojd@altlinux.org> 0.2.1-alt1
  - Initial build for ALT.
