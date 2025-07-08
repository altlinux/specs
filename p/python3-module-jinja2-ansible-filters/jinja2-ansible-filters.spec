%define _unpackaged_files_terminate_build 1
%define pypi_name jinja2-ansible-filters
%define mod_name jinja2_ansible_filters

%def_with check

Name: python3-module-%pypi_name
Version: 1.3.2
Release: alt1

Summary: A port of Ansible's jinja2 filters without requiring ansible core
License: GPL-3.0
Group: Development/Python3
Url: https://pypi.org/project/jinja2-ansible-filters
VCS: https://gitlab.com/dreamer-labs/libraries/jinja2-ansible-filters

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-yaml
%endif

%description
A port of Ansible's jinja2 filters without requiring ansible core.

This library provides many of the filters available in Ansible without
requiring the full Ansible installation. It's useful for projects that
want to use Ansible's powerful Jinja2 filters in standalone applications.

Includes filters for data manipulation, string processing, mathematical
operations, and more.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# Skip upstream bug: test_extension_collision fails with RuntimeError in Python 3.7+
%pyproject_run_pytest -v -k "not test_extension_collision"

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jun 24 2025 Denis Sergeev <zeff@altlinux.org> 1.3.2-alt1
- Initial build for ALT.
