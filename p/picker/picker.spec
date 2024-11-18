%define APP_ID io.github.mezoahmedii.Picker
%def_enable check

Name: picker
Version: 1.1.1
Release: alt1

Summary: Randomly pick something to do
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://github.com/mezoahmedii/picker
Vcs: https://github.com/mezoahmedii/picker
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: meson
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(gio-2.0)
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
BuildRequires: libgio
%endif

BuildArch: noarch

%description
Picker is a simple app that can pick something for you from a list of things.
For example, if you can't decide what to have for dinner, put your favorite
meals in and let the Picker choose one for you.

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
%_datadir/applications/%APP_ID.desktop
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_iconsdir/hicolor/scalable/actions/*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml
%_datadir/%name

%changelog
* Fri Nov 15 2024 Oleg Shchavelev <oleg@altlinux.org> 1.1.1-alt1
- Initial build
