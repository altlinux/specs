## define _requires_exceptions perl(controllib.pl)\\|perl(file)

Summary: Package maintenance system for Debian Linux
Name: dpkg
Version: 1.16.3
Release: alt1
License: GPLv2+
Group: System/Configuration/Packaging
Url: http://packages.debian.org/unstable/base/dpkg.html
Source0: ftp://ftp.debian.org/debian/pool/main/d/dpkg/%{name}_%version.tar.bz2
Patch3: gentoo-bug-289094.patch

# Automatically added by buildreq on Mon Dec 13 2010
BuildRequires: dpkg perl-podlators po4a zlib-devel

BuildRequires: perl-Storable perl-TimeDate perl-File-FcntlLock
## BuildRequires: gettext-devel
## Provides: usineagaz = 0.1-0.beta1mdk

%description
This is dpkg, Debian's package maintenance system.

%package -n	perl-Dpkg
Summary: Package maintenance system for Debian Linux
Group: Development/Perl
BuildArch: noarch

%description -n	perl-Dpkg
This module provides dpkg functionalities.

%prep
%setup
%patch3 -p1

%build
%configure \
    --disable-dselect \
    --with-admindir=%_localstatedir/lib/%name

%make

%install
%makeinstall_std

# cleanup
rm -fr %buildroot%_datadir/locale/en/
rm -fr %buildroot%_sysconfdir/alternatives
rm -f %buildroot%_bindir/update-alternatives
rm -f %buildroot%_sbindir/update-alternatives
rm -fr %buildroot/usr/share/doc
mv %buildroot/%_man8dir/start-stop-daemon.8 %buildroot/%_man8dir/dpkg-start-stop-daemon.8

find %buildroot -name "md5sum*" -exec rm -f {} \;
find %buildroot%_mandir -name "update-alternatives*" -exec rm -f {} \;

%find_lang %name
%find_lang dpkg-dev
cat dpkg-dev.lang >> %name.lang

%files -f dpkg.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %_bindir/dpkg*
%dir %_libdir/%name
%dir %_libdir/%name/parsechangelog
%attr(0755,root,root) %dir %_libdir/%name/parsechangelog/debian
%attr(0755,root,root) %_sbindir/*
%dir %_datadir/%name
%dir %_localstatedir/lib/%name
%_datadir/%name/*table
%_datadir/%name/*.mk
%_localstatedir/lib/%name/*
%dir %_sysconfdir/%name
%_man1dir/dpkg*
%_man5dir/*
%_man8dir/*
%lang(pl) %_mandir/pl/man?/*
%lang(de) %_mandir/de/man?/*
%lang(ja) %_mandir/ja/man?/*
%lang(sv) %_mandir/sv/man?/*
%lang(fr) %_mandir/fr/man?/*
%lang(hu) %_mandir/hu/man?/*
%lang(es) %_mandir/es/man?/*
%_includedir/dpkg/*
%_man3dir/*
%_libdir/libdpkg.a
%_libdir/pkgconfig/libdpkg.pc

%files -n perl-Dpkg
%perl_vendorlib/Dpkg
%perl_vendorlib/Dpkg.pm

%changelog
* Thu May 03 2012 Fr. Br. George <george@altlinux.ru> 1.16.3-alt1
- Autobuild version bump to 1.16.3
- Fix build (kick dselect back off)

* Mon Mar 26 2012 Fr. Br. George <george@altlinux.ru> 1.16.2-alt1
- Autobuild version bump to 1.16.2
- Fix dependency
- Tryncate patch (not a bug)

* Tue Jan 10 2012 Fr. Br. George <george@altlinux.ru> 1.16.1.2-alt1
- Autobuild version bump to 1.16.1.2

* Fri Sep 30 2011 Fr. Br. George <george@altlinux.ru> 1.16.1-alt1
- Autobuild version bump to 1.16.1
- Patch adapted
- .mk files added

* Mon Jun 27 2011 Fr. Br. George <george@altlinux.ru> 1.16.0.3-alt1
- Autobuild version bump to 1.16.0.3

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.16.0.2-alt1
- Autobuild version bump to 1.16.0.2

* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 1.16.0.1-alt1
- Autobuild version bump to 1.16.0.1
- Remove applied patch

* Mon Jan 31 2011 Fr. Br. George <george@altlinux.ru> 1.15.8.10-alt1
- Autobuild version bump to 1.15.8.10

* Fri Jan 14 2011 Fr. Br. George <george@altlinux.ru> 1.15.8.8-alt1
- Autobuild version bump to 1.15.8.8

* Fri Dec 24 2010 Fr. Br. George <george@altlinux.ru> 1.15.8.7-alt1
- Autobuild version bump to 1.15.8.7

* Mon Dec 13 2010 Fr. Br. George <george@altlinux.ru> 1.15.8.4-alt1
- Renewal build from MDV
- Some fixes

* Wed Dec 12 2007 Vitaly Lipatov <lav@altlinux.ru> 1.14.7-alt2
- add missed perl module Dpkg

* Sat Dec 08 2007 Vitaly Lipatov <lav@altlinux.ru> 1.14.7-alt1
- new version 1.14.7 (with rpmrb script)

* Thu Sep 07 2006 Vitaly Lipatov <lav@altlinux.ru> 1.13.22-alt0.1
- new version (1.13.22)
- fix group, fix description (bug #8266)

* Mon Feb 13 2006 Vitaly Lipatov <lav@altlinux.ru> 1.13.14-alt0.1
- new version

* Wed Dec 21 2005 Vitaly Lipatov <lav@altlinux.ru> 1.13.11-alt0.1
- new version

* Thu May 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.6.15-alt6
- do not build utils (md5sum, start-stop-daemon).
- use find-lang --with-man.

* Wed May 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.6.15-alt5
- fixed dependencies.

* Mon May 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.6.15-alt4
- exclude {%%_sbindir,%%_man8dir}/*start-stop-daemon*

* Tue Oct 15 2002 Stanislav Ievlev <inger@altlinux.ru> 1.6.15-alt3
- exclude manpages provided by other packages

* Mon Oct 14 2002 Stanislav Ievlev <inger@altlinux.ru> 1.6.15-alt2
- rebuild with gcc3
- comment locale man pages: must be in man-pages-locale package (ALT Packaging Policy).
- little spec improvements

* Tue Nov 13 2001 Yuri N. Sedunov <aris@altlinux.ru> 1.4.8-alt1
- First build for Sisyphus. Thanks PLD Team for specfile.
