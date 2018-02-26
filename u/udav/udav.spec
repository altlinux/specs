Name: udav
Version: 0.7.1.2
Release: alt1.1

Summary: UDAV is program for data visualization based on MathGL

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPLv2
Group: Sciences/Mathematics
Url: http://udav.sourceforge.net/

Source: http://prdownloads.sf.net/%name/%name-%version.tar

# Automatically added by buildreq on Sun Jan 03 2010
BuildRequires: gcc-c++ libgsl-devel libhdf5-devel libmathgl5-devel libqt4-devel

BuildPreReq: libmathgl5-devel >= 1.10

%description
UDAV is program for data arrays visualization based on MathGL library.
It support wide spectrum of graphics, simple script language and
visual data handling and editing. It has windows interface for data
viewing, changing and plotting. Also it can execute MGL scripts, setup
and rotate graphics and so on. MathGL is a free library of fast C++
routines for the plotting

%prep
%setup

%build
export QT4DIR=%_qt4dir
export PATH=$QT4DIR/bin:$PATH
%__subst "s|/usr/local|%_prefix|g" src/src.pro src/main.cpp src/prop_dlg.cpp src/udav_wnd.h
echo "INCLUDEPATH += $(pkg-config hdf5 --cflags | sed -e 's|-I||g')" >>src/src.pro
# use compat functions as in hdf5 1.6
echo "DEFINES += H5_USE_16_API" >>src/src.pro
qmake-qt4 udav.pro
# fix inlined qmake
#%__subst "s|/usr/bin/qmake|qmake-qt4|g" Makefile
%make_build
# MGLDOCDIR="%_docdir/udav/"

%install
%__make install INSTALL_ROOT=%buildroot
%find_lang %name

cat <<EOF >%buildroot%_desktopdir/UDAV.desktop
[Desktop Entry]
Encoding=UTF-8
Name=UDAV
Comment[en_US]=Data handling and plotting tool
Comment[ru_RU]=Обработка и отображение данных
Exec=%name
Icon=%name.png
Terminal=false
Type=Application
Categories=Application;Science;Math
EOF

%files -f %name.lang
%_bindir/udav
%doc TODO ChangeLog.txt
%_datadir/%name/
%_pixmapsdir/%name.png
%_desktopdir/UDAV.desktop

%changelog
* Sun May 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1.2-alt1.1
- Fixed build

* Thu Sep 08 2011 Vitaly Lipatov <lav@altlinux.ru> 0.7.1.2-alt1
- new version 0.7.1.2 (with rpmrb script)

* Mon Jan 24 2011 Vitaly Lipatov <lav@altlinux.ru> 0.7.0.1-alt1
- new version 0.7.0.1 (with rpmrb script)

* Tue Nov 09 2010 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt1
- new version 0.7 (with rpmrb script)

* Tue Nov 09 2010 Vitaly Lipatov <lav@altlinux.ru> 0.6.3-alt1
- new version 0.6.3 (with rpmrb script) (ALT bug #24482)

* Mon Jan 11 2010 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt2
- cleanup spec, fix icon placement

* Sun Jan 03 2010 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- new version (0.6) import in git

* Sun Jan 03 2010 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt1
- initial build for ALT Linux Sisyphus
