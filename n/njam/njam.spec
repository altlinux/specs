Name: njam
Version: 1.25
Release: alt1

Summary: Njam is fast-paced cross-platform pacman-like game written in C++ using SDL library

License: GPL
Group: Games/Arcade
Url: http://njam.sourceforge.net

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name-%version-src.tar

# Automatically added by buildreq on Mon Jan 03 2011
BuildRequires: gcc-c++ libSDL_image-devel libSDL_mixer-devel libSDL_net-devel

%description
Njam is fast-paced cross-platform pacman-like game written in C++ using
SDL library

Features
- Single and multiplayer mode (local or network)
- Duel games (players compete each other to get more points)
- Cooperative games (players cooperate to finish as many levels as they can)
- Great music and sound effects
- Runs on Linux, Windows, NetBSD, FreeBSD, BeOS, and probably more platforms
- Customizable level skins
- Many different levels
- Integrated level editor
- Open Source (GPL Licence)

%prep
%setup -n %name-%version-src
%__subst "s|LogFile::LogFile|LogFile|g" src/njamedit.cpp

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_datadir/%name/

%changelog
* Mon Jan 03 2011 Vitaly Lipatov <lav@altlinux.ru> 1.25-alt1
- fix build, cleanup spec, update buildreqs

* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.25-alt0.1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for njam
  * postclean-05-filetriggers for spec file

* Sat Jan 07 2006 Vitaly Lipatov <lav@altlinux.ru> 1.25-alt0.1
- initial build for ALT Linux Sisyphus
