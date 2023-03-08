%define _unpackaged_files_terminate_build 1

Name:    gwe
Version: 0.15.5
Release: alt2

Summary: System utility designed to provide information, control the fans and overclock your NVIDIA card
License: GPL-3.0
Group:   Other
Url:     https://gitlab.com/leinardi/gwe

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar
# https://gitlab.com/leinardi/gwe/-/merge_requests/73
Patch: AyatanaAppIndicator3.patch

BuildArch: noarch

BuildRequires(pre): meson
BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-gir
BuildRequires: gobject-introspection-devel

%add_python3_req_skip gi.repository.GObject

# require typelib(AyatanaAppIndicator3) instead typelib(AppIndicator3)
%add_typelib_req_skiplist typelib(AppIndicator3)

%description
GWE is a GTK system utility designed to provide information, control the fans
and overclock your NVIDIA video card and graphics processor.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%doc *.md
%_bindir/gwe
%python3_sitelibdir/gwe
%_desktopdir/*.desktop
%_datadir/metainfo/*.appdata.xml
%_datadir/dbus-1/services/*.service
%_datadir/glib-2.0/schemas/*.gschema.xml
%_datadir/gwe
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/symbolic/apps/*.svg

%changelog
* Mon Mar 06 2023 Anton Midyukov <antohami@altlinux.org> 0.15.5-alt2
- NMU: add patch for AyatanaAppIndicator3 support

* Mon Jun 06 2022 Andrey Cherepanov <cas@altlinux.org> 0.15.5-alt1
- Initial build for Sisyphus.
