Name: osec
Version: 1.2.4
Release: alt2

Summary: Lightweight file permission checker
License: GPL3
Group: System/Base
Url: https://sourceforge.net/projects/o-security/
Packager: Alexey Gladkov <legion@altlinux.ru>

Source: osec-%version.tar

PreReq: shadow-utils

Provides: mtree-sec = %version-%release
Obsoletes: mtree-sec

%define osec_statedir /var/lib/osec
%define osec_group osec
%define osec_user osec

# Automatically added by buildreq on Sat Apr 21 2007 (-bi)
BuildRequires: help2man libcdb-devel libcap-devel perl-RPM

%package cronjob
Summary: General cron framework for osec
Requires: %name = %version-%release
Requires: %name-reporter
Group: System/Base

%package mailreport
Summary: Collection of reporters for osec
Group: System/Base
Provides: %name-reporter
Requires: %name = %version-%release
Requires: %name-cronjob
Requires: /bin/mail
Requires: perl-base
PreReq: coreutils

%description
This package contains osec program which performs files integrity check
by traversing filesystem and making human readable reports about changes
and found files/directories with suspicious ownership or permissions.

%description cronjob
This package contains a general framework for osec pipelines.

%description mailreport
This package contains a set of reporters to use with osec:
osec_reporter - creates human readable reports;
osec_mailer - send mail only if some changes was detected;
osec_rpm_reporter - additional filter for osec_reporter,
add name of rpm packages for files in report.

%prep
%setup -q

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

cd %buildroot
#cron job file
mkdir -p -- etc/cron.daily
mv -- .%_datadir/osec.cron etc/cron.daily/osec
chmod 700 -- etc/cron.daily/osec

