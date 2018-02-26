# Speed-up build process
%define _verify_elf_method skip
%define _strip_method none

%define t3branch 4.5
%define beta %nil

Name: typo3_src
Version: 4.5.16
Release: alt1

Summary: A free, feature rich, Content Management Framework/System
License: GPL
Group: Networking/Other

Url: http://www.typo3.org
Source: %name-%version%beta.tar.gz
Source100: typo3_src.watch
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

AutoReqProv: no

#Requires: php-engine
Requires: typo3-webserver
Requires: ImageMagick
Requires: freetype2

%define installdir %_datadir/%name-%version

%description
TYPO3 is a free Open Source content management system for
enterprise purposes on the web and in intranets. It offers full
flexibility and extendability while featuring an accomplished set
of ready-made interfaces, functions and modules.

To find out more, see http://www.typo3.org | http://www.typo3.ru.

You should install MySQL-server package or care of DBAL
setup yourself.  It's also highly recommended to install some
sort of PHP accelerator, like php-mmcache, php5-eaccelerator
or php5-xcache.

%package -n typo3-apache
Summary: apache 1.3 dependency package
Group: Networking/Other
Provides: typo3-webserver
Requires: apache
Requires: apache-mod_php5
Requires: php5-mysql
Requires: php5-gd2
Requires: php5-curl
Requires: php5-mbstring
Requires: php5-eaccelerator

%description -n typo3-apache
apache 1.3/php 5.x dependency package

%package -n typo3-apache2
Summary: apache 2.x dependency package
Group: Networking/Other
Provides: typo3-webserver
Requires: apache2
Requires: apache2-mod_php5
Requires: php5-mysql
Requires: php5-gd2
Requires: php5-curl
Requires: php5-mbstring
# Recommends: php5-eaccelerator || php5-xcache

%description -n typo3-apache2
apache 2.x/php 5.x dependency package

%prep
%setup -n %name-%version%beta
gzip -9nf ChangeLog

%install
mkdir -p %buildroot%installdir
# no need to copy the engine
mv */ index.php %buildroot%installdir/
ln -s %name-%version %buildroot%_datadir/%name-%t3branch

%files
%installdir/
%_datadir/%name-%t3branch
%doc ChangeLog* *.txt

%files -n typo3-apache
%files -n typo3-apache2

%changelog
* Tue May 22 2012 Michael Shigorin <mike@altlinux.org> 4.5.16-alt1
- 4.5.16: bugfixes, see
  http://wiki.typo3.org/wiki/TYPO3_4.5.16#Changes

* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 4.5.15-alt2
- added watch file (4.5.x series)

* Tue Apr 17 2012 Michael Shigorin <mike@altlinux.org> 4.5.15-alt1
- 4.5.15: security fixes (XSS in exception handler), see
  https://typo3.org/teams/security/security-bulletins/typo3-core/typo3-core-sa-2012-002/

* Wed Mar 28 2012 Michael Shigorin <mike@altlinux.org> 4.5.14-alt1
- 4.5.14: security fixes (information disclosure, XSS), see
  https://typo3.org/teams/security/security-bulletins/typo3-core/typo3-core-sa-2012-001/

* Tue Mar 13 2012 Michael Shigorin <mike@altlinux.org> 4.5.13-alt1
- 4.5.13: bugfixes

* Tue Mar 06 2012 Michael Shigorin <mike@altlinux.org> 4.5.12-alt1
- 4.5.12: bugfixes

* Tue Jan 24 2012 Michael Shigorin <mike@altlinux.org> 4.5.11-alt1
- 4.5.11: bugfixes

* Tue Dec 20 2011 Michael Shigorin <mike@altlinux.org> 4.5.10-alt1
- 4.5.10: regression fixes (custom CSS in backend RTE), see
  http://wiki.typo3.org/index.php/TYPO3_4.5.10

* Fri Dec 16 2011 Michael Shigorin <mike@altlinux.org> 4.5.9-alt1
- 4.5.9: critical security fix (remote code exec possible), see
  https://typo3.org/teams/security/security-bulletins/typo3-core/typo3-core-sa-2011-004/

* Fri Nov 25 2011 Michael Shigorin <mike@altlinux.org> 4.5.8-alt1
- 4.5.8: bugfixes
- 4.5.7: bugfixes
  + and a security fix which is only exploiteable by admins

* Wed Sep 14 2011 Michael Shigorin <mike@altlinux.org> 4.5.6-alt1
- 4.5.6: medium security fixes (potential SQL injection), see
  http://typo3.org/teams/security/security-bulletins/typo3-core/typo3-core-sa-2011-002/
  http://typo3.org/teams/security/security-bulletins/typo3-core/typo3-core-sa-2011-003/
  + thanks Yuri Bushmelev for even quicker heads-up

