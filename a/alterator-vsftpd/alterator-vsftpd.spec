%define _altdata_dir %_datadir/alterator

Name: alterator-vsftpd
Version: 0.10
Release: alt1

Packager: Stanislav Ievlev <inger@altlinux.org>

BuildArch:	noarch

Source:%name-%version.tar

Summary: alterator module for vsftpd configuration
License: GPL
Group: System/Configuration/Other
Requires: alterator >= 4.6-alt4 alterator-sh-functions >= 0.13-alt2 libshell vsftpd
Requires: alterator-l10n >= 1.1-alt4
Conflicts: alterator-fbi < 5.25-alt9
Conflicts: ahttpd < 3.2-alt3

BuildPreReq: alterator >= 4.6-alt4

# Automatically added by buildreq on Mon Jul 11 2005 (-bi)
BuildRequires: alterator

%description
alterator module for vsftpd configuration

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*
%_alterator_backend3dir/*

%changelog
* Fri Dec 18 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.10-alt1
- update translations in desktop files
- tune UI

* Mon Nov 30 2009 Stanislav Ievlev <inger@altlinux.org> 0.9-alt1
- use alterator_export_proc

* Thu Aug 20 2009 Stanislav Ievlev <inger@altlinux.org> 0.8-alt3
- ui-users-write: call backend only if user was selected

* Wed Jul 29 2009 Stanislav Ievlev <inger@altlinux.org> 0.8-alt2
- fix i18n

* Wed Jul 29 2009 Stanislav Ievlev <inger@altlinux.org> 0.8-alt1
- use workflow 'none':
  * ajax based effects
  * ajax based 'alterator-listbox' widget in 'multi-select' mode

* Thu Apr 23 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt1
- ui: remove link to alterator-users, replace optionlist with enumref
- backend: alterator_api_version = 1

* Fri Mar 27 2009 Stanislav Ievlev <inger@altlinux.org> 0.6-alt3
- remove link to alterator-services

* Tue Jan 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt2
- fix label

* Mon Jan 26 2009 Stanislav Ievlev <inger@altlinux.org> 0.6-alt1
- update module for modern alterator-fbi
- use help and translations directly from alterator-l10n

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt4
- use help from new l10n

* Wed Nov 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt3
- add DOCTYPE to html template

* Sat Nov 01 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt2
- fix label: "start, stop..." -> "Start, stop...."
- remove titles from html template

* Mon Jun 30 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- use effects
- use write_enum/write_enum_item
- remove po-files
- use module.mak

* Mon May 26 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt6
- fix xinetd reloading (thanks to vyt@)
- remove 'DEFAULT' state for added users
- use write_bool_param

* Wed May 21 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt5
- fix reset button in html ui

* Wed Apr 30 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt4
- join to common translation database

* Wed Apr 30 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt3
- replace alterator-chkconfig with alterator-services
- remove html-messages
- use libshell

* Wed Mar 19 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt2
- add <br/> around reset/submit buttons in html UI

* Thu Mar 06 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- remove template-*

* Tue Feb 05 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- add missing requires (alterator-chkconfig)
- use alterator-sh-functions
- update to new help system
- fix Ukrainian translation

* Thu Jan  3 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt14
- build for Sisyphus

* Thu Dec 13 2007 Grigory Batalov <bga@altlinux.ru> 0.2-alt13
- Add link to the service restart.
- Link to the user account administration.
- Use dash in "FTP server" translation.

* Thu Jun 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt12
- switch to new menu system

* Wed May 02 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt11
- update Ukrainian translation

* Mon Apr 23 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt10
- update Ukrainian translation

* Thu Apr 19 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt9
- little CSS optimization

* Fri Mar 30 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt8
- help improvements from kirill@
- fix titles

* Thu Mar 29 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt7
- add Ukrainian translation

* Tue Mar 27 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt6
- add documentation

* Fri Mar 23 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt5
- improve po template generation

* Mon Mar 19 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4
- rename 'upload' dir to 'incoming'

* Fri Mar 16 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- remove sudo, thanks to Artem Zolochevskiy

* Wed Mar 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- fix write_enable value reading
- add default upload directory

* Tue Mar 13 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- resurrect for html interface

* Fri Oct 27 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- improve backend from mvc project

* Mon Oct 02 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- initial release
