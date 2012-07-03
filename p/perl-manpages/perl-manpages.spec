Name: perl-manpages
Version: 0.1.1
Release: alt1

Summary: Generate manual pages for all Perl modules and pod files
License: GPL
Group: Development/Perl

Source0: perlman.pl
Source1: perlman.sh

BuildArch: noarch

%description
This package has two scripts:
1) %_sbindir/perlman, capable of generating manual pages for all
perl modules and pod files under "core" and "vendor" directores;
2) %_sysconfdir/cron.daily/perlman, a daily job that will generate/update
manual pages in %_cachedir/perlman/man{1,3} and then will make
symbolic links for them in /usr/local/man/man{1,3}.

%install
install -pD -m755 %SOURCE0 %buildroot%_sbindir/perlman
install -pD -m755 %SOURCE1 %buildroot%_sysconfdir/cron.daily/perlman
mkdir -p %buildroot%_cachedir/perlman/man{1,3}

%files
%_sbindir/perlman
%config %_sysconfdir/cron.daily/perlman

%defattr(644,root,man,2775)
%dir %_cachedir/perlman
%dir %_cachedir/perlman/man1
%dir %_cachedir/perlman/man3

%changelog
* Sun Mar 02 2008 Alexey Tourbin <at@altlinux.ru> 0.1.1-alt1
- set the "release" field of manpage using rpm package URL
  and/or src.rpm package name

* Sun Apr 08 2007 Alexey Tourbin <at@altlinux.ru> 0.1-alt2
- cron.daily/perlman: create destination directory before installing
  symbolic links (#11207, reported by Sergey V Kovalyov)

* Fri Aug 12 2005 Alexey Tourbin <at@altlinux.ru> 0.1-alt1
- initial revision
