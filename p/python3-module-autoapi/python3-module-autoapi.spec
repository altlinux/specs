%define pypi_name autoapi

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.1
Release: alt1

Summary: Automatic Python API reference documetation generator for Sphinx
License: Apache-2.0
Group: Development/Python3
URL: https://github.com/carlos-jenkins/autoapi

Packager: Ulysses Apokin <ulysses@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-sphinx

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-jinja2
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
Automatic Python API reference documentation generator for Sphinx,
inspired by Doxygen.

AutoAPI is a Sphinx extension that allows to automatically generate API
reference documentation for Python packages, recursively, without any
intervention from the developer. It will discover all the package modules
and their public objects and document them.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE doc/
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Mon Dec 02 2024 Ulysses Apokin <ulysses@altlinux.org> 2.0.1-alt1
- Initial build for Sisyphus.
