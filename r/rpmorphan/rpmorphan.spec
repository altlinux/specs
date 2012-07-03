Name: rpmorphan
Version: 1.8
Release: alt2.1

Summary: Find orphaned RPM packages

Group: System/Configuration/Packaging
License: GPL
Url: http://rpmorphan.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/rpmorphan/%version/%name-%version.tar

BuildArch: noarch

BuildRequires: perl-Pod-Parser

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
%_bindir/rpmorphan*
%_bindir/rpmorphan-lib.pl
%_bindir/rpmusage*
%_bindir/rpmdep*
%_bindir/rpmduplicates*
%_man1dir/rpmorphan.1*
%_man1dir/rpmusage.1*
%_man1dir/rpmdep.1*
%_man1dir/rpmduplicates.1*
%_logrotatedir/%name
%_prefix/lib/%name/
%dir %_var/lib/rpmorphan/
%_var/lib/rpmorphan/keep

%changelog
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

