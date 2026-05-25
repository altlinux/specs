%define oname solitaire
%define oname2 org.gnome.gitlab.wwarner.Solitaire

Name: gnome-games-solitaire
Version: 50.2
Release: alt1

Summary: GNOME Solitaire game
License: GPL-3.0-or-later and LGPL-3.0-only
Group: Games/Boards

Url: https://gitlab.gnome.org/wwarner/Solitaire
VCS: https://gitlab.gnome.org/wwarner/Solitaire

Source0: %name-%version.tar
Source1: vendor.tar

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-meson
BuildRequires: /proc rust-cargo meson cmake
BuildRequires: pkgconfig(glib-2.0) pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1) blueprint-compiler
BuildRequires: /usr/bin/appstreamcli pkgconfig(libxml-2.0)

%description
%summary.

%prep
%setup -a1

mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%meson -Dbuildtype=release
%meson_build

%install
%meson_install

%find_lang %oname --with-gnome --all-name

%files -f %oname.lang
%doc *.md COPYING COPYING.LGPL3
%_bindir/%oname
%_desktopdir/%oname2.desktop
%_datadir/dbus-1/services/%oname2.service
%_datadir/glib-2.0/schemas/%oname2.gschema.xml
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/metainfo/%oname2.*.xml
%_datadir/%oname

%changelog
* Mon May 25 2026 Aleksandr Shamaraev <shad@altlinux.org> 50.2-alt1
- 50.1 -> 50.2

* Thu May 21 2026 Aleksandr Shamaraev <shad@altlinux.org> 50.1-alt2
- updated license

* Wed May 20 2026 Aleksandr Shamaraev <shad@altlinux.org> 50.1-alt1
- Initial build for ALT Linux.

