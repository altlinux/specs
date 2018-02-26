Name: python-module-xpresser
Version: 1.0
Release: alt1.1

Summary: Python library to script Graphic User Interfaces
Group: Development/Python
License: LGPLv3
URL: https://launchpad.net/xpresser
BuildArch: noarch

%define mname xpresser

%setup_python_module %mname

Source: %name-%version.tar

%description
Xpresser is a Python module which enables trivial automation of
Graphic User Interfaces (GUIs) via image matching algorithms.

%prep
%setup -n %name-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir_noarch/*
%doc README

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.1
- Rebuild with Python-2.7

* Wed Jul 13 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0-alt1
- initial build for Sisyphus


