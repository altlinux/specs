Name: gnome-mastermind
Version: 0.3.1
Release: alt1

Summary: A Mastermind clone for GNOME Desktop

License: GPL
Group: Games/Arcade
Url: http://www.autistici.org/gnome-mastermind

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://download.gna.org/gnome-mastermind/%name-%version.tar.bz2

# Automatically added by buildreq on Sun Jan 04 2009
BuildRequires: gnome-doc-utils-xslt libGConf-devel libgtk+2-devel librarian perl-XML-Parser

# missed by buildreq
BuildPreReq: gnome-doc-utils

%description
GNOME Mastermind is a little Mastermind? game for linux that I've
written, mainly for fun, while I was learning some programming with gtk
and cairo. At first I was not intentioned to share it, but now I think
it has become quite stable so I decided to distribute it. I like it and
I hope someone else would like it too.

The goal of this game is to break a hidden color code following the hints
that the game gives us. Check the game manual for a better explanation
about how the game works and is played.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std
%find_lang %name --with-gnome

%files -f %name.lang
%_bindir/*
%_datadir/%name/
%_desktopdir/*
%_pixmapsdir/*
%_iconsdir/*/*/apps/*

%changelog
* Sun Jan 04 2009 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt1
- initial build for ALT Linux Sisyphus
