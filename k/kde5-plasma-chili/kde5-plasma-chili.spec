%define themename chili

Name: kde5-plasma-%themename
Version: 0.5.5 
Release: alt1
Summary: Login theme for KDE Plasma
License: GPL-3
Group: Graphical desktop/KDE
Url: https://github.com/MarianArlt/kde-plasma-chili
Source: %name-%version.tar
Patch1: add-translate-for-buttons.patch
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildArch: noarch

%description
Chili is hot, just like a real chili! Spice up the login
experience for your users, your family and yourself.
Chili reduces all the clutter and leaves you with a clean,
easy to use, login interface with a modern yet classy touch.

%prep
%setup
%patch1 -p1

%install
mkdir -p %buildroot%_datadir/sddm/themes/%themename
install -m 0644 Background.qml %buildroot%_datadir/sddm/themes/%themename
install -m 0644 Login.qml %buildroot%_datadir/sddm/themes/%themename
install -m 0644 Main.qml %buildroot%_datadir/sddm/themes/%themename
install -m 0644 metadata.desktop %buildroot%_datadir/sddm/themes/%themename
install -m 0644 preview.png %buildroot%_datadir/sddm/themes/%themename
install -m 0644 SessionButton.qml %buildroot%_datadir/sddm/themes/%themename
install -m 0644 theme.conf %buildroot%_datadir/sddm/themes/%themename
cp -pr components %buildroot%_datadir/sddm/themes/%themename

%files
%_datadir/sddm/themes/%themename
%doc AUTHORS CREDITS LICENSE.md

%changelog
* Sun Apr 12 2020 Alexander Makeenkov <amakeenk@altlinux.org> 0.5.5-alt1
- Initial build for ALT