* Tue Aug 16 2011 Michael Shigorin <mike@altlinux.org> 4.5.5-alt1
- 4.5.5: bugfixes for 4.5.4 regression fixes, see
  http://wiki.typo3.org/wiki/TYPO3_4.5.5

* Fri Aug 05 2011 Michael Shigorin <mike@altlinux.org> 4.5.4-alt1
- 4.5.4: major security fixes, see
  http://typo3.org/teams/security/security-bulletins/typo3-core/typo3-core-sa-2011-001/
  + XSS in frontend (can be mitigated with realurl)
  + information disclosure in css_styled_content (headlines)
  + unserialize() vulnerability in backend
  + missing access control in backend (ExtDirect)
  + several more mid/low-severity problems

* Tue May 24 2011 Michael Shigorin <mike@altlinux.org> 4.5.3-alt1
- 4.5.3: bugfixes, see http://wiki.typo3.org/wiki/TYPO3_4.5.3
  + NB: typo3_dummy is no longer maintained

* Sat Feb 26 2011 Michael Shigorin <mike@altlinux.org> 4.5.2-alt1
- 4.5.2: bugfixes (including 4.5.1 regression fixes), see
  http://wiki.typo3.org/TYPO3_4.5.2

* Wed Feb 23 2011 Michael Shigorin <mike@altlinux.org> 4.5.1-alt1
- 4.5.1: bugfixes, see http://wiki.typo3.org/TYPO3_4.5.1

* Wed Jan 26 2011 Michael Shigorin <mike@altlinux.org> 4.5.0-alt1
- 4.5.0

* Tue Dec 28 2010 Michael Shigorin <mike@altlinux.org> 4.3.10-alt1
- 4.3.10: regression fixes, see
  http://wiki.typo3.org/wiki/TYPO3_4.3.10

* Thu Dec 16 2010 Michael Shigorin <mike@altlinux.org> 4.3.9-alt1
- 4.3.9: major security fixes, see
  http://typo3.org/teams/security/security-bulletins/typo3-sa-2010-022/
  + XSS in click-enlarge FE functionality if caching is enabled
  + arbitrary code execution due to insufficient input validation
    in PHP file inclusion protection API
  + a few more less severe problems, see the link above

* Tue Oct 12 2010 Michael Shigorin <mike@altlinux.org> 4.3.8-alt1
- 4.3.8: a regression fix, see
  http://wiki.typo3.org/wiki/TYPO3_4.3.8

* Wed Oct 06 2010 Michael Shigorin <mike@altlinux.org> 4.3.7-alt1
- 4.3.7: critical security fixes, see
  http://typo3.org/teams/security/security-bulletins/typo3-sa-2010-020/
  + remote file disclosure (no auth required)
  + several XSS in backend (valid backend login required)
  + remote file disclosure in EM (valid backend admin login required)
  + privilege escalation possible for backend user having permission
    to create other backend users due to improper user input validation
  + DoS with php crash in t3lib_div::validEmail()
  + XSS protection incomplete in RemoveXSS()

* Tue Sep 28 2010 Michael Shigorin <mike@altlinux.org> 4.3.6-alt1
- 4.3.6: bugfixes, see http://wiki.typo3.org/wiki/TYPO3_4.3.6

* Fri Aug 06 2010 Michael Shigorin <mike@altlinux.org> 4.3.5-alt1
- 4.3.5: regression fixes, see also:
  + http://news.typo3.org/news/article/regressions-in-latest-security-release/
  + http://wiki.typo3.org/index.php/TYPO3_4.3.5

* Sun Aug 01 2010 Michael Shigorin <mike@altlinux.org> 4.3.4-alt1
- 4.3.4: major/medium security fixes:
  + several XSS in backend (valid backend login required)
  + open redirection in backend (valid backend login required)
  + SQL injection in some backend record editing forms
    (special backend login/configuration required)
  + arbitrary code execution depending on server configuration
    (valid backend login required to upload .phtml)
  + webroot path disclosure possible with defective extensions
  + Extension Manager: XSS and arbitrary file access
    (valid backend admin login required)
  + user auth, "forgot password": PHP insecure randomness
  + form content element data check failure (spam abuse)
  + header injection with jumpurl feature
  + frontend login box: open redirection, XSS
  + install tool: session fixation
  + extbase XSS possible with FLUID Templating Engine
  + t3lib_htmlmail includes the exact CMS version in headers

* Tue Feb 23 2010 Michael Shigorin <mike@altlinux.org> 4.3.2-alt1
- 4.3.2: major/medium security fixes (no CVE so far)
  + frontend login: possible auth bypass using a hash
    *if* "saltedpasswords" is enabled
    *and* several auth services are configured
  + frontend: possible CSS if running on php-cgi
  + backend: possible XSSes (valid backend login required)
  + backend: information disclosure with specific
    sys_action setup (valid backend login required)
  + https://typo3.org/teams/security/security-bulletins/typo3-sa-2010-004/

