%define _unpackaged_files_terminate_build 1
%define xdg_name io.github.Rirusha.Cassette

Name: cassette
Version: 0.2.0
Release: alt1

Summary: GTK/Adwaita application that allows you to use Yandex Music service on Linux operating systems
License: GPL-3.0
Group: Sound
Url: https://github.com/Rirusha/Cassette
VCS: https://github.com/Rirusha/Cassette

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson cmake vala
BuildRequires: blueprint-compiler
BuildRequires: libgtk4-devel libadwaita-gir-devel libadwaita-devel
BuildRequires: libjson-glib-devel
BuildRequires: libsqlite3-devel
BuildRequires: libgee-devel libxml2-devel
BuildRequires: libgstreamer1.0-gir-devel libgio-devel
BuildRequires: libwebkitgtk6.0-devel

%description
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc README.md
%_bindir/cassette
%_datadir/appdata/%xdg_name.appdata.xml
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/*.svg

%changelog
* Thu Jul 11 2024 Alexey Volkov <qualimock@altlinux.org> 0.2.0-alt1
- New version 0.2.0

* Sun Jan 28 2024 Alexey Volkov <qualimock@altlinux.org> 0.1.4-alt1
- New version 0.1.4

* Wed Jan 3 2024 Alexey Volkov <qualimock@altlinux.org> 0.1.1-alt1
- Initial build for ALT
