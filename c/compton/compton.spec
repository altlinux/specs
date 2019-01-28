# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: compton
Version: 5
Release: alt1
Summary: fork of xcompmgr
Summary(ru_RU.UTF-8): Форк xcompmgr
License: MPL-2.0 or MIT
Group: System/X11
Url: https://github.com/yshui/compton
Source: %name-%version.tar

BuildRequires: meson
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libconfig-devel
BuildRequires: libpcre-devel
BuildRequires: libGL-devel
BuildRequires: libdbus-devel
BuildRequires: libev-devel
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(libxdg-basedir)

%description
Compton is a compositor for X, and a fork of xcompmgr-dana.

I was frustrated by the low amount of standalone lightweight compositors. 
Compton was forked from Dana Jansens' fork of xcompmgr and refactored. 
I fixed whatever bug I found, and added features I wanted. 
Things seem stable, but don't quote me on it. 
I will most likely be actively working on this until I get the features I want. 
This is also a learning experience for me. 
That is, I'm partially doing this out of a desire to learn Xlib. 

%description -l ru_RU.UTF-8
Лёгкий композитный менеджер окон. Является форком xcompmgr-dana, который в свою очередь
тоже является форком xcompmgr. В общем - исправленное и дополненое.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%files -f %name.lang
%_bindir/compton*
%_datadir/applications/%name.desktop
%_iconsdir/hicolor/*/*/*

%changelog
* Sun Jan 27 2019 Anton Midyukov <antohami@altlinux.org> 5-alt1
- new version 5
- fix license
- fix URL

* Fri Aug 01 2014 Konstantin Artyushkin <akv@altlinux.org> 0.1_beta2_1-alt3
- change Group

* Fri Aug 01 2014 Konstantin Artyushkin <akv@altlinux.org> 0.1_beta2_1-alt2
- update compton 

* Thu Aug 23 2012 bla-bla <bla-bla@gmail.com> - alt1
- This packeg was create with --no-sisyphus-chek parameter and can contains some mistakes
- Данный пакет был собран с параметрами --no-sisyphus-check и может содежать ошибки
