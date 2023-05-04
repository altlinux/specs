Name: python3-module-voluptuous-serialize
Version: 2.6.0
Release: alt1

Summary: Python data validation library
License: BSD
Group: Development/Python
Url: https://pypi.org/project/voluptuous-serialize/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(pytest)
BuildRequires: python3(voluptuous)

%description
Voluptuous, despite the name, is a Python data validation library.
It is primarily intended for validating data coming into Python as JSON or YAML.
This package provides Voluptuous schemas to dictionaries converter.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/voluptuous_serialize
%python3_sitelibdir/voluptuous_serialize-%version.dist-info

%changelog
* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.0-alt1
- 2.6.0 released

* Tue Feb 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.0-alt1
- 2.5.0 released

* Tue Aug 18 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.0-alt1
- 2.4.0 released

* Thu Nov 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.0-alt1
- initial
