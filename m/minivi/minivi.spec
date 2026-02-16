Name: minivi
Version: 0.10.4
Release: alt1

Summary: A small application for viewing images

License: GPL-3.0-only
Group: Graphics

Url: https://altlinux.space/shad/minivi
Vcs: https://altlinux.space/shad/minivi

Source: %name-%version.tar
Source1: minivi.desktop

BuildRequires: lazarus

%description
A small application for viewing images.
Everything is minimalistic.
Functionality:
    closing the application by pressing Esc / Q / Ctrl + Q
    opening images, both when associating files and from the application by pressing Ctrl + O / O
    setting an image as a desktop background by pressing W
    deleting an image by pressing Del / D
    calling help by pressing F1
    switch images with arrows

%prep
%setup

%build
lazbuild src/minivi.lpi

%install
install -D src/%name %buildroot%_bindir/%name
install -Dm 0644 src/%name.png %buildroot%_iconsdir/hicolor/128x128/apps/%name.png
install -Dm 0644 %SOURCE1 %buildroot%_datadir/applications/%name.desktop

%files
%_bindir/%name
%_iconsdir/hicolor/128x128/apps/%name.png
%_datadir/applications/%name.desktop
%doc README.md

%changelog
* Mon Feb 16 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.10.4-alt1
- 0.10.3 -> 0.10.4
- changed Url tag

* Tue Feb 03 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.10.3-alt1
- 0.10.1 -> 0.10.3

* Mon Feb 02 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.10.1-alt1
- 0.10.0 -> 0.10.1

* Tue Jan 13 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.10.0-alt1
- Initial build for ALT Linux.

