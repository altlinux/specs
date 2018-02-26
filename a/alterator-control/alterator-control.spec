# -*- mode: RPM-SPEC; tab-width: 8; fill-column: 70; -*- 
# $Id: alterator-control.spec,v 1.15 2006/04/28 10:48:26 inger Exp $ 

%define _altdata_dir %_datadir/alterator

Name: alterator-control
Version: 2.2
Release: alt1

Packager: Stanislav Ievlev <inger@altlinux.org>

BuildArch:	noarch

Source:%name-%version.tar

Summary: alterator module for control package
License: GPL
Group: System/Configuration/Other

Requires: alterator >= 4.7-alt1, control >= 0.7.1-alt1, alterator-sh-functions >= 0.13-alt2
Requires: alterator-l10n >= 1.5-alt5
Conflicts: alterator-fbi < 5.25-alt7
Conflicts: alterator-lookout < 2.2-alt2

BuildPreReq: alterator >= 4.7-alt1

%description
alterator module for control package

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_altdata_dir/applications/*
%_altdata_dir/ui/*/
%_alterator_backend3dir/*


%changelog
* Mon Nov 23 2009 Stanislav Ievlev <inger@altlinux.org> 2.2-alt1
- use woo-call and alterator_export_proc
- use table.alterator-listbox with single-select feature
- share callbacks between qt and html interfaces

* Wed Sep 23 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt1
- use workflow 'none' for all html interfaces

* Fri Jul 24 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt2
- html ui: use ajax for the main page

* Mon Feb 02 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt1
- use help and translations directly from alterator-l10n
- use new form library

* Tue Sep 30 2008 Stanislav Ievlev <inger@altlinux.org> 1.0-alt3
- improve unit-tests

* Mon Sep 01 2008 Stanislav Ievlev <inger@altlinux.org> 1.0-alt2
- html ui: "alterator-listbox" table

* Mon Sep 01 2008 Stanislav Ievlev <inger@altlinux.org> 1.0-alt1
- qt ui: use enumref
- backend: alterator_api_version = 1

* Fri Aug 01 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt1
- add unit-tests for backend

* Fri Jul 04 2008 Stanislav Ievlev <inger@altlinux.org> 0.8-alt2
- rename
- use module.mak
- remove h1,titles, javasript scripts for card-index.

* Tue May 13 2008 Stanislav Ievlev <inger@altlinux.org> 0.8-alt1
- remove html-messages.mak
- remove po-files
- use write_string_param

* Wed Mar 12 2008 Stanislav Ievlev <inger@altlinux.org> 0.7-alt1
- remove template-*
- improve qt ui

* Sat Mar 01 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt3
- fix requires

* Fri Feb 29 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt2
- use alterator-sh-functions

* Thu Jan 10 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt1
- update module to new help subsystem

* Wed Jun 13 2007 Stanislav Ievlev <inger@altlinux.org> 0.5-alt15
- add desktop file

* Fri May 25 2007 Stanislav Ievlev <inger@altlinux.org> 0.5-alt14
- switch to new card-index scripts

* Mon Apr 23 2007 Stanislav Ievlev <inger@altlinux.org> 0.5-alt12
- update Ukrainian translation

* Thu Apr 19 2007 Stanislav Ievlev <inger@altlinux.org> 0.5-alt11
- little CSS optimizations

* Wed Apr 18 2007 Stanislav Ievlev <inger@altlinux.org> 0.5-alt10
- change search icon to setup
- move style sheets to separate subdirectory

* Thu Apr 05 2007 Stanislav Ievlev <inger@altlinux.org> 0.5-alt9
- remove config-*

* Tue Apr 03 2007 Stanislav Ievlev <inger@altlinux.org> 0.5-alt8
- help improvements from kirill@

* Mon Apr 02 2007 Stanislav Ievlev <inger@altlinux.org> 0.5-alt7
- add 'alt' to img
- add documentation

* Tue Mar 27 2007 Stanislav Ievlev <inger@altlinux.org> 0.5-alt6
- add Ukrainian translation

* Mon Mar 26 2007 Stanislav Ievlev <inger@altlinux.org> 0.5-alt5
- fix CSS, remove unused up-level hyperlink

* Fri Mar 23 2007 Stanislav Ievlev <inger@altlinux.org> 0.5-alt4
- improve po template autogeneration
- assign group 'System'

* Fri Mar 09 2007 Stanislav Ievlev <inger@altlinux.org> 0.5-alt3
- more translations

* Thu Feb 15 2007 Stanislav Ievlev <inger@altlinux.org> 0.5-alt2
- add menu

* Thu Feb 08 2007 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- add fbi data

* Mon Jan 29 2007 Stanislav Ievlev <inger@altlinux.org> 0.4-alt4
- add label contraints

* Wed Jan 10 2007 Stanislav Ievlev <inger@altlinux.org> 0.4-alt3
- don't use woo-extract-name

* Wed Dec 13 2006 Stanislav Ievlev <inger@altlinux.org> 0.4-alt2
- fixes in backend for html interface

* Fri Oct 27 2006 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- improve backend (from mvc project)

* Fri Sep 29 2006 Stanislav Ievlev <inger@altlinux.org> 0.3-alt4
- update build system

* Mon Sep 25 2006 Stanislav Ievlev <inger@altlinux.org> 0.3-alt3
- move icons to separate package
- fixed usage of radiolist widget
- turn of change button by default

* Wed Sep 06 2006 Stanislav Ievlev <inger@altlinux.org> 0.3-alt2
- rebuild for new menu policy

* Fri Sep 01 2006 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- move to desktop files
- use radiolist widget

* Wed Aug 23 2006 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4
- improve build system

* Wed May 31 2006 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- fixed for latest alterator

* Thu May 11 2006 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- code improvements, build from git

* Fri Apr 28 2006 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- rewritten

* Wed Oct 19 2005 Stanislav Ievlev <inger@altlinux.org> 0.1.2.2-alt5
- added icons

* Mon Sep 12 2005 Stanislav Ievlev <inger@altlinux.org> 0.1.2.2-alt4
- remove acc hook

* Wed Aug 31 2005 Stanislav Ievlev <inger@altlinux.org> 0.1.2.2-alt3
- use generic make templates

* Mon Aug 01 2005 Stanislav Ievlev <inger@altlinux.org> 0.1.2.2-alt2
- Belarusian translation

* Wed Jul 20 2005 Stanislav Ievlev <inger@altlinux.org> 0.1.2.2-alt1
- updates

* Thu Jul 07 2005 Stanislav Ievlev <inger@altlinux.org> 0.1.2.1-alt1
- modernization

* Tue Jul 05 2005 Alexey Gladkov <legion@altlinux.ru> 0.1.2-alt1
- new version;

* Fri Jul 01 2005 Alexey Gladkov <legion@altlinux.ru> 0.1.1-alt1
- translation bugfix.
- minor bugfix.

* Thu Jun 30 2005 Alexey Gladkov <legion@altlinux.ru> 0.1-alt1
- Initial release
