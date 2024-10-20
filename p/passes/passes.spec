%define APP_ID me.sanchezrodriguez.passes
%def_enable check

Name: passes
Version: 0.10
Release: alt1

Summary: Manage your digital passes
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://github.com/pablo-s/passes
Vcs: https://github.com/pablo-s/passes
Source: %name-%version.tar

%add_python3_path %_datadir/%name

AutoProv: nopython3

BuildRequires(pre): rpm-macros-meson rpm-macros-python3
BuildRequires: meson >= 0.59.0
BuildRequires: cmake
BuildRequires: blueprint-compiler
BuildRequires: rpm-build-python3
BuildRequires: rpm-build-gir
BuildRequires: zint-devel
BuildRequires: pkgconfig(gio-2.0)
%if_enabled check
BuildRequires: %_bindir/desktop-file-validate
BuildRequires: %_bindir/appstream-util
BuildRequires: %_bindir/glib-compile-schemas
%endif

%description
Passes is a handy app that helps you manage all your digital passes
effortlessly. With Passes, you can conveniently store your boarding passes,
coupons, loyalty cards, event tickets, and more, all in PKPass or esPass format.

Moreover, the app seamlessly adjusts to different screen sizes, allowing you
to access your passes on various devices, whether it's a desktop computer
or a mobile phone.

Stop wasting time searching through your email or printing out your digital
passes. Download Passes now and keep all your passes in one convenient location.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_libdir/%name
%_desktopdir/%APP_ID.desktop
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_iconsdir/hicolor/scalable/actions/*.svg
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml
%_datadir/mime/packages/%APP_ID.espass.xml
%_datadir/%name

%changelog
* Sun Oct 20 2024 Oleg Shchavelev <oleg@altlinux.org> 0.10-alt1
- Initial build
