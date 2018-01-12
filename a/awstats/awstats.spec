%define _pseudouser_user awstats
%define _pseudouser_group awstats
%define _pseudouser_home %_localstatedir/%name
%define	docdir %_docdir/%name-%version

Name: awstats
Version: 7.7
Release: alt0.2.20180105

Summary: Real-time logfile analyzer to get advanced web statistics
Summary(ru_RU.KOI8-R):	Анализатор логов Web-сервера в режиме реального времени
License: GPL3
Group: Monitoring

Url: http://www.awstats.org
BuildArch: noarch

# https://github.com/eldy/awstats
Source: %name-%version.tar
Source1: awstats.cron
Source2: apache.modconfdir
Source3: apache2.mods-start
Source4: apache2.sites-available
Source5: apache2.sites-start
Source6: apache2.ports-start
Source7: README.ALT.ru_RU.UTF8

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-apache
BuildRequires(pre): rpm-build-apache2

# Automatically added by buildreq on Wed Jul 21 2010 (-bi)
BuildRequires: apache2-common perl-libwww tzdata perl-Switch perl-CGI

%description
AWStats is a short for Advanced Web Statistics. It's a free tool that generates
advanced web (but also ftp, syslog or mail) server access statistics
graphically. This log analyzer works as a CGI or from command line and shows
you all possible information your log contains, in few graphical web pages. It
uses a partial information file to be able to process large log files, often
and quickly. It can analyze log files from IIS (W3C log format), Apache log
files (NCSA combined/XLF/ELF log format or common/CLF log format), WebStar and
most of all web, proxy, wap, streaming servers (and even syslog, ftp servers or
mail logs).

%description -l ru_RU.KOI8-R
AWStats это сокращение от Advanced Web Statistics (расширеная Веб-статистика).
Это бесплатный инструмент для генерации расширеной статистики графиков о работе
http (а так же ftp, syslog или mail) сервисов. Данный анализатор работает как
из командной строки так и в виде CGI-скрипта.

%package docs
Summary: AWStats documentation set
Group: Monitoring

%description docs
AWStats is a short for Advanced Web Statistics. It's a free tool that generates
advanced web (but also ftp, syslog or mail) server access statistics
graphically. This log analyzer works as a CGI or from command line and shows
you all possible information your log contains, in few graphical web pages. It
uses a partial information file to be able to process large log files, often
and quickly. It can analyze log files from IIS (W3C log format), Apache log
files (NCSA combined/XLF/ELF log format or common/CLF log format), WebStar and
most of all web, proxy, wap, streaming servers (and even syslog, ftp servers or
mail logs).

%package apache
Summary: AWStats apache-related config
Group: Monitoring
Requires: %name = %version-%release
Requires: apache-base

%description apache
AWStats apache-related config

%package apache2
Summary: AWStats apache2-related config
Group: Monitoring 
Requires: %name = %version-%release
Requires: apache2-base

%description apache2
AWStats apache2-related config

%prep
%setup
%patch -p1
cp %SOURCE7 ./

%build
# build awgraphapplet.jar from source, avoiding upstream shipped binary
cd wwwroot/classes/src/
perl Makefile.pl

%install
install -d %buildroot%_datadir/%name
install -d %buildroot%_sysconfdir/{%name,cron.d}
install -d %buildroot%_pseudouser_home
install -d %buildroot%apache_modconfdir
install -d %buildroot%apache2_mods_start
install -d %buildroot%apache2_sites_available
install -d %buildroot%apache2_sites_start
install -d %buildroot%apache2_ports_start

cp -r {tools,wwwroot} %buildroot%_datadir/%name/
mv %buildroot%_datadir/%name/wwwroot/cgi-bin/{lang,lib,plugins} %buildroot%_datadir/%name/

# move unneeded files
mkdir examples
mv %buildroot%_datadir/%name/tools/{awstats_configure.pl,httpd_conf,webmin,xslt} examples/
mv %buildroot%_datadir/%name/wwwroot/cgi-bin/awredir.pl examples/
mv %buildroot%_datadir/%name/plugins/example/example.pm examples/

