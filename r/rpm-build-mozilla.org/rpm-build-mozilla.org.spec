# -*- mode: RPM-SPEC; tab-width: 8; fill-column: 70; -*-

%define xulr_name    xulrunner
%define xulr_version 33.0.2
%define xulr_release alt3

Name:	 	rpm-build-mozilla.org
Version:	33.0.2
Release:	alt3
Summary: 	RPM helpers to build Mozilla.org packages
Packager:	Alexey Gladkov <legion@altlinux.ru>

Group:		Development/Other
License:	GPL
BuildArch:	noarch

Source0:	rpm.macros.standalone

%description
These helpers provide possibility to build Mozilla.org packages
by some Alt Linux Team Policy compatible way.

%install
install -D -m644 %SOURCE0 %buildroot/%_sysconfdir/rpm/macros.d/%xulr_name

sed -i \
	-e 's,@xulr_name@,%xulr_name,g' \
	-e 's,@xulr_version@,%xulr_version,g' \
	-e 's,@xulr_release@,%xulr_release,g' \
	\
	%buildroot/%_sysconfdir/rpm/macros.d/%xulr_name

%files
%_sysconfdir/rpm/macros.d/%xulr_name

%changelog
* Mon Feb 15 2016 Alexey Gladkov <legion@altlinux.ru> 33.0.2-alt3
- Remove all utilities.

* Mon Dec 08 2008 Alexey Gladkov <legion@altlinux.ru> 1.1-alt2
- New build.

* Tue Nov 18 2008 Alexey Gladkov <legion@altlinux.ru> 1.1-alt1
- New build for firefox-3.0.4.
- Add applicationini.sh.

* Mon Oct 06 2008 Alexey Gladkov <legion@altlinux.ru> 1.0-alt6
- New build for firefox-3.0.3.

* Mon Sep 08 2008 Alexey Gladkov <legion@altlinux.ru> 1.0-alt5
- New build.

* Fri Jul 18 2008 Alexey Gladkov <legion@altlinux.ru> 1.0-alt4
- New build for firefox-3.0.1.

* Fri Jul 11 2008 Alexey Gladkov <legion@altlinux.ru> 1.0-alt3
- New build.

* Thu Jun 05 2008 Alexey Gladkov <legion@altlinux.ru> 1.0-alt2
- New build for 1.9.0.2pre.

* Fri Jan 25 2008 Alexey Gladkov <legion@altlinux.ru> 1.0-alt1
- first build for ALT linux.
