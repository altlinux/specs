%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define oname pure_eval

Name: python3-module-pure-eval
Version: 0.2.1
Release: alt1
Summary: Safely evaluate AST nodes without side effects
License: MIT
Group: Development/Python3
Url: https://github.com/alexmojaki/pure_eval

BuildArch: noarch

# https://github.com/alexmojaki/pure_eval.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-setuptools_scm python3(wheel)
# test dependencies
BuildRequires: python3(pytest)

%description
This is a Python package that lets you safely evaluate certain AST nodes
without triggering arbitrary code that may have unwanted side effects.

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
* Tue Jan 18 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.1-alt1
- Initial build for ALT.
