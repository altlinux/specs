Name: lordsawar
Version: 0.3.1
Release: alt1

Summary: Turn-based strategy game in a fantasy setting
License: GPLv2+
Group: Games/Arcade

Url: http://www.nongnu.org/lordsawar/

Source: %name-%version.tar
Patch1: %name-%version-upstream-gstreamer-1.0.patch

BuildRequires: gcc-c++ intltool libgtkmm3-devel
BuildRequires: libxslt-devel libxml++2-devel libarchive-devel libgstreamermm1.0-devel

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
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/*
%_man6dir/*

%files data
%_desktopdir/*
%_datadir/appdata/%name-appdata.xml
%_datadir/%name
%_iconsdir/hicolor/*/apps/*

%changelog
* Wed Nov 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.1-alt1
- Updated to stable upstream version 0.3.1.

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.0-alt1.2.1
- Rebuilt for gcc5 C++11 ABI.

* Fri Dec 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.2
- Fixed build with gcc 4.7

* Fri Jul 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.1
- Fixed build

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
