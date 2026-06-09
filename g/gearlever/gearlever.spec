%define _unpackaged_files_terminate_build 1
%define APP_ID it.mijorus.gearlever
%def_enable check

Name: gearlever
Version: 3.3.3
Release: alt3

Summary: Manage AppImages
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://mijorus.it/projects/gearlever/
Vcs: https://github.com/mijorus/gearlever
Source: %name-%version.tar
Patch: %name-%version-%release.patch

%add_python3_path %_datadir/%name

%filter_from_requires /^\/usr\/bin\/bash/d

AutoProv: nopython3

Requires: 7-zip

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: meson
BuildRequires: gtk4-update-icon-cache
BuildRequires: pkgconfig(gio-2.0)
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
BuildRequires: libgio
%endif

BuildArch: noarch

%description
An utility to manage AppImages with ease! Gear lever will organize
and manage AppImage files for you, generate desktop entries and
app metadata, update apps in-place or keep multiple versions side-by-side.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
rm %buildroot%_datadir/gearlever/gearlever/assets/demo.AppImage
install -Dm755 "build-aux/get_appimage_offset.sh" "%buildroot%_libexecdir/%name/get_appimage_offset"
%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/appdata/%APP_ID.appdata.xml
%_libexecdir/%name/get_appimage_offset
%_desktopdir/%APP_ID.desktop
%_datadir/%name
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_iconsdir/hicolor/scalable/actions
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg

%changelog
* Tue Jun 09 2026 Vladislav Petrukhin <vladp@altlinux.org> 3.3.3-alt3
- Remove p7zip dependency.

* Wed Jul 09 2025 Semen Fomchenkov <armatik@altlinux.org> 3.3.3-alt2
- Remove user manual (ALT #55037).
- Added 7-zip dependency (ALT #55043).

* Wed Jun 25 2025 Semen Fomchenkov <armatik@altlinux.org> 3.3.3-alt1
- New version 3.3.3

* Thu Mar 20 2025 Oleg Shchavelev <oleg@altlinux.org> 3.0.2-alt1
- New version 3.0.2
- Enable strict mode for unpackaged files
- Added p7zip dependency (ALT #53225)

* Fri Dec 06 2024 Oleg Shchavelev <oleg@altlinux.org> 2.3.2-alt1
- New version 2.3.2

* Sat Nov 30 2024 Oleg Shchavelev <oleg@altlinux.org> 2.3.1-alt1
- New version 2.3.1

* Fri Nov 22 2024 Oleg Shchavelev <oleg@altlinux.org> 2.2.1-alt2
- Add macro %%add_python3_path (ALT #52122)
- Rename macro %%__meson_test -> %%meson_test
- Update BuildRequires

* Mon Nov 18 2024 Oleg Shchavelev <oleg@altlinux.org> 2.2.1-alt1
- Initial build
