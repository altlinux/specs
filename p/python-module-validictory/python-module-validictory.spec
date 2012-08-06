%define module_name validictory

Name: python-module-%module_name
Version: 0.8.3
Release: alt1
Summary: A general purpose Python data validator.
License: MIT
Group: Development/Python
Url: http://github.com/sunlightlabs/validictory

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python-devel python-module-distribute

%setup_python_module %module_name

%description
A general purpose Python data validator.
Works with Python 2.6+ (Including Python 3)
Schema format based on JSON Schema Proposal (http://json-schema.org)
Contains code derived from jsonschema, by Ian Lewis and Yusuke Muraoka.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc AUTHORS.txt LICENSE.txt README.rst
%python_sitelibdir/%module_name
%python_sitelibdir/%module_name-*.egg-info
%exclude %python_sitelibdir/%module_name/tests

%changelog
* Mon Aug 06 2012 Alexey Shabalin <shaba@altlinux.ru> 0.8.3-alt1
- Initial build for ALT Linux
