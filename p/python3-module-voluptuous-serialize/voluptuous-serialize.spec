Name: python3-module-voluptuous-serialize
Version: 2.3.0
Release: alt1

Summary: Python data validation library
License: BSD
Group: Development/Python
Url: https://pypi.org/project/voluptuous-serialize/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
Voluptuous, despite the name, is a Python data validation library.
It is primarily intended for validating data coming into Python as JSON or YAML.
This package provides Voluptuous schemas to dictionaries converter.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/voluptuous_serialize
%python3_sitelibdir/voluptuous_serialize-%version-*-info

%changelog
* Thu Nov 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.0-alt1
- initial
