%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define oname executing

Name: python3-module-executing
Version: 0.8.2
Release: alt1
Summary: Get information about what a Python frame is currently doing, particularly the AST node being executed
License: MIT
Group: Development/Python3
Url: https://github.com/alexmojaki/executing

BuildArch: noarch

# https://github.com/alexmojaki/executing.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
# test dependencies
BuildRequires: python3(asttokens)

%description
This mini-package lets you get information about
what a frame is currently doing, particularly the AST node being executed.

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
%doc LICENSE.txt
%doc README.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py3*.egg-info

%changelog
* Tue Jan 18 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.2-alt1
- Initial build for ALT.
