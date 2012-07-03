%define packagename eGroupWare
%define egwdirname egroupware
%define egwversion 1.8
%define httpdconfd %_sysconfdir/httpd2/conf/addon.d
%define php php5

Name: eGroupWare
Version: %egwversion
Release: alt4
Epoch: 1
Summary: eGroupWare is a web-based groupware suite written in php
Summary(ru_RU.UTF-8): eGroupWare - это сервер групповой работы, написанный на php

Group: Networking/WWW
License: GPL/LGPL
Url: http://www.egroupware.org/
Source: %packagename-%egwversion.tar
Source1: %packagename-addressbook-%egwversion.tar
Source2: %packagename-admin-%egwversion.tar
Source3: %packagename-bookmarks-%egwversion.tar
Source4: %packagename-calendar-%egwversion.tar
Source5: %packagename-developer_tools-%egwversion.tar
Source6: %packagename-egw-pear-%egwversion.tar
Source7: %packagename-emailadmin-%egwversion.tar
Source8: %packagename-etemplate-%egwversion.tar
Source9: %packagename-felamimail-%egwversion.tar
Source10: %packagename-importexport-%egwversion.tar
Source11: %packagename-infolog-%egwversion.tar
Source12: %packagename-manual-%egwversion.tar
Source13: %packagename-news_admin-%egwversion.tar
Source14: %packagename-notifications-%egwversion.tar
Source15: %packagename-phpbrain-%egwversion.tar
Source16: %packagename-phpgwapi-%egwversion.tar
Source17: %packagename-phpsysinfo-%egwversion.tar
Source18: %packagename-polls-%egwversion.tar
Source19: %packagename-preferences-%egwversion.tar
Source20: %packagename-projectmanager-%egwversion.tar
Source21: %packagename-registration-%egwversion.tar
Source22: %packagename-resources-%egwversion.tar
Source23: %packagename-sambaadmin-%egwversion.tar
Source24: %packagename-setup-%egwversion.tar
Source25: %packagename-sitemgr-%egwversion.tar
Source26: %packagename-syncml-%egwversion.tar
Source27: %packagename-timesheet-%egwversion.tar
Source28: %packagename-tracker-%egwversion.tar
Source29: %packagename-wiki-%egwversion.tar
Source30: %packagename-filemanager-%egwversion.tar
Source32: %packagename-icalsrv-%egwversion.tar
Source33: %packagename-mydms-%egwversion.tar
Source34: %packagename-workflow-%egwversion.tar
Source73: %packagename-gallery-%egwversion.tar
Source80: egroupware_alt.tar
Source90: README.ALT

BuildRequires: perl-Text-Iconv perl-CGI perl-String-CRC32 perl-DBI
Requires: apache2-httpd-prefork apache2
Requires: php-engine %php-libs %php-mysql %php-pdo_mysql %php-ldap %php-mbstring %php-imap %php-gd2 rpm-build-pear pear-core pear-Auth_SASL %php-xmlrpc %php-dom apache2-mod_php5
Requires: %packagename-egw-pear = %epoch:%egwversion-%release %packagename-core = %epoch:%egwversion-%release %packagename-emailadmin = %epoch:%egwversion-%release %packagename-addressbook = %epoch:%egwversion-%release %packagename-felamimail = %epoch:%egwversion-%release

%add_findreq_skiplist /usr/share/egroupware/doc/rpm-build/build-egw-rpms.sh

BuildArch: noarch
Packager: Aleksey Avdeev <solo@altlinux.ru>

%description
eGroupWare is a web-based groupware suite written in PHP.

This package provides the eGroupWare default applications:

egroupware core with: admin, api, docs, etemplate, prefereces and setup,
addressbook, bookmarks, calendar, translation-tools, emailadmin, felamimail,
filemanager, infolog, manual, mydms, news admin, knowledgebase, polls,
projectmanager, resources, sambaadmin, sitemgr, syncml, timesheet, tracker, wiki

It also provides an API for developing additional applications.

Further contributed applications are avalible in single packages.

%description -l ru_RU.UTF-8
eGroupWare - это свободное, готовое к использованию в компаниях, 
групповое программное обеспечение для вашей сети. 
Оно позволит вам управлять контактами, назначенными встречами, 
задачами и многим другим для всей вашей работы.

