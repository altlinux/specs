%define oname page.codeberg.M23Snezhok.Vinyl
%define nameU vinyl-player

Name: vinyl
Version: 1.4.1
Release: alt1

Summary: Simple adwaita audio player
License: GPL-3.0-only
Group: Sound

Url: https://codeberg.org/M23Snezhok/Vinyl
VCS: https://codeberg.org/M23Snezhok/Vinyl

Source: %name-%version.tar
Source1: vendor.tar
Source2: %oname.desktop
 
BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: pkgconfig(glib-2.0) pkgconfig(gio-2.0)
BuildRequires: pkgconfig(pango) pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(cairo-gobject) pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gtk4) pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gstreamer-video-1.0)
BuildRequires: pkgconfig(gstreamer-play-1.0)

%description
Simple adwaita music player, developed on relm4 and gst-rs

Vinyl inspired by another music player, Amberol. In other
words, it just plays music. Nothing superfluous.

One of the most important aim of Vinyl is a simple codebase
that does not lag behind or overtake Amberol in functionality.
Relm4 and GstPlayApi are responsible for this.

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
%rust_build

%install
install -D target/release/%nameU %buildroot%_bindir/%nameU
install -Dm 644 %SOURCE2 %buildroot%_desktopdir/%oname.desktop
install -Dm 644 data/%oname.metainfo.xml \
	%buildroot%_datadir/metainfo/%oname.metainfo.xml
install -Dm 644 data/hicolor/scalable/apps/%oname.svg \
	%buildroot%_iconsdir/hicolor/128x128/apps/%oname.svg

%files
%doc *.md LICENSE
%_bindir/%nameU
%_desktopdir/%oname.desktop
%_datadir/metainfo/%oname.metainfo.xml
%_iconsdir/hicolor/128x128/apps/%oname.svg

%changelog
* Wed Jun 10 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.4.1-alt1
- autobuild: 1.4.0 -> 1.4.1

* Sun Jun 07 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.4.0-alt1
- 1.3.2 -> 1.4.0

* Sat May 02 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.3.2-alt1
- 1.3.1 -> 1.3.2

* Wed Apr 29 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.3.1-alt1
- 1.3.0 -> 1.3.1

* Fri Apr 24 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.3.0-alt1
- 1.2.2 -> 1.3.0

* Sat Apr 04 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.2.2-alt1
- 1.2.1 -> 1.2.2

* Thu Apr 02 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.2.1-alt1
- 1.2.0 -> 1.2.1

* Fri Mar 27 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.2.0-alt1
- 1.1.0 -> 1.2.0

* Wed Mar 18 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.1.0-alt1
- 1.0.1 -> 1.1.0

* Sat Mar 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.0.1-alt1
- Initial build for ALT Linux.

