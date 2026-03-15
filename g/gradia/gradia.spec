%define _unpackaged_files_terminate_build 1
%define app_id be.alexandervanhee.gradia
# %set_verify_elf_method fhs=relaxed

Name: gradia
Version: 1.12.0
Release: alt1
Epoch: 1

Summary: Make your screenshots ready for all
License: GPL-3.0-or-later
Group: Graphics

Url: https://github.com/AlexanderVanhee/Gradia
Vcs: https://github.com/AlexanderVanhee/Gradia
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-python3
BuildRequires: meson
BuildRequires: appstream
BuildRequires: desktop-file-utils
BuildRequires: blueprint-compiler
BuildRequires: gtk4-update-icon-cache
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: typelib(GtkSource) = 5

Requires: python3(gi)
Requires: python3(PIL)
Requires: python3(cairo)
Requires: python3(gi._gi_cairo)
Requires: python3(pytesseract)
Requires: libwebp-pixbuf-loader

%description
On social media, it's often hard to control how your images appear to others.
Transparent or oddly sized images, like screenshots often don't display well.
Fixing these issues can feel like more trouble than it's worth.

This tool aims to alleviate that problem by allowing you to quickly edit
images to address these issues, while also offering options to enhance their
overall appearance.

%prep
%setup
%patch -p1

%build
%meson --buildtype=release
%meson_build

%install
%meson_install
%find_lang %name

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%_desktopdir/%app_id.desktop
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/fonts/*
%doc README.md

%changelog
* Sat Mar 07 2026 David Sultaniiazov <x1z53@altlinux.org> 1:1.12.0-alt1
- Update to v1.12.0.

* Thu Jul 24 2025 x1z53 <x1z53@altlinux.org> 1:1.7.1-alt1
- Update to v1.7.1
- Remove D-Bus service

* Sat Jun 07 2025 David Sultaniiazov <x1z53@altlinux.org> 1:1.4.0-alt1
- Update to v1.4.0

* Fri Jun 06 2025 David Sultaniiazov <x1z53@altlinux.org> 1:1.2.1-alt1
- Update to v1.2.1

* Wed May 28 2025 David Sultaniiazov <x1z53@altlinux.org> 20250528-alt1
- Initial build
