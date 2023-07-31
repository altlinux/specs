## define _requires_exceptions perl(controllib.pl)\\|perl(file)
%def_without extbuild

Name: dpkg
Version: 1.21.22
Release: alt2

Summary: Package maintenance system for Debian Linux

License: GPLv2+
Group: System/Configuration/Packaging
Url: http://packages.debian.org/unstable/base/dpkg

Source0: http://ftp.debian.org/debian/pool/main/d/dpkg/%{name}_%version.tar.xz
Patch: dpkg-ALT-e2k-cputable.patch

# boostrap notes:
# 1) build dep loop via perl-Dpkg (just add noarch package);
# 2) dpkg stub is really needed (for abitable, cputable, ostable,
#    triplettable and --print-architecture); DIY or ask mike@

%{?!_with_bootstrap:BuildRequires: po4a}

BuildRequires: perl-podlators perl-Storable perl-TimeDate perl-File-FcntlLock perl-parent perl-Time-Piece

BuildRequires: zlib-devel liblzma-devel libmd-devel libzstd-devel

Requires: perl-Digest-SHA

%description
This is dpkg, Debian's package maintenance system.

%package -n perl-Dpkg
Summary: Package maintenance system for Debian Linux
Group: Development/Perl
BuildArch: noarch

%description -n perl-Dpkg
This module provides dpkg functionalities.

%set_perl_req_method relaxed
%prep
%setup
%patch -p2

%build
%autoreconf
%configure \
    --disable-update-alternatives \
    --disable-start-stop-daemon \
    --disable-dselect \
    --with-admindir=/var/lib/%name \
    --with-logdir=/var/lib/%name/log

%make

%install
%makeinstall_std

rm -f %buildroot%_man7dir/deb-version.*

# cleanup
%if_without extbuild
rm -rf %buildroot%_mandir/??/
rm -rf %buildroot%_includedir/dpkg/*
rm -rf %buildroot%_libdir/libdpkg.a
rm -rf %buildroot/usr/share/aclocal/
rm -rf %buildroot%_libdir/pkgconfig/libdpkg.pc
%endif

# remove unpacked files
rm -v %buildroot/usr/lib/dpkg/dpkg-db-backup
rm -v %buildroot/usr/sbin/dpkg-fsys-usrunmess
rm -rf %buildroot/usr/share/doc/dpkg/
#rm -v %buildroot%_man8dir/dpkg-fsys-usrunmess.8.*
rm -v %buildroot/usr/share/zsh/vendor-completions/_dpkg-parsechangelog


%find_lang %name
%find_lang dpkg-dev
cat dpkg-dev.lang >> %name.lang

%files -f dpkg.lang
%attr(0755,root,root) %_bindir/dpkg*
%dir %_datadir/%name
%_datadir/%name/*table
%_datadir/%name/*.mk
%_datadir/%name/*.specs
%dir %_datadir/%name/sh
%_datadir/%name/sh/dpkg-error.sh
%dir /var/lib/%name/
/var/lib/%name/*
%dir %_sysconfdir/%name
%_man1dir/dpkg*
%_man5dir/*
%_man8dir/*
%if_with extbuild
%lang(pl) %_mandir/pl/man?/*
%lang(de) %_mandir/de/man?/*
%lang(ja) %_mandir/ja/man?/*
%lang(sv) %_mandir/sv/man?/*
%lang(fr) %_mandir/fr/man?/*
%lang(hu) %_mandir/hu/man?/*
%lang(es) %_mandir/es/man?/*
%lang(it) %_mandir/it/man?/*
%_includedir/dpkg/*
/usr/share/aclocal/*
%_libdir/libdpkg.a
%_libdir/pkgconfig/libdpkg.pc
%endif

%files -n perl-Dpkg
%_man3dir/*
%perl_vendorlib/Dpkg/
%perl_vendorlib/Dpkg.pm

%changelog
* Tue Aug 01 2023 Vitaly Lipatov <lav@altlinux.ru> 1.21.22-alt2
- add Requires: perl-Digest-SHA (ALT bug 46636)

* Sat Jul 29 2023 Vitaly Lipatov <lav@altlinux.ru> 1.21.22-alt1
- new version 1.21.22 (with rpmrb script)

* Fri Apr 28 2023 Vitaly Lipatov <lav@altlinux.ru> 1.21.21-alt1
- new version 1.21.21 (with rpmrb script)
- add BR: liblzma-devel libmd-devel libzstd-devel

* Sat Aug 27 2022 Vitaly Lipatov <lav@altlinux.ru> 1.21.9-alt1
- new version 1.21.9 (with rpmrb script)
- remove unpacked files

* Wed Jun 15 2022 Fr. Br. George <george@altlinux.org> 1.21.8-alt1
- Autobuild version bump to 1.21.8

* Sat Oct 26 2019 Fr. Br. George <george@altlinux.ru> 1.19.7-alt1
- Autobuild version bump to 1.19.7

* Tue May 14 2019 Vitaly Lipatov <lav@altlinux.ru> 1.19.6-alt1
- new version 1.19.6 (with rpmrb script)

* Mon May 06 2019 Vitaly Lipatov <lav@altlinux.ru> 1.19.5-alt1
- new version 1.19.5 (with rpmrb script) (ALT bug 36230)

* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 1.19.0.5-alt1
- Autobuild version bump to 1.19.0.5
- Pick e2k hack into a patch

* Fri Nov 03 2017 Michael Shigorin <mike@altlinux.org> 1.18.7-alt2
- BOOTSTRAP: avoid BR: po4a; add notes
- E2K: add e2k to cputable

* Thu Jun 30 2016 Vitaly Lipatov <lav@altlinux.ru> 1.18.7-alt1
- new version 1.18.7 (with rpmrb script)
- cleanup spec
- drop start-stop-daemon (ALT bug #32238)

* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 1.18.1-alt1
- Autobuild version bump to 1.18.1

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 1.17.25-alt1
- Autobuild version bump to 1.17.25

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 1.17.23-alt1
- Autobuild version bump to 1.17.23

* Wed Oct 22 2014 Fr. Br. George <george@altlinux.ru> 1.17.19-alt1
- Autobuild version bump to 1.17.19

* Sat Sep 27 2014 Fr. Br. George <george@altlinux.ru> 1.17.13-alt1
- Autobuild version bump to 1.17.13

* Tue Aug 19 2014 Fr. Br. George <george@altlinux.ru> 1.17.12-alt1
- Autobuild version bump to 1.17.12

* Mon Jun 09 2014 Fr. Br. George <george@altlinux.ru> 1.17.10-alt1
- Autobuild version bump to 1.17.10

* Mon May 12 2014 Fr. Br. George <george@altlinux.ru> 1.17.9-alt1
- Autobuild version bump to 1.17.9

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 1.17.6-alt1
- Autobuild version bump to 1.17.6

* Sun Jan 12 2014 Fr. Br. George <george@altlinux.ru> 1.17.5-alt1
- Autobuild version bump to 1.17.5

* Wed Aug 21 2013 Fr. Br. George <george@altlinux.ru> 1.17.1-alt1
- Autobuild version bump to 1.17.1
- Use .xz instead of .bz2 archive

* Sat Aug 03 2013 Vitaly Lipatov <lav@altlinux.ru> 1.16.10-alt1
- new version 1.16.10 (with rpmrb script)

* Tue Jul 24 2012 Fr. Br. George <george@altlinux.ru> 1.16.4.3-alt1
- Autobuild version bump to 1.16.4.3
- Remove inactual patch

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
