%def_disable snapshot
%define _name blanket
%define ver_major 0.7
%define rdn_name com.rafaelmardojai.Blanket

%def_enable check

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: Listen to ambient sounds
License: GPL-3.0-or-later
Group: Sound
Url: https://apps.gnome.org/Blanket
Vcs: https://github.com/rafaelmardojai/blanket.git

%if_disabled snapshot
Source: https://github.com/rafaelmardojai/blanket/archive/%version/%name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

BuildArch: noarch

%add_python3_path %_datadir/%_name

Requires: typelib(Gtk) = 4.0
Requires: typelib(Adw) = 1

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson blueprint-compiler typelib(Adw)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils /usr/bin/glib-compile-schemas}

%description
Improve focus and increase your productivity by listening to different
ambient sounds. Or allows you to fall asleep in a noisy environment.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %_name

%check
%__meson_test

%files -f %_name.lang
%_bindir/%_name
%_desktopdir/%rdn_name.desktop
%_datadir/%_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Mon Apr 08 2024 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0

* Fri Nov 25 2022 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt2
- updated to 0.6.0-34-g9b0a1dc

* Sun Apr 17 2022 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Mon Apr 11 2022 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt2
- updated to 0.5.0-65-gaf542e4 (fixed for GStreamer-1.20)

* Thu Jan 27 2022 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus (0.5.0-31-g148df25)



