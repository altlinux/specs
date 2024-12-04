%define APP_ID io.github.nokse22.ultimate-tic-tac-toe
%def_enable check

Name: ultimate-tic-tac-toe
Version: 1.0.2
Release: alt1

Summary: (Tic Tac Toe)2
License: GPL-3.0-or-later
Group: Games/Puzzles

Url: https://github.com/Nokse22/ultimate-tic-tac-toe
Vcs: https://github.com/Nokse22/ultimate-tic-tac-toe
Source: %name-%version.tar

%add_python3_path %_datadir/%name

AutoProv: nopython3

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: meson
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: gtk4-update-icon-cache
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
BuildRequires: libgio
%endif

BuildArch: noarch

%description
Play with your friends or against the algorithm. You can read the rules in the
game.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%APP_ID.desktop
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_datadir/%name
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml

%changelog
* Tue Dec 03 2024 Oleg Shchavelev <oleg@altlinux.org> 1.0.2-alt1
- Initial build