* Thu Jan 14 2010 Michael Shigorin <mike@altlinux.org> 4.3.1-alt1
- 4.3.1: major security fix for "openid" system extension
  (possible backend user authentication bypass if it's enabled):
  http://typo3.org/teams/security/security-bulletins/typo3-sa-2010-001/

* Sun Dec 13 2009 Michael Shigorin <mike@altlinux.org> 4.3.0-alt2
- gzip ChangeLog (repocop)

* Mon Nov 30 2009 Michael Shigorin <mike@altlinux.org> 4.3.0-alt1
- 4.3.0: new and improved series, see also
  https://typo3.org/download/release-notes/typo3-43/
- %_datadir/%name-$major.$minor symlink to ease deployment
  and upgrade throughout patchlevel series

* Sun Oct 25 2009 Michael Shigorin <mike@altlinux.org> 4.2.10-alt1
- 4.2.10: multiple vulnerabilities in TYPO3 core:
  http://typo3.org/teams/security/security-bulletins/typo3-sa-2009-016/

* Mon Sep 28 2009 Michael Shigorin <mike@altlinux.org> 4.2.9-alt1
- 4.2.9: current bugfixes

* Sat Jul 04 2009 Michael Shigorin <mike@altlinux.org> 4.2.8-alt1
- 4.2.8: maintenance release (bugfixes and minor security improvements)
  + 4.2.7 contained a glitch so was effectively skipped

* Tue Feb 10 2009 Michael Shigorin <mike@altlinux.org> 4.2.6-alt1
- 4.2.6: [critical] information disclosure and XSS fixes:
  http://typo3.org/teams/security/security-bulletins/typo3-sa-2009-002/

* Tue Jan 20 2009 Michael Shigorin <mike@altlinux.org> 4.2.4-alt1
- 4.2.4: multiple important security fixes in TYPO3 core:
  http://typo3.org/teams/security/security-bulletins/typo3-sa-2009-001/

* Thu Nov 13 2008 Michael Shigorin <mike@altlinux.org> 4.2.3-alt1
- 4.2.3: fixes for two XSS issues in TYPO3 core
  + "file" backend module:
    http://typo3.org/teams/security/security-bulletins/typo3-20081113-1/
  + "felogin" sysext:
    http://typo3.org/teams/security/security-bulletins/typo3-20081113-2/

* Sat Oct 18 2008 Michael Shigorin <mike@altlinux.org> 4.2.2-alt1
- 4.2.2: current bugfixes/updates

* Wed Jun 11 2008 Michael Shigorin <mike@altlinux.org> 4.2.1-alt1
- 4.2.1: security fixes:
  + default fileDenyPattern update to bar .htaccess uploads
    (backend/frontend users might be able to execute arbitrary
    code depending on some conditions);
  + fixed fe_adminlib.inc XSS issue (used in direct_mail_subscription,
    feuser_admin, kb_md5fepw)
  + for more information and a workaround, see
    http://typo3.org/teams/security/security-bulletins/typo3-20080611-1/

* Wed Apr 23 2008 Michael Shigorin <mike@altlinux.org> 4.2.0-alt1
- 4.2.0

* Sat Apr 19 2008 Michael Shigorin <mike@altlinux.org> 4.2.0-alt0.2
- 4.2.0RC2: php5 required

* Tue Mar 04 2008 Michael Shigorin <mike@altlinux.org> 4.1.6-alt1
- 4.1.6: minor bugfixes (including windows-only)

* Sun Mar 02 2008 Michael Shigorin <mike@altlinux.org> 4.1.5-alt3
- moved apache/php-version dependent requires into subpackages
  + NB: I only care for typo3-apache right now, please correct
    me on typo3-apache2 if something's wrong
  + 4.2 will be php5 only, so -apache will go php5 too
    (I'm just too lazy at the moment)

* Tue Jan 01 2008 Michael Shigorin <mike@altlinux.org> 4.1.5-alt2
- fix requires by moving back to php4: maybe it's some local
  problem but both php 5.2.2/5.2.3 builds are severely broken
  for me (would randomly bail out on different require_once 
  calls with comparable php.ini)

* Mon Dec 31 2007 Michael Shigorin <mike@altlinux.org> 4.1.5-alt1
- 4.1.5: minor bugfix (for regression introduced in 4.1.4)
- 4.1.4: minor security fixes
- 4.1.3: lots of bugfixes

* Tue Jul 17 2007 Michael Shigorin <mike@altlinux.org> 4.1.2-alt1
- 4.1.2 (minor bugfixes)
- minor spec cleanup

* Tue Jun 05 2007 Michael Shigorin <mike@altlinux.org> 4.1.1-alt1
- built for ALT Linux
- partially based on seiroswiki.spec (0.0.1-alt4) by vvk@ 
  and typo3.spec.m4 (3.6.2-0.6) by Dimitri Tarassenko <mitka mitka us>
- for now, rather hardwired for apache+mod_php
