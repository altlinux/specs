Name: lightdm-webkit2-greeter
Version: 3.5.2
Release: alt1

Summary: A modern, visually appealing greeter for LightDM
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/JezerM/web-greeter

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

ExcludeArch: ppc64le

Requires: lightdm
Provides: lightdm-greeter

Requires: python3-module-ruamel-yaml python3-module-PyQt5 python3-module-PyQtWebEngine python3-module-pygobject3 liblightdm-gobject
Requires: accountsservice

Source: %name-%version.tar
Source1: %name.conf

Patch: lightdm-webkit2-greeter-3.4.1-makefile.patch
Patch1: lightdm-webkit2-greeter-3.4.1-basedir.patch
Patch2: lightdm-webkit2-greeter-3.4.1-opt.patch
Patch3: lightdm-webkit2-greeter-3.5.1-dia.patch

%add_python3_path   %_libdir/web-greeter
%add_python3_req_skip gi.repository.GLib

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires(pre): rpm-build-intro >= 1.9.18
BuildRequires(pre): rpm-macros-nodejs >= 0.20.5

BuildRequires: rpm-build-nodejs

# Automatically added by buildreq on Mon May 16 2022
# optimized out: libgpg-error libqt5-core libqt5-xml libxcb-devel pkg-config python3 python3-base python3-module-PyQt5 python3-module-PyQt5-sip sh4 xorg-proto-devel
BuildRequires: libX11-devel python3-module-PyQt5-devel rsync zsh

BuildRequires: python3-module-pygobject3-devel python3-module-PyQtWebEngine python3-module-ruamel-yaml npm
BuildRequires: python3-module-pyinotify qt5-webengine-devel gem-gobject-introspection-devel libxcb-devel
BuildRequires: liblightdm-gobject lightdm-gir-devel lightdm-devel node-typescript
BuildRequires: bash-completion zsh-completions

BuildRequires: %_bindir/python3

%description
A modern, visually appealing greeter for LightDM, that allows to create web based themes with HTML, CSS and JavaScript.
This is a fork of the Antergos web-greeter that tries to fix and improve this project for a modern and current use. Due to this, some API changes are needed, which implies that current themes would need to do changes to work correctly.
Also, check out nody-greeter, a greeter made in Node.js with Electron! (Actually, faster than Web Greeter)

%prep
%setup
%__subst 's|\(#\!%_bindir/env python\)$|\13|' src/bridge/*.py

%make clean
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%__subst 's,\<lib\>,%_lib,g' Makefile

%build
#set -m
#%npm_build
#npm i -g typescript

#configure
%make

%install
%makeinstall_std

install -m 644 %SOURCE1 %buildroot%_sysconfdir/lightdm/

#check
#make check

%files
%config(noreplace) %_sysconfdir/lightdm/%name.conf

%_sysconfdir/lightdm/Xgreeter
%_sysconfdir/lightdm/web-greeter.yml
%config(noreplace) %_sysconfdir/xdg/lightdm/lightdm.conf.d/90-greeter-wrapper.conf

%_bindir/web-greeter

%dir %_libdir/web-greeter/
%_libdir/web-greeter/*

%_desktopdir/*
%_datadir/bash-completion/*
%_datadir/metainfo/*
%_datadir/web-greeter/*
%_datadir/xgreeters/*
%_datadir/zsh/site-functions/*

%_iconsdir/*/*/*/*

%_docdir/web-greeter/*

%_man1dir/*
%doc *.md

%changelog
* Sun Jan 29 2023 Hihin Ruslan <ruslandh@altlinux.ru> 3.5.2-alt1
- New Version

* Sun Jan 29 2023 Hihin Ruslan <ruslandh@altlinux.ru> 3.5.1-alt3
- Build to Sisyphus

* Sat Jan 7 2023 Sergey Markov <sergey@markow.su> 3.5.1-alt2
- Add lightdm-webkit2-greeter-3.5.1-dia.patch

* Sun Dec 11 2022 Sergey Markov <sergey@markow.su> 3.5.1-alt1
- New version

* Mon May 16 2022 Hihin Ruslan <ruslandh@altlinux.ru> 3.4.1-alt5
- Add Requres accountsservice, thanks zerg@

* Sun May 15 2022 Hihin Ruslan <ruslandh@altlinux.ru> 3.4.1-alt4
- Added Spec fix by aris@, thanks to him

* Sat May 14 2022 Hihin Ruslan <ruslandh@altlinux.ru> 3.4.1-alt3
- Add lightdm-webkit2-greeter.conf
- Add lightdm-webkit2-greeter-3.4.1-opt.patch

* Fri May 13 2022 Hihin Ruslan <ruslandh@altlinux.ru> 3.4.1-alt2
- Add lightdm-webkit2-greeter-3.4.1-basedir.patch

* Tue May 10 2022 Hihin Ruslan <ruslandh@altlinux.ru> 3.4.1-alt1.3
- add add_find(prov/req)_skiplist

* Mon May 09 2022 Hihin Ruslan <ruslandh@altlinux.ru> 3.4.1-alt1
- Initial build for Sisyphus
