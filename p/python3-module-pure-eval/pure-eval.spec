%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define oname pure_eval

%def_with check

Name: python3-module-pure-eval
Version: 0.2.2
Release: alt1
Summary: Safely evaluate AST nodes without side effects
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/pure-eval
VCS: https://github.com/alexmojaki/pure_eval

BuildArch: noarch

# https://github.com/alexmojaki/pure_eval.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3(pytest)
%endif

%description
This is a Python package that lets you safely evaluate certain AST nodes
without triggering arbitrary code that may have unwanted side effects.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE.txt README.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Sun May 19 2024 Grigory Ustinov <grenka@altlinux.org> 0.2.2-alt1
- Automatically updated to 0.2.2.

* Tue Jan 18 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.1-alt1
- Initial build for ALT.
