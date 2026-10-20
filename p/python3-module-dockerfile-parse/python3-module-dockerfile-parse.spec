%define pypi_name dockerfile-parse
%define mod_name dockerfile_parse

%def_with check

Name:    python3-module-%pypi_name
Version: 2.0.1
Release: alt1

Summary: Python library for parsing Dockerfile files
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/dockerfile-parse/
VCS:     https://github.com/containerbuildsystem/dockerfile-parse

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc LICENSE *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Oct 03 2026 Evgeniy Serov <scala@altlinux.org> 2.0.1-alt1
- Initial build for Sisyphus.