eGroupWare - это сервер групповой работы. Он укомплектован собственным веб-интерфейсом, 
который обеспечивает доступ к вашим данным с любой платформы по всей планете. 
Более того, вы также можете выбрать для доступа к серверу eGroupWare свой любимый клиент 
групповой работы (Kontact, Evolution, Outlook) и даже мобильный телефон или КПК посредством SyncML.

%package core
Summary: The eGroupWare contrib package
Group: Networking/WWW
Provides: %packagename-core
Requires: %packagename = %epoch:%egwversion-%release
%description core
This package provides the eGroupWare contrib applications.
%post core

%package addressbook
Version: %egwversion
Summary: The eGroupWare addressbook application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release
Provides: %packagename-addressbook
%description addressbook
Contact manager with Vcard support.
addressbook is the egroupware default contact application.
It makes use of the egroupware contacts class to store and retrieve
contact information via SQL, LDAP or Active Directory.

%package bookmarks
Version: %egwversion
Summary: The eGroupWare bookmarks application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release
%description bookmarks
Manage your bookmarks with eGroupWare. Has Netscape plugin.

%package calendar
Version: %egwversion
Summary: The eGroupWare calendar application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release
%description calendar
Powerful calendar with meeting request system, Alarms, ICal and E-Mail support,
and ACL security.

%package developer_tools
Version: %egwversion
Summary: The eGroupWare developer_tools application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release
%description developer_tools
The TranslationTools allow to create and extend translations-files for eGroupWare.
They can search the sources for new / added phrases and show you the ones missing in your language.

%package egw-pear
Version: %egwversion
Summary: The eGroupWare egw-pear application
Group: Networking/WWW
Requires: pear-core
Requires: %packagename-core = %epoch:%egwversion-%release
%description egw-pear
egw-pear contains the pear classes modified to work with eGroupWare

%package emailadmin
Version: %egwversion
Summary: The eGroupWare emailadmin application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release, %packagename-egw-pear = %epoch:%egwversion-%release, %php-openssl
%description emailadmin
EmailAdmin allow to maintain User email accounts

%package felamimail
Version: %egwversion
Summary: The eGroupWare felamimail application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release, %packagename-emailadmin = %epoch:%egwversion-%release, %packagename-egw-pear = %epoch:%egwversion-%release
%description felamimail
The Email application for eGroupWare.

%package filemanager
Version: %egwversion
Summary: The eGroupWare filemanager application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release, %packagename-egw-pear = %epoch:%egwversion-%release
%description filemanager
This is the filemanager app for eGroupWare.

%package gallery
Version: %egwversion
Summary: The eGroupWare gallery application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release, %packagename-egw-pear = %epoch:%egwversion-%release
%description gallery
An embedded Gallery2 for eGroupWare.

%package icalsrv
Version: %egwversion
Summary: The eGroupWare icalsrv application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release
%description icalsrv
This is the icalsrv app for eGroupWare.

%package infolog
Version: %egwversion
Summary: The eGroupWare infolog application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release
%description infolog
This is the infolog app for eGroupWare (Notes, ToDo, Phonelogs, CRM).

%package importexport
Version: %egwversion
Summary: The eGroupWare importexport application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release
%description importexport
This is the importexport app for eGroupWare. It includes a comandline client.

%package manual
Version: %egwversion
Summary: The eGroupWare manual application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release
%description manual
This is the manual app for eGroupWare: online help system.

%package mydms
Version: %egwversion
Summary: The eGroupWare mydms application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release, %packagename-egw-pear = %epoch:%egwversion-%release
%description mydms
This is a mydms port to eGroupWare.

%package news_admin
Version: %egwversion
Summary: The eGroupWare news_admin application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release, pear-XML_Feed_Parser
%description news_admin
This is the news_admin app for eGroupWare.

%package notifications
Version: %egwversion
Summary: The eGroupWare notifications application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release
%description notifications
This is the notifications app for eGroupWare.

%package phpbrain
Version: %egwversion
Summary: The eGroupWare phpbrain application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release, %packagename-addressbook = %epoch:%egwversion-%release
%description phpbrain
This is the phpbrain app for eGroupWare.

%package phpsysinfo
Version: %egwversion
Summary: The eGroupWare phpsysinfo application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release
%description phpsysinfo
This is the phpsysinfo app for eGroupWare.

%package polls
Version: %egwversion
Summary: The eGroupWare polls application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release
%description polls
This is the polls app for eGroupWare.

