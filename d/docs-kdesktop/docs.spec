%define variant kdesktop
%define Variant KDesktop

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux docs-lxdesktop docs-lxdesktop-lite

Name: docs-%variant
Version: 6.0.1
Release: alt1

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
* Mon Mar 19 2012 Artem Zolochevskiy <azol@altlinux.ru> 6.0.1-alt1
- update for 6.0.1

* Fri Mar 09 2012 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt14
- fix some typos

* Tue Mar 08 2012 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt13
- improve sumode section
- add docs-lxdesktop, docs-lxdesktop-lite to conflicts list

* Fri Oct 21 2011 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt9
- update documentation
- closes bug: #26457

* Mon Aug 29 2011 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt8
- fix some typos

* Fri Aug 26 2011 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt7
- update

* Fri Aug 19 2011 Alexandr Boltris <alex@altlinux.org> 6.0-alt6
- fix previous changelog entry

* Fri Aug 18 2011 Alexandr Boltris <alex@altlinux.org> 6.0-alt5
- update

* Thu Aug 18 2011 Alexandr Boltris <alex@altlinux.org> 6.0-alt4
- update

* Fri Jul 01 2011 Alexandr Boltris <alex@altlinux.org> 6.0-alt3
- some rephrasings / typo fixes

* Fri Jun 09 2011 Alexandr Boltris <alex@altlinux.ru> 6.0-alt2
- system-management: add initial network section
- kde-quickstart: update system-tray description
- add packages section
- desktop-software: update software descriptions
- some rephrasings / typo fixes
- update screenshots

* Mon Jun 06 2011 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt1
- update for ALT Linux 6.0 KDesktop

* Mon Mar 07 2011 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt8
- update Conflicts list

* Fri Feb 26 2010 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt7
- install-guide: fix info on RAID creation during install
- whatis-alt: fix 'Le Mythe de Sisyphe' link
- add docs-school-terminal to Conflicts list

* Mon Feb 22 2010 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt6
- simplify datetime section (#19084)
- typo and punctuation fixes
- small rephrasings

* Fri Jan 29 2010 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt5
- typo fixes, small improvements

* Wed Dec 23 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt4
- update screenshots (thx Sergey V Turchin)

* Fri Dec 18 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt3
- add initial 'applications' section

* Fri Nov 27 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt2
- add dolphin section

* Thu Nov 26 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt1
- initial build for Sisyphus
  + based on docs-desktop-5.0-alt8 package
