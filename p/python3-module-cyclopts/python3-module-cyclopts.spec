%define pypi_name cyclopts

Name: python3-module-%pypi_name
Version: 4.7.0
Release: alt1

Summary: Intuitive, easy CLIs based on Python type hints
License: Apache-2.0
Group: Development/Python3
URL: https://github.com/BrianPugh/cyclopts

BuildArch: noarch

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs

%description
Cyclopts is a modern, easy-to-use command-line interface (CLI)
framework for Python. It uses type hints to generate CLI
argument parsers with minimal boilerplate.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%files
%_bindir/cyclopts
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Mar 05 2026 Vitaly Lipatov <lav@altlinux.ru> 4.7.0-alt1
- initial build

