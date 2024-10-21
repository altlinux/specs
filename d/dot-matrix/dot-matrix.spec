%define APP_ID io.github.lainsce.DotMatrix
%def_enable check

Name: dot-matrix
Version: 3.2.0
Release: alt1

Summary: Convert between currencies
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://github.com/lainsce/dot-matrix
Vcs: https://github.com/lainsce/dot-matrix
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= 0.59.0
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(libadwaita-1)
%if_enabled check
BuildRequires: %_bindir/desktop-file-validate
BuildRequires: %_bindir/appstream-util
%endif

%description
Make out icons, glyphs, or anything you can create with lines in this grid
of dots
* Select whetether to draw with lines or curves.
* Quit anytime with the shortcut Ctrl + Q
* Undo with the shortcut Ctrl + Z
* Change line thickness by +5 or -5 with the respective shortcuts Ctrl + X
and Ctrl + Shift + X

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %APP_ID

%check
%__meson_test

%files -f %APP_ID.lang
%_bindir/%APP_ID
%_desktopdir/%APP_ID.desktop
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_datadir/icons/hicolor/scalable/actions/*.svg
%_datadir/icons/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml

%changelog
* Wed Oct 16 2024 Oleg Shchavelev <oleg@altlinux.org> 3.2.0-alt1
- Initial build
