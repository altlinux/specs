Name: lordsawar
Version: 0.2.0
Release: alt1

Summary: Turn-based strategy game in a fantasy setting
License: GPLv2+
Group: Games/Arcade

Url: http://www.nongnu.org/lordsawar/
Source: http://download.savannah.gnu.org/releases-noredirect/lordsawar/lordsawar-%version.tar.gz
Patch1: lordsawar-0.1.7-asneeded.patch

# Automatically added by buildreq on Sat Mar 12 2011
BuildRequires: boost-devel-headers gcc-c++ intltool libSDL_mixer-devel libexpat-devel libgnet-devel libgtkmm2-devel libtar-devel zlib-devel

# For gnome_helpdir definition:
BuildPreReq: rpm-build-gnome

Requires: %name-data = %version

%description
LordsAWar! is a turn-based strategy game set in a fantasy setting. The goal of
this project is to make a game that is similar to Warlords II.

%package data
Summary: Data files for lordsawar game
Group: Games/Arcade
BuildArch: noarch

%description data
Data files for lordsawar game.

%prep
%setup
%patch1 -p1

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

subst 's/.png//' %buildroot%_desktopdir/lordsawar.desktop

%files -f %name.lang
%_bindir/*

%files data
%_desktopdir/*
%_datadir/lordsawar
%gnome_helpdir/lordsawar
%_iconsdir/hicolor/*/apps/*

%changelog
* Sat Mar 26 2011 Victor Forsiuk <force@altlinux.org> 0.2.0-alt1
- 0.2.0

* Sat Mar 12 2011 Victor Forsiuk <force@altlinux.org> 0.1.9-alt2
- Refresh BuildRequires.

* Thu Jul 08 2010 Victor Forsiuk <force@altlinux.org> 0.1.9-alt1
- 0.1.9

* Thu Mar 25 2010 Victor Forsiuk <force@altlinux.org> 0.1.8-alt1
- 0.1.8

* Tue Mar 09 2010 Victor Forsiuk <force@altlinux.org> 0.1.7-alt1
- 0.1.7
- Move architecture-independent files to noarch subpackage.

* Tue Oct 27 2009 Victor Forsyuk <force@altlinux.org> 0.1.6-alt1
- Initial build.
