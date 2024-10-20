%define APP_ID io.github.fkinoshita.Telegraph
%def_enable check

Name: telegraph
Version: 0.1.8
Release: alt1
BuildArch: noarch

Summary: Write and decode morse
License: GPL-3.0-only
Group: Graphical desktop/GNOME

Url: https://github.com/fkinoshita/Telegraph
Vcs: https://github.com/fkinoshita/Telegraph
Source: %name-%version.tar

%add_python3_path %_datadir/%name

AutoProv: nopython3

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: rpm-build-gir
BuildRequires: rpm-build-python3
BuildRequires: pkgconfig(libadwaita-1)
%if_enabled check
BuildRequires: %_bindir/desktop-file-validate
BuildRequires: %_bindir/appstream-util
BuildRequires: %_bindir/glib-compile-schemas
%endif

%description
Telegraph is a simple Morse translator, start typing your message to see
the resulting Morse code and vice versa.

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
%_datadir/%name
%_desktopdir/%APP_ID.desktop
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_datadir/metainfo/%APP_ID.metainfo.xml

%changelog
* Sun Oct 20 2024 Oleg Shchavelev <oleg@altlinux.org> 0.1.8-alt1
- Initial build
