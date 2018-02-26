%define _altdata_dir %_datadir/alterator

Name: alterator-xinetd
Version: 1.9
Release: alt1

Packager: Vladislav Zavjalov <slazav@altlinux.org>

BuildArch: noarch

Source:%name-%version.tar

Summary: alterator module for xinetd
License: GPL
Group: System/Configuration/Other
Requires:  gettext xinetd
Requires:  alterator-services

# we use alterator-read-desktop from alterator >= 3.6-alt7
Requires: alterator >= 3.6-alt7
Requires:  alterator-perl-functions >= 0.4-alt4
Conflicts: alterator-fbi < 5.23-alt1
Conflicts: alterator-lookout < 1.3-alt10
BuildPreReq: alterator >= 3.6-alt7
BuildPreReq: alterator-perl-functions >= 0.4-alt4

%description
alterator module for xinetd

%prep
%setup -q

%build
%make_build libdir=%_libdir

%install
%makeinstall

%files
%_altdata_dir/applications/*
%_altdata_dir/ui/*
%_sysconfdir/alterator/xinetd/*
%_alterator_backend3dir/*

%changelog
* Wed Oct 14 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.9-alt1
- ajax.scm: use new card-index module
- backend: fix handling of services with id!=name
- qt ui: use /std/frame

* Thu Apr 30 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt1
- cleanup ui/ajax.scm

* Wed Apr 29 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.7-alt2
- fix name parameter handling in html

* Wed Apr 29 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.7-alt1
- rewrite user interfaces for new alterator:
  - do't use wf=card-index, use ajax
  - use new effect functions

* Mon Apr 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.6-alt1
- qt ui: use new form library
- fix error in config file writing

* Mon Apr 06 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.5-alt1
- service reload on write
- move html UI in ui dir
- remove "Start, stop or restart service..." reference
- update translations in desktop-file
- fix writing empty values

* Fri Jan 23 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.4-alt4
- move help and po to alterator-l10n

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.4-alt3
- use help from l10n

* Tue Nov 18 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.4-alt2
- add ... to reference
- don't include std/functions in qt
- don't include card-index.js and submit.js in html template

* Fri Nov 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.4-alt1
- add support for desktop files with service descriptions

* Fri Oct 17 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt5
- Categories=X-Alterator-System
- rebuild with new alterator-l10n

* Thu Oct 16 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt4
- remove implicit attribute for groupbox

* Wed Oct 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt3
- use new alterator-lookout form module

* Tue Oct 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt2
- add bind parameter support (fix #17403)
- (edit "" -> (edit value ""

* Mon Oct 06 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt1
- use form-* functions from new alterator-lookout
- use enumref

* Wed Oct 01 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt11
- backend: fix default section writing
- qt ui: create write/read-form functions

* Tue Sep 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt10
- constraints -> types

* Wed Sep 17 2008 Stanislav Ievlev <inger@altlinux.org> 1.2-alt9
- fix English messages

* Tue Sep 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt8
- rebuild with new alterator-l10n

* Fri Jul 04 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt7
- make internal service flag to be boolean

* Fri Jul 04 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt6
- remove titile and h1-header from html

* Fri Jul 04 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt5
- update Require in spec

* Fri Jul 04 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt4
- remove translations from desktop-file

* Fri Jul 04 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt3
- remove unused images/* 
- use module.mak

* Wed Jul 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt2
- rewrite qt ui.
  - replace all cells by hidden widgets
  - use auto hide/disable

* Thu Jun 26 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt1
- auto hide/disable fields in html
- remove xinetd.css

* Fri Jun 06 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt15
- small changes in interface

* Tue Jun 03 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt14
- fix help

* Tue Jun 03 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt13
- fix backend's action list

* Mon Jun 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt12
- modify backend output
- alterator-perl-functions >=0.3-alt4

* Mon Jun 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt11
- change xgettext keyword in perl backend: N_ -> _
- remove PERL_TRANSLATE definition from makefile (using std def from alterator's po.mak)
- Requires: alterator >= 3.3-alt6 alterator-perl-functions >=0.3-alt3

* Fri May 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt10
- fix translations

* Fri May 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt9
- remove po directory

* Fri May 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt8
- use alterator-perl-functions 0.3-alt2

* Wed May 28 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt7
- use alterator-perl-functions 0.3-alt1

* Tue May 27 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt6
- use alterator-perl-functions 0.1-alt1

* Mon May 26 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt6
- main gridbox -> splitbox

* Thu May 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt5
- fix "reset" translation

* Thu May 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt4
- move ui/xinetd.scm -> ui/xinetd/indes.scm
- fix translations
- use alterator-l10n

* Thu May 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt3
- fix translations and align of labels in html

* Mon May 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt2
- fix translations

* Tue Apr 29 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt1
- remove template- backend
- rewrite backend (awk->perl) (see full description in backend file)
- rewrite QT UI
- rewrite HTML UI

* Mon Apr 28 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt1
- remove html-messages.scm
- use alterator-sh-functions in template- backend

* Fri Mar 28 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.1-alt8
- repair broken FBI UI - add template-xinetd backend
- fix service descriptions in qt ui

* Tue Mar 18 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.1-alt7
- repair broken FBI UI

* Tue Mar 18 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.1-alt6
- Improve QT UI

* Fri Mar 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.1-alt5
- add QT UI
- making backend to use (state #f/#t), not (state "enabled"/"disabled") in read and write (not list!) actions.

* Tue Mar 04 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.1-alt4
- Change help paths to the new style.

* Thu Dec 13 2007 Grigory Batalov <bga@altlinux.ru> 0.1-alt3
- Russian help page.
- Rename translated title.

* Wed Sep 19 2007 Grigory Batalov <bga@altlinux.ru> 0.1-alt2
- Skip .rpmold/.rpmnew services.

* Thu Sep 13 2007 Grigory Batalov <bga@altlinux.ru> 0.1-alt1
- Initial release