# fix permissions (again)
find %buildroot%_datadir/%name -name \*.pl -exec chmod 0755 {} \;

install -p -m644 %SOURCE1 %buildroot%_sysconfdir/cron.d/%name
install -p -m644 %SOURCE2 %buildroot%apache_modconfdir/%name.conf
install -p -m644 %SOURCE3 %buildroot%apache2_mods_start/%name.conf
install -p -m644 %SOURCE4 %buildroot%apache2_sites_available/%name.conf
install -p -m644 %SOURCE5 %buildroot%apache2_sites_start/%name.conf
install -p -m644 %SOURCE6 %buildroot%apache2_ports_start/%name.conf

%pre 
/usr/sbin/groupadd -r -f %_pseudouser_group ||:
/usr/sbin/useradd -g %_pseudouser_group -c 'AWStats log analyzer' \
        -d %_pseudouser_home -s /dev/null -r %_pseudouser_user >/dev/null 2>&1 ||:

%pre apache
/usr/sbin/usermod -g %_pseudouser_group -G %apache_group %_pseudouser_user

%pre apache2
/usr/sbin/usermod -g %_pseudouser_group -G %apache2_group %_pseudouser_user

%post apache
%post_apacheconf

%postun apache
%postun_apacheconf

%post apache2
%apache2_sbindir/a2chkconfig
%post_apache2conf

%postun apache2
%apache2_sbindir/a2chkconfig
%postun_apache2conf

