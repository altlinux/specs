Name: rpmorphan
Version: 1.16
Release: alt1

Summary: Find orphaned RPM packages

Group: System/Configuration/Packaging
License: GPL
Url: http://rpmorphan.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/rpmorphan/%version/%name-%version.tar

BuildArch: noarch

# manually removed: python-module-google python-module-mwlib python3-dev python3-module-yieldfrom python3-module-zope ruby ruby-stdlibs
# Automatically added by buildreq on Mon Aug 01 2016 (-bi)
# optimized out: fontconfig perl perl-Curses perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-TermReadKey perl-Tk perl-podlators python-base python-modules python3 python3-base rpm-build-python3 xz
BuildRequires: perl-Curses-UI perl-Pod-Usage perl-Tk-MListbox

BuildRequires: perl-Pod-Parser perl-Curses-UI

Requires: perl-podlators

%description
rpmorphan  finds  "orphaned"  packages  on  your system. It determines
which packages have no other packages depending on their installation,
and shows you a list of these packages.
It intends to be clone of deborphan debian tools for rpm packages.

It will try to help you to remove unused packages, for exemple :
- after a distribution upgrade
- when you want to suppress packages after some tests

several tools are also provided :
- rpmusage : display rpm packages last use date
- rpmdep   : display the full dependency of an installed rpm package
- rpmduplicates : find programs with several version installed

%prep
%setup
# fix bug #23750 (yearly is supported since logrotate 3.7.7)
%__subst "s|yearly|monthly|g" rpmorphan.logrotate

%install
%makeinstall_std
rm -f %buildroot%_logdir/*

%files
%doc Authors Changelog COPYING NEWS Readme rpmorphan.lsm Todo
%_sysconfdir/rpmorphanrc
%_bindir/rpmorphan*
%_bindir/grpmorphan
%_bindir/rpmusage*
%_bindir/rpmextra*
%_bindir/rpmdep*
%_bindir/rpmduplicates*
%_man1dir/rpmorphan.1*
%_man1dir/rpmusage.1*
%_man1dir/rpmextra.1*
%_man1dir/rpmdep.1*
%_man1dir/rpmduplicates.1*
%_logrotatedir/%name
%_prefix/lib/%name/
%dir %_var/lib/rpmorphan/
%_var/lib/rpmorphan/keep

%changelog
* Thu Jul 28 2016 Vitaly Lipatov <lav@altlinux.ru> 1.16-alt1
- new version 1.16 (with rpmrb script)

* Sat Oct 17 2015 Vitaly Lipatov <lav@altlinux.ru> 1.15-alt1
- new version 1.15 (with rpmrb script)

* Tue Aug 27 2013 Vitaly Lipatov <lav@altlinux.ru> 1.12-alt1
- new version 1.12 (with rpmrb script)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 1.11-alt1
- new version 1.11 (with rpmrb script)

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.8-alt2.1
- rebuilt with perl 5.12

* Wed Jul 14 2010 Vitaly Lipatov <lav@altlinux.ru> 1.8-alt2
- pack locale (ALT bug #23764)

* Tue Jul 13 2010 Vitaly Lipatov <lav@altlinux.ru> 1.8-alt1
- new version 1.8 (with rpmrb script)
- remove yearly command from logrotate config (ALT bug #23750)

* Thu Jan 14 2010 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt1
- new version 1.5 (with rpmrb script)

* Thu Dec 11 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- new version 1.3 (with rpmrb script)

* Wed Jul 16 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- initial build for ALT Linux Sisyphus

* Sat Jan 19 2008 David Walluck <walluck@mandriva.org> 1.1-1mdv2008.1
+ Revision: 155106
- 1.1

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 16 2007 David Walluck <walluck@mandriva.org> 0:1.0-2mdv2008.0
+ Revision: 64097
- remove duplicate docs
- reflect name that we install as
- Requires: perl-Tk

* Sat Apr 28 2007 David Walluck <walluck@mandriva.org> 0:1.0-1mdv2008.0
+ Revision: 18912
- 1.0

* Wed Apr 04 2007 David Walluck <walluck@mandriva.org> 0.9-1mdv2007.1
+ Revision: 150461
- 0.9

* Thu Mar 08 2007 David Walluck <walluck@mandriva.org> 0:0.8-1mdv2007.1
+ Revision: 138535
- 0.8

* Wed Feb 28 2007 Lenny Cartier <lenny@mandriva.com> 0:0.4-1mdv2007.1
+ Revision: 127181
- Update to 0.4

* Mon Feb 05 2007 David Walluck <walluck@mandriva.org> 0:0.3-1mdv2007.1
+ Revision: 116398
- 0.3

* Wed Jan 24 2007 David Walluck <walluck@mandriva.org> 0:0.1-1mdv2007.1
+ Revision: 113033
- Import rpmorphan

* Wed Jan 24 2007 David Walluck <walluck@mandriva.org> 0:0.1-1mdv2007.1
- release

