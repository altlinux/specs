%define _altdata_dir %_datadir/alterator

Name: alterator-services
Version: 1.9
Release: alt1

Summary: Simple SysV services configurator
License: GPL
Group: System/Configuration/Other

Url: http://wiki.sisyphus.ru/Alterator
Source: %name-%version.tar
Packager: Vladislav Zavjalov <slazav@altlinux.org>

# we use alterator-read-desktop from alterator >= 3.6-alt7
Requires: alterator >= 3.6-alt7
Requires: alterator-sh-functions >= 0.6-alt3
Conflicts: alterator-fbi < 5.23-alt1
Conflicts: alterator-lookout < 1.2-alt1

BuildArch: noarch
BuildPreReq: alterator >= 3.6-alt7
BuildPreReq: alterator-standalone >= 2.5-alt0.3
BuildPreReq: alterator-profile


%description
Alterator module for SysV services administration

%description -l ru_RU.UTF-8
Модуль для управления сервисами на платформе Альтератор

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_altdata_dir/ui/*/*
%_altdata_dir/applications/*
%_sysconfdir/alterator/services/*
%_alterator_backend3dir/*

%changelog
* Wed Oct 14 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.9-alt1
- ajax.scm: use new card-index module

* Wed Oct 14 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt6
- ajax.scm: fix l10n

* Tue Sep 29 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt5
- update translations in desktop-files from alterator-l10n

* Mon Sep 28 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt4
- update desktop files for services (by cas@)

* Tue Sep 15 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt3
- QT UI: use /std/frame, fix widget name (closes: #21568)

* Fri Aug 28 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt2
- html ui: add class="btn" to button (closes: #21163)

* Wed Jun 03 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt1
- use experimental card-index module

* Thu Apr 30 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.7-alt1
- backend: status=unknown if initscript does not have status action
- cleanup ui/ajax.scm

* Wed Apr 29 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.6-alt1
- rewrite user interfaces for new alterator, don't use wf=card-index, use ajax

* Wed Apr 01 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.5-alt10
- fix service status handling

* Wed Apr 01 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.5-alt9
- status=stopped if service "is dead, but stale PID file exists" (fix #19283)

* Thu Jan 29 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.5-alt8
- fix translation in desktop-file

* Wed Jan 28 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.5-alt7
- Add localized description for nslcd and fix translation for ethtool (by cas@)

* Fri Jan 23 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.5-alt6
- move po and help to alterator-l10n

* Mon Jan 19 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.5-alt5
- update service list on each list command

* Mon Dec 29 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.4-alt5
- add desktop files (by cas@)

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.4-alt4
- update po and help

* Thu Dec 04 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.4-alt3
- add sleep 1 after service restarting

* Mon Nov 17 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.4-alt2
- add ru help (by @azol)

* Fri Nov 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.4-alt1
- add support for desktop files with service descriptions

* Fri Nov 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt9
- add po

* Mon Sep 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt8
- remove div class="main-menu" from html template (fix #16593)

* Wed Jul 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt7
- remove empty (_ "") in ui (fix #16464)

* Wed Jul 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt6
- rewrite qt ui: use enumref, remove cells

* Wed Jul 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt5
- modify backend
  - remove po_domain setting
  - use alterator_api_version=1

* Wed Jul 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt4
- remove with-translation and "/std/functions" include from qt

* Wed Jul 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt3
- remove translations from desktop file

* Wed Jul 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt2
- remove services.css
- remove card-index.js and submit.js includes
- remove title and h1-header from html

* Wed Jul 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt1
- use module.mak
- remove po/*

* Mon Jun 16 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt6
- fix desktop file (fix #15956)

* Thu May 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt5
- fix translations

* Wed May 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt4
- remove html-messages
- use alterator-l10n

* Sun May 04 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt3
- remove Requires: alterator-standalone, alterator-fbi

* Fri Apr 11 2008 Michael Shigorin <mike@altlinux.org> 1.2-alt2
- pulled in changes by slazav@
- fixed changelog

* Thu Apr 10 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt1
- change version to 1.2
- change Categories to X-Alterator-System
- change ru translation for Apply button
- "start automaticcaly" -> "start on boot"

* Wed Apr 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1.6-alt14
- fix bug in HTML UI

* Tue Apr 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1.6-alt13
- Make Name, Descr, State fields to be text, not inputs
  (need alterator-fbi>=1.1.6-alt13)
- 100%%->98%% in css (growing select field fix)

* Mon Apr 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1.6-alt12
- fix problem with tranlations in backend

* Mon Apr 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1.6-alt11
- exclude ahttpd and configd from list
- remove space in 'ret ="#t"'
- add translations to backend messages

* Tue Apr 01 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1.6-alt10
- change bash-specific [[ =~ ]] -> grep 

* Thu Mar 27 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1.6-alt9
- rewrite QT UI

* Mon Mar 24 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1.6-alt8
- remove layout-policy attribute (bug #14945)
- remove profile.d/services
- remove maps/services.map
- remove ui/services.map.in
- remove /usr/share/alterator/applications/alterator-services.desktop
  (copy of .../services.desktop)
- completely rewrite backend and HTML UI

* Sat Mar 22 2008 Michael Shigorin <mike@altlinux.org> 1.1.6-alt8
- fix build [requires], thanks ldv@ and inger@ for a hint

* Mon Aug 06 2007 Grigory Batalov <bga@altlinux.ru> 1.1.6-alt7
- Switch to new menu system.

* Fri May 25 2007 Grigory Batalov <bga@altlinux.ru> 1.1.6-alt6
- Encode Russian text in UTF-8 for alterator-fbi compatibility.

* Thu May 03 2007 Grigory Batalov <bga@altlinux.ru> 1.1.6-alt5
- Show service description.
- Guess default runlevels on a new service addition.
- Change 'New service' workflow from form to card-index.
- Code cleanup:
  + wrap function works on stdin;
  + hide service status command errors.

* Sat Apr 28 2007 Grigory Batalov <bga@altlinux.ru> 1.1.6-alt4
- Ukrainian localization (tanks to Serhii Hlodin).

* Fri Apr 27 2007 Grigory Batalov <bga@altlinux.ru> 1.1.6-alt3
- List all known services by default.
- Look for unknown services in initdir.
- Replace "New service" link with a button.
- Update for resent CSS.

* Tue Apr 24 2007 Grigory Batalov <bga@altlinux.ru> 1.1.6-alt2
- Choose service to enable from list. 

* Tue Apr 17 2007 Grigory Batalov <bga@altlinux.ru> 1.1.6-alt1
- Web-frontend added. 

* Mon Apr 02 2007 Michael Shigorin <mike@altlinux.org> 1.1.5-alt1
- fixed silly thinko in maps/services.map

* Mon Apr 02 2007 Michael Shigorin <mike@altlinux.org> 1.1.4-alt1
- remembered to cleanup deprecated renew_services in backend3/services

* Mon Apr 02 2007 Michael Shigorin <mike@altlinux.org> 1.1.3-alt4
- hopefully fixed maps/

* Mon Apr 02 2007 Michael Shigorin <mike@altlinux.org> 1.1.3-alt3
- fixed %%files

* Mon Apr 02 2007 Michael Shigorin <mike@altlinux.org> 1.1.3-alt2
- looked further (at build deps)...

* Mon Apr 02 2007 Michael Shigorin <mike@altlinux.org> 1.1.3-alt1
- looked at alterator-control/Makefile, as proposed by inger@

* Mon Apr 02 2007 Michael Shigorin <mike@altlinux.org> 1.1.2-alt1
- *fixed* Makefile

* Mon Apr 02 2007 Michael Shigorin <mike@altlinux.org> 1.1.1-alt4
- fixed %%setup

* Mon Apr 02 2007 Michael Shigorin <mike@altlinux.org> 1.1.1-alt3
- added Packager:

* Mon Apr 02 2007 Michael Shigorin <mike@altlinux.org> 1.1.1-alt2
- s/tar\.bz2/tar/

* Mon Apr 02 2007 Michael Shigorin <mike@altlinux.org> 1.1.1-alt1
- 1.1.1 (s/ui\.mak/ui2.mak/, should fix build)

* Sun Oct 01 2006 Michael Shigorin <mike@altlinux.org> 1.1-alt1
- 1.1 (updated to current alterator)

* Sat May 13 2006 Michael Shigorin <mike@altlinux.org> 1.0-alt3
- fixed #9545 (spurious messages due to global var influenced)
  + thanks Alexey Gladkov (legion@) for debug/fix!

* Sat May 06 2006 Michael Shigorin <mike@altlinux.org> 1.0-alt2
- typo fixes

* Fri May 05 2006 Dmitri Kuzishchin <dim@altlinux.ru> 1.0-alt1
- this version switches on/off the services for all runlevel and add stop/start function

* Wed Apr 19 2006 Michael Shigorin <mike@altlinux.org> 0.1.2-alt1
- minor ui enhancement/speedup (no more flicker/scrollbar reset
  due to full document reload), thanks inger@

* Wed Apr 19 2006 Michael Shigorin <mike@altlinux.org> 0.1.1-alt1
- minor backend fixes/cleanups

* Wed Apr 19 2006 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release
- based on Stanislav Ievlev's proposed spec template
- thanks for advice:
  + Stanislav Ievlev (inger@)
  + Sergey Bolshakov (sbolshakov@)
  + Anton Farygin (rider@)
