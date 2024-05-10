%def_enable snapshot

%define _name Annotator
%define ver_major 1.2
%define rdn_name com.github.phase1geo.annotator

# No tests defined
%def_enable check

Name: annotator
Version: %ver_major.1
Release: alt1

Summary: Image annotation for Elementary OS
License: GPL-2.0-or-later
Group: Graphics
Url: https://github.com/phase1geo/Annotator
Vcs: https://github.com/phase1geo/Annotator.git

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Patch1: annotator-1.2.1-alt-no-gtk3-dep.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson vala-tools
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libportal-gtk4)
BuildRequires: pkgconfig(pangocairo)
%{?_enable_check:BuildRequires: /usr/bin/appstream-util desktop-file-utils /usr/bin/glib-compile-schemas}

%description
Annotate your images and let a picture say 1000 words.

- Load image from the file system or clipboard.
- Add shapes, stickers, text, drawings, and other callouts to highlight image details.
- Add magnifiers to enhance image details.
- Blur out portions of the image to obfuscate data.
- Crop, resize and add image borders.
- Control colors, line thickness and font details.
- Zoom support.
- Unlimited undo/redo of any change.
- Export to JPEG, PNG, TIFF, BMP, PDF and SVG image formats.
- Support for copying annotated image to clipboard.
- Printer support.

%prep
%setup -n %{?_enable_snapshot:%name}%{?_disable_snapshot:%_name}-%version
%patch1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %rdn_name

%check
%__meson_test

%files -f %rdn_name.lang
%_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.appdata.xml
%doc AUTHORS* README* TODO


%changelog
* Fri May 10 2024 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- first build for Sisyphus (1.2.1-62-gdf6f74d)


