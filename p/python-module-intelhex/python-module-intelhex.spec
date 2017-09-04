Name: python-module-intelhex
Version: 2.1
Release: alt1

Summary: Python module for manipulating Intel HEX files
License: BSD
Group: Development/Python
Url: https://github.com/bialix/intelhex

Source: %name-%version.tar

BuildRequires: python-module-distribute
BuildArch: noarch

%description
%summary

%prep
%setup

%install
python setup.py install --root %buildroot

%files
%_bindir/*.py
%python_sitelibdir/*

%changelog
* Fri Sep 01 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt1
- initial
