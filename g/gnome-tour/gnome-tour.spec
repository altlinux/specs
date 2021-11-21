%define ver_major 41
%define beta .rc
%define xdg_name org.gnome.Tour

%def_disable intro
%define welcome_video altlinux-initial-intro.webm

Name: gnome-tour
Version: %ver_major
Release: alt0.9%beta

Summary: GNOME Tour and Greeter
Group: Graphical desktop/GNOME
License: GPL-3.0
Url: https://gitlab.gnome.org/GNOME/gnome-tour

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
# https://pagure.io/fedora-workstation/issue/175
%{?_enable_intro:Source1: %welcome_video}

Requires: /etc/os-release

BuildRequires(pre): rpm-macros-meson
BuildRequires: /proc meson rust rust-cargo
BuildRequires: pkgconfig(gio-2.0) >= 2.64
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gstreamer-1.0) > 1.12
BuildRequires: pkgconfig(gstreamer-video-1.0)
BuildRequires: pkgconfig(gstreamer-player-1.0)
BuildRequires: pkgconfig(libhandy-1) >= 1.0

%description
A guided tour and greeter for GNOME.

%prep
%setup -n %name-%version%beta

%build
%meson \
    %{?_enable_intro:-Dvideo_path=%_datadir/%name/%welcome_video}
%nil
%meson_build

%install
%meson_install
# install ALTLinux video
%{?_enable_intro:install -pD -m 0644 %SOURCE1 %buildroot%_datadir/gnome-tour/%welcome_video}
%find_lang %name

%check
%meson_test

%files -f %name.lang
%_bindir/gnome-tour
%_datadir/applications/%xdg_name.desktop
%_datadir/icons/hicolor/scalable/apps/%xdg_name.svg
%_datadir/icons/hicolor/symbolic/apps/%xdg_name-symbolic.svg
%_datadir/metainfo/%xdg_name.metainfo.xml
%{?_enable_intro:
%dir %_datadir/%name
%_datadir/%name/%welcome_video}
%doc NEWS README.md


%changelog
* Sun Sep 05 2021 Yuri N. Sedunov <aris@altlinux.org> 41-alt0.9.rc
- 41.rc

* Tue Mar 23 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- first build for Sisyphus


