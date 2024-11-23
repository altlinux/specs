%define APP_ID com.github.geigi.cozy
%def_enable check

Name: cozy
Version: 1.3.0
Release: alt2

Summary: Listen to audio books
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://cozy.sh
Vcs: https://github.com/geigi/cozy/
Source: %name-%version.tar

Requires: python3-modules-sqlite3

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: meson
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: python3-module-distro
BuildRequires: python3-module-peewee
BuildRequires: python3-module-mutagen
BuildRequires: python3-module-pygobject3
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
BuildRequires: libgio
%endif

BuildArch: noarch

%description
Do you like audio books? Then lets get cozy!

Cozy is a audio book player. Here are some of the features:

* Import all your audio books into Cozy to browse them comfortably
* Listen to your DRM free mp3, m4b, m4a (aac, ALAC), flac,
ogg and wav audio books
* Remembers your playback position
* Sleep timer
* Playback speed control for each book individually
* Search your library
* Multiple storage location support
* Offline Mode! This allows you to keep an audio book on your internal
storage if you store your audio books on an external or network drive.
Perfect to listen to on the go!
* Drag and Drop to import new audio books
* Sort your audio books by author, reader and name

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %APP_ID

%check
%meson_test

%files -f %APP_ID.lang
%python3_sitelibdir/%name/
%_bindir/%APP_ID
%_desktopdir/%APP_ID.desktop
%_datadir/%APP_ID
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_iconsdir/hicolor/scalable/actions/*.svg
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.appdata.xml

%changelog
* Sat Nov 23 2024 Oleg Shchavelev <oleg@altlinux.org> 1.3.0-alt2
- Add python3-modules-sqlite3 dependency from Requires (ALT #52135)
- Rename macro %%__meson_test -> %%meson_test
- Update BuildRequires

* Sun Nov 17 2024 Oleg Shchavelev <oleg@altlinux.org> 1.3.0-alt1
- Initial build
