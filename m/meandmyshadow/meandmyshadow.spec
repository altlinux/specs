Name: meandmyshadow
Version: 0.4.1
Release: alt3
License: GPLv3
Summary: Puzzle/platform game with two protagonists performing shared task
Url: http://meandmyshadow.sourceforge.net/
Source: %name-%version-src.tar.gz
Group: Games/Puzzles
Requires: %name-data = %version

# Automatically added by buildreq on Tue Mar 27 2012
# optimized out: cmake-modules libSDL-devel libstdc++-devel pkg-config
BuildRequires: cmake gcc-c++ libSDL_gfx-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libarchive-devel libcurl-devel libssl-devel

%description
Me and My Shadow is a puzzle/platform game written by Luka Horvat. The
author has given us permission to gpl the game, and develop it further.
It has an interesting concept and rather unique gameplay.

    18 different block types.
    Theme system
    Addon manager
    Cross platform

%package data
Group: Games/Puzzles
Summary: Data files for %name, %summary
BuildArch: noarch
%description data
Data files for %name, %summary

%prep
%setup
sed -i '/OpenGL REQUIRED/aINCLUDE(FindX11)' CMakeLists.txt

%build
%cmake -DHARDWARE_ACCELERATION=True
%make_build -C BUILD


%install
cp -al data BUILD
%makeinstall DESTDIR=%buildroot -C BUILD

for i in icons/*/%name.png; do
  d=$(basename $(dirname $i))
  install -D $i %buildroot%_iconsdir/hicolor/$d/apps/%name.png
done

%files
%doc docs
%_bindir/*
%dir %_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%files data
%_datadir/%name/*

%changelog
* Mon Jul 11 2016 Fr. Br. George <george@altlinux.ru> 0.4.1-alt3
- Fix DSO build

* Thu Dec 11 2014 Fr. Br. George <george@altlinux.ru> 0.4.1-alt2
- Rebuild with new SDL

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 0.4.1-alt1
- Autobuild version bump to 0.4.1

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.4-alt1.qa1
- NMU: rebuilt with libarchive.so.13.

* Tue Oct 23 2012 Fr. Br. George <george@altlinux.ru> 0.4-alt1
- Autobuild version bump to 0.4
- Fix build and cleanup spec from error-unaware subshells

* Tue Mar 27 2012 Fr. Br. George <george@altlinux.ru> 0.3-alt1
- Autobuild version bump to 0.3
- Native icons used

* Sun Jan 22 2012 Fr. Br. George <george@altlinux.ru> 0.2-alt1
- Autobuild version bump to 0.2
- Upstream installation procedure used
- Noarch package separated