#configs
mkdir -pm700 -- etc/osec
mv -- etc/dirs.conf .%_datadir/pipe.conf etc/osec/
chmod 600 -- etc/osec/*.conf

#install directory for the databases
mkdir -p -- .%osec_statedir

%pre
/usr/sbin/groupadd -r -f %osec_group
/usr/sbin/useradd -r -g %osec_group -d /dev/null -s /dev/null -n %osec_user >/dev/null 2>&1 ||:

%triggerpostun -- %name < 0:1.0.0-alt1
rm -f %osec_statedir/osec.db.*

%files
%doc ChangeLog NEWS README src/restore data/osec-recheck
%_bindir/osec
%_bindir/osec2txt
%_bindir/txt2osec
%_bindir/osec-migrade-db
%_man1dir/*

%files cronjob
%config(noreplace) /etc/cron.daily/osec
%defattr(600,root,root,700)
%config(noreplace) /etc/osec

%files mailreport
%_bindir/osec_mailer
%_bindir/osec_reporter
%_bindir/osec_rpm_reporter
%attr(770,root,%osec_group) %osec_statedir

%changelog
* Wed Oct 14 2009 Alexey Gladkov <legion@altlinux.ru> 1.2.4-alt2
- osec.cron: Add number of added, deleted and changed files;
- osec.cron, osec_mailer: Add IGNORE_NO_CHANGES option.

* Fri Oct 02 2009 Alexey Gladkov <legion@altlinux.ru> 1.2.4-alt1
- New version (1.2.4);
- Use fts(3) to traverse a file hierarchy;
- Add osec2txt and txt2osec utilities;
- Add simple restore utility;
- Add osec-recheck;
- Add time of last modification to report;
- osec.cron: Add allow customize ionice arguments;
- osec_mailer: Add number of added, deleted and changed files to a mail report.

* Thu Jul 30 2009 Alexey Gladkov <legion@altlinux.ru> 1.2.3-alt1
- New version (1.2.3);
- Add --ignore option;
- osec.cron: Add nice support.

* Thu Oct 30 2008 Alexey Gladkov <legion@altlinux.org> 1.2.2-alt1
- New version (1.2.2);
- Dont ignore cdb_seqnext() errors.
- Add --exclude and --exclude-from options.
- Fix for gcc-4.3.

* Thu Sep 18 2008 Alexey Gladkov <legion@altlinux.ru> 1.2.1-alt1
- New version (1.2.1);
- Create temprary database in subdirectory (ALT#9612);
- Add syslog messages in osec.cron (ALT#7099);
- Add ionice support in osec.cron;
- Small code optimization.

* Thu Jun 05 2008 Alexey Gladkov <legion@altlinux.ru> 1.2.0-alt1
- New version (1.2.0);
- Almost completely rewritten from scratch in C;
- Reduce requires (do not use openssl, libcdbxx);
- Change database format;
- Change checksum algorithm from MD5 to SHA1;
- Add osec database versioning;
- pipe.conf: Show hostname in mail subject;
- Improvements in osec:
  + track inode changes;
  + track symlink changes;

* Mon Apr 23 2007 Stanislav Ievlev <inger@altlinux.org> 1.1.0-alt1
- use std::tr1 instead of boost

* Sat Apr 21 2007 Dmitry V. Levin <ldv@altlinux.org> 1.0.2-alt2
- Added /bin/mail to -mailreport subpackage requirements (#6137).
- Added osec to -mailreport subpackage requirements (#11589).
- Updated package description (#7098).
- Removed -mailreport %%post script.
- Made /var/lib/osec directory owned by root.
- Updated build dependencies.
- Cleaned up osec_mailer.
- Added lib64 directories to dirs.conf file.

* Thu Apr 19 2007 Stanislav Ievlev <inger@altlinux.org> 1.0.2-alt1
- fix requires

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.2-alt0.2.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Fri Mar 10 2006 Stanislav Ievlev <inger@altlinux.org> 1.0.2-alt0.2
- rebuild

* Thu Mar 09 2006 Stanislav Ievlev <inger@altlinux.org> 1.0.2-alt0.1
- updated from CVS

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.1-alt3.1
- Rebuilt with libstdc++.so.6.

* Tue Jan 11 2005 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt3
- added new directory to list, fix building with gcc3.4

* Tue Oct 12 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt2
- update from CVS: added new directories to list, allow to work 
  with nonexistent directories

* Tue Aug 10 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt1
- 1.0.1 final: goto Sisyphus

* Tue Aug 03 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt0.rc2
- 1.0.1rc2
    osec: pathname quotation (space class symbols)
    osec_mailer: fix possible DoS

* Mon Jul 05 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt0.rc1
- 1.0.1rc1:
    - change ':' separator to '\t' to avoid extra quotation
    - more report filters

* Tue Jun 01 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.0-alt11
- update from CVS: fixed typo in reporter

* Tue May 18 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.0-alt10
- final

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.0-alt9.1
- Rebuilt with openssl-0.9.7d.

* Thu May 06 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.0-alt9
- rc5:
    improved filter (for files that turned into symlinks)

* Thu Apr 22 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.0-alt8
- rc4:
   improved filter (uninitialized values)
   improved cron job (save osec's exit code)

* Mon Apr 05 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.0-alt7
- rc3:
    added sorting to filter

* Fri Apr 02 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.0-alt6
- rc2:
   remove debug message from the report filter ;)

* Wed Mar 31 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.0-alt5
- rc1:
    minor fixes in report
    move rm -f from post to triggers

* Tue Mar 30 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.0-alt4
- minor improvements
- move post script to mailreport

* Mon Mar 29 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.0-alt3
- beta2
   improvements in reporter:
    -- print date
    -- don't print about new normal files during database init
   improvements in osec:
    -- print user and group names
    -- renice
    -- print information about processing and database init

* Fri Mar 26 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.0-alt2
- added reporter module

* Thu Mar 25 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.0-alt1
- new ideas,new versions
  TODO: remove old *.db files
  
* Wed Mar 03 2004 Stanislav Ievlev <inger@altlinux.org> 0.6.0-alt2.1
- rebuild with libdb4.2
- this is a latest this osec generation release

* Wed May 14 2003 Stanislav Ievlev <inger@altlinux.ru> 0.6.0-alt2
- fix backward compatibility during delete

* Mon May 05 2003 Stanislav Ievlev <inger@altlinux.ru> 0.6.0-alt1
- new release

* Tue Apr 08 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5.4-alt1
- minor features, bugfixes

* Wed Mar 19 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5.3-alt1
- fix race during filesystem walking

* Wed Mar 12 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5.2-alt4
- rebuid with latest libing

* Tue Mar 04 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5.2-alt3
- fine sources

* Wed Feb 05 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5.2-alt2
- unslash now in libing
- daedalus release

* Tue Feb 04 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5.2-alt1
- fix map usage

* Mon Jan 27 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5.1-alt1
- minor fixes

* Thu Jan 16 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5-alt3
- daedalus release

* Mon Jan 13 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5-alt2
- sync with stable

* Fri Jan 10 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5-alt1
- begin unstable branch

* Wed Jan 08 2003 Stanislav Ievlev <inger@altlinux.ru> 0.4.1-alt3
- sync with latest libing changes

* Fri Dec 27 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.1-alt1
- development version
- ported to libing (general config file format)

* Wed Dec 18 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4-alt2
- update documentation, write TODO and future plans

* Wed Dec 11 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4-alt1
- final 0.4. TODO done.
- fix minor bugs, added filtering

* Mon Dec 02 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3.6.4-alt1
- experimental: dropping privs, manpage, signal handlers
- config(noreplace) for cron.daily
- added contrib from Andy Gorev <gorev@mailru.com>

* Fri Nov 29 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3.6.3-alt1
- more changes in memory work
- added support for symlink checkings ( when file became symlink )
- added command-line options

* Thu Nov 28 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3.6.2-alt1
- development version. finally move to new object scheme
  added to Sisyphus 'cause previous version was too unstable (memory corruptions)
  new features will be in the next version.

* Mon Nov 25 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3.5-alt1
- bugfixes, code improvements.

* Sun Nov 10 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3.4-alt1
- light improvements in bad files' report
- more flexible config file (stage 1: checkers definitions for each directory)
  TODO: may be hash_storage object over storage?

* Wed Sep 04 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3.3-alt2
- fixed bug in default config (database location)

* Mon Sep 02 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3.3-alt1
- move to XML config file
  TODO: make osec more flexible (name,depth)

* Thu Aug 15 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3.2-alt3
- light improvements in report and code

* Wed Aug 14 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3.2-alt2
- light code cleanup

* Tue Aug 13 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3.2-alt1
- Improvements. See changelog for details

* Thu Aug 08 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3-alt2
- Added provides/obsoletes to mtree-sec

* Mon Aug 05 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3-alt1
- first release

* Fri Jul 12 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.98.3-alt0.1
- fix very big first e-mails

* Thu Jul 11 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.98.2-alt0.2
- new report style

* Wed Jul 10 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.98.1-alt0.2
- don't see symlinks: useless thing

* Wed Jul 10 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.98.1-alt0.1
- improvements

* Tue Jul 09 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.98-alt0.1
- Initial release for Sisyphus
