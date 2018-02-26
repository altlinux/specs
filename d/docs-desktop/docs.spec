%define variant desktop
%define Variant Desktop

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus

Name: docs-%variant
Version: 5.0
Release: alt12

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
* Mon Mar 07 2011 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt12
- update Conflicts list

* Fri Feb 26 2010 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt11
- install-guide: fix info on RAID creation during install
- whatis-alt: fix 'Le Mythe de Sisyphe' link
- add docs-school-terminal to Conflicts list

* Mon Feb 22 2010 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt10
- simplify datetime section (#19084)
- typo and punctuation fixes
- small rephrasings

* Wed Jan 27 2010 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt9
- typo fixes, small improvements

* Wed Nov 04 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt8
- install-guide: fix typos (thx Rinat Bikov)
- add authorship and revision information

* Mon Oct 26 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt7
- update installer screenshots
- fix typos
- small improvements

* Fri Oct 23 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt6
- add initial office-desktop-auth step description
- update Conflicts list

* Thu Oct 22 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt5
- completely rewritten (thanks Andrey Cherepanov)
- package renamed docs-desktop-quickstart -> docs-desktop
- add %%_defaultdocdir/documentation dir (used in indexhtml packages)
- add conflicts to other 'docs' packages

* Tue Aug 18 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt4
- add Provides: docs-desktop
- add link to standart documentation directory

* Tue May 19 2009 Vladimir Zhukov <bertis@altlinux.org> 5.0-alt3
- new version
+ NetworkManager section added
+ screenshots partly updated and scaled

* Thu May 07 2009 Vladimir Zhukov <bertis@altlinux.org> 5.0-alt2
- new version
+ existent sections edited and expanded
+ new sections added

* Tue Apr 07 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt1
- initial build
