%define _altdata_dir %_datadir/alterator

Name: alterator-users
Version: 10.5
Release: alt1

Source:%name-%version.tar

Packager: Stanislav Ievlev <inger@altlinux.org>

Summary: alterator module for system users administration
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
Requires: alterator >= 4.10-alt5 alterator-sh-functions >= 0.12-alt1
Requires: shadow-groups, coreutils, passwdqc-utils
Conflicts: alterator-fbi < 5.16-alt1
Conflicts: alterator-lookout < 2.1-alt1

Provides: alterator-backend-local_users = %version
Obsoletes: alterator-backend-local_users

BuildPreReq: alterator >= 4.10-alt5

%description
alterator module for system users administration

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/
%_alterator_backend3dir/*

%changelog
* Wed Nov 25 2009 Stanislav Ievlev <inger@altlinux.org> 10.5-alt1
- use alterator_export_proc
- fix field cleanup (update for current behaviour of form-update-value-list())
- replace obsolete woo-throw with woo-error call


* Thu Nov 12 2009 Stanislav Ievlev <inger@altlinux.org> 10.4-alt1
- use alterator_export_var

* Wed Sep 02 2009 Stanislav Ievlev <inger@altlinux.org> 10.3-alt3
- fix name of widget (closes: #21338)

* Tue Aug 11 2009 Stanislav Ievlev <inger@altlinux.org> 10.3-alt2
- add support of $ALTERATOR_DESTDIR variable (stanv@)

* Mon Aug 10 2009 Alexey I. Froloff <raorn@altlinux.org> 10.3-alt1
- also fill GECOS un /users/add

* Tue May 19 2009 Stanislav Ievlev <inger@altlinux.org> 10.2-alt1
- share callbacks between interfaces

* Thu Apr 30 2009 Stanislav Ievlev <inger@altlinux.org> 10.1-alt1
- use nameref attribute
- fix web UI for IE and Konqueror

* Fri Apr 24 2009 Stanislav Ievlev <inger@altlinux.org> 10.0-alt1
- port to new form library

* Wed Jan 28 2009 Vladislav Zavjalov <slazav@altlinux.org> 9.4-alt2
- fix backend: add returns after password setting errors

* Wed Jan 28 2009 Vladislav Zavjalov <slazav@altlinux.org> 9.4-alt1
- revert LDAP-support (reverted changes will be moved to alterator-ldap-users)
- move help and translations to alterator-l10n

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 9.2-alt5
- use help from new l10n

* Tue Dec 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 9.2-alt4
- update ru help (by azol@)

* Mon Sep 29 2008 Stanislav Ievlev <inger@altlinux.org> 9.2-alt3
- use general system-account-name type

* Mon Sep 22 2008 Stanislav Ievlev <inger@altlinux.org> 9.2-alt1.2
- rename label in html interface too

* Mon Sep 22 2008 Stanislav Ievlev <inger@altlinux.org> 9.2-alt1.1
- hotfix

* Mon Sep 22 2008 Stanislav Ievlev <inger@altlinux.org> 9.2-alt1
- replace constraints with types
- fix label for allow_su option

* Thu Aug 07 2008 Stanislav Ievlev <inger@altlinux.org> 9.1-alt3
- fix user creation
- remove h1

* Thu Jul 24 2008 Stanislav Ievlev <inger@altlinux.org> 9.1-alt2
- users backend: action new - check password before useradd

* Wed Jun 25 2008 Stanislav Ievlev <inger@altlinux.org> 9.1-alt1
- use module.mak
- use effectShow instead of special passwordbox

* Tue Jun 24 2008 Stanislav Ievlev <inger@altlinux.org> 9.0-alt3
- /users/add -- for installer only

* Thu May 29 2008 Stanislav Ievlev <inger@altlinux.org> 9.0-alt2
- fix work with latest alterator-sh-functions
- remove pot-file

* Mon May 26 2008 Stanislav Ievlev <inger@altlinux.org> 9.0-alt1
- process local users only
- use enumref, write_bool_param, write_string_param
- don't use implicit attributes in qt ui

* Fri May 23 2008 Stanislav Ievlev <inger@altlinux.org> 8.2-alt7
- remove autoinstall backend usage
- remove po files

* Thu Apr 17 2008 Stanislav Ievlev <inger@altlinux.org> 8.2-alt6
- join to common dictionary project

* Thu Apr 17 2008 Stanislav Ievlev <inger@altlinux.org> 8.2-alt5
- little ui improvements

* Tue Apr 15 2008 Stanislav Ievlev <inger@altlinux.org> 8.2-alt4
- remove orphaned uris
- fix form layout according HIG
- remove html-messages.mak

* Thu Apr 03 2008 Stanislav Ievlev <inger@altlinux.org> 8.2-alt3
- little ui improvements

* Thu Mar 27 2008 Stanislav Ievlev <inger@altlinux.org> 8.2-alt2
- resurrect behaviour /users/add in installer (allow to skip step)

* Tue Mar 25 2008 Stanislav Ievlev <inger@altlinux.org> 8.2-alt1
- remove backend2 (second level backend)
- index: new ui (HTML and QT)
- user-add: new ui, edit in focus by default

* Mon Mar 24 2008 Stanislav Ievlev <inger@altlinux.org> 8.1-alt4
- update design uris

* Thu Mar 20 2008 Vladislav Zavjalov <slazav@altlinux.org> 8.1-alt3
- fix bug with shell check

* Wed Mar 19 2008 Vladislav Zavjalov <slazav@altlinux.org> 8.1-alt2
- check existance of shell programs in backend

* Wed Mar 05 2008 Stanislav Ievlev <inger@altlinux.org> 8.1-alt1
- remove template-*

* Mon Feb 04 2008 Stanislav Ievlev <inger@altlinux.org> 8.0-alt2
- sync widget size of /users/add with /root

* Wed Jan 23 2008 Stanislav Ievlev <inger@altlinux.org> 8.0-alt1
- move to new help subsystem
- move system administrator stuff into separate package

* Thu Nov 29 2007 Stanislav Ievlev <inger@altlinux.org> 7.3-alt4
- allow to skip step if some user already exists
- add ability to read default groups from template file
  (/etc/alterator/default-groups or /usr/share/install3/default-groups)

* Thu Sep 20 2007 Stanislav Ievlev <inger@altlinux.org> 7.3-alt3
- fix group creation

* Tue Sep 04 2007 Stanislav Ievlev <inger@altlinux.org> 7.3-alt2
- fix translation

* Wed Aug 15 2007 Stanislav Ievlev <inger@altlinux.org> 7.3-alt1
- move installer dialogs into this package

* Wed Jun 13 2007 Stanislav Ievlev <inger@altlinux.org> 7.2-alt16
- add desktop file
- little UI improvements

* Thu May 31 2007 Stanislav Ievlev <inger@altlinux.org> 7.2-alt15
- fix translation

* Wed May 30 2007 Stanislav Ievlev <inger@altlinux.org> 7.2-alt14
- add /sbin/nologin to list of the valid shells (we need it for ldap users)
- rebuild with latest standalone

* Tue May 29 2007 Stanislav Ievlev <inger@altlinux.org> 7.2-alt13
- assign 'Users' group

* Fri May 25 2007 Stanislav Ievlev <inger@altlinux.org> 7.2-alt12
- switch to new card-index scripts

* Wed May 02 2007 Stanislav Ievlev <inger@altlinux.org> 7.2-alt11
- improve password box UI layout

* Mon Apr 23 2007 Stanislav Ievlev <inger@altlinux.org> 7.2-alt10
- update Ukrainian translation

* Thu Apr 19 2007 Stanislav Ievlev <inger@altlinux.org> 7.2-alt9
- little CSS optimizations

* Fri Apr 06 2007 Stanislav Ievlev <inger@altlinux.org> 7.2-alt8
- assign weight

* Thu Apr 05 2007 Stanislav Ievlev <inger@altlinux.org> 7.2-alt7
- remove config-*
- remove deps on alterator-standalone

* Mon Apr 02 2007 Stanislav Ievlev <inger@altlinux.org> 7.2-alt6
- local_users: fix typo
- add Ukrainian translation
- help improvements from kirill@

* Fri Mar 30 2007 Stanislav Ievlev <inger@altlinux.org> 7.2-alt5
- local_users backend: use getent instead of /etc/passwd, skip users with invalid shells
- improve po template generation
- add documentation

* Wed Mar 07 2007 Stanislav Ievlev <inger@altlinux.org> 7.2-alt4
- more translations
- fix tabbox's "current" attribute usage
- fix "expanded" attribute usage

* Tue Mar 06 2007 Stanislav Ievlev <inger@altlinux.org> 7.2-alt3
- more translations
- top level menu

* Fri Feb 09 2007 Stanislav Ievlev <inger@altlinux.org> 7.2-alt2
- bugfix: resurrect 'allow_su' control

* Thu Feb 08 2007 Stanislav Ievlev <inger@altlinux.org> 7.2-alt1
- add fbi data
- remove backend subpackage

* Wed Jan 31 2007 Stanislav Ievlev <inger@altlinux.org> 7.1-alt2
- use ->bool from library

* Fri Jan 12 2007 Stanislav Ievlev <inger@altlinux.org> 7.1-alt1
- improve passwordbox dialog (legion)
- add label constraints

* Wed Jan 10 2007 Stanislav Ievlev <inger@altlinux.org> 7.0-alt7
- don't use woo-extract-name
- don't add root to user's groups

* Tue Dec 12 2006 Stanislav Ievlev <inger@altlinux.org> 7.0-alt6
- add allow_su to list
- always return "ok" when remove user from group

* Mon Dec 11 2006 Stanislav Ievlev <inger@altlinux.org> 7.0-alt5
- improve usability of password widget
- add constraints visualization
- define default value for gecos
- local_users: allow to setup an empty gecos

* Thu Dec 07 2006 Stanislav Ievlev <inger@altlinux.org> 7.0-alt4
- save translation in utf8
- remove unused UI

* Mon Dec 04 2006 Stanislav Ievlev <inger@altlinux.org> 7.0-alt3
- fix backend: resurrect listing of the available shells, fix reading of unexistent users

* Thu Nov 30 2006 Stanislav Ievlev <inger@altlinux.org> 7.0-alt2
- fix backend: exceptions on new for existing user, and write for non-existing user

* Tue Nov 14 2006 Stanislav Ievlev <inger@altlinux.org> 7.0-alt1
- enable constraints

* Wed Nov 08 2006 Stanislav Ievlev <inger@altlinux.org> 6.0-alt0.2
- use native popup message boxes

* Tue Oct 31 2006 Stanislav Ievlev <inger@altlinux.org> 6.0-alt0.1
- move all local_users + local_groups logic to second level backend

* Fri Oct 27 2006 Stanislav Ievlev <inger@altlinux.org> 5.0-alt0.1
- update all backends to backend3
- update to new build system

* Mon Sep 25 2006 Stanislav Ievlev <inger@altlinux.org> 4.0-alt0.3
- icons now in separate design package (alterator-icons)

* Wed Aug 23 2006 Stanislav Ievlev <inger@altlinux.org> 4.0-alt0.2
- update build system

* Wed May 31 2006 Stanislav Ievlev <inger@altlinux.org> 4.0-alt0.1
- ported to alterator-2.9

* Fri May 12 2006 Stanislav Ievlev <inger@altlinux.org> 3.2-alt0.1
- move to git
- improve change password dialog
- removed model

* Mon Mar 27 2006 Stanislav Ievlev <inger@altlinux.org> 3.1-alt0.5
- code improvements

* Tue Mar 14 2006 Stanislav Ievlev <inger@altlinux.org> 3.1-alt0.4
- improved button state checking

* Mon Mar 06 2006 Stanislav Ievlev <inger@altlinux.org> 3.1-alt0.3
- remove extra get-content

* Thu Feb 16 2006 Stanislav Ievlev <inger@altlinux.org> 3.1-alt0.2
- fixed for guile18

* Mon Feb 13 2006 Stanislav Ievlev <inger@altlinux.org> 3.1-alt0.1
- move to new backend2 system, more translations

* Fri Feb 10 2006 Stanislav Ievlev <inger@altlinux.org> 3.0-alt0.2.1
- fixed typo

* Thu Feb 09 2006 Stanislav Ievlev <inger@altlinux.org> 3.0-alt0.2
- makefile improvements

* Wed Feb 08 2006 Stanislav Ievlev <inger@altlinux.org> 3.0-alt0.1
- model fixes
- added password generation facility
- adduser ready now

* Tue Feb 07 2006 Stanislav Ievlev <inger@altlinux.org> 2.1-alt0.5.2
- minor backend improvements
- added demo interface for installer

* Thu Feb 02 2006 Stanislav Ievlev <inger@altlinux.org> 2.1-alt0.5.1
- adaptations for new alterator, added support for acc-{leave,apply}

* Mon Jan 30 2006 Stanislav Ievlev <inger@altlinux.org> 2.1-alt0.5
- yet another usability improvements

* Fri Jan 27 2006 Stanislav Ievlev <inger@altlinux.org> 2.1-alt0.4
- another usability improvements

* Thu Jan 26 2006 Stanislav Ievlev <inger@altlinux.org> 2.1-alt0.3
- usability improvements

* Mon Jan 23 2006 Stanislav Ievlev <inger@altlinux.org> 2.1-alt0.2
- move to new frame scheme

* Fri Jan 20 2006 Stanislav Ievlev <inger@altlinux.org> 2.1-alt0.1
- move to profile based scheme for standalone

* Wed Jan 18 2006 Stanislav Ievlev <inger@altlinux.org> 2.0-alt0.8
- fixed checking for new

* Tue Dec 20 2005 Stanislav Ievlev <inger@altlinux.org> 2.0-alt0.7
- locale improvements

* Mon Dec 19 2005 Stanislav Ievlev <inger@altlinux.org> 2.0-alt0.6
- little code improvements

* Tue Nov 29 2005 Stanislav Ievlev <inger@altlinux.org> 2.0-alt0.5.1
- bugfix

* Tue Nov 29 2005 Stanislav Ievlev <inger@altlinux.org> 2.0-alt0.5
- interface improvements

* Thu Nov 10 2005 Stanislav Ievlev <inger@altlinux.org> 2.0-alt0.4
- layout improvements

* Tue Nov 08 2005 Stanislav Ievlev <inger@altlinux.org> 2.0-alt0.3
- fixed layout, added caption

* Thu Nov 03 2005 Stanislav Ievlev <inger@altlinux.org> 2.0-alt0.2
- improvements

* Wed Nov 02 2005 Stanislav Ievlev <inger@altlinux.org> 2.0-alt0.1
- initial build for unstable alterator

* Wed Oct 19 2005 Stanislav Ievlev <inger@altlinux.org> 1.1-alt14
- minor interface fixes
- added icons

* Mon Sep 12 2005 Stanislav Ievlev <inger@altlinux.org> 1.1-alt13
- added user to scanner group

* Wed Aug 31 2005 Stanislav Ievlev <inger@altlinux.org> 1.1-alt12
- use generic make templates
- disable all input widgets by default

* Tue Aug 30 2005 Sergey V Turchin <zerg at altlinux dot org> 1.1-alt11.1
- fix widgets layout

* Wed Aug 24 2005 Stanislav Ievlev <inger@altlinux.org> 1.1-alt11
- fixed on-apply on-error

* Fri Aug 19 2005 Stanislav Ievlev <inger@altlinux.org> 1.1-alt10
- code improvements

* Fri Aug 05 2005 Stanislav Ievlev <inger@altlinux.org> 1.1-alt9
- improve latest fixes

* Tue Aug 02 2005 Stanislav Ievlev <inger@altlinux.org> 1.1-alt8
- check for user existance before add it

* Mon Aug 01 2005 Stanislav Ievlev <inger@altlinux.org> 1.1-alt7
- Belarusian translation

* Thu Jul 21 2005 Stanislav Ievlev <inger@altlinux.org> 1.1-alt6
- added chrootpasswd tab
- fixed menufile

* Wed Jul 20 2005 Stanislav Ievlev <inger@altlinux.org> 1.1-alt5
- updates

* Tue Jul 19 2005 Stanislav Ievlev <inger@altlinux.org> 1.1-alt4
- minor updates

* Thu Jul 14 2005 Stanislav Ievlev <inger@altlinux.org> 1.1-alt3
- interface improvements
- rename users-config to config-users

* Tue Jul 12 2005 Stanislav Ievlev <inger@altlinux.org> 1.1-alt2
- user added to groups in model now
- usability improvements

* Wed Jul 06 2005 Stanislav Ievlev <inger@altlinux.org> 1.1-alt1
- adopted to new scheme

* Tue Jun 28 2005 Stanislav Ievlev <inger@altlinux.org> 1.0-alt8
- minor bugfixes

* Mon Jun 27 2005 Stanislav Ievlev <inger@altlinux.org> 1.0-alt7
- minor bugfixes

* Thu Jun 23 2005 Stanislav Ievlev <inger@altlinux.org> 1.0-alt6
- updated po by kirill

* Tue Jun 21 2005 Stanislav Ievlev <inger@altlinux.org> 1.0-alt5
- improvements

* Mon Jun 20 2005 Stanislav Ievlev <inger@altlinux.org> 1.0-alt4
- added menu file

* Thu Jun 16 2005 Stanislav Ievlev <inger@altlinux.org> 1.0-alt3
- adopted for new look

* Tue Jun 14 2005 Stanislav Ievlev <inger@altlinux.org> 1.0-alt2
- adopted for new look

* Thu Jun 09 2005 Stanislav Ievlev <inger@altlinux.org> 1.0-alt1
- added standalone version of configurator

* Tue Jun 07 2005 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- improvements

* Mon Jun 06 2005 Stanislav Ievlev <inger@altlinux.org> 0.3-alt3
- new url scheme

* Tue May 31 2005 Stanislav Ievlev <inger@altlinux.org> 0.3-alt2
- current snapshot

* Fri May 27 2005 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- more help, and translation fixes (kirill@)

* Wed May 25 2005 Stanislav Ievlev <inger@altlinux.org> 0.2-alt11
- for developers only: for testing new look, added help

* Tue May 24 2005 Stanislav Ievlev <inger@altlinux.org> 0.2-alt10
- for developers only: for testing new look

* Wed May 04 2005 Stanislav Ievlev <inger@altlinux.org> 0.2-alt9
- new shapshot

* Wed Apr 27 2005 Stanislav Ievlev <inger@altlinux.org> 0.2-alt8
- new snapshot

* Mon Apr 25 2005 Stanislav Ievlev <inger@altlinux.org> 0.2-alt7
- improved files layout

* Fri Apr 22 2005 Stanislav Ievlev <inger@altlinux.org> 0.2-alt6
- bugfixes
- added support for ALT control center
- use gpasswd from shadow groups instead of usermod

* Thu Apr 21 2005 Stanislav Ievlev <inger@altlinux.org> 0.2-alt5
- changed backend format
- minor bugfixes
- additional ui for future configurator

* Wed Apr 13 2005 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4
- add users to groups

* Tue Apr 12 2005 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- added checking for valid username

* Mon Apr 04 2005 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- little fixes

* Mon Mar 28 2005 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- move ui and model files from main alterator tarball
- new backend format available now

* Thu Mar 24 2005 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- minor bugfixes (allow to change uid)

* Mon Mar 21 2005 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial release
