Name: outwiker
Version: 1.9.0.790
Release: alt1

Summary: OutWiker is designed to store notes in a tree

License: GPL3
Group: Text tools
Url: http://jenyay.net/Soft/Outwiker

Packager: Vitaly Lipatov <lav@altlinux.ru>

# ource-url:https://github.com/Jenyay/outwiker/archive/unstable_%version.tar.gz
# Source-url: https://github.com/Jenyay/outwiker/archive/release_%version.tar.gz
Source: %name-%version.tar

Requires: python-module-wx

BuildArch: noarch

%description
OutWiker is designed to store notes in a tree. Such programs are called
"outliner", personal wiki, or tree-like editors. OutWiker's main difference
from the other similar programs is keeping the tree of notes in the form of
directories on disk, and encouraging changing the base by external sources
and programs. Also any number of files can be attached to the page. OutWiker
can contain pages of different types, currently supports two types of pages:
plain text and HTML, but the number of types of pages will increase in future.


%prep
%setup
# 2.0 hack
#rm -rf need_for_build/{linux,windows}
#cp -a need_for_build/debian_debsource/* .

%__subst "s|\r$||g" src/runoutwiker.py
%__subst "s|LD_PRELOAD.* python2.7|python2.7|" %name

%build
%make_build

%install
%makeinstall_std

%find_lang %name

%files
#-f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%_iconsdir/hicolor/*/apps/*
%_man1dir/*
%_mandir/ru/man1/*
%_pixmapsdir/*

%changelog
* Tue Sep 27 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.0.790-alt1
- new version 1.9.0.790 (with rpmrb script) (ALT bug #32526)

* Tue Sep 27 2016 Vitaly Lipatov <lav@altlinux.ru> 2.0.0.800-alt1
- new version 2.0.0.800 (with rpmrb script) (ALT bug #32526)

* Wed May 30 2012 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- initial build for ALT Linux Sisyphus