%package projectmanager
Version: %egwversion
Summary: The eGroupWare projectmanager application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release
Requires: fonts-ttf-vera
Requires: fonts-ttf-dejavu
Requires: /usr/share/php/modules/jpgraph
%description projectmanager
The projectmanager is eGroupWare's new project management application.
It's fully integrated into eGroupWare and use the data of InfoLog and Calendar.
Plugable datasources allow to support and manage further applications.

%package registration
Version: %egwversion
Summary: The eGroupWare registration application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release
%description registration
This is the registration app for eGroupWare.

%package resources
Version: %egwversion
Summary: The eGroupWare resources application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release
%description resources
resources is a resource booking sysmtem for eGroupWare.
Which integrates into the calendar.

%package sambaadmin
Version: %egwversion
Summary: The eGroupWare sambaadmin application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release
%description sambaadmin
Manage LDAP based sambaacounts and workstations.

%package sitemgr
Version: %egwversion
Summary: The eGroupWare Sitemanager CMS application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release
%description sitemgr
This is the Sitemanager CMS app for eGroupWare.

%package syncml
Version: %egwversion
Summary: The eGroupWare syncml application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release, %php >= 5.0.0
%description syncml
This is the syncml app for eGroupWare.

%package timesheet
Version: %egwversion
Summary: The eGroupWare timesheet application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release
%description timesheet
Simple timesheet application, which allow to record and report
the times and other expenses. It can be uses as well standalone
as together with the ProjectManager application.

%package tracker
Version: %egwversion
Summary: The eGroupWare trouble ticket system application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release
Requires: %packagename-notifications = %epoch:%egwversion-%release
%description tracker
This is the trouble ticket system app for eGroupWare.

%package wiki
Version: %egwversion
Summary: The eGroupWare wiki application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release
%description wiki
This is the wiki app for eGroupWare.

%package workflow
Version: %egwversion
Summary: The eGroupWare wiki application
Group: Networking/WWW
Requires: %packagename-core = %epoch:%egwversion-%release
%description workflow
This is the workflow app for eGroupWare.
This was first a port from Galaxia workflow, a project from the TikiWiki group.

%prep
%setup -c -n %egwdirname
%setup -T -D -a 1 -n %egwdirname/egroupware
%setup -T -D -a 2 -n %egwdirname/egroupware
%setup -T -D -a 3 -n %egwdirname/egroupware
%setup -T -D -a 4 -n %egwdirname/egroupware
%setup -T -D -a 5 -n %egwdirname/egroupware
%setup -T -D -a 6 -n %egwdirname/egroupware
%setup -T -D -a 7 -n %egwdirname/egroupware
%setup -T -D -a 8 -n %egwdirname/egroupware
%setup -T -D -a 9 -n %egwdirname/egroupware
%setup -T -D -a 10 -n %egwdirname/egroupware
%setup -T -D -a 11 -n %egwdirname/egroupware
%setup -T -D -a 12 -n %egwdirname/egroupware
%setup -T -D -a 13 -n %egwdirname/egroupware
%setup -T -D -a 14 -n %egwdirname/egroupware
%setup -T -D -a 15 -n %egwdirname/egroupware
%setup -T -D -a 16 -n %egwdirname/egroupware
%setup -T -D -a 17 -n %egwdirname/egroupware
%setup -T -D -a 18 -n %egwdirname/egroupware
%setup -T -D -a 19 -n %egwdirname/egroupware
%setup -T -D -a 20 -n %egwdirname/egroupware
%setup -T -D -a 21 -n %egwdirname/egroupware
%setup -T -D -a 22 -n %egwdirname/egroupware
%setup -T -D -a 23 -n %egwdirname/egroupware
%setup -T -D -a 24 -n %egwdirname/egroupware
%setup -T -D -a 25 -n %egwdirname/egroupware
%setup -T -D -a 26 -n %egwdirname/egroupware
%setup -T -D -a 27 -n %egwdirname/egroupware
%setup -T -D -a 28 -n %egwdirname/egroupware
%setup -T -D -a 29 -n %egwdirname/egroupware
%setup -T -D -a 30 -n %egwdirname/egroupware
%setup -T -D -a 32 -n %egwdirname/egroupware
%setup -T -D -a 33 -n %egwdirname/egroupware
%setup -T -D -a 34 -n %egwdirname/egroupware
%setup -T -D -a 73 -n %egwdirname
%setup -T -D -a 80 -n %egwdirname

