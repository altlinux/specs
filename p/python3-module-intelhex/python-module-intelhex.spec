%define oname intelhex

Name: python3-module-%oname
Version: 2.2.1
Release: alt2

Summary: Python module for manipulating Intel HEX files
License: BSD
Group: Development/Python3
Url: https://github.com/bialix/intelhex
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): python3-module-setuptools


%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%_bindir/*.py
%python3_sitelibdir/*


%changelog
* Thu Jan 09 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.2.1-alt2
- porting on python3

* Tue Dec 03 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.1-alt1
- 2.2.1 released

* Fri Sep 01 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt1
- initial
