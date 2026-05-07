%define pypi_name json-logic
%define mod_name json_logic

Name:    python3-module-%pypi_name
Version: 0.6.3
Release: alt1

Summary: Build complex rules, serialize them as JSON, and execute them in Python

License: MIT
Group:   Development/Python3
Url:     https://github.com/nadirizr/json-logic-py

BuildArch: noarch

# Source-url: https://files.pythonhosted.org/packages/source/j/json-logic/json_logic-%version.tar.gz
Source:  %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
This parser accepts JsonLogic rules and executes them in Python.

JsonLogic is a format for sharing rules (logic) between front-end and
back-end code regardless of language difference, even storing logic
along with a record in a database.

This is a Python port of the json-logic-js JavaScript library.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Thu May 07 2026 Vitaly Lipatov <lav@altlinux.ru> 0.6.3-alt1
- initial build for ALT Sisyphus
