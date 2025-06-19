%define _unpackaged_files_terminate_build 1
%define pypi_name sarif-tools
%define mod_name sarif

%def_with check

Name: python3-module-%pypi_name
Version: 3.0.4
Release: alt1

Summary: A set of Python command line tools for working with SARIF files produced by code analysis tools
License: MIT
Group: Development/Tools
Url: https://pypi.org/project/sarif-tools/
Vcs: https://github.com/microsoft/sarif-tools

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-jsonpath-ng
BuildRequires: python3-module-matplotlib
BuildRequires: python3-module-poetry
BuildRequires: python3-module-yaml
BuildRequires: python3-module-docx
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-jsonschema
%endif

%description
A set of command line tools and Python library for working with SARIF files.
Read more about the SARIF format here: https://sarifweb.azurewebsites.net.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README.md
%_bindir/%mod_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Jun 19 2025 Dmitry Mikhalchenko <tascad@altlinux.org> 3.0.4-alt1
- Initial build for ALT Sisyphus.
