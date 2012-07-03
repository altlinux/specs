# see as TODO: http://packages.debian.org/sid/xrdp
# TODO: move to autotools?
# TODO: write init.d script
# TODO: move executables from /usr/lib, move data files to share
# TODO: send patches to upstream

Name: xrdp
Version: 0.4.2
Release: alt1

Summary: An open source remote desktop protocol (RDP) server

License: GPL
Group: System/Servers
Url: http://xrdp.sourceforge.net/

Packager: Lunar Child <luch@altlinux.org>

# FIXME
%if %_vendor == "alt"
%add_findprov_lib_path %_libdir/%name
%endif

Source: http://prdownloads.sourceforge.net/%name/%name-%version.tar
Source1: %name-init-gen
Source2: %name-init-alt

# manually removed: libnss-mysql 
# Automatically added by buildreq on Mon Aug 27 2007
BuildRequires: libpam-devel libssl-devel

BuildPreReq: rpm-build-intro

Patch0: xrdp_sesman.patch
Patch1: xrdp_sesmantools.patch
Patch2: xrdp_docs.patch
Patch3: xrdp_Makefile.patch

%description
The goal of this project is to provide a fully
functional Linux terminal server, capable of
accepting connections from rdesktop and
Microsoft's own terminal server / remote
desktop clients.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3

%if %_vendor == "alt"
cp %SOURCE2 %name-init
%else
cp %SOURCE1 %name-init
%endif

%__subst "s|/usr/lib|%_libdir|g" %name-init
%__subst "s|DefaultWindowManager=startwm\.sh|DefaultWindowManager=/etc/X11/xdm/Xsession|g" sesman/sesman.ini
%__subst "s|/usr/share/man|%_mandir|g" docs/Makefile

%build
%make_build \
        DESTDIR=%_libdir/xrdp \
        CFGDIR=%_sysconfdir/xrdp \
        MANDIR=%_mandir \
        DOCDIR=%_docdir

%install
# TODO: fix it in make
mkdir -p %buildroot%_sysconfdir/pam.d
mkdir -p %buildroot%_man8dir %buildroot%_man5dir

%make_install install \
        DESTDIR=%buildroot%_libdir/xrdp \
        CFGDIR=%buildroot%_sysconfdir/xrdp \
        MANDIR=%buildroot%_mandir \
        DOCDIR=%buildroot%_docdir

make -C docs installdeb DESTDIRDEB=%buildroot

rm -f %buildroot/%_libdir/xrdp/startwm.sh
rm -f %buildroot/%_libdir/xrdp/xrdp_control.sh
install -D -m755 %name-init %buildroot%_initrddir/%name

%post
%post_service %name
%start_service %name

%preun
%preun_service %name

%files
%config %_sysconfdir/pam.d/sesman
%dir %_sysconfdir/xrdp/
%_initrddir/xrdp
%config %_sysconfdir/xrdp/rsakeys.ini
%config %_sysconfdir/xrdp/sesman.ini
%config %_sysconfdir/xrdp/xrdp.ini
%_libdir/%name/
%_man5dir/*
%_man8dir/*


%changelog
* Thu Aug 18 2011 Denis Baranov <baraka@altlinux.ru> 0.4.2-alt1
- new version (0.4.2) with rpmbs script

* Mon Oct 11 2010 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt2
- fix build, cleanup spec

* Tue Oct 07 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt1
- new version 0.4.1 (with rpmrb script)

* Sun Nov 04 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt4
- provide internal lib
- install generic init script, add ALT init script
- use config mark for ini files

* Mon Sep 24 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt3
- NMU build
- fix source tarball url
- set all destination pathes from spec
- add rpath to fix linking
- use /etc/X11/xdm/Xsession instead sessionwm.sh

* Wed Sep 12 2007 Lunar Child <luch@altlinux.ru> 0.4.0-alt2
- added patch by Nickolay <sn@m2.sta.gov.ua>
- fixing bug this documentation.

* Mon Aug 27 2007 Lunar Child <luch@altlinux.ru> 0.4.0-alt1
- new version

* Wed Jan 17 2007 Lunar Child <luch@altlinux.ru> 0.3.2-alt1
- First Build for ALT Linux Sisyphus
