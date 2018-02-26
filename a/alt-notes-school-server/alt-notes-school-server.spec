Name: alt-notes-school-server
Version: 4.1
Release: alt3

Summary: Linux School Server 4.1 distribution license and relnotes
License: Distributable
Group: Documentation
Packager: Artem Zolochevskiy <azol@altlinux.ru>

Source: %name-%version-%release.tar

BuildArch: noarch

Conflicts: alt-notes-children
Conflicts: alt-notes-desktop
Conflicts: alt-notes-hpc
Conflicts: alt-notes-junior
Conflicts: alt-notes-junior-sj
Conflicts: alt-notes-junior-sm
Conflicts: alt-notes-server-lite
Conflicts: alt-notes-skif
Conflicts: alt-notes-terminal

%description
Linux School Server 4.1 distribution license and release notes.

%prep
%setup

%install
install -d %buildroot%_datadir/alt-notes
install -pm0644 *.html %buildroot/%_datadir/alt-notes/

%files
%_datadir/alt-notes/*

%changelog
* Sun Jan 11 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt3
- add Conflicts to alt-notes packages (reported by repocop)

* Sun Dec 07 2008 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt2
- fix xhtml markup

* Sat Dec 06 2008 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt1
- initial build for Sisyphus