%files
%_datadir/%name
%exclude %_datadir/%name/wwwroot/cgi-bin/awstats.model.conf
%exclude %_datadir/%name/wwwroot/classes/src
%exclude %_datadir/%name/plugins/example
# fix plugins perms
%attr(0644,root,root) %_datadir/%name/plugins/*.pm
%_sysconfdir/%name
%dir %attr(1775,root,%_pseudouser_group) %_pseudouser_home
%config(noreplace) %_sysconfdir/cron.d/%name
%doc README.md README.ALT.ru_RU.UTF8 wwwroot/cgi-bin/awstats.model.conf


%files docs
%doc docs examples

%files apache
%config(noreplace) %apache_modconfdir/%name.conf

%files apache2
%config(noreplace) %apache2_mods_start/%name.conf
%config(noreplace) %apache2_sites_available/%name.conf
%config(noreplace) %apache2_sites_start/%name.conf
%config(noreplace) %apache2_ports_start/%name.conf

%changelog
* Fri Jan 12 2018 L.A. Kostis <lakostis@altlinux.ru> 7.7-alt0.2.20180105
- Updated to GIT f316b1f (7.7 20180105).
- Rediffed all alt- patches:
  + tools: fix defaults paths.
  + lib/search_engines.pm: update russian search.
  + maxmind plugin: update asnum URLs.
  + lang/awstats-ru.txt: fix translation.
  + lib/operating_systems.pm: add ALTLinux.
  + awstats.pl: improve Opera detection.
  + lib/browsers.pm: Add Yandex Browser detection.

* Sat Aug 22 2015 L.A. Kostis <lakostis@altlinux.ru> 7.4-alt0.10.20150714
- lib/search_engines.pm: disable keywords decoding for google/yandex due
  result encryption.

* Mon Aug 10 2015 L.A. Kostis <lakostis@altlinux.ru> 7.4-alt0.9.20150714
- Add awstats to apache2 group too (closes #28698).

* Tue Aug 04 2015 L.A. Kostis <lakostis@altlinux.ru> 7.4-alt0.7.20150714
- More fixes and improvements:
  + improve Opera detection.
  + Add Yandex Browser detection.
  + fix Edge detection.

* Mon Aug 03 2015 L.A. Kostis <lakostis@altlinux.ru> 7.4-alt0.6.20150714
- Some improvements:
  + add M$ Edge browser
  + Improve Windows 10 detection.

* Sun Aug 02 2015 L.A. Kostis <lakostis@altlinux.ru> 7.4-alt0.5.20150714
- Synced with 7.4 2015-07-14 12:55 snapshot.

* Thu Jun 25 2015 L.A. Kostis <lakostis@altlinux.ru> 7.4-alt0.4.20150618
- Synced with 2015-06-18 snapshot.

* Mon Apr 27 2015 L.A. Kostis <lakostis@altlinux.ru> 7.4-alt0.3
- fix broken url for asnum query.

* Sat Apr 18 2015 L.A. Kostis <lakostis@altlinux.ru> 7.4-alt0.2
- Fix yandex detection (s/text/etext/g).

* Fri Apr 17 2015 L.A. Kostis <lakostis@altlinux.ru> 7.4-alt0.1
- Update to 7.4.
- Re-apply all patches:
  + lib/{robots,search_engines}.pm: update for ru.
  + wwwroot/cgi-bin/lib/browsers.pm: Add WebSec.
  + lib/operating_systems.pm: add ALTLinux.
  + tools: fix defaults paths.
  + lang/awstats-ru.txt: fix translation.

* Fri Mar 15 2013 L.A. Kostis <lakostis@altlinux.ru> 7.1.1-alt0.1
- 7.1.1.
- possibly fixes perl 5.16 compatibility issues (ALT #28686).

* Fri Oct 05 2012 L.A. Kostis <lakostis@altlinux.ru> 7.1-alt3.cvs20120604
- more fixes for yandex search.

* Wed Oct 03 2012 L.A. Kostis <lakostis@altlinux.ru> 7.1-alt2.cvs20120604
- update russian search engines.
- rebuild due /usr/sbin/service -> /sbin/service migration (ALT #27795).

* Wed Oct 03 2012 L.A. Kostis <lakostis@altlinux.ru> 7.1-alt1.cvs20120604
- Bug fixes:
  + fix permissions for .pl files.
  + awstats.pl: fix opera version detection (upstream #3564921)
  + browsers_phone.pm: add missing %%BrowsersFamily (upstream #3430233)

* Tue Oct 02 2012 L.A. Kostis <lakostis@altlinux.ru> 7.1-alt0.1.cvs20120604
- Updated to CVS 2012/06/04 shapshot.
- re-apply all azol@ patches.
- update buildreq: add perl-Switch, perl-CGI.

* Sat Jul 17 2010 Artem Zolochevskiy <azol@altlinux.ru> 6.95-alt1
- update to 6.95
- move webserver integration part to subpackages:
  + awstats-apache
  + awstats-apache2
- build awgraphapplet.jar from source, avoiding upstream shipped binary
- move example config file from sysconfdir to docdir
- move unneeded stuff to doc subpackge
- add post/postun webserver reload (#15191)
- reset icon,css,classes,js aliases to upstreams default
- set proper awstatsmisctrackerurl variable in awstats_misc_tracker.js
- modify default path to awstats.pl in awsatats_{buildstaticpages,updateall}.pl
- add ALTLinux to OS detection list
- fix typos in russian lang file
- add README.ALT.ru_RU.UTF8
- add patches from Debian:
  + Add WebSec to robots list
  + Correct link to the GNU Hurd homepage
  + Updated Russian translation

* Wed Dec 02 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 6.9-alt1.b2008.11.30
- Add dependency on perl-Encode.
- Prevent unneeded unix -> dos conversion (add "-U" to dos2unix call).
- Reduce macro abuse in specfile.

* Wed Oct 28 2009 L.A. Kostis <lakostis@altlinux.ru> 6.95-alt0.2009.10.28
- Update to unreleased 6.95 (2009-10-28 CVS snapshot).

* Sun Dec 07 2008 L.A. Kostis <lakostis@altlinux.ru> 6.9-alt0.b2008.11.30
- new unstable beta snapshot (2008-11-30).
- re-apply browser list.
- update buildreq: add perl-Encode.

* Fri Sep 05 2008 L.A. Kostis <lakostis@altlinux.ru> 6.9-alt0.b2008.08.05
- new unstable beta version (2008-08-05 shapshot).
- sync browsers list w/ forum.mozilla-russia.org detection code.
- fix file mode for cron.d file.

* Thu Nov 29 2007 L.A. Kostis <lakostis@altlinux.ru> 6.8-alt0.b2007.11.24
- NMU.
- new unstable version (2007-11-24 6.8 beta release).

* Wed Apr 25 2007 Igor Muratov <migor@altlinux.org> 6.6-alt2
- bugfix #11609

* Sun Jan 14 2007 Igor Muratov <migor@altlinux.org> 6.6-alt1
- nev version

* Tue Oct 03 2006 Igor Muratov <migor@altlinux.org> 6.5-alt2
- patch for seamonkey detection (thanks to lakostis@)

* Tue May 28 2006 Igor Muratov <migor@altlinux.org> 6.5-alt1
- New version

* Tue Aug 16 2005 Igor Muratov <migor@altlinux.org> 6.4-alt2
- Fix for package requires

* Mon Mar 21 2005 Igor Muratov <migor@altlinux.org> 6.4-alt1
- new version with security fixes

* Sat Feb 26 2005 Igor Muratov <migor@altlinux.org> 6.3-alt4
- play with geoip plugin

* Mon Feb 14 2005 Igor Muratov <migor@altlinux.org> 6.3-alt3
- Security fix CAN-2005-0116

* Tue Feb 08 2005 Igor Muratov <migor@altlinux.org> 6.3-alt2
- Fix permissions for /var/log/httpd

* Sun Jan 30 2005 Igor Muratov <migor@altlinux.org> 6.3-alt1
- New version

* Wed Nov 10 2004 Igor Muratov <migor@altlinux.org> 6.2-alt1
- New version
- Remove mail config template

* Tue May 25 2004 Igor Muratov <migor@altlinux.org> 6.1-alt1
- New version
- Spec cleanup
- Move all files to %_datadir/%name

* Fri Jan 23 2004 Igor Muratov <migor@altlinux.ru> 6.0-alt1
- New version

* Wed Oct 22 2003 Igor Muratov <migor@altlinux.ru> 5.9-alt1
- New version
- Fix for perl syntax error in plugins
- Move documentation to awstats-docs package

* Mon Jul  7 2003 Igor Muratov <migor@altlinux.ru> 5.6-alt1
Fixes:
- Domain with no pages hits were always reported as other in domain chart.
- percent for other in full list of "links for internet search engines"
  has been fixed.
New features/improvments:
- Report compression ratios with mod_deflate feature (Apache 2).
- A better browser detection.
- Can add regex values for a lot of list parameters (HostAliases,
  SkipDNSLookupFor, ...)
- StyleSheet parameter works completely now and sample of CSS files are
  provided.
- Add meta tags robots noindex,nofollow to avoid indexing of stats pages by
  compliant robots.
- Added a "Miscellanous chart" to report ratio of Browsers that support:
  Java, Flash, Real reader, Quicktime reader, WMA reader, PDF reader.
- "Miscellanous chart" also report the "Add to favourites" (must remove the
  "robots.txt" and "favicon.ico" entries off your SkipFiles parameter in your
  config file to have this feature working.
- Update process now try a direct access at last updated record when a new
  update is ran. If it fails (file changed or wrong checksum of record), then
  it does a scan from the beginning of file until a new date has been
  reached (This was the only way of working on older version). So now update
  process is very much faster for thoose who don't purge/rotate their log
  file between two update process (direct access is faster than full scan).
- Better look for report pages on Netscape/Mozilla browsers.
Other/Documentation:
- Updated documentation.
- Update wap/imode browser list.
Note 1:
  You should remove the "robots.txt" and "favicon.ico" entries in the SkipFiles
  parameter in your config files after updgrading to 5.6.

Version 5.5
Fixes:
- Summary robots list was limited to MaxNbOfLoginShown instead of being
  limited to MaxNbOfRobotShown value.
- Fixed a bug when using HBL codes in ShowRobotsStats parameter.
- AllowAccessFromWebToFollowingAuthenticatedUsers now works for users with
  space in name.
- Bug 730996. When URLWithQueryWithoutFollowingParameters was used with a
  value and another parameter was ended with this value, the wrong parameter
  was truncated from URL.
New features/improvments:
- Added a 'Screen Size' report.
- Group OS by families. Added a detailed OS version chart.
- Better 404 errors management. URLs are always cleaned from their parameter
  to build '404 not found' URLs list (because parameters are not interesting
  as they can't have effect as page is not found). Referrer URLs list for '404
  not found' URLs are kept with parameters only if URLReferrerWithQuery is set
  to 1. This make this report more useful.
- Added 'geoipfree' plugin (same than 'geoip' plugin but using the free
  Perl module Geo::IPfree).
- 'geoip' plugin can works with Perl module Geo::IP but also with Perl module
  Geo::IP::PurePerl).
- Added 'userinfo' plugin to add information from a text file (like lastname,
  office department,...) in authenticated user chart.
- month parameter can accept format -month=D, not only -month=DD
- Optimized code size.
- Optimized HTML output report size.
- Added plugin ipv6 to fully support IPv6 (included reverse DNS lookup).
- Split month summary chart and days of month chart in two different charts in
  main page. This also means that ShowDaysOfMonthStats and
  AddDataArrayShowDaysOfMonthStats parameters were added.
- Added -staticlinksext to build static pages with another extension than
  default .html
- Added QMail support and better working support for Postfix and Sendmail (SMA
  preprocessor was replaced by maillogconv.pl).
Other/Documentation:
- AWStats default install directory is /usr/local/awstats for unix like OS.
- Added Isle of Man, Monserat, and Palestinian flag icon.
- Added "local network host" and "Satellite access host" in label of possible
  countries and icons (They appears when using geoip plugins).
- Better management of parsed lines counting. The last line number is also
  stored in history file, for a future use.
- Removed LogFormat=5 option for ISA log file because I am fed up of
  supporting bugged and non standard MS products. Sorry but this takes me too
  many times. To use AWStats with an ISA server, just use now a preprocessor
  tool to convert into a W3C log file.
- Added estonian, serban and icelandic language files.
- Updated documentation.

* Wed Mar  5 2003 Igor Muratov <migor@altlinux.ru> 5.4-alt1
Fixes:
- File name with space inside were not correctly reported when doing FTP log
  server analysis.
- Problem in Wy tag for ten first weeks of year (coded on 1 char instead
  of 2: First week should be "00" instead of "0").
- Tooltips now works correctly with Netscape (>= 5.0).
- Better parsing of parameters (Solved bug 635962).
- Users did not appear in Authenticated users list if hits on pages were 0.
- Value of title "Top x" for domains chart was not always correct.
- Fixed bug 620040 that prevented to use "#" char in HTMLHeadSection.
- Whois link did not work for jp, au, uk and nz domains.
- WhoIs link did not work if host name contained a "-" char.
- Fixed a bug in mod_gzip stats when only ratio was given in log.
New features/improvments:
- Lang parameter accepts 'auto' value (Choose first available language
  accepted by browser).
- Little support for realmedia server.
- Added urlaliasbuilder.pl tool.
- Added URL in possible values for ExtraSection first column.
- New parameter: URLWithAnchor (set to 0 by default).
- Export tooltips features in a plugin (plugin tooltips disabled by default).
- Added average session length in Visit Duration report.
- Added percentage in Visit Duration report.
- logresolvemerge.pl can read .gz or .bz2 files.
- Added icons and Mime label for file types report.
- Added parameters AddDataArrayMonthDayStats, AddDataArrayShowDaysOfWeekStats,
  and AddDataArrayShowHoursStats.
- Added the Whois info in a centered popup window.
- Cosmetic change of browsers reports (group by family and add bar in
  browserdetail).
- Other minor cosmetic change (remove ShowHeader parameter).
- Authenticated user field in log file can contain space with LogFormat=1,
  and they are purged of " with Logformat=6 (Lotus Notes/Domino).
- The AWSTATS_CURRENT_CONFIG environment variable is now always defined
  into AWStats environment with value of config (Can be used inside config
  file like other environment variables).
- Added offset of last log line read and a signature of line into the
  history file after the LastLine date.
- Better error report in load of plugins.
Other/Documentation:
- AWSTATS_CONFIG environment variable renamed into AWSTATS_FORCE_CONFIG.
- Replaced -month=year option by -month=all.
- Added an error message if a -migrate is done on an history file with
  wrong file name.
- GeoIP memory cache code is now stored inside plugin code.
- Added list of loaded plugins in AWStats copyright string.
- Added European and Sao Tome And Principe country flag.
- Added Safari browser icon.
- Updated documentation.
Note 1:
  Old deprecated values for -lang option (-lang=0, -lang=1...) has been
  removed. Use -lang=code_language instead (-lang=en, -lang=fr, ...).
Note 2:
  Old deprecated -month=year option must be replaced by -month=all when
  used on command line.

* Tue Feb 11 2003 Igor Muratov <migor@altlinux.ru> 5.3-alt1
- Fixed: Bad documentation for use of ExtraSection.
- Fixed: Bug in ValidSMTPCodes parameter.
- Fixed: Remove AWStats header on left frame if ShowHeader=0.
- Fixed: 29th february 2004 will be correctly handled.
- Fixed: Another try to fix the #include not working correctly.
- Fixed: Columns not aligned in unknownip view when not all fields are
  choosed.
- Fixed: Columns not aligned in allhosts and lasthosts view when not all
  fields are choosed.
- Added awstats_exportlib.pl tool.
- Added 'Full list' view for Domains/Country report.
- Added 'Full list' and 'Last visits' for email senders/receivers chart.
- Added a memory cache for GeoIP plugin resolution (geoip is faster).
- New parameter: Added AuthenticatedUsersNotCaseSensitive.
- Speed increased when ExtraSection is used.
- Updates to AWStats robots, os, browsers, search_engines databases.
- Added awstats_logo3.png
- Added X11 as Unknown Unix OS, and Atari OS.
- Change way of reading -output= parameter to prepare build of several output
  with same running process.
- Updated documentation.

* Mon Dec 16 2002 Igor Muratov <migor@altlinux.ru> 5.2-alt1
- First build for ALT.
- Added urlalias plugin to replace URL values in URL reports by a text.
- Added geoip plugin to track countries from IP location instead of domain
  value.
- Support for postfix mail log.
- Added total and average row at bottom of day data array.
- Added dynamic filter in Host and Referer pages when used as CGI like
  in Url report.
- Removed "Bytes" text when values is 0.
- Reduced main page size.
- New parameter: Added OnlyHosts parameter.
- New parameter: Added ErrorMessages to use a personalized error message.
- New parameter: Added DebugMessages to not allow debug messages.
- New parameter: Added URLQuerySeparators parameter.
- New parameter: Added UseHTTPSLinkForUrl parameter.
- Report for robots accept codes like others charts ('HBL').
- Can use "char+" instead of "char" for LogSeparator.
- Records with bad http code for Microsoft Index Servers (on 1 digit instead
  of 3) are no more reported as corrupted records.
- Little support for IPv6.
- Static string changed from "string" to 'string'.
- Fixed: Fix a bug when using IIS and query or cs-query-string tag in
  LogFormat and URLWithQuery=1.
- Fixed: #include now works correctly.
- Added Albanian, Bulgarian and Welsh language.
- Added Seychelles flag.

