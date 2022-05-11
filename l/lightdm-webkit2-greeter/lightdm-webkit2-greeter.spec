Name:     lightdm-webkit2-greeter
Version:  3.4.1
Release:  alt1.3

Summary:  A modern, visually appealing greeter for LightDM.
License:  GPL-3.0
Group:    Other
Url:      https://github.com/JezerM/web-greeter

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

ExcludeArch: aarch64 armh ppc64le

Source:   %name-%version.tar

Patch: lightdm-webkit2-greeter-3.4.1-makefile.patch

%add_findprov_skiplist %_libdir/web-greeter/*.py
%add_findreq_skiplist %_libdir/web-greeter/*.py

%add_python3_path   %_libdir/web-greeter/bridge/__init__.py

BuildRequires(pre): rpm-build-python3


# Automatically added by buildreq on Mon May 09 2022
# optimized out: libgpg-error libqt5-core libqt5-xml libxcb-devel pkg-config python3 python3-base python3-module-PyQt5 python3-module-PyQt5-sip sh4 xorg-proto-devel
BuildRequires: libX11-devel python3-module-PyQt5-devel rsync zsh

BuildRequires: python3-module-pygobject3-devel python3-module-PyQtWebEngine python3-module-ruamel-yaml
BuildRequires: python3-module-pyinotify qt5-webengine-devel gem-gobject-introspection-devel libxcb-devel
BuildRequires: liblightdm-gobject lightdm-gir-devel lightdm-devel
BuildRequires: bash-completion zsh-completions

BuildRequires: /usr/bin/python3 

%description
A modern, visually appealing greeter for LightDM, that allows to create web based themes with HTML, CSS and JavaScript.
This is a fork of the Antergos web-greeter that tries to fix and improve this project for a modern and current use. Due to this, some API changes are needed, which implies that current themes would need to do changes to work correctly.
Also, check out nody-greeter, a greeter made in Node.js with Electron! (Actually, faster than Web Greeter)\

%prep
%setup
%make clean
%patch -p1

subst 's,\<lib\>,%_lib,g' Makefile


%build
#configure
%make

%install
%makeinstall_std


#check
#make check

%files
%_sysconfdir/lightdm/Xgreeter
%_sysconfdir/lightdm/web-greeter.yml
%_sysconfdir/xdg/lightdm/lightdm.conf.d/90-greeter-wrapper.conf

%_bindir/web-greeter

%dir %_libdir/web-greeter/
%_libdir/web-greeter/*

%_datadir/applications/*
%_datadir/bash-completion/*
%_datadir/metainfo/*
%_datadir/web-greeter/*
%_datadir/xgreeters
%_datadir/zsh/site-functions/*

%_docdir/web-greeter/*

%_man1dir/*
%doc *.md

%changelog
* Tue May 10 2022 Hihin Ruslan <ruslandh@altlinux.ru> 3.4.1-alt1.3
- add add_find(prov/req)_skiplist

* Mon May 09 2022 Hihin Ruslan <ruslandh@altlinux.ru> 3.4.1-alt1
- Initial build for Sisyphus

