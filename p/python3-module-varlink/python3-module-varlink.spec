%define pypi_name varlink

Name: python3-module-%pypi_name
Version: 32.1.0
Release: alt1

Summary: Python3 implementation of Varlink
License: Apache-2.0
Group: Development/Python3

URL: https://varlink.org/python/
VCS: https://github.com/varlink/python

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm

%description
An python3 module for Varlink with client and server support.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE.txt README.md
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Mar 10 2026 Valentin Sokolov <sova@altlinux.org> 32.1.0-alt1
- Initial build for Sisyphus.

