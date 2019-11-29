Name: python3-module-voluptuous
Version: 0.11.7
Release: alt1

Summary: Voluptuous is a Python data validation library
License: BSD
Group: Development/Python
Url:  http://github.com/alecthomas/voluptuous

Source: %name-%version.tar
BuildArch: noarch

BuildRequires: rpm-build-python3 python3-module-setuptools

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
%python3_build

%install
%python3_install

%files
%doc COPYING README.md
%python3_sitelibdir/*

%changelog
* Fri Nov 29 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.7-alt1
- 0.11.7 released

* Tue Aug 01 2017 Mikhail Gordeev <obirvalger@altlinux.org> 0.10.5-alt1
- new version 0.10.5

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 0.8.11-alt1
- Initial build for Sisyphus
