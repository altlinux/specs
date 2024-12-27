%def_enable check

%define nameU com.vixalien.sticky

Name:    sticky
Version: 0.2.6
Release: alt2

Summary: A simple sticky notes app for GNOME
License: MIT
Group:   Other

Url: https://github.com/vixalien/sticky
Vcs: https://github.com/vixalien/sticky

Source0: %name-%version.tar
Source1: gi-types.tar
Source2: node_modules.tar

ExclusiveArch: x86_64

BuildRequires(pre): rpm-macros-meson rpm-build-nodejs
BuildRequires: libgjs-devel yarn meson

%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils /usr/bin/glib-compile-schemas /usr/bin/gtk4-update-icon-cache /usr/bin/gtk-update-icon-cache}

%description
Sticky Notes is a simple note taking application for the GNOME desktop. It is written in GJS and uses GTK4.

%prep
%setup

tar -xf %SOURCE1 -C %_builddir/%name-%version/
tar -xf %SOURCE2 -C %_builddir/%name-%version/

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %nameU

%check
%__meson_test

%files -f %nameU.lang
%_bindir/%nameU
%_datadir/appdata/%nameU.appdata.xml
%_datadir/applications/%nameU.desktop
%_datadir/glib-2.0/schemas/%nameU.gschema.xml
%_iconsdir/hicolor/*/apps/%{nameU}*.svg
%_datadir/locale/*/LC_MESSAGES/%name-notes.mo
%_datadir/%name-notes/*
%doc *.md

%changelog
* Thu Dec 26 2024 Aleksandr Shamaraev <shad@altlinux.org> 0.2.6-alt2
- Fixed rebuild error.

* Tue Nov 26 2024 Aleksandr Shamaraev <shad@altlinux.org> 0.2.6-alt1
- Initial build for Sisyphus
