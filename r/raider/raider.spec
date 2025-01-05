%define APP_ID com.github.ADBeveridge.Raider
%def_enable check

Name: raider
Version: 3.0.2
Release: alt1

Summary: Permanently delete your files
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://apps.gnome.org/Raider
Vcs: https://github.com/ADBeveridge/raider
Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(gtk4) >= 4.12.0
BuildRequires: pkgconfig(libadwaita-1) >= 1.4.0
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
%endif

%description
File Shredder is a file deletion program designed to permanently remove
sensitive files from your computer, enhancing data privacy.

Within a certain limit, it is effective. However, modern SSDs use certain
technologies to extend its lifetime, which has the side effect of ensuring that
shredding is never perfect, and no software can fix that. But shredding
significantly increases the difficulty of data recovery since it requires
specialized software and hardware.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%APP_ID.desktop
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml

%changelog
* Sun Jan 05 2025 Oleg Shchavelev <oleg@altlinux.org> 3.0.2-alt1
- New version 3.0.2
- Update Vcs URL
- Update build dependencies

* Sat Oct 26 2024 Oleg Shchavelev <oleg@altlinux.org> 3.0.1-alt1
- Initial build
