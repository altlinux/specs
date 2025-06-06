%define _unpackaged_files_terminate_build 1
%define app_id be.alexandervanhee.gradia
%def_enable check
%set_verify_elf_method fhs=relaxed

Name: gradia
Version: 1.2.1
Release: alt1
Epoch: 1

Summary: Make your screenshots ready for all
License: GPL-3.0-or-later
Group: Graphics

Url: https://github.com/AlexanderVanhee/Gradia
Vcs: https://github.com/AlexanderVanhee/Gradia
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-python3
BuildRequires: meson
BuildRequires: gtk4-update-icon-cache
BuildRequires: pkgconfig(gio-2.0)
%if_enabled check
BuildRequires: appstream
BuildRequires: desktop-file-utils
%endif

Requires: python3(gi)
Requires: python3(PIL)

%description
On social media, it's often hard to control how your images appear to others.
Transparent or oddly sized images, like screenshots often don't display well.
Fixing these issues can feel like more trouble than it's worth.

This tool aims to alleviate that problem by allowing you to quickly edit
images to address these issues, while also offering options to enhance their
overall appearance.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%_desktopdir/%app_id.desktop
%_datadir/dbus-1/services/%app_id.service
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/fonts/*
%doc README.md

%changelog
* Fri Jun 06 2025 David Sultaniiazov <x1z53@altlinux.org> 1:1.2.1-alt1
- Update to v1.2.1

* Wed May 28 2025 David Sultaniiazov <x1z53@altlinux.org> 20250528-alt1
- Initial build
