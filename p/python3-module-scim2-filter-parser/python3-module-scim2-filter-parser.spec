%define pypi_name scim2_filter_parser

%def_with check

Name: python3-module-scim2-filter-parser
Version: 0.7.0
Release: alt1

Summary: A customizable parser/transpiler for SCIM2.0 filters

License: MIT
Group: Development/Python3
URL: https://github.com/15five/scim2-filter-parser
# Source-url: %__pypi_url %pypi_name
Source: %pypi_name-%version.tar
Patch: scim2-filter-parser-alt-poetry-core.patch

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core

%if_with check
BuildRequires: python3-module-sly
%endif

%description
A customizable parser/transpiler for SCIM2.0 filters.

%prep
%setup -n %pypi_name-%version
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 -c 'from scim2_filter_parser import transpilers, parser, lexer'

%files
%doc README*
%_bindir/sfp-*
%python3_sitelibdir/scim2_filter_parser/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- initial build for Sisyphus
