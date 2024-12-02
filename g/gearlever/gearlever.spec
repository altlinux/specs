%define APP_ID it.mijorus.gearlever
%def_enable check

Name: gearlever
Version: 2.3.1
Release: alt1

Summary: Manage AppImages
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://mijorus.it/projects/gearlever/
Vcs: https://github.com/mijorus/gearlever
Source: %name-%version.tar

%add_python3_path %_datadir/%name

AutoProv: nopython3

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

%build
%meson
%meson_build

%install
%meson_install
rm %buildroot%_datadir/gearlever/gearlever/assets/demo.AppImage
%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/appdata/%APP_ID.appdata.xml
%_desktopdir/%APP_ID.desktop
%_datadir/%name
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_iconsdir/hicolor/scalable/actions
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg

%changelog
* Sat Nov 30 2024 Oleg Shchavelev <oleg@altlinux.org> 2.3.1-alt1
- New version 2.3.1

* Fri Nov 22 2024 Oleg Shchavelev <oleg@altlinux.org> 2.2.1-alt2
- Add macro %%add_python3_path (ALT #52122)
- Rename macro %%__meson_test -> %%meson_test
- Update BuildRequires

* Mon Nov 18 2024 Oleg Shchavelev <oleg@altlinux.org> 2.2.1-alt1
- Initial build
