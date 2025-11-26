%define _unpackaged_files_terminate_build 1
%def_enable check
%define app_id io.github.wartybix.Constrict

Name: constrict
Version: 25.10
Release: alt1
Summary: Compress videos to target sizes
Group: Video
License: GPL-3.0-or-later
Url: https://github.com/Wartybix/Constrict
Vcs: https://github.com/Wartybix/Constrict

BuildArch: noarch

Source0: %name-%version.tar

Requires: ffmpeg
Requires: ffprobe

BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-python3
BuildRequires: meson
BuildRequires: blueprint-compiler
BuildRequires: desktop-file-utils
BuildRequires: appstream
BuildRequires: libgio
BuildRequires: libgtk4

%description
Constrict compresses your videos to your chosen file size - useful for uploading
to services with specific file size limits. No more relying on online services
for video compression, or the manual trial-and-error of reencoding
at various bitrates yourself.

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
%_datadir/%name/%name/*.py
%_datadir/%name/%name.gresource
%_datadir/dbus-1/services/%app_id.service
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/symbolic/apps/%app_id-symbolic.svg
%_iconsdir/hicolor/scalable/apps/%app_id.svg

%changelog
* Mon Nov 24 2025 Vladislav Petrukhin <vladp@altlinux.org> 25.10-alt1
- Initial build.
