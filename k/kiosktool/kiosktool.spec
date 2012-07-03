%define qtdir %_qt3dir
%define kdedir %_K3prefix

Name: kiosktool
Version: 1.0
Release: alt2

Group: System/Configuration/Other
Summary: KIOSK administration admin tool
License: GPL
Url: http://extragear.kde.org/apps/kiosktool.php
Packager: Roman Savochenko <rom_as@altlinux.ru>

Requires: kdelibs >= %{get_version kdelibs}

Source: ftp://ftp.kde.org/pub/kde/stable/apps/KDE3.x/admin/kiosktool-%version.tar.gz
Patch1: tde-3.5.13-build-defdir-autotool.patch

# Automatically added by buildreq on Fri Mar 24 2006
#BuildRequires: doxygen fontconfig gcc-c++ gcc-g77 graphviz imake kdepim-devel kdepim-libs libjpeg-devel libpng-devel libXext-devel libXt-devel linux-libc-headers qt3-designer qt3-doc-html xml-utils xorg-cf-files

BuildRequires: doxygen gcc-c++ libjpeg-devel libpng-devel
BuildRequires: xml-utils kdelibs-devel libqt3-devel

%description
A Point and Click tool for system administrators to enable KDE's KIOSK features
or otherwise preconfigure KDE for groups of users.

%prep
%setup -q
%patch1

cp -Rp /usr/share/libtool/aclocal/libtool.m4 admin/libtool.m4.in
cp -Rp /usr/share/libtool/config/ltmain.sh admin/ltmain.sh
make -f admin/Makefile.common cvs ||:

%build
rm -rf %buildroot
export QTDIR=%qtdir
export KDEDIR=%kdedir

export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

%K3configure \
    --without-arts \
    --disable-debug \
    --enable-final \
    --disable-rpath \
    --enable-dependency-tracking \
    --enable-pch \
    
%make_build

%install
%K3install

%find_lang --with-kde %name

%files -f %name.lang
%doc ChangeLog README
#
%_K3bindir/%name
%_K3bindir/%name-kdedirs
%_K3xdg_apps/%name.desktop
%_K3apps/%name
%_K3iconsdir/crystalsvg/*/apps/%name.*

%changelog
* Fri May 25 2012 Roman Savochenko <rom_as@altlinux.ru> 1.0-alt2
- Build for TDE 3.5.13 release

* Fri Mar 24 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt1
- initial specfile
