Name: compton
Version: 0.1_beta2_1
Release: alt3
Summary: fork of xcompmgr
Summary(ru_RU.UTF-8): Форк xcompmgr
License: GPL
Group: System/X11
Url: https://github.com/chjj/compton.git
Source: %name-%version.tar.gz
#Patch: 
BuildRequires: rpm-utils libX11-devel libXcomposite-devel libXdamage-devel
BuildRequires: libXfixes-devel libXrender-devel pkg-config xorg-xproto-devel
BuildRequires: libXext-devel libXrandr-devel libXinerama-devel libpcre-devel
BuildRequires: libconfig-devel libdrm-devel libGL-devel libdbus-devel asciidoc
BuildRequires: asciidoc-a2x
#Requires
#Conflicts:
#Obsoletes:
#Provides:

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

%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/compton*
%_mandir/man1/compton*
%_datadir/applications/%name.desktop

%changelog
* Fri Aug 01 2014 Konstantin Artyushkin <akv@altlinux.org> 0.1_beta2_1-alt3
- change Group

* Fri Aug 01 2014 Konstantin Artyushkin <akv@altlinux.org> 0.1_beta2_1-alt2
- update compton 

* Thu Aug 23 2012 bla-bla <bla-bla@gmail.com> - alt1
- This packeg was create with --no-sisyphus-chek parameter and can contains some mistakes
- Данный пакет был собран с параметрами --no-sisyphus-check и может содежать ошибки
