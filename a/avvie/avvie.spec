%define APP_ID com.github.taiko2k.avvie
# Validate appstream file FAIL
%def_disable check

Name: avvie
Version: 2.4
Release: alt1

Summary: Quick and easy image cropping
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://github.com/Taiko2k/avvie
Vcs: https://github.com/Taiko2k/avvie
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: meson
BuildRequires: python3-module-piexif
BuildRequires: python3-module-pycairo
BuildRequires: python3-module-Pillow
BuildRequires: python3-module-pygobject3
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
%endif

BuildArch: noarch

%description
A simple tool for cropping and downsizing images. Suitable for avatars
or cropping photos for use as desktop wallpapers. Convert PNG to JPG.
Export in one click to your Pictures folder.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/appdata/%APP_ID.appdata.xml
%_datadir/applications/%APP_ID.desktop
%_datadir/%name
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg

%changelog
* Mon Nov 18 2024 Oleg Shchavelev <oleg@altlinux.org> 2.4-alt1
- Initial build
