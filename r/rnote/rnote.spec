%define APP_ID com.github.flxzt.rnote
%def_enable check

Name: rnote
Version: 0.14.2
Release: alt1

Summary: Sketch and take handwritten notes
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://rnote.flxzt.net
Vcs: https://github.com/flxzt/rnote
Source0: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: rpm-build-cmake
BuildRequires: rust-cargo
BuildRequires: gcc-c++
BuildRequires: pkgconfig(glib-2.0) >= 2.76
BuildRequires: pkgconfig(gio-2.0) >= 2.76
BuildRequires: pkgconfig(cairo) >= 1.18
BuildRequires: pkgconfig(appstream)
BuildRequires: pkgconfig(poppler-glib)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libxml-2.0)
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
BuildRequires: libgio
%endif

ExcludeArch: %ix86

%description
Rnote is a vector-based drawing app for sketching, handwritten notes and
to annotate documents and pictures.

Disclaimer: The file format is still unstable. It might change and break
compatibility between versions.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

%build
%meson
%meson_build

%install
%meson_install
# drop unknown languages, find known
rm -r %buildroot%_datadir/locale/zh_Han{s,t}
%find_lang --with-gnome %name
# add menu sub-categories (repocop freedesktop-categories)
sed -i 's/^Categories=GNOME;GTK;Graphics;$/Categories=GNOME;GTK;Graphics;2DGraphics;VectorGraphics;/' \
	%buildroot%_desktopdir/%APP_ID.desktop

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_bindir/%name-cli
%_desktopdir/%APP_ID.desktop
%_datadir/fonts/rnote-fonts
%_datadir/glib-2.0/schemas/%{APP_ID}.gschema.xml
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_iconsdir/hicolor/scalable/mimetypes/application-rnote.svg
%_datadir/metainfo/%APP_ID.metainfo.xml
%_datadir/mime/packages/%APP_ID.xml
%_datadir/%name
%_datadir/thumbnailers/%name.thumbnailer

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 0.14.2-alt1
- NMU: new version 0.14.2
- Package rnote-cli and the thumbnailer
- Replace BuildRequires: cmake with rpm-build-cmake
- Add 2DGraphics and VectorGraphics menu categories (repocop)

* Wed Nov 20 2024 Oleg Shchavelev <oleg@altlinux.org> 0.11.0-alt2
- Rebuild improved spec (ALT #51842)
- Add macro %%meson_build, rename macro %%__meson_test -> %%meson_test
- Update BuildRequires
- Drop unknown languages, find known
- Enable check

* Tue Oct 22 2024 Oleg Shchavelev <oleg@altlinux.org> 0.11.0-alt1
- Initial build
