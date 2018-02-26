# -*- mode: RPM-SPEC; tab-width: 8; fill-column: 70; -*- 
# $Id: alterator-control.spec,v 1.15 2006/04/28 10:48:26 inger Exp $ 

%define _altdata_dir %_datadir/alterator

Name: alterator-wizardface
Version: 2.0
Release: alt2

Packager: Stanislav Ievlev <inger@altlinux.org>

BuildArch: noarch

Source:%name-%version.tar

#replace previous version in branch
Provides: alterator-wizard = %version
Obsoletes: alterator-wizard

Requires: alterator >= 4.7-alt1 alterator-sh-functions
Requires: alterator-lookout >= 2.1-alt4
Requires: alterator-l10n >= 2.5-alt8
Requires: alterator-browser-qt

%add_findreq_skiplist %_datadir/install2/postinstall.d/*
%add_findreq_skiplist %_datadir/install2/initinstall.d/*

Summary: alterator's wizard like module aggregator
License: GPL
Group: System/Configuration/Other

BuildPreReq: alterator >= 4.7-alt1

# Automatically added by buildreq on Mon Jul 11 2005 (-bi)
BuildRequires: alterator

%description
alterator's wizard like module aggregator

%package usermode
Summary: Usermode bindings for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release
Requires: consolehelper

%description usermode
Usermode bindings for %name

%prep
%setup -q

%build
%make_build

%install
%makeinstall

#install consolehelper
obj=alterator-wizard

%__install -d %buildroot/%_bindir
%__ln_s %_libexecdir/consolehelper/helper %buildroot%_bindir/$obj
%__install -d %buildroot%_sysconfdir/pam.d/

cat>%buildroot%_sysconfdir/pam.d/$obj<<EOF
#%PAM-1.0
auth	sufficient	pam_rootok.so
auth	required	pam_stack.so service=system-auth
account	required	pam_permit.so
password	required	pam_deny.so
session	optional	pam_xauth.so
EOF

%__install -d %buildroot%_sysconfdir/security/console.apps/
cat>%buildroot%_sysconfdir/security/console.apps/$obj<<EOF
USER=root
PROGRAM=%_sbindir/$obj
SESSION=true
FALLBACK=true
EOF

%files
%_sbindir/*
%_altdata_dir/ui/wizard/*
%_alterator_backend3dir/*
%_datadir/install2/initinstall.d/*
%_datadir/install2/postinstall.d/*

%files usermode
%config(noreplace) %_sysconfdir/pam.d/*
%config(noreplace) %_sysconfdir/security/console.apps/*
%_bindir/*

%changelog
* Wed Mar 17 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.0-alt2
- small fix in postinstall.d/01-wizard-log.sh from @sbolshakov

* Tue Nov 10 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt1
- use external alteratord service

* Wed Sep 30 2009 Stanislav Ievlev <inger@altlinux.org> 1.1-alt4
- replace frame:call-next, frame:call-back with wizard-bind from
  (alterator wizard) library

* Wed Aug 26 2009 Stanislav Ievlev <inger@altlinux.org> 1.1-alt3
- fix title localization (closes: #21179)
- initial support of (alterator wizard) library
- redesign "on-next" overflow protection to allow wizard branches

* Fri May 22 2009 Stanislav Ievlev <inger@altlinux.org> 1.1-alt2
- move consolehelper stuff to separate package
- backend: add default steps value (for hacks in sysconfig-base), fix steps processing

* Fri May 22 2009 Stanislav Ievlev <inger@altlinux.org> 1.1-alt2

* Thu May 21 2009 Stanislav Ievlev <inger@altlinux.org> 1.1-alt1
- use consolehelper
- support both /usr/share/alterator/steps and /usr/share/install2/steps directories
- allow to use alternate steps-file
- backend: alterator_api_version = 1

* Thu Jan 29 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt1
- update for new alterator
- use translations directly from alterator-l10n

* Tue Dec 09 2008 Stanislav Ievlev <inger@altlinux.org> 0.10-alt1
- switch to guile-1.8

* Wed Aug 06 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt1
- replace alterator-read-desktop with alterator-dump-desktop

* Thu Jul 31 2008 Stanislav Ievlev <inger@altlinux.org> 0.8-alt1
- require alterator-browser-qt
- use module.mak

* Thu Jul 24 2008 Stanislav Ievlev <inger@altlinux.org> 0.7-alt2
- replace desktop.awk with alterator-read-desktop

* Sat Jun 07 2008 Stanislav Ievlev <inger@altlinux.org> 0.7-alt1
- improve ui layout

* Fri May 30 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt1
- replace layouts with standalone scripts
- remove pot-files

* Mon May 26 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt7
- require latest alterator-lookout (with bugfix)

* Fri May 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt6
- add postinstall script to save wizard.log
- join to common translation database
- don't require alterator-autoinstall
- fix Help button translation

* Thu May 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt5
- fix (update for new help backend from alterator-menu)

* Thu May 15 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt4
- fix (replace with-widgets with make-widget)

* Wed Apr 16 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt3
- fix autoskip feature support

* Tue Apr 15 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt2
- remove orphaned uris

* Mon Apr 14 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- remove map files

* Mon Apr 14 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- use common /std/frame

* Fri Apr 11 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- update to new alterator-lookout

* Thu Apr 10 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt7
- use alterator-sh-functions

* Wed Mar 12 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt6
- conflicts alterator-wizard -> provides/obsoletes alterator-wizard

* Thu Mar 06 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt5
- resurrect  help button

* Tue Jan 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4
- add to requires alterator-autoinstall

* Mon Jan 21 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- resurrect step icons

* Tue Jan 15 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- use common code for desktop-file reading from alterator-menu
- add support for translation fallback

* Thu Jan 10 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- use common help backend from alterator-menu

* Tue Oct 23 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- add common frame:skip utility

* Wed Oct 10 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- remove requires for alterator-icons

* Tue Oct 09 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- add support for two help directories

* Fri Oct 05 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- new profile system
