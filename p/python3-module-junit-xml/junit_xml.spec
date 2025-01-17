%define _unpackaged_files_terminate_build 1
%define pypi_name junit-xml
%define mod_name junit_xml

%def_with check

Name:    python3-module-%pypi_name
Version: 1.9
Release: alt1

Summary:   Creates JUnit XML test result documents that can be read by tools such as Jenkins
License:   MIT
Group:     Development/Python3
Url:       https://github.com/kyrus/python-junit-xml
Vcs:       https://github.com/kyrus/python-junit-xml.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-six
%endif

%description
A Python module for creating JUnit XML test result documents
that can be read by tools such as Jenkins or Bamboo.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE.* README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Sep 30 2024 Martynenko Evgeniy <enimalojd@altlinux.org> 1.9-alt1
  - Initial build for ALT.
