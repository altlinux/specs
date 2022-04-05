Name: re2c
Version: 2.2
Release: alt1

Summary: re2c - A tool for generating C-based recognizers from regular expressions

Group: Development/Other
License: Public Domain
Url: http://sourceforge.net/projects/re2c/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/skvadrik/re2c/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake

%description
re2c is a great tool for writing fast and flexible lexers. It has
served many people well for many years and it deserves to be
maintained more actively. re2c is on the order of 2-3 times faster
than a flex based scanner, and its input model is much more
flexible.

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std

%files
%_bindir/re2c
%_bindir/re2go
%_man1dir/re2c.1*
%_man1dir/re2go.1*
%_datadir/%name/
%doc README.md
# re2c/examples

%changelog
* Tue Apr 05 2022 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt1
- new version 2.2 (with rpmrb script)

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- new version 2.1.1 (with rpmrb script)
- switch to cmake build

* Sat Oct 13 2018 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- new version 1.1.1 (with rpmrb script)

* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- new version 1.0.3 (with rpmrb script)

* Sun Oct 08 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- new version 1.0.1 (with rpmrb script)

* Sat Oct 17 2015 Vitaly Lipatov <lav@altlinux.ru> 0.14.3-alt1
- new version (0.14.3) with rpmgs script

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.13.5-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Sep 21 2009 Vitaly Lipatov <lav@altlinux.ru> 0.13.5-alt1
- new version 0.13.5 (with rpmrb script)

* Tue Feb 06 2007 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt0.1
- new version 0.11.0 (with rpmrb script)

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 0.10.6-alt0.1
- initial build for ALT Linux Sisyphus
