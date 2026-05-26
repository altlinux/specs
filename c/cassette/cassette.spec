%define _unpackaged_files_terminate_build 1
%define xdg_name space.rirusha.Cassette

Name: cassette
Version: 0.2.4
Release: alt1

Summary: GTK/Adwaita application that allows you to use Yandex Music service on Linux operating systems
License: GPL-3.0
Group: Sound
Url: https://altlinux.space/rirusha/Cassette
VCS: https://altlinux.space/rirusha/Cassette

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

Requires: xdg-dbus-proxy
Requires: libGLES

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(webkitgtk-6.0)

BuildRequires: gir(Adw) = 1

%description
%summary.

%prep
%setup
%autopatch -p1

%ifarch %e2k
sed -i "s/subdir('tests')/# subdir('tests')/" meson.build
%endif

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
* Tue May 26 2026 Alexey Volkov <qualimock@altlinux.org> 0.2.4-alt1
- new version 0.2.4 (closes: #57610)

* Tue Oct 21 2025 Alexey Volkov <qualimock@altlinux.org> 0.2.1.g49-alt1
- new version 0.2.1.g49

* Mon Jun 09 2025 Michael Shigorin <mike@altlinux.org> 0.2.1-alt2
- E2K: tests ftbfs workaround (Anton Palgunov)

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
