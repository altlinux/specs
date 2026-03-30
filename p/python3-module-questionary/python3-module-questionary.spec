%define _unpackaged_files_terminate_build 1
%define pypi_name questionary

%def_with check

Name: python3-module-%pypi_name
Version: 2.1.1
Release: alt1.1

Summary: Python library to build pretty command line user prompts
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/questionary
Vcs: https://github.com/tmbo/questionary

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core

%if_with check
BuildRequires: python3-module-mypy
BuildRequires: python3-module-pre-commit
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-toml

BuildRequires: python3-module-prompt-toolkit
%endif

%description
Questionary is a Python library for effortlessly building pretty
command line interfaces.

It's easy to use and yet powerful:
- Build beautiful prompts with a simple Python API
- Customize every detail of your prompts
- Create complex workflows with conditional questions
- Full Unicode support including emojis

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v -k 'not test_print_with_style'

%files
%doc README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.1.1-alt1.1
- Demodernized packaging.

* Tue Sep 02 2025 Denis Sergeev <zeff@altlinux.org> 2.1.1-alt1
- 2.1.0 -> 2.1.1.

* Tue Jun 24 2025 Denis Sergeev <zeff@altlinux.org> 2.1.0-alt1
- Initial build for ALT.
