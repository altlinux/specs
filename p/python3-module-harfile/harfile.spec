%define _unpackaged_files_terminate_build 1
%define pypi_name harfile

%def_with check

Name:    python3-module-%pypi_name
Version: 0.3.0
Release: alt1

Summary:   This package provides zero dependency writer for building HAR (HTTP Archive) files in Python
License:   MIT
Group:     Development/Python3
Url:       https://github.com/schemathesis/harfile
Vcs:       https://github.com/schemathesis/harfile.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-hypothesis
%endif

%description
This package provides zero dependency writer for building
HAR (HTTP Archive) files in Python.

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
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Sep 30 2024 Martynenko Evgeniy <enimalojd@altlinux.org> 0.3.0-alt1
  - Initial build for ALT.
