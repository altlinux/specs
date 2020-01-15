%define oname tracing

Name: python3-module-%oname
Version: 0.9
Release: alt2

Summary: Python debug logging helper
License: GPLv3+
Group: Development/Python3
Url: http://liw.fi/%oname/
BuildArch: noarch

Source: %name-%version.tar
Source44: import.info

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx


%description
The Python library tracing helps with logging debug messages. It
provides a couple of functions for logging debug messages, and allows
the user to enable or disable logging for particular code modules.

It is sometimes practical to add a lot of debugging log messages to a
program, but having them enabled all the time results in very large
log files. Also, logging that much takes quite a bit of time.

This module provides a way to turn such debugging or tracing messages
on and off, based on the filename they occur in. The logging can that
be left in the code, and only enabled when it is needed.

%package docs
Group: Other
Summary: Documentation for %oname

%description docs
This package contains the documentation for %oname a Python debug
logging helper.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' doc/Makefile

%build
%python3_build

# Build documentation
make -C doc html

%install
%python3_install

%files
%doc COPYING NEWS README
%python3_sitelibdir_noarch/*

%files docs
%doc doc/_build/html/* example.py


%changelog
* Wed Jan 15 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.9-alt2
- porting on python3

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- new version 0.9 (with rpmrb script)

* Thu Aug 13 2015 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt3
- human build for ALT Linux Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_2
- update to new release by fcimport

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_1
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_3
- update to new release by fcimport

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_2
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_4
- update to new release by fcimport

* Sun Dec 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_3
- initial fc import

