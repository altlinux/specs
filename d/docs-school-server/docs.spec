%define variant school-server
%define Variant School Server

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux

Name: docs-%variant
Version: 5.0
Release: alt16

Summary: %Variant documentation
License: %fdl
Group: Documentation

Packager: ALT Docs Team <docs@packages.altlinux.org>
BuildArch: noarch

Source: %name-%version-%release.tar

Conflicts: %(for n in %variants ; do [ "$n" = %name ] || echo -n "$n "; done)

BuildRequires(pre):rpm-build-licenses
BuildRequires: asciidoc-a2x

%description
%Variant documentation.

%prep
%setup -n %name-%version-%release

%build
%make_build

%install
%make_install DESTDIR=%buildroot docdir=%_docsinstalldir install
ln -s $(relative %_docsinstalldir %_documentationdir) %buildroot%_documentationdir

%files
%_docsinstalldir
%_documentationdir

%changelog
* Fri Jun 10 2011 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt16
- add docs-simply-linux to Conflicts list

* Mon Mar 07 2011 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt15
- add docs-school-newlite docs-centaurus to Conflicts list

* Mon Dec 27 2010 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.0-alt14
- modify RUJEL docs (by Gennady Kushnir)

* Mon Dec 20 2010 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.0-alt13
- add links in rujel documentation

* Thu Dec 16 2010 Andrey Cherepanov <cas@altlinux.org> 5.0-alt12
- RUJEL docs modified (by Gennady Kushnir)

* Mon Dec 13 2010 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.0-alt11
- expand rujel extractions

* Sat Dec 11 2010 Andrey Cherepanov <cas@altlinux.org> 5.0-alt10
- reformat texts
- rename skf/ subdirectory to netpolice/

* Fri Dec 10 2010 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.0-alt9
- add rujel documentation
- new screenshots
- add Netpolice documentation
- add rujel documentation
- add note about domain choose
- description 'nostatic' installer option
- add root password step in installer

* Fri Feb 26 2010 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt8
- install-guide: fix info on RAID creation during install
- whatis-alt: fix 'Le Mythe de Sisyphe' link
- add docs-school-terminal to Conflicts list

* Mon Feb 22 2010 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt7
- simplify datetime section (#19084)
- typo and punctuation fixes
- small rephrasings

* Wed Feb 10 2010 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt6
- remove support section (Closes: #22921)

* Mon Feb 08 2010 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt5
- fix hyperlink formatting (Closes: #22236)
- more typo & punctuation fixes

* Fri Jan 29 2010 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt4
- typo fixes, small improvements

* Mon Nov 09 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt3
- install-guide: fix typo (thx Rinat Bikov)
- update screenshots
- moodle: fix (rename) login screenshot
- add authorship and revision information

* Mon Oct 26 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt2
- update installer screenshots
- fix typos
- small improvements

* Fri Oct 23 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt1
- initial build for Sisyphus

