%define pypi_name openapi-core
%define mod_name openapi_core

%def_with check

Name: python3-module-%pypi_name
Version: 0.17.2
Release: alt1
Summary: Client-side and server-side support for the OpenAPI Specification v3
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/openapi-core/
Vcs: https://github.com/python-openapi/openapi-core
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-lazy-object-proxy
BuildRequires: python3-module-jsonschema-spec
BuildRequires: python3-module-openapi-spec-validator
BuildRequires: python3-module-werkzeug
BuildRequires: python3-module-isodate
BuildRequires: python3-module-more-itertools
BuildRequires: python3-module-parse
BuildRequires: python3-module-flask
%endif

%description
Openapi-core is a Python library that adds client-side and server-side support
for the OpenAPI v3.0 and OpenAPI v3.1 specification.

%prep
%setup
sed -i '/--cov/d' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests/unit -v

%files
%doc README.*
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Mon Jun 19 2023 Anton Vyatkin <toni@altlinux.org> 0.17.2-alt1
- Initial build for Sisyphus
