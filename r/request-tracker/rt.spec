%define svn svn17640
# Apache1 setup
%define webusr apache
%define webgrp apache
# Apache2 setup
%define webusr2 apache2
%define webgrp2 webmaster
%define rtname rt
%define fullrtname request-tracker
# Database setup
%define dbhost localhost
%define mysql_dba    root
%define pgsql_dba    postgres
%define oracle_dba    system
%define sqlite_dba    root

%define dbname %rtname
%define dbuser %rtname

%define wwwroot %webserver_webappsdir

Summary: Request Tracker (RT) is an enterprise-grade issue tracking system
Name: %fullrtname
Version: 3.8.10
Release: alt1
Group: Networking/WWW
License: GPL
Url: http://www.bestpractical.com/rt/
BuildArch: noarch

# Obsolete old names
Obsoletes: rt

Source0: %name-%version.tar

%add_findreq_skiplist */bin/webmux.pl 
%add_findreq_skiplist */lib/RT/Config.pm
%add_findreq_skiplist */sbin/rt-setup-database
%add_findreq_skiplist */lib/RT/Test/*
%add_findreq_skiplist */lib/RT/Test.pm
%add_findreq_skiplist */lib/RT/Handle.pm
%add_findreq_skiplist */lib/RT/I18N/i_default.pm
%add_findreq_skiplist */lib/RT/Search.pm
%add_findreq_skiplist */lib/RT/Search/*

%define _perl_lib_path %_libexecdir/%rtname/lib/

%define siteconfig %_sysconfdir/%rtname/RT_SiteConfig.pm

# Apache1 and mod_fastcgi
%define apacheconfig %_sysconfdir/httpd/conf/vhosts.d/%rtname.conf.example
# Apache2 and mod_perl
# FIXME Where should i put this?
%define apache2config %_sysconfdir/httpd2/conf/%rtname.conf.example

# Common packages
Requires: smtpd
# Perl modules
Requires: perl(CGI.pm) >= 3.350
Requires: perl(DBIx/SearchBuilder.pm) >= 1.510
Requires: perl(Text/Quoted.pm) >= 2.020
Requires: perl(Module/Versions/Report.pm) >= 1.030
Requires: perl(Text/Quoted.pm) >= 2.05
# Manual
Requires: perl(Data/ICal.pm)
# Main package is builded with mysql support
Requires: perl(DBD/mysql.pm)

Requires: perl(Term/ReadKey.pm)
Requires: perl(FCGI.pm)
Requires: perl(Apache/Session/Postgres.pm)
Requires: perl(CSS/Squish.pm)
Requires: perl(Calendar/Simple.pm)
Requires: perl(Mouse.pm)

BuildRequires(pre): rpm-build-fonts rpm-build-webserver-common

# Automatically added by buildreq on Wed Jul 16 2008 (-ba)
BuildRequires: gnupg perl-Apache-Session perl-CPAN perl-CSS-Squish perl-Calendar-Simple perl-DBD-mysql perl-DBIx-SearchBuilder perl-Data-ICal perl-DateTime-TimeZone perl-Email-Address perl-FCGI perl-File-ShareDir perl-GnuPG-Interface perl-GraphViz perl-HTML-Format perl-HTML-RewriteAttributes perl-HTML-Scrubber perl-HTTP-Server-Simple-Mason perl-IPC-Run-SafeHandles perl-Locale-Maketext-Fuzzy perl-Locale-Maketext-Lexicon perl-Log-Agent perl-Log-Dispatch perl-MIME-Types perl-MIME-tools perl-Mail-SpamAssassin perl-Module-Versions-Report perl-Net-Server perl-PerlIO-eol perl-Regexp-Common perl-Term-ReadKey perl-Test-HTTP-Server-Simple perl-Test-WWW-Mechanize perl-Text-Quoted perl-Text-Template perl-Text-WikiFormat perl-Text-Wrapper perl-Time-modules perl-Tree-Simple perl-UNIVERSAL-require perl-XML-RSS perl-XML-Simple perl-capitalization sendmail-common
BuildRequires: perl-FCGI-ProcManager fonts-ttf-droid
# build fix by hiddenman
BuildRequires: perl-Mouse perl-GD perl-GD-Graph perl-GD-Text

%description
Request Tracker (RT) is an enterprise-grade issue tracking system. It allows
organizations to keep track of their to-do lists, who is working
on which tasks, what's already been done, and when tasks were
completed. It is available under the terms of version 2 of the GNU
General Public License (GPL), so it doesn't cost anything to set
up and use.

Built with options:
     --with-db-type=mysql
     --with-db-host=%dbhost
     --with-db-dba=%mysql_dba --with-db-rt-user=%dbuser
     --with-db-database=%dbname
     --with-web-user=%webusr --with-web-group=%webgrp

%package apache
Summary: Apache 1.x support the %name
Group: Networking/WWW
Requires: %name = %version
Requires: apache-common
Requires: mod_fastcgi

%description apache
%summary

%package apache2
Summary: Apache 2.x support the %name
Group: Networking/WWW
Requires: %name = %version
Requires: apache2-common
Requires: apache2-mod_perl

%description apache2
%summary

%package postgresql
Summary: PostgreSQL support for the %name
Group: Networking/WWW
Requires: %name = %version
Requires: perl(DBD/Pg.pm)

%description postgresql
%summary

#%%package oracle
#Summary: Oracle support for the %name
#Group: Networking/WWW
#Requires: %name = %version
#Requires: perl(DBD/Oracle.pm)

#%%description oracle
#%%summary

%package sqlite
Summary: SQLite support for the %name
Group: Networking/WWW
Requires: %name = %version
Requires: perl(DBD/SQLite.pm)

%description sqlite
%summary


%prep

# now the normal stuff
%setup

cat <<EOF >>config.layout
<Layout ALT>
  prefix:              %_prefix
  exec_prefix:         %_prefix
  bindir:              %_libexecdir/%rtname/bin
  sbindir:             %_libexecdir/%rtname/sbin
  sysconfdir:          %_sysconfdir/%rtname
  datadir:             %_datadir
  libdir:              %_libexecdir/%rtname/lib
  mandir:              %_mandir
  vardir:              %_var
  htmldir:             %wwwroot/%rtname
  fontdir:             %wwwroot/%rtname/fonts
  manualdir:           %_defaultdocdir/%rtname-%version
  localstatedir:       %_localstatedir/%rtname/
  logfiledir:          %_logdir/%rtname
  masonstatedir:       %_localstatedir/%rtname/cache/mason_data
  sessionstatedir:     %_localstatedir/%rtname/cache/session_data
  customdir:           %_libexecdir/%rtname/local
  customdir2:          %wwwroot/%rtname/local
  custometcdir:        %_libexecdir/%rtname/local/etc
  customhtmldir:       %wwwroot/%rtname/local/html
  customlexdir:        %_libexecdir/%rtname/local/po
  customlibdir:        %_libexecdir/%rtname/local/lib
</Layout>
EOF

%build

#sed -i "s/\[3.8.0\]/\[%version\]/g" ./configure.ac
%autoreconf
%configure --enable-layout=ALT \
	    --enable-graphviz \
	    --enable-gpg \
            --with-db-type=mysql \
            --with-db-host=%dbhost \
            --with-db-dba=%mysql_dba --with-db-rt-user=%dbuser \
            --with-db-database=%dbname \
            --with-web-user=%webusr --with-web-group=%webgrp \
            --with-apachectl=%_sbindir/apachectl

%install
make DESTDIR=%buildroot install

mkdir -p %buildroot%_localstatedir/%rtname/cache/mason_data/{cache,etc,obj}
mkdir -p %buildroot%_localstatedir/%rtname/cache/session_data
mkdir -p %buildroot%_localstatedir/%rtname/data/gpg

mkdir -p %buildroot%wwwroot/%rtname/local/html
mkdir -p %buildroot%wwwroot/%rtname/RTx
mkdir -p %buildroot%_libexecdir/%rtname/bin
mkdir -p %buildroot%_libexecdir/%rtname/lib/RTx
mkdir -p %buildroot%_libexecdir/%rtname/local/{etc,po,lib}

# apache config
mkdir -p %buildroot%_sysconfdir/httpd/conf/vhosts.d
cp altlinux/%rtname-apache-vhost.conf %buildroot%apacheconfig

# apache2 config
mkdir -p %buildroot%_sysconfdir/httpd2/conf/
cp altlinux/%rtname-apache2-vhost.conf %buildroot%apache2config

# rt-remind,rt-count and rt-escalate scripts
cp altlinux/%rtname-rt-remind %buildroot%_libexecdir/%rtname/bin/rt-remind
cp altlinux/%rtname-rt-count %buildroot%_libexecdir/%rtname/bin/rt-count
cp altlinux/%rtname-rt-escalate %buildroot%_libexecdir/%rtname/bin/rt-escalate

# fix permissions
find %buildroot%_libexecdir/%rtname/ -type d -print0 | xargs -r0 chmod 2755 --
find %buildroot%_libexecdir/%rtname/ -type f -print0 | xargs -r0 chmod 0644 --
find %buildroot%_libexecdir/%rtname/ -name '*.pm' -type f -print0 | xargs -r0 chmod 0755 --
find %buildroot%_libexecdir/%rtname/bin/ -type f -print0 |xargs -r0 chmod 0755 --
find %buildroot%_libexecdir/%rtname/sbin/ -type f -print0 |xargs -r0 chmod 0755 --
find %buildroot%wwwroot/%rtname -type d -print0 |xargs -r0 chmod 2755 --
find %buildroot%wwwroot/%rtname -type f -print0 |xargs -r0 chmod 0644 --
find %buildroot%_libexecdir/%rtname/local -type d -print0 |xargs -r0 chmod 2755 --
#this will be /usr/share/docs
find docs -type f -print0 |xargs -r0 chmod 0644 --

mkdir -p %buildroot%_var/log/%rtname
touch %buildroot%_var/log/%rtname/%rtname.log

# Remove win32 service
rm -f %buildroot/%_libexecdir/rt/bin/mason_handler.svc

# Replace /usr/local
sed -i "s|#!/usr/local/bin/perl|#!/usr/bin/perl|" %buildroot%_libexecdir/%rtname/bin/rt-count
sed -i "s|#!/usr/local/bin/perl|#!/usr/bin/perl|" %buildroot%_libexecdir/%rtname/bin/rt-escalate
sed -i "s|#!/usr/local/bin/speedy|#!/usr/bin/speedy|" %buildroot%_libexecdir/%rtname/bin/mason_handler.scgi

rm -f %wwwroot/%rtname/fonts/*ttf
ln -sf %_ttffontsdir/droid/DroidSans{,Fallback}.ttf %buildroot%wwwroot/%rtname/fonts/

#%pre
#/usr/sbin/groupadd -r %rtname


%post
#check for compliance
perl %_libexecdir/%rtname/sbin/rt-test-dependencies --with-mysql --with-fastcgi

cat <<EOF
	Congratulations. RT has been installed.

You must now configure RT by editing %siteconfig and %apacheconfig.

(You will definitely need to set RT's database password before continuing. Not doing
so could be very dangerous)

After that, you need to initialize RT's database by running:

%_libexecdir/%rtname/sbin/rt-setup-database --action init \ 
     --dba %mysql_dba --prompt-for-dba-password

If something goes wrong you can always drop everything, by executing:

%_libexecdir/%rtname/sbin/rt-setup-database --action drop \ 
     --dba %mysql_dba --prompt-for-dba-password

Look into these scripts and put them in the crontab:

%_libexecdir/%rtname/bin/rt-remind
%_libexecdir/%rtname/bin/rt-escalate
%_libexecdir/%rtname/bin/rt-count

Put these lines in the /etc/aliases and read the docs:

# RT aliases
support: "|%_libexecdir/%rtname/bin/rt-mailgate --queue 'General' --action correspond --url https://rt.example.com/"
support-comments: "|%_libexecdir/%rtname/bin/rt-mailgate --queue 'General' --action comment --url https://rt.example.com/"
#
    Go to the http://wiki.bestpractical.com/ for contribs and docs

EOF

%post postgresql

echo ""
echo "You must change database type in the config."
echo ""
echo "After that, you need to initialize RT's database by running"
echo ""
echo "%_libexecdir/%rtname/sbin/rt-setup-database --action init \ "
echo "     --dba %pgsql_dba --prompt-for-dba-password"
echo ""
echo "If something goes wrong you can always drop everything, by executing"
echo ""
echo "%_libexecdir/%rtname/sbin/rt-setup-database --action drop \ "
echo "     --dba %pgsql_dba --prompt-for-dba-password"
echo ""

#%%post oracle

#echo ""
#echo "You must change database type in the config."
#echo ""
#echo "After that, you need to initialize RT's database by running"
#echo ""
#echo "%_libexecdir/%rtname/sbin/rt-setup-database --action init \ "
#echo "     --dba %oracle_dba --prompt-for-dba-password"
#echo ""
#echo "If something goes wrong you can always drop everything, by executing"
#echo ""
#echo "%_libexecdir/%rtname/sbin/rt-setup-database --action drop \ "
#echo "     --dba %oracle_dba --prompt-for-dba-password"
#echo ""

%post sqlite

echo ""
echo "You must change database type in the config."
echo ""
echo "After that, you need to initialize RT's database by running"
echo ""
echo "%_libexecdir/%rtname/sbin/rt-setup-database --action init \ "
echo "     --dba %sqlite_dba --prompt-for-dba-password"
echo ""
echo "If something goes wrong you can always drop everything, by executing"
echo ""
echo "%_libexecdir/%rtname/sbin/rt-setup-database --action drop \ "
echo "     --dba %sqlite_dba --prompt-for-dba-password"
echo ""

%files
%doc etc/upgrade README README.Oracle COPYING docs UPGRADING.mysql UPGRADING
%_libexecdir/%rtname
%attr(3775,root,%webgrp) %dir %_var/log/%rtname
%attr(0664,root,%webgrp) %_var/log/%rtname/%rtname.log
%dir %_localstatedir/%rtname
%attr(3775,root,%webgrp) %dir %_localstatedir/%rtname/cache
%attr(3775,root,%webgrp) %dir %_localstatedir/%rtname/cache/mason_data
%attr(3775,root,%webgrp) %dir %_localstatedir/%rtname/cache/mason_data/cache
%attr(3775,root,%webgrp) %dir %_localstatedir/%rtname/cache/mason_data/etc
%attr(3775,root,%webgrp) %dir %_localstatedir/%rtname/cache/mason_data/obj
%attr(3775,root,%webgrp) %dir %_localstatedir/%rtname/cache/session_data
%attr(3775,root,%webgrp) %dir %_localstatedir/%rtname/data
%attr(3775,root,%webgrp) %dir %_localstatedir/%rtname/data/gpg
%wwwroot/%rtname
%dir %_sysconfdir/%rtname
%attr(0640,root,%webgrp) %config(noreplace) %_sysconfdir/%rtname/RT_SiteConfig.pm
%attr(0644,root,%webgrp) %config %_sysconfdir/%rtname/RT_Config.pm
%attr(0644,root,%webgrp) %_sysconfdir/%rtname/acl*
%attr(0644,root,%webgrp) %_sysconfdir/%rtname/initialdata
%attr(0644,root,%webgrp) %_sysconfdir/%rtname/schema*
%exclude %apacheconfig
%exclude %apache2config

%files apache 
%attr(0640,root,%webgrp) %config(noreplace) %apacheconfig

%files apache2
%attr(0640,root,%webgrp) %config(noreplace) %apache2config

%files postgresql
#%%files oracle
%files sqlite

%changelog
* Tue Apr 19 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 3.8.10-alt1
- 3.8.10. Security fixes:
  + CVE-2011-1689
  + CVE-2011-1688
  + CVE-2011-1687
  + CVE-2011-1686
  + CVE-2011-1685
- Enhance findreq skiplist.

* Tue Nov 09 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 3.8.8-alt2
- Cherry-pick upstream commit fixes working with PostgreSQL 9.

* Wed May 26 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 3.8.8-alt1
- 3.8.8
- Relocate web part into /var/www/webapps/rt/.
- Don't mark some files in /etc/rt/ as configs (shema files etc).

* Tue Jan 12 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 3.8.7-alt1
- 3.8.7
- Add dependency on perl(Mouse.pm).

* Mon Nov 02 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 3.8.6-alt1
- 3.8.6
- Remove obsoleted russian localization subpackage.
- Update buildreqs for fix building (hiddenman@).

* Wed Sep 16 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 3.8.5-alt1
- 3.8.5. Security fix:
  + RT Custom Fields Script Insertion Vulnerability, see
    http://secunia.com/advisories/36752/
- Add missing Requires (Closes: #21203, #21210, #21211, #21460, #21512)

* Fri Mar 06 2009 Andrew Kornilov <hiddenman@altlinux.ru> 3.8.2-alt4
- Removed Oracle support due to the eternal perl-DBD-Oracle unmet

* Thu Mar 05 2009 Andrew Kornilov <hiddenman@altlinux.ru> 3.8.2-alt3
- Added Test.pm to the findreq_skiplist

* Thu Jan 08 2009 Andrew Kornilov <hiddenman@altlinux.ru> 3.8.2-alt2
- 3.8.2 major release
- Russian translation is updated

* Mon Nov 24 2008 Andrew Kornilov <hiddenman@altlinux.ru> 3.8.2-alt1.svn17009
- SVN trunk
- Fixed apache and apache2 owners

* Fri Nov 21 2008 Andrew Kornilov <hiddenman@altlinux.ru> 3.8.2-alt1
- SVN trunk

* Wed Aug 20 2008 Andrew Kornilov <hiddenman@altlinux.ru> 3.8.1-alt1
- 3.8.1 release
- Updated Russian translation
- Makefile patch recreated

* Sun Jul 13 2008 Andrew Kornilov <hiddenman@altlinux.ru> 3.8.0-alt2
- 3.8.0 major release
- ChangeLog.bz2 moved from the archive to the sources
- Makefile patch recreated
- ru.po updated a bit (it will have finished by next release)
- Reduced non-root file-owning

* Sun Jun 22 2008 Andrew Kornilov <hiddenman@altlinux.ru> 3.8.0-alt1.svn13532
- Latest svn sources
- Updated rt-alt-perl-5.8.4-support.patch and alt-makefile.patch patches
- Do not put the svn revision in the version
- New directory /var/lib/rt/data/gpg as GPG home
- Directory perms changed to 3775

* Thu Jun 12 2008 Andrew Kornilov <hiddenman@altlinux.ru> 3.7.86-alt1.svn13229
- Latest svn sources
- Updated makefile patch

* Thu Jun 05 2008 Andrew Kornilov <hiddenman@altlinux.ru> 3.7.85-alt2.svn12903
- Latest svn sources
- Requires perl(Text/Quoted.pm) >= 2.05
- Changes localstatedir in the layout to the /var/lib/rt/

* Thu Jun 05 2008 Andrew Kornilov <hiddenman@altlinux.ru> 3.7.85-alt2.svn12879
- Latest svn sources

* Thu May 08 2008 Andrew Kornilov <hiddenman@altlinux.ru> 3.7.85-alt1.svn12138
- Latest svn sources

* Tue May 06 2008 Andrew Kornilov <hiddenman@altlinux.ru> 3.7.82-alt3.svn12076
- Latest svn sources
- Fixed hardcoded perl versions

* Sat May 03 2008 Andrew Kornilov <hiddenman@altlinux.ru> 3.7.82-alt2.svn12035
- Latest svn sources

* Fri May 02 2008 Andrew Kornilov <hiddenman@altlinux.ru> 3.7.82-alt1.svn11994
- Latest svn sources

* Wed Apr 16 2008 Andrew Kornilov <hiddenman@altlinux.ru> 3.7.81-alt1.svn11748
- Requires smtpd instead of postfix
- Removed manual perl requirements (except some of them with fixed version)
- Fixed spec (twice listed files)
- Fixed /usr/local in some scripts
- New subpackages apache and apache2

* Wed Feb 27 2008 Andrew Kornilov <hiddenman@altlinux.ru> 3.7.22-alt2.svn10939
- Latest svn sources with email content-type fix
- Removed tests
- Enabled and fixed AutoReqProv (thanks to Nikolay Fetisov)
- Use libexecdir instead of libdir (revert back to the old scheme)

* Mon Feb 25 2008 Andrew Kornilov <hiddenman@altlinux.ru> 3.7.22-alt1.10927
- New version
- Requires perl-DBIx-SearchBuilder >= 1.51

* Thu Jan 17 2008 Andrew Kornilov <hiddenman@altlinux.ru> 3.7.21-alt2.10373
- Enabled autoreq
- Deleted mason_handler.svc (win32)
- Use RT libs for findreq

* Thu Jan 17 2008 Andrew Kornilov <hiddenman@altlinux.ru> 3.7.21-alt1.10373
- Latest svn sources
- New File::Sharedir dependency
- New CSS::Squish dependency

* Tue Nov 13 2007 Andrew Kornilov <hiddenman@altlinux.ru> 3.7.20-alt1.9652
- New version

* Tue Sep 18 2007 Andrew Kornilov <hiddenman@altlinux.ru> 3.7.15-alt1.9080
- New version 

* Mon Sep 03 2007 Andrew Kornilov <hiddenman@altlinux.ru> 3.7.14-alt2.8879
- Updates

* Sat Sep 01 2007 Andrew Kornilov <hiddenman@altlinux.ru> 3.7.14-alt1.8868
- New experimental version from SVN
- New dependencies on GnuPG::Interface and PerlIO::eol

* Fri Jul 06 2007 Andrew Kornilov <hiddenman@altlinux.ru> 3.6.4-alt1
- New release
- Spec cleanups (removed conditional builds, new macroses etc.)
- Now requires perl-Text-Quoted >= 2.02, perl-Module-Versions-Report >= 1.03

* Tue Mar 27 2007 Andrew Kornilov <hiddenman@altlinux.ru> 3.6.3-alt3.svn7331
- Requires SearchBuilder >=1.48

* Sun Mar 25 2007 Andrew Kornilov <hiddenman@altlinux.ru> 3.6.3-alt2.svn7331
- Latest SVN updates
- Spec cleanups
- rt.conf is in the vhosts.d now
- New dependency on postfix
- Updated rt-remind script
- New rt-escalate and rt-count scripts

* Mon Feb 05 2007 Andrew Kornilov <hiddenman@altlinux.ru> 3.6.3-alt1.svn6946
- Bugfixes from SVN
- Added virtual packages which provide PostgreSQL, Oracle and SQLite support

* Tue Dec 26 2006 Andrew Kornilov <hiddenman@altlinux.ru> 3.6.3-alt1.svn6691
- Bugfix release

* Tue Dec 19 2006 Andrew Kornilov <hiddenman@altlinux.ru> 3.6.2-alt1
- 3.6.2 release
- Updated russian translation
- Fixed perl-UNIVERSAL-require dependency

* Tue Oct 03 2006 Andrew Kornilov <hiddenman@altlinux.ru> 3.6.1-alt1.svn6144
- Latest SVN updates
- Updated russian translation
- Spec cleanups
- rt-remind script fixes
- Patch #1 (layout) moved to the spec for buildtime macroses
- New perl modules dependencies (UNIVERSAL/require.pm)

* Wed Jun 21 2006 Andrew Kornilov <hiddenman@altlinux.ru> 3.6.0-alt2.svn5413
- New major release with many of new features (+ updates from SVN)
- Added upgrade directory
- New requirement (Calendar/Simple.pm)
- Requires SearchBuilder >=1.39
- Updated russian translation and russian initialdata

* Fri May 05 2006 Andrew Kornilov <hiddenman@altlinux.ru> 3.4.5-alt1.svn5167
- Latest SVN updates
- libexecdir changed to libdir

* Wed Feb 08 2006 Andrew Kornilov <hiddenman@altlinux.ru> 3.4.5-alt1.svn4503
- Latest SVN updates
- Added perl-CPAN dependency, updated SearchBuilder version dependency

* Sat Jan 21 2006 Andrew Kornilov <hiddenman@altlinux.ru> 3.4.5-alt1.svn4431
- 3.4.5 and latest SVN updates
- lib/RTx and html/RTx created now by main package

* Wed Sep 28 2005 Andrew Kornilov <hiddenman@altlinux.ru> 3.4.4-alt3.svn3881
- Moved /usr/lib/rt/RT to /usr/lib/rt/lib
- Removed *.in files 

* Sun Sep 25 2005 Andrew Kornilov <hiddenman@altlinux.ru> 3.4.4-alt2.svn3881
- Fixed configuration files permissions
- Patch autoconf script for version
- Fresh translations
- Fixed layout patch

* Sat Sep 24 2005 Andrew Kornilov <hiddenman@altlinux.ru> 3.4.4-alt1.svn3881
- Latest svn updates
- Package renamed to request-tracket
- First build with deps

* Sat Aug 27 2005 Andrew Kornilov <hiddenman@altlinux.ru> 3.4.4rc3-alt1.svn3726
- Latest svn updates

* Thu May 26 2005 Andrew Kornilov <hiddenman@altlinux.ru> 3.4.2-alt1.svn2969
- Latest svn updates
- Updated translation

* Tue May 24 2005 Andrew Kornilov <hiddenman@altlinux.ru> 3.4.2-alt2.svn2931
- Fixed wrong fs layout (cache moved back to /var/lib/rt)
- Typo in previous build wasn't typo ;) Fixed
- Fixed wrong permissions on critical config files (anybody can see database
  password)
- Added missed requires: perl(FCGI.pm) and mod_fastcgi  

* Mon May 23 2005 Andrew Kornilov <hiddenman@altlinux.ru> 3.4.2-alt1.svn2931
- Version 3.4.2 + latest updates from SVN
- Fixed typo in vhosts file rt.conf
- Updated translation
- /var/lib/rt/local moved to /usr/lib/rt/local
- Removed .svn
- Corrected options for rt-test-dependencies (now --with-fastcgi)

* Mon Apr 04 2005 Andrew Kornilov <hiddenman@altlinux.ru> 3.4.1-alt3.svn2586
- Latest updates from SVN

* Mon Mar 14 2005 Andrew Kornilov <hiddenman@altlinux.ru> 3.4.1-alt3.svn2464
- Latest updates from SVN

* Wed Mar 02 2005 Andrew Kornilov <hiddenman@altlinux.ru> 3.4.1-alt2
- New heavy updated Russian translation from me

* Tue Mar 01 2005 Andrew Kornilov <hiddenman@altlinux.ru> 3.4.1-alt1
- latest 3.4.1 from svn
- rt.conf cleanups
- ru.po fixed (removed RTFM messages) + additional translation
- updated makefile patch

* Wed Feb 02 2005 Andrew Kornilov <hiddenman@altlinux.ru> 3.4.0-alt1
- New upstream release
- New Apache's rt.conf file with examples of external auth
- New messages from upstream ru.po file merged to my own ;-)
- New patch for support koi8-r and cp1251 encodings in email
- Added fresh Changelog

* Fri Dec 10 2004 Andrew Kornilov <hiddenman@altlinux.ru> 3.3.14-alt1
- New version
- Spec fixes (added noreplace for configs)

* Thu Nov 11 2004 Andrew Kornilov <hiddenman@altlinux.ru> 3.3.9-alt2
- Some fixes. Added russian package (my initial data and my reworked ru.po)

* Thu Nov 11 2004 Andrew Kornilov <hiddenman@altlinux.ru> 3.3.9-alt1
- First build for Sisyphus. Inital spec based on spec by Paulo Matos
  <paulo.matos@fct.unl.pt> (but fully reworked)
- Many bugs in spec, wrong FSH and other. But it works ;-)

