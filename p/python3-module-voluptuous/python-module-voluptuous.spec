Name: python3-module-voluptuous
Version: 0.15.2
Release: alt1

Summary: Voluptuous is a Python data validation library
License: BSD-3-Clause
Group: Development/Python
Url:  http://github.com/alecthomas/voluptuous

Source: %name-%version.tar
BuildArch: noarch

BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(pytest)

%description
Voluptuous, *despite* the name, is a Python data validation library. It
is primarily intended for validating data coming into Python as JSON,
YAML, etc.

It has three goals:

1. Simplicity.
2. Support for complex data structures.
3. Provide useful error messages.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest voluptuous/tests

%files
%doc COPYING README.md
%python3_sitelibdir/voluptuous
%python3_sitelibdir/voluptuous-%version.dist-info

%changelog
* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.15.2-alt1
- 0.15.2 released

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.1-alt1
- 0.13.1 released

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.2-alt1
- 0.12.2 released

* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.1-alt1
- 0.12.1 released

* Fri Oct 16 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.0-alt1
- 0.12.0 released

* Fri Nov 29 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.7-alt1
- 0.11.7 released

* Tue Aug 01 2017 Mikhail Gordeev <obirvalger@altlinux.org> 0.10.5-alt1
- new version 0.10.5

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 0.8.11-alt1
- Initial build for Sisyphus
