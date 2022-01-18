%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define oname typeguard

Name: python3-module-typeguard
Version: 2.13.3
Release: alt1
Summary: Run-time type checker for Python
License: MIT
Group: Development/Python3
Url: https://github.com/agronholm/typeguard

BuildArch: noarch

# https://github.com/agronholm/typeguard.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-setuptools_scm

%description
This library provides run-time type checking for functions
defined with PEP 484 argument (and return) type annotations.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

%python3_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

python3 setup.py test

%files
%doc LICENSE
%doc README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py3*.egg-info

%changelog
* Tue Jan 18 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 2.13.3-alt1
- Initial build for ALT.
