# -*- mode: RPM-SPEC; tab-width: 8; fill-column: 70; -*-

%define sunbird_name    sunbird
%define sunbird_version 0.9.0
%define sunbird_release alt2

Name:		rpm-build-sunbird
Version:	%sunbird_version
Release:	%sunbird_release
Summary:	RPM helper macros to rebuild sunbird packages
Packager:	Alexey Gladkov <legion@altlinux.ru>

Group:		Development/Other
License:	GPL
BuildArch:	noarch

Requires:       rpm-build-mozilla.org

Source0:	rpm.macros.sunbird.standalone
Source1:	sunbird.req
Source2:	sunbird.req.files

%description
These helper macros provide possibility to rebuild
sunbird packages by some Alt Linux Team Policy compatible way.

%install
%__mkdir_p \
	%buildroot/%_sysconfdir/rpm/macros.d \
	%buildroot/%_rpmlibdir

%__cp %SOURCE0 %buildroot/%_sysconfdir/rpm/macros.d/%sunbird_name
%__cp %SOURCE1 %SOURCE2 %buildroot/%_rpmlibdir/
chmod 755 %buildroot/%_rpmlibdir/*

%__subst 's,@sunbird_name@,%sunbird_name,'       %buildroot/%_sysconfdir/rpm/macros.d/%sunbird_name
%__subst 's,@sunbird_version@,%sunbird_version,' %buildroot/%_sysconfdir/rpm/macros.d/%sunbird_name
%__subst 's,@sunbird_release@,%sunbird_release,' %buildroot/%_sysconfdir/rpm/macros.d/%sunbird_name

%files
%_rpmlibdir/*
%_sysconfdir/rpm/macros.d/%sunbird_name

%changelog
* Fri Sep 26 2008 Alexey Gladkov <legion@altlinux.ru> 0.9.0-alt2
- New version.

* Tue Sep 09 2008 Alexey Gladkov <legion@altlinux.ru> 0.9.0-alt1.20080909
- New version.

* Tue Oct 23 2007 Alexey Gladkov <legion@altlinux.ru> 0.7.0-alt2
- first build for ALT linux.
