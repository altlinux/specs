%def_enable snapshot
%define _name blanket
%define ver_major 0.5
%define rdn_name com.rafaelmardojai.Blanket

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: Listen to different sounds
License: GPL-3.0-or-later
Group: Sound
Url: https://github.com/rafaelmardojai/blanket

Vcs: https://github.com/rafaelmardojai/blanket.git
Source: %_name-%version.tar

BuildArch: noarch

%add_python3_path %_datadir/%_name

Requires: typelib(Gtk) = 4.0
Requires: typelib(Adw) = 1

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson /usr/bin/appstream-util desktop-file-utils

%description
Improve focus and increase your productivity by listening to different
sounds. Or allows you to fall asleep in a noisy environment.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %_name

%files -f %_name.lang
%_bindir/%_name
%_desktopdir/%rdn_name.desktop
%_datadir/%_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Thu Jan 27 2022 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus (0.5.0-31-g148df25)


