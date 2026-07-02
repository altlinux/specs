%define _unpackaged_files_terminate_build 1
%define oname net.trowell.typesetter

Name: typesetter
Version: 0.14.0
Release: alt1

Summary: A minimalist, local-first Typst editor
License: GPL-3.0-only
Group: Editors
Url: https://typesetter.trowell.net
VCS: https://codeberg.org/haydn/typesetter

Source: %name-%version.tar
Source1: vendor.tar
 
BuildRequires(pre): rpm-build-rust rpm-macros-meson
BuildRequires: /proc
BuildRequires: pkgconfig(glib-2.0) pkgconfig(gio-2.0)
BuildRequires: pkgconfig(pango) pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(cairo-gobject) pkgconfig(gtk4)
BuildRequires: pkgconfig(graphene-gobject-1.0) meson
BuildRequires: pkgconfig(gtksourceview-5) pkgconfig(openssl)
BuildRequires: pkgconfig(libspelling-1) pkgconfig(libadwaita-1)
BuildRequires: /usr/bin/appstreamcli libzstd-devel

%description
Typesetter is a lightweight desktop application for creating beautiful documents with Typst.
- Adaptive, user-friendly interface: Focus on writing. Great for papers, reports, slides, books, and any structured writing.
- Powered by Typst: A modern markup-based typesetting language, combining the simplicity of Markdown with the power of LaTeX.
- Local-first: Your files stay on your machine. No cloud lock-in.
- Package support: Works offline, but can fetch and update packages online when needed.
- Automatic preview: See your rendered document update as you write.
- Click-to-jump: Click on a part of the preview to jump to the corresponding position in the source file.
- Magnifier tool: Click and hold on the preview to inspect fine details.
- Centered scrolling: Keeps your writing visually anchored as you type.
- Syntax highlighting: Makes your documents easier to read and edit.
- Document statistics: Easily calculate page, word, and character counts.
- Fast and native: Built in Rust and GTK following the GNOME human interface guidelines.

%prep
%setup -a1
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

sed -i 's/pages.len()/pages().len()/g' src/typst_system/mod.rs

%build
export ZSTD_SYS_USE_PKG_CONFIG=1
%meson
%meson_build

%install
%meson_install

%find_lang %name --all-name

%files -f %name.lang
%doc *.md COPYING LICENSE
%_bindir/%name
%_datadir/applications/%oname.desktop
%_datadir/dbus-1/services/%oname.service
%_datadir/fonts/Typesetter*.ttf
%_datadir/fonts/Source*.ttf
%_datadir/glib-2.0/schemas/%oname.gschema.xml
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/metainfo/%oname.metainfo.xml
%_datadir/mime/packages/typst.xml
%_datadir/%name

%changelog
* Thu Jul 02 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.14.0-alt1
- 0.13.5 -> 0.14.0

* Sat Jun 06 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.13.5-alt1
- updated from 0.13.4 to 0.13.5

* Wed Jun 03 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.13.4-alt1
- 0.13.3 -> 0.13.4

* Sun May 31 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.13.3-alt1
- 0.13.2 -> 0.13.3

* Sat May 30 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.13.2-alt1
- 0.13.1 -> 0.13.2

* Wed May 20 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.13.1-alt1
- 0.13.0 -> 0.13.1

* Fri May 15 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.13.0-alt1
- 0.12.6 -> 0.13.0

* Tue Apr 28 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.12.6-alt1
- 0.12.5 -> 0.12.6

* Fri Apr 24 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.12.5-alt1
- 0.12.4 -> 0.12.5

* Wed Apr 22 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.12.4-alt1
- 0.12.3 -> 0.12.4

* Tue Mar 31 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.12.3-alt1
- 0.12.2 -> 0.12.3

* Fri Mar 27 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.12.2-alt1
- 0.11.4 -> 0.12.2

* Fri Mar 13 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.11.4-alt1
- 0.11.3 -> 0.11.4

* Wed Mar 11 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.11.3-alt1
- 0.11.2 -> 0.11.3

* Thu Mar 05 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.11.2-alt1
- 0.11.1 -> 0.11.2

* Sat Feb 28 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.11.1-alt1
- 0.11.0 -> 0.11.1

* Thu Feb 26 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.11.0-alt1
- 0.10.1 -> 0.11.0

* Tue Feb 17 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.10.1-alt1
- 0.10.0 -> 0.10.1

* Thu Feb 12 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.10.0-alt1
- 0.9.1 -> 0.10.0

* Wed Jan 21 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.1-alt1
- 0.9.0 -> 0.9.1

* Wed Jan 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.0-alt1
- 0.8.4 -> 0.9.0

* Tue Dec 30 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.8.4-alt1
- 0.8.3 -> 0.8.4

* Thu Dec 25 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.8.3-alt1
- Initial build for Sisyphus.

