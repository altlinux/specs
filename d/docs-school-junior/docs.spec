%define variant school-junior
%define Variant School Junior

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux docs-lxdesktop docs-lxdesktop-lite docs-school-teacher docs-alt-education docs-alt-kworkstation docs-alt-server docs-alt-workstation

Name: docs-%variant
Version: 7.0.5
Release: alt3

Summary: %Variant documentation
License: %fdl
Group: Documentation

Packager: ALT Docs Team <docs@packages.altlinux.org>
BuildArch: noarch

Source: %name-%version-%release.tar

Conflicts: %(for n in %variants ; do [ "$n" = %name ] || echo -n "$n "; done)

BuildRequires(pre):rpm-build-licenses
BuildRequires: publican
BuildRequires: perl-podlators

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
* Fri Feb 17 2017 Elena Mishina <lepata@altlinux.org> 7.0.5-alt3
- update Conflicts list

* Sat Jan 23 2016 Artem Zolochevskiy <azol@altlinux.org> 7.0.5-alt2
- rebuild with publclian4

* Sat Jan 23 2016 Artem Zolochevskiy <azol@altlinux.org> 7.0.5-alt1
- update to 7.0.5

* Fri Dec 27 2013 Andrey Cherepanov <cas@altlinux.org> 7.0-alt3
- Update screenshots

* Tue Dec 17 2013 Artem Zolochevskiy <azol@altlinux.ru> 7.0-alt2
- fix distro version

* Sun Dec 15 2013 Artem Zolochevskiy <azol@altlinux.ru> 7.0-alt1
- Update documentation and screenshots

* Sat Aug 18 2012 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt1
- initial Informika 6.0 School Junior version

* Fri Jun 10 2011 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt7
- add docs-simply-linux to Conflicts list

* Mon Mar 07 2011 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt6
- add docs-school-newlite docs-centaurus to Conflicts list

* Fri Feb 26 2010 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt5
- install-guide: fix info on RAID creation during install
- add docs-school-terminal to Conflicts list

* Mon Feb 22 2010 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt4
- simplify datetime section (#19084)
- typo and punctuation fixes
- use 'io'
- small rephrasings

* Wed Nov 04 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt3
- install-guide: fix typos (thx Rinat Bikov)
- add authorship and revision information

* Mon Oct 26 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt2
- update installer screenshots
- fix typos
- small improvements

* Fri Oct 23 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt1
- initial build for Sisyphus