%build
%install
mkdir -p %buildroot%_datadir/%egwdirname
cp -aRf  etc var %buildroot
cp -aRf egroupware/* %buildroot%_datadir/%egwdirname
install -p -m 644 %SOURCE90 README.ALT
rm -f %buildroot%_datadir/%egwdirname/.htaccess

find %buildroot%_datadir/%egwdirname -name .svn | xargs rm -rf
find %buildroot%_datadir/%egwdirname -type f -name "Thumbs.db" -print | xargs /bin/rm -f
find %buildroot%_datadir/%egwdirname -type f -name "*.swp" -print | xargs /bin/rm -f

chmod +x %buildroot%_datadir/%egwdirname/*/*cli.php %buildroot%_datadir/%egwdirname/phpgwapi/cron/*.php

cd %buildroot%_datadir/%egwdirname
ln -s ../../../var/lib/egroupware/header.inc.php

%post
pear install --nodeps -s --force --register-only /usr/share/php/pear/.pkgxml/Auth_SASL.xml >/dev/null || :

%files
%doc README.ALT

%files core
%dir %_datadir/%egwdirname
%dir /var/lib/egroupware
%_datadir/%egwdirname/*.php
%_datadir/%egwdirname/*.template
%_datadir/%egwdirname/*.htaccess
%_datadir/%egwdirname/admin
%_datadir/%egwdirname/doc
%_datadir/%egwdirname/etemplate
%_datadir/%egwdirname/home
%_datadir/%egwdirname/phpgwapi
%_datadir/%egwdirname/preferences
%_datadir/%egwdirname/setup
%_sysconfdir/cron.d/egroupware
%config %attr(0644,root,root) %httpdconfd/A.egroupware.conf
%dir %attr(0755,apache2,apache2) /var/lib/egroupware/default
%dir %attr(0755,apache2,apache2) /var/lib/egroupware/default/files
%dir %attr(0755,apache2,apache2) /var/lib/egroupware/default/backup
#%%dir %attr(0755,apache2,apache2) /var/lib/egroupware/sessions
%config %attr(0640,apache2,apache2) /var/lib/egroupware/header.inc.php

%files addressbook
%_datadir/%egwdirname/addressbook
%files calendar
%_datadir/%egwdirname/calendar
%files developer_tools
%_datadir/%egwdirname/developer_tools
%files egw-pear
%_datadir/%egwdirname/egw-pear
%files emailadmin
%_datadir/%egwdirname/emailadmin
%files felamimail
%_datadir/%egwdirname/felamimail
%files filemanager
%_datadir/%egwdirname/filemanager
%files gallery
%_datadir/%egwdirname/gallery
%files icalsrv
%_datadir/%egwdirname/icalsrv
%files infolog
%_datadir/%egwdirname/infolog
%files importexport
%_datadir/%egwdirname/importexport
%files bookmarks
%_datadir/%egwdirname/bookmarks
%files syncml
%_datadir/%egwdirname/syncml
%files manual
%_datadir/%egwdirname/manual
%files mydms
%_datadir/%egwdirname/mydms
%files news_admin
%_datadir/%egwdirname/news_admin
%files notifications
%_datadir/%egwdirname/notifications
%files phpbrain
%_datadir/%egwdirname/phpbrain
%files phpsysinfo
%_datadir/%egwdirname/phpsysinfo
%files polls
%_datadir/%egwdirname/polls
%files projectmanager
%_datadir/%egwdirname/projectmanager
%files registration
%_datadir/%egwdirname/registration
%files resources
%_datadir/%egwdirname/resources
%files sambaadmin
%_datadir/%egwdirname/sambaadmin
%files sitemgr
%_datadir/%egwdirname/sitemgr
%files timesheet
%_datadir/%egwdirname/timesheet
%files tracker
%_datadir/%egwdirname/tracker
%files wiki
%_datadir/%egwdirname/wiki
%files workflow
%_datadir/%egwdirname/workflow

%changelog
* Wed Jun 13 2012 Pavel Isopenko <pauli@altlinux.org> 1:1.8-alt4
- Update to 1.8.004.20120515

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:1.8-alt3.1
- Rebuild with Python-2.7

* Sat May 07 2011 Aleksey Avdeev <solo@altlinux.ru> 1:1.8-alt3
- Update to 1.8.001.20110421
- Update projectmanager:
  + DejaVu fonts use
  + fix jpgraph use
- Updating workflow for %%name-1.8

* Tue Apr 05 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 1:1.8-alt2
- Remove fonts from eGroupWare-projectmanager (ALT#25323)

* Fri Feb 25 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 1:1.8-alt1
- Update to 1.8.001.20110216 (ALT#24933)
- Minimal testing! Need maintainer!

* Sat Jul 24 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 1:1.6-alt8
- Added patch class.phpmailer.inc.php.patch (ALT #23218)

* Tue Mar 16 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 1:1.6-alt7
- EGroupware 1.6.003 security and bugfix release
  +  implements SyncML 1.2 support and many SyncML fixes
  +  fix cross-site scripting (XSS)
  +  fix serious remote command execution

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.6-alt6.002.1
- Rebuilt with python 2.6

* Tue Jul 21 2009 gray_graff <gray_graff@altlinux.org> 1:1.6-alt6.002
- EGroupware 1.6.002 security and bugfix release
  +  FCKeditor (remote file upload)
  +  Tracker (XSS problem)
  +  Knowledgebase (SQL injection)
  +  Added HTML Purifier as preventive measure for FCKeditor content

* Tue May 12 2009 gray_graff <gray_graff@altlinux.org> 1:1.6-alt5.001
- Add README.ALT
- Fix Requires (Addressbook must be installed for setup)
- Fix Requires (Notifications need for Tracker)
- Fix bug whis not working php value "mbstring.func_overload"
- Added patch wizard.scrolling_sidebox.patch for pERP
- Added patch class.asyncservice.inc.php.patch (fix crontab)
- Fix Requires (Felamimail need for crontab)

* Mon Apr 27 2009 gray_graff <gray_graff@altlinux.org> 1:1.6-alt4.001
- Update to revision 26892.
- Update translations (ALT #19601, #19604)
- Remove class.uiasyncservice.inc.php.patch

* Tue Mar 31 2009 gray_graff <gray_graff@altlinux.org> 1:1.6-alt3.001
- Update to revision 26706.

* Fri Feb 13 2009 gray_graff <gray_graff@altlinux.org> 1:1.6-alt2.001
- 1:1.6-alt2.001
- Update to revision 26549.

* Thu Nov 27 2008 gray_graff <gray_graff@altlinux.org> 1:1.6-alt1.001
- 1.6 final release
- switch svn from trunk to 1.6 branch

* Wed Nov 19 2008 gray_graff <gray_graff@altlinux.org> 1.6.rc5-alt1
- 1.6.rc5 (revision 26404)

* Wed Nov 12 2008 gray_graff <gray_graff@altlinux.org> 1.6.rc4-alt1
- 1.6.rc4 (revision 26330)

* Thu Oct 30 2008 gray_graff <gray_graff@altlinux.org> 1.6.rc3-alt1
- 1.6.rc3 (revision 26293)
- Update dummy header.inc.php (from upstream)
- Change session.save_path to apache default
- Change open_basedir (add path to php pear)
- Add requred for setup emailadmin
- Spec cleanup

* Thu Oct 23 2008 gray_graff <gray_graff@altlinux.org> 1.6.rc2-alt1
- 1.6.rc2
- Update Requires. added php5-dom
- Update Requires in news_admin (close #17564)
- Added module workflow

* Tue Oct 14 2008 gray_graff <gray_graff@altlinux.org> 1.6.rc1-alt1
- 1.6.rc1

* Thu Oct 09 2008 gray_graff <gray_graff@altlinux.org> 1.6.pre1-alt3.1
- Update to SVN revision 26109

* Tue Oct 07 2008 gray_graff <gray_graff@altlinux.org> 1.6.pre1-alt3
- Update to SVN r26042 (2008-10-05)

* Wed Aug 20 2008 gray_graff <gray_graff@altlinux.org> 1.6.pre1-alt2
- Update to latest cvs
- Support for Russian filenames in Attachments from 1.4
- Update russian in Felamimail
- Update Requires. add php5-pdo_mysql
- Fix asyncservices (cron)

* Mon Aug 18 2008 gray_graff <gray_graff@altlinux.org> 1.6.pre1-alt1
- 1.6.pre1

* Tue Jul 29 2008 gray_graff <gray_graff@altlinux.org> 1.4.004-alt3
- Fix Packager email in spec
- Fix Repocop warnings. "backup-file-in-package" and "windows-thumbnail-database-in-package"
- Support for Russian filenames in Attachments
- Add russian translate for Tracker
- Update russian in Felamimail

* Thu Jun 19 2008 gray_graff <gray_graff@altlinux.org> 1.4.004-alt2
- Fix Requires

* Tue Jun 17 2008 gray_graff <gray_graff@altlinux.org> 1.4.004-alt1
- Initial build
