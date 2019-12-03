Name: python-module-intelhex
Version: 2.2.1
Release: alt1

Summary: Python module for manipulating Intel HEX files
License: BSD
Group: Development/Python
Url: https://github.com/bialix/intelhex

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python-module-setuptools

%description
%summary

%prep
%setup

%build
%python_build

%install
%python_install

%files
%_bindir/*.py
%python_sitelibdir/*

%changelog
* Tue Dec 03 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.1-alt1
- 2.2.1 released

* Fri Sep 01 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt1
- initial
