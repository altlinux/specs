%define pypi_name json-logic
%define mod_name json_logic
%define upstream_version 0.7.0a0

Name:    python3-module-%pypi_name
Version: 0.7.0
Release: alt0.a0

Summary: Build complex rules, serialize them as JSON, and execute them in Python

License: MIT
Group:   Development/Python3
Url:     https://github.com/nadirizr/json-logic-py

BuildArch: noarch

# Source-url: https://files.pythonhosted.org/packages/7d/05/5b516986c0706b7ae5f4b2155b1c32979479b378b55c0dd9bcc48e70fc5d/json_logic-%{upstream_version}.tar.gz
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
%python3_sitelibdir/%{mod_name}-%{upstream_version}.dist-info

%changelog
* Sat Oct 31 2026 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt0.a0
- new version 0.7.0a0


* Thu May 07 2026 Vitaly Lipatov <lav@altlinux.ru> 0.6.3-alt1
- initial build for ALT Sisyphus
