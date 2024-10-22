%define APP_ID com.github.flxzt.rnote
%def_disable check

Name: rnote
Version: 0.11.0
Release: alt1

Summary: Sketch and take handwritten notes
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://rnote.flxzt.net
Vcs: https://github.com/flxzt/rnote
Source0: %name-%version.tar
Source1: %name-vendor.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: cmake
BuildRequires: rust-cargo
BuildRequires: gcc-c++
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(appstream)
BuildRequires: pkgconfig(poppler-glib)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libxml-2.0)
%if_enabled check
BuildRequires: %_bindir/desktop-file-validate
BuildRequires: %_bindir/appstreamcli
BuildRequires: %_bindir/glib-compile-schemas
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

%install
%meson_install
%find_lang --with-gnome %name
echo '%%lang(zh-Hans) %_datadir/locale/zh_Hans/LC_MESSAGES/rnote.mo' >> %name.lang
echo '%%lang(zh-Hans) %_datadir/locale/zh_Hans/LC_MESSAGES/rnote.mo' >> %name.lang

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%APP_ID.desktop
%_datadir/fonts/rnote-fonts
%_datadir/glib-2.0/schemas/%{APP_ID}.gschema.xml
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_iconsdir/hicolor/scalable/mimetypes/application-rnote.svg
%_datadir/metainfo/%APP_ID.metainfo.xml
%_datadir/mime/packages/%APP_ID.xml
%_datadir/%name

%changelog
* Tue Oct 22 2024 Oleg Shchavelev <oleg@altlinux.org> 0.11.0-alt1
- Initial build
