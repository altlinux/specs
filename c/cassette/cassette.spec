%define _unpackaged_files_terminate_build 1
%define xdg_name space.rirusha.Cassette

Name: cassette
Version: 0.2.1
Release: alt1

Summary: GTK/Adwaita application that allows you to use Yandex Music service on Linux operating systems
License: GPL-3.0
Group: Sound
Url: https://gitlab.gnome.org/Rirusha/Cassette
VCS: https://gitlab.gnome.org/Rirusha/Cassette

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

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
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc README.md
%_bindir/cassette
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.metainfo.xml
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/*.svg

%changelog
* Tue Mar 04 2025 Alexey Volkov <qualimock@altlinux.org> 0.2.1-alt1
- new version 0.2.1

* Fri Oct 4 2024 Alexey Volkov <qualimock@altlinux.org> 0.2.0-alt2
- Change upstream sources to the current (closes: #51091)

* Thu Jul 11 2024 Alexey Volkov <qualimock@altlinux.org> 0.2.0-alt1
- New version 0.2.0

* Sun Jan 28 2024 Alexey Volkov <qualimock@altlinux.org> 0.1.4-alt1
- New version 0.1.4

* Wed Jan 3 2024 Alexey Volkov <qualimock@altlinux.org> 0.1.1-alt1
- Initial build for ALT
