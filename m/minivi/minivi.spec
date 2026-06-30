%define _unpackaged_files_terminate_build 1

Name: minivi
Version: 0.17.2
Release: alt1

Summary: A small application for viewing images

License: GPL-3.0-only
Group: Graphics

Url: https://altlinux.space/shad/minivi
Vcs: https://altlinux.space/shad/minivi

Source: %name-%version.tar

Requires: libwebp-tools ImageMagick-tools libheif

BuildRequires: lazarus qt6pas-devel

%description
A small application for viewing images.
Everything is minimalistic.
Functionality:
	- closing the application by pressing Esc / Q / Ctrl + Q / mouse wheel
	- opening images, both when associating files and from the application by pressing Ctrl + O / O
	- setting an image as a desktop background by pressing W
	- information about the image I
	- deleting an image by pressing Del / D
	- calling help by pressing F1
	- switch images using arrows or the right/left mouse button
	- zoom/unzoom using the mouse wheel, or +/- (may not work in tiling)

%prep
%setup
subst 's|/usr/bin|%buildroot%_bindir|' Makefile
subst 's|/usr/share|%buildroot%_datadir|' Makefile

%build
make build

%install
make install

%files
%doc README.md
%_bindir/%{name}*
%_iconsdir/hicolor/*/apps/%name.png
%_datadir/applications/%name.desktop

%changelog
* Tue Jun 30 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.17.2-alt1
- 0.17.1 -> 0.17.2

* Fri Jun 26 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.17.1-alt1
- 0.17.0 -> 0.17.1

* Fri Jun 26 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.17.0-alt1
- 0.16.0 -> 0.17.0

* Fri May 29 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.16.0-alt1
- 0.15.2 -> 0.16.0

* Fri May 22 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.15.2-alt1
- 0.15.1 -> 0.15.2

* Tue May 19 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.15.1-alt1
- 0.15.0 -> 0.15.1

* Mon May 18 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.15.0-alt1
- 0.14.0 -> 0.15.0
- migrated to qt6

* Thu Apr 23 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.14.0-alt1
- 0.13.0 -> 0.14.0

* Tue Mar 31 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.13.0-alt1
- 0.12.2 -> 0.13.0

* Mon Mar 09 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.12.2-alt1
- 0.12.1 -> 0.12.2

* Sat Feb 28 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.12.1-alt1
- 0.11.0 -> 0.12.1

* Mon Feb 23 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.11.0-alt1
- 0.10.5 -> 0.11.0

* Fri Feb 20 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.10.5-alt1
- 0.10.4 -> 0.10.5

* Mon Feb 16 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.10.4-alt1
- 0.10.3 -> 0.10.4
- changed Url tag

* Tue Feb 03 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.10.3-alt1
- 0.10.1 -> 0.10.3

* Mon Feb 02 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.10.1-alt1
- 0.10.0 -> 0.10.1

* Tue Jan 13 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.10.0-alt1
- Initial build for ALT Linux.

