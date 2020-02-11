%define oldname python-ttystatus
%global pkgname ttystatus

Name: python3-module-ttystatus
Version: 0.34
Release: alt2

Summary: Progress and status updates on terminals for Python
License: GPLv3+
Group: Development/Python3
Url: http://liw.fi/%pkgname/
Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Source: http://code.liw.fi/debian/pool/main/p/%oldname/%{oldname}_%version.orig.tar.gz
Source44: import.info
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-modules-curses
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-alabaster


%description
ttystatus is a Python library for showing progress reporting and
status updates on terminals, for (Unix) command line programs. Output
is automatically adapted to the width of the terminal: truncated if it
does not fit, and re-sized if the terminal size changes.

Output is provided via widgets. Each widgets formats some data into a
suitable form for output. It gets the data either via its initializer,
or from key/value pairs maintained by the master object. The values
are set by the user. Every time a value is updated, widgets get
updated (although the terminal is only updated every so often to give
user time to actually read the output).

%package doc
Group: Other
Summary: Documentation for %pkgname

%description doc
This package contains the documentation for %pkgname, a Python
library providing progress and status updates on terminals.

%prep
%setup -n %pkgname-%version
%patch0 -p2

sed -i 's|sphinx-build|sphinx-build-3|' doc/Makefile

%build
%python3_build

# Build documentation
%make

%install
%python3_install

%check
exit 0
# CoverageTestRunner trips up on build directory;
# since we've already done the install phase, remove it first
rm -rf build
%make check

%files
%doc COPYING NEWS README
%python3_sitelibdir_noarch/*

%files doc
%doc doc/_build/html/*


%changelog
* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.34-alt2
- Porting to python3.

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 0.34-alt1
- new version 0.34 (with rpmrb script)

* Sat Apr 23 2016 Vitaly Lipatov <lav@altlinux.ru> 0.32-alt1
- new version 0.32 (with rpmrb script)

* Sun Jan 03 2016 Vitaly Lipatov <lav@altlinux.ru> 0.26-alt1
- new version 0.26 (with rpmrb script)

* Thu Aug 13 2015 Vitaly Lipatov <lav@altlinux.ru> 0.23-alt4
- human build for ALT Linux Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_3
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_2
- update to new release by fcimport

* Fri Jul 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_1
- update to new release by fcimport

* Thu Mar 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_1
- update to new release by fcimport

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_1
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_2
- update to new release by fcimport

* Sun Dec 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_1
- initial fc import

