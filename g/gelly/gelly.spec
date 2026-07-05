%define _unpackaged_files_terminate_build 1
%define oname io.m51.Gelly

Name: gelly
Version: 1.9.0
Release: alt1

Summary: A native music client for Jellyfin and Navidrome/Subsonic
License: GPL-3.0-or-later
Group: Sound

Url: https://github.com/Fingel/gelly
VCS: https://github.com/Fingel/gelly

Source: %name-%version.tar
Source1: vendor.tar

Patch: i18n-1.6.2-alt-fix.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust pkgconfig(glib-2.0) pkgconfig(gio-2.0)
BuildRequires: pkgconfig(pango) pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(cairo-gobject) pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gtk4) pkgconfig(gstreamer-audio-1.0)
BuildRequires: pkgconfig(libadwaita-1) pkgconfig(dbus-1) gettext-tools
BuildRequires: libseccomp-devel /usr/bin/glib-compile-resources

%description
%summary. Built with Rust and GTK.

%prep
%setup -a1
%patch -p0
%rust_prep

%build
%rust_build
pushd resources
glib-compile-resources resources.gresource.xml
popd

%install
%rust_install

install -Dm 0644 resources/%oname.desktop %buildroot%_desktopdir/%oname.desktop
install -Dm 0644 resources/%oname.metainfo.xml %buildroot%_datadir/metainfo/%oname.metainfo.xml
install -Dm 0644 resources/%oname.gschema.xml %buildroot%_datadir/glib-2.0/schemas/%oname.gschema.xml
install -Dm 0644 resources/resources.gresource %buildroot%_datadir/%name/%oname.gresource
install -Dm 0644 resources/%oname.svg %buildroot%_iconsdir/hicolor/128x128/apps/%oname.svg

for locale in po/*.po; do
 dirname=$(basename "$locale" .po)
 mkdir -p %buildroot%_datadir/locale/${dirname}/LC_MESSAGES
 msgfmt -o "%buildroot%_datadir/locale/${dirname}/LC_MESSAGES/%name.mo" "$locale"
done

%find_lang --all-name %name

%files -f %name.lang
%doc *.md LICENSE
%_bindir/%name
%_desktopdir/%oname.desktop
%_datadir/metainfo/%oname.metainfo.xml
%_datadir/glib-2.0/schemas/%oname.*
%_datadir/%name/%oname.gresource
%_iconsdir/hicolor/128x128/apps/%oname.svg

%changelog
* Mon Jul 06 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.9.0-alt1
- 1.8.0 -> 1.9.0

* Fri Jun 26 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.8.0-alt1
- 1.7.0 -> 1.8.0

* Thu Jun 18 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.7.0-alt1
- automatic build: 1.6.2 -> 1.7.0

* Sun Jun 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.6.2-alt2
- fixed: locale path

* Sun Jun 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.6.2-alt1
- Initial build for ALT Linux.

