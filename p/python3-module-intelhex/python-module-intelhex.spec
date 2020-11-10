%define oname intelhex

Name: python3-module-%oname
Version: 2.3.0
Release: alt1

Summary: Python module for manipulating Intel HEX files
License: BSD
Group: Development/Python3
Url: https://github.com/bialix/intelhex
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): python3-module-setuptools

Conflicts: python-module-%oname <= %EVR
Obsoletes: python-module-%oname <= %EVR

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
* Tue Nov 10 2020 Grigory Ustinov <grenka@altlinux.org> 2.3.0-alt1
- Build new version.

* Tue Oct 06 2020 Grigory Ustinov <grenka@altlinux.org> 2.2.1-alt3
- Fix port on python3 (Closes: #39039).

* Thu Jan 09 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.2.1-alt2
- porting on python3

* Tue Dec 03 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.1-alt1
- 2.2.1 released

* Fri Sep 01 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt1
- initial
