# spec file for package preload (Version 0.2)
#
# Copyright (c) 2008 Stas Myasnikov
# Copyright (c) 2008 Kirill A. Shutemov
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

Name:		preload
Version:	0.2
Release:	alt2
Summary:	Preloads Files into System Cache for Faster Booting
License:	%gpl2plus
#License:	GPLv2+
Group:		System/Configuration/Boot and Init
Source:		%name-%version-%release.tar

# TODO: Preload lists are arch dependent. There is only lists for %ix86.
ExclusiveArch: %ix86

#Packager: Kirill A. Shutemov <kas@altlinux.org>
Packager: Gleb Stiblo <ulfr@altlinux.org>

BuildRequires: rpm-build-licenses
BuildRequires: crontabs service perl-base 

%description
Preload lists files to load into the system cache. This shortens system
boot time if used correctly.

%prep
%setup -q -n %name-%version-%release

%build
gcc $RPM_OPT_FLAGS -DUSE_FADVISE -o preload preload.c
gcc $RPM_OPT_FLAGS -o print-bmap print-bmap.c
gcc $RPM_OPT_FLAGS -o precated precat.c

%install
mkdir -p %buildroot{%_bindir,%_sbindir,%_initdir,%_sysconfdir/cron.daily,%_cachedir/%name}
install -pm755 preload precated %buildroot%_bindir
install -pm755 print-bmap update_preload prepare_preload update_precat %buildroot%_sbindir
install -pm755 init.preload %buildroot/%_initdir/%name
cp -a preload.d %buildroot%_sysconfdir
install -pm755 cron %buildroot/%_sysconfdir/cron.daily/update-preload
cp kde.precat2 %buildroot/%_cachedir/%name/

%post
echo "Generating caches, please wait..."
update_preload >/dev/null 2>&1
update_precat >/dev/null 2>&1
%post_service %name

%preun
%preun_service %name
rm -rf %_cachedir/%name/*.preload

%files
%_bindir/*
%_sbindir/*
%_sysconfdir/cron.daily/update-preload
%_sysconfdir/preload.d
%_initdir/%name
%_cachedir/%name

%changelog
* Thu Jan 31 2008 Gleb Stiblo <ulfr@altlinux.org> 0.2-alt2
- rebuild for Sisyphus

* Thu Jan 24 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.2-alt1
- First build for ALT Linux

* Fri Jan 19 2008 - Stas Myasnikov <myst@velesys.com>
- initial package
