%define SVN r36
Name: qxkb
Version: 0.4.4
Release: alt1%SVN
License: GPLv2
Url: http://qxkb.googlecode.com
# svn checkout http://qxkb.googlecode.com/svn/trunk/ qxkb-read-only 
Source: %name-%version.tar.bz2
Group: System/X11
Summary: Qt keyboard layout switcher

# Automatically added by buildreq on Sun Jul 29 2012
# optimized out: cmake-modules fontconfig libICE-devel libSM-devel libX11-devel libXau-devel libXcursor-devel libXext-devel libXfixes-devel libXi-devel libXinerama-devel libXrandr-devel libXrender-devel libXtst-devel libXv-devel libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-xml libstdc++-devel xorg-kbproto-devel xorg-xproto-devel
BuildRequires: cmake gcc-c++ libXScrnSaver-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXft-devel libXpm-devel libXt-devel libXxf86vm-devel libxkbfile-devel phonon-devel qt4-designer xorg-xf86miscproto-devel

%description
The keypad switch written on Qt4.
Uses setxkbmap; The interface repeats kxkb;
Can use svg icon for indicate language layer.
This is bugfix %SVN build.

%prep
%setup

%build
%cmake
%make_build -C BUILD

%install
%makeinstall_std -C BUILD

%files
%doc COPYING NEWS README TODO
%_bindir/%name
%_datadir/%name
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.png

%changelog
* Sun Jul 29 2012 Fr. Br. George <george@altlinux.ru> 0.4.4-alt1r36
Bugfix SVN r63 update

* Sun Jul 29 2012 Fr. Br. George <george@altlinux.ru> 0.4.4-alt1
- Initial build from Mageia spec

