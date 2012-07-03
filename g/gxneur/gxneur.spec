%define oname gXNeur

Name: gxneur
Version: 0.15.0
Release: alt1.1

Summary: GTK frontend for X Neural Switcher

License: GPL
Group: Office
Url: http://xneur.ru/

Source: %name-%version.tar.bz2
Source1: %name.png
Patch0: %name-0.15.0-alt-libX11.patch
Patch1: %name-0.15.0-alt-glib2.patch

# Automatically added by buildreq on Sun May 22 2011
# optimized out: fontconfig fontconfig-devel glib2-devel libX11-devel libaspell-devel libatk-devel libcairo-devel libdbus-glib libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgtk+2-devel libpango-devel libpcre-devel pkg-config xorg-kbproto-devel xorg-xproto-devel
BuildRequires: libGConf libGConf-devel libglade-devel libxneur-devel

Requires: xneur >= %version

%description
Xneur is program like Punto Switcher, but has other
functionality and features for configuring.

%prep
%setup
%patch0 -p2
%patch1 -p2

%build
# autoreconf breaks on ALT 4.1
%configure
%make_build

%install
%makeinstall_std
rm -rf %buildroot%prefix/doc/
%find_lang %name

install -Dm 0644 %SOURCE1 %buildroot%_pixmapsdir/%name.png
mkdir -p %buildroot%_desktopdir/
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=gXNeur
GenericName=Keyboard Layout Switcher
GenericName[ru]=Переключатель раскладки клавиатуры
Type=Application
Exec=gxneur
Icon=gxneur
Categories=GTK;Utility
Comment=Automatic keyboard layout switcher
Comment[ru]=Автоматический переключатель раскладки клавиатуры
StartupNotify=false
Terminal=false
EOF

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/gxneur
%_datadir/%name/
%_man1dir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*
%_iconsdir/hicolor/scalable/apps/%name.*
%_pixmapsdir/%name.png

%changelog
* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.0-alt1.1
- Fixed build with new libX11

* Tue Jan 10 2012 Fr. Br. George <george@altlinux.ru> 0.15.0-alt1
- Autobuild version bump to 0.15.0

* Tue Jun 28 2011 Fr. Br. George <george@altlinux.ru> 0.13.0-alt1
- Autobuild version bump to 0.13.0

* Tue Jun 27 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.8-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gxneur

* Mon Mar 29 2010 Vitaly Lipatov <lav@altlinux.ru> 0.9.8-alt1
- new version 0.9.8 (with rpmrb script)

* Wed Jan 13 2010 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt2
- fix build

* Sat Nov 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- new version 0.9.7 (with rpmrb script)

* Sun Oct 11 2009 Vitaly Lipatov <lav@altlinux.ru> 0.9.6-alt1
- new version 0.9.6
- add .desktop and icon

* Sun Nov 02 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt1
- new version 0.9.2 (with rpmrb script)

* Fri Jul 25 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt2
- release version 0.9.1

* Wed Jul 02 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- 0.9.1 (svn revision 162)
- cleanup spec, update buildreqs

* Thu Oct 11 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt1
- new version 0.8.0 (with rpmrb script)

* Wed Sep 19 2007 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt1
- new version 0.6.2 (with rpmrb script)

* Sat May 19 2007 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- new version 0.6.1 (with rpmrb script)

* Tue Apr 24 2007 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- new version 0.6.0 (with rpmrb script)

* Wed Mar 14 2007 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt1
- new version 0.5.0, update buildreq

* Tue Jan 23 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt0.1
- new version 0.4.0 (with rpmrb script)

* Thu Dec 21 2006 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1
- new version (0.3.0)

* Sun Oct 15 2006 Vitaly Lipatov <lav@altlinux.ru> 0.1.0_1-alt1
- initial build for Sisyphus
