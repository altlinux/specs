%define module_name pycall

Name: python-module-%module_name
Version: 2.0
Release: alt1.1

Summary: flexible python library for creating and using Asterisk call files
License: Public Domain
Group: Development/Python
Url: http://pycall.org/

Source: python-module-%module_name-%version.tar

BuildArch: noarch

BuildRequires: python-module-setuptools

%setup_python_module %module_name

%description
%summary

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc AUTHORS README CHANGES UNLICENSE
%python_sitelibdir/pycall
%python_sitelibdir/*.egg-info


%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt1.1
- Rebuild with Python-2.7

* Tue Jun 07 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.0-alt1
- Initial build for Sisyphus.
