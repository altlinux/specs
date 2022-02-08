# -*- coding: utf-8 -*-
Name: calibre
Version: 5.36.0
Release: alt1

Summary: A e-book library management application
Summary(ru_RU.UTF8): Программа для работы с личной электронной библиотекой

License: GPLv2
Group: File tools
Url: http://calibre-ebook.com/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# https://calibre-ebook.com/dist/src redirect to
# Source-url: http://download.calibre-ebook.com/%version/calibre-%version.tar.xz
Source: %name-%version.tar
Source1: calibre-mount-helper

Patch: calibre-no-update.patch
Patch1: calibre-0.8.55-alt-no-macmenu.patch

AutoProv:yes,nopython3
ExclusiveArch: %qt5_qtwebengine_arches

Requires: fonts-ttf-core
Requires: xkeyboard-config

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro >= 1.9.19
BuildRequires(pre): rpm-macros-qt5-webengine

# FIXME: hack
%add_python3_req_skip calibre.ebooks.markdown.__main__

# Windows's modules
%add_python3_req_skip win32serviceutil win32service win32event win32con win32com win32api win32gui winerror _winreg pywintypes pythoncom usbobserver calibre_extensions.winsapi

# internal extensions?
%add_python3_req_skip calibre_extensions calibre_extensions.fast_css_transform calibre_extensions.freetype calibre_extensions.progress_indicator calibre_extensions.speedup

%add_python3_path %_libdir/%name

BuildRequires: chrpath
BuildRequires: /proc

BuildRequires: cmake gcc-c++ libX11-devel libXext-devel libXrender-devel libjpeg-devel libsqlite3-devel
BuildRequires: libusb-devel >= 1.0.22

####### Building headless QPA plugin #######
#Project MESSAGE: This project is using private headers and will therefore be tied to this specific Qt module build version.
#Project MESSAGE: Running this project against other versions of the Qt modules may crash at any arbitrary point.
#Project MESSAGE: This is not a bug, but a result of using Qt internals. You have been warned!
#make: *** No rule to make target '/usr/lib64/libQt5ThemeSupport.a', needed by '/usr/src/RPM/BUILD/calibre/src/calibre/plugins/libheadless.so'.  Stop.
BuildRequires: qt5-base-devel-static glibc-devel-static


BuildRequires: qt5-base-devel
# >= 5.13
BuildRequires: qt5-svg-devel qt5-declarative-devel qt5-imageformats qt5-webchannel-devel qt5-location-devel qt5-x11extras-devel qt5-wayland-devel qt5-sensors-devel qt5-webengine-devel

BuildRequires: xdg-utils >= 1.0.2

BuildRequires: libpoppler-qt5-devel >= 0.20.2
# TODO: new version 20.08.0
BuildRequires: libpoppler-devel >= 0.76.1
BuildRequires: libpodofo-devel >= 0.9.6
BuildRequires: libwmf-devel >= 0.2.8
BuildRequires: libchm-devel >= 0.40
# upstream uses 6.7
BuildRequires: libicu-devel >= 5.6
BuildRequires: libmtp-devel >= 1.1.17

%py3_use dbus >= 1.2.16
BuildRequires: libdbus-devel >= 1.10.8
# https://bugzilla.altlinux.org/show_bug.cgi?id=39224
BuildRequires: libdbus-glib-devel >= 0.110
BuildRequires: optipng >= 0.7.7
Requires: optipng >= 0.7.7


# missed in the official list
BuildRequires: glib2-devel fontconfig-devel libfreetype-devel libssl-devel libudev-devel

BuildRequires: python3
Requires: python3

BuildRequires: python3-modules-curses

BuildRequires: libmtdev-devel libts-devel libinput-devel libxkbcommon-devel

BuildRequires: zlib-devel bzlib-devel
BuildRequires: libexpat >= 2.2.4
BuildRequires: libffi-devel >= 3.3
BuildRequires: libwebp-devel >= 1.1.0
BuildRequires: libpng-devel >= 1.6.37
BuildRequires: libjxr-devel >= 0.2.1
# iconv?
BuildRequires: libxml2-devel >= 2.9.10
BuildRequires: libxslt-devel >= 1.1.34
BuildRequires: libgpg-error-devel >= 1.36
# TODO:
BuildRequires: libgcrypt-devel >= 1.8.6

BuildRequires: libhunspell-devel >= 1.7.0
BuildRequires: libhyphen-devel >= 2.8.8
# TODO: 2.1.0
BuildRequires: libstemmer-devel

# Checked 12.07.2021 with
# https://github.com/kovidgoyal/build-calibre/blob/master/scripts/sources.json
# calibre/bypy/sources.json

%py3_use six >= 1.15.0
%py3_use unrardll >= 0.1.3
%py3_use lxml >= 4.5.2
%py3_use pychm >= 0.8.6
%py3_use html5-parser >= 0.4.9
%py3_use css-parser >= 1.0.6
%py3_use dateutil >= 2.8.1
%py3_use jeepney >= 0.6.0
#py3_use dns >= 2.0.0
%py3_use dns
%py3_use mechanize >= 0.4.5
%py3_use feedparser >= 5.2.1
%py3_use markdown >= 3.2.2
%py3_use html2text >= 2020.1.16
# no need really
%py3_use soupsieve >= 2.0.1
# TODO: bs4 >= 4.7.1
%py3_use beautifulsoup4 >= 4.9.1
%py3_use regex >= 2020.07.14
%py3_use chardet >= 3.0.4
%py3_use cchardet >= 2.1.7
%py3_use msgpack >= 1.0.0
%py3_use Pygments >= 2.6.1
%py3_use pycryptodome >= 3.9.8
# https://bugzilla.altlinux.org/40472
%py3_use apsw > 3.35.4-alt1.r1
%py3_use webencodings >= 0.5.1
%py3_use html5lib >= 1.1
%py3_use Pillow >= 7.2.0
%py3_use netifaces >= 0.10.9
%py3_use psutil >= 5.7.2
%py3_use ifaddr >= 0.1.7
%py3_use texttable >= 1.6.3
# TODO: build it
#py3_use py7zr >= 0.11.1
%py3_use zeroconf >= 0.31.0
%py3_use toml >= 0.10.1
%py3_use pyparsing >= 2.4.7
%py3_use packaging >= 20.4

%py3_buildrequires sip6 >= 5.5.0
%py3_buildrequires PyQt-builder >= 1.6.0
%py3_buildrequires PyQt5-sip >= 12.8.1
BuildRequires: python3-module-PyQt5-devel
%py3_use PyQt5 >= 5.15.2
%py3_use PyQtWebEngine >= 5.15.2

#py3_use dukpy
# TODO: p3_use mozjpeg 3.3.1

# TODO: https://github.com/brailcom/speechd >= 0.10.1


%description
calibre is an e-book library manager. It can view, convert and catalog e-books
in most of the major e-book formats. It can also talk to e-book reader
devices. It can go out to the internet and fetch metadata for your books.
It can download newspapers and convert them into e-books for convenient
reading. It is cross platform, running on Linux, Windows and OS X.

%description -l ru_RU.UTF8
Calibre - свободная программа для создания и управления библиотекой электронных книг,.
которая работает в среде Linux, OSX и Windows. Calibre должна уметь делать все, что
необходимо для поддержки электронной библиотеки: работать с каталогом, преобразовывать.
форматы, загружать новости и адаптировать их для устройств чтения, а также.
синхронизировать коллекцию с устройствами для чтения.

Поддерживаемые форматы: MOBI, LIT, PRC, EPUB, ODT, HTML, CBR, CBZ, RTF,
TXT, PDF, LRS и FB2.

%prep
%setup
%__subst "s|libdir = s.get_python_lib.*|libdir = '%buildroot%python3_sitelibdir'|" setup/install.py
%__subst "s|hunspell-1.7|hunspell|" setup/extensions.json
# don't check for new upstream version
#patch -p1
#patch1 -p1

# TODO: remove or replace with python
find -type f -name "*.py" | xargs %__subst "s|^#!/usr/bin/env python$|#!/usr/bin/python3|"
#find -type f -name "*.py" | xargs %__subst "s|^#!/usr/bin/python2$|#!/usr/bin/python3|"

# fix default libdir
%__subst "s|/usr/lib|%_libdir|" setup/build_environment.py

# setup QMAKE compile flags
sed -i 's|^\(.*QMAKE_LIBS_PRIVATE.*\+=.*glib.*fontconfig.*\)$|\1\n            QMAKE_CXXFLAGS += %optflags|' setup/build.py

%build
%python3_build

%install
#python_install (not use due skip-build unsupported)
mkdir -p %buildroot%python3_sitelibdir/
python3 setup.py install --staging-libdir=%buildroot%_libdir --libdir=%_libdir --prefix=%_prefix --root=%buildroot --staging-root=%buildroot/%_prefix
%find_lang --with-kde %name

# fix bash completion file placement
#install -m644 -D %buildroot%_datadir/bash-completion/completions/calibre %buildroot/etc/bash_completion.d/%name
rm -rfv %buildroot%_datadir/bash-completion
rm -rfv %buildroot%_libdir/calibre/tinycss/tests

#chrpath -d %buildroot%_libdir/%name/%name/plugins/*.so

rm -fv %buildroot%_bindir/calibre-uninstall
rm -rf %buildroot%_datadir/%name/fonts/liberation/
rm -fv %buildroot%_datadir/%name/calibre-portable.*
install -m 755 %SOURCE1 %buildroot%_bindir/calibre-mount-helper

rm -vf %buildroot%_libdir/calibre/calibre/translations/msgfmt.py

%files -f %name.lang
%doc README.md Changelog.txt
#/etc/bash_completion.d/%name
%_bindir/*
%_libdir/%name/
%python3_sitelibdir/*
%_datadir/%name/
%_datadir/metainfo/calibre-ebook-edit.metainfo.xml
%_datadir/metainfo/calibre-ebook-viewer.metainfo.xml
%_datadir/metainfo//calibre-gui.metainfo.xml
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/*/mimetypes/*.png
%_datadir/mime/packages/calibre-mimetypes.xml

%changelog
* Fri Feb 04 2022 Vitaly Lipatov <lav@altlinux.ru> 5.36.0-alt1
- new version 5.36.0 (with rpmrb script)

* Fri Feb 04 2022 Sergey V Turchin <zerg@altlinux.org> 5.33.2-alt1.1
- NMU: build according qtwebengine arches

* Mon Dec 13 2021 Vitaly Lipatov <lav@altlinux.ru> 5.33.2-alt1
- new version 5.33.2 (with rpmrb script)
- build with sip6

* Sun Sep 12 2021 Vitaly Lipatov <lav@altlinux.ru> 5.26.0-alt1
- new version 5.26.0 (with rpmrb script)

* Thu Aug 26 2021 Vitaly Lipatov <lav@altlinux.ru> 5.25.0-alt1
- new version 5.25.0 (with rpmrb script)

* Tue Aug 10 2021 Vitaly Lipatov <lav@altlinux.ru> 5.24.0-alt1
- new version 5.24.0 (with rpmrb script)

* Thu Jul 15 2021 Vitaly Lipatov <lav@altlinux.ru> 5.23.0-alt2
- add BR: python3-module-PyQt5-devel

* Sun Jul 11 2021 Vitaly Lipatov <lav@altlinux.ru> 5.23.0-alt1
- new version 5.23.0 (with rpmrb script)
- official python3 build
- big build requires update

* Thu Jul 01 2021 Vitaly Lipatov <lav@altlinux.ru> 4.23.0-alt3
- fix build with ICU >= 68

* Tue Feb 16 2021 Vitaly Lipatov <lav@altlinux.ru> 4.23.0-alt2
- drop python2 requires

* Fri Aug 21 2020 Vitaly Lipatov <lav@altlinux.ru> 4.23.0-alt1
- new version 4.23.0 (with rpmrb script)
- replace fonts-ttf-liberation requires with fonts-ttf-core (ALT bug 38831)

* Sat Aug 01 2020 Vitaly Lipatov <lav@altlinux.ru> 4.22.0-alt1
- new version 4.22.0 (with rpmrb script)

* Wed Jun 24 2020 Vitaly Lipatov <lav@altlinux.ru> 4.19.0-alt1
- new version 4.19.0 (with rpmrb script)

* Fri Jun 19 2020 Vitaly Lipatov <lav@altlinux.ru> 4.18.0-alt1
- new version 4.18.0 (with rpmrb script)

* Fri May 29 2020 Vitaly Lipatov <lav@altlinux.ru> 4.17.0-alt1
- new version 4.17.0 (with rpmrb script)

* Tue May 05 2020 Vitaly Lipatov <lav@altlinux.ru> 4.15.0-alt1
- new version 4.15.0 (with rpmrb script)

* Sun Mar 29 2020 Vitaly Lipatov <lav@altlinux.ru> 4.13.0-alt1
- new version 4.13.0 (with rpmrb script)

* Thu Mar 19 2020 Vitaly Lipatov <lav@altlinux.ru> 4.12.0-alt1
- new version 4.12.0 (with rpmrb script)

* Sun Mar 01 2020 Vitaly Lipatov <lav@altlinux.ru> 4.11.2-alt1
- new version 4.11.2 (with rpmrb script)

* Wed Feb 19 2020 Vitaly Lipatov <lav@altlinux.ru> 4.10.1-alt1
- new version 4.10.1 (with rpmrb script)

* Fri Jan 24 2020 Vitaly Lipatov <lav@altlinux.ru> 4.9.1-alt1
- new version 4.9.1 (with rpmrb script)

* Tue Dec 24 2019 Vitaly Lipatov <lav@altlinux.ru> 4.6.0-alt1
- new version 4.6.0 (with rpmrb script)

* Wed Dec 11 2019 Vitaly Lipatov <lav@altlinux.ru> 4.5.0-alt1
- new version 4.5.0 (with rpmrb script)

* Fri Oct 25 2019 Vitaly Lipatov <lav@altlinux.ru> 4.2.0-alt1
- new version (4.2.0) with rpmgs script

* Wed Oct 16 2019 Vitaly Lipatov <lav@altlinux.ru> 4.1.0-alt1
- new version 4.1.0 (with rpmrb script)
- switch to python3

* Mon Oct 07 2019 Vitaly Lipatov <lav@altlinux.ru> 4.0.0-alt1
- new version 4.0.0 (with rpmrb script)
- update build requires to the latest used versions

* Tue Sep 17 2019 Vitaly Lipatov <lav@altlinux.ru> 3.48.0-alt1
- new version (3.48.0) with rpmgs script

* Tue Aug 13 2019 Vitaly Lipatov <lav@altlinux.ru> 3.46.0-alt1
- new version 3.46.0 (with rpmrb script)
- pack desktop files and icons

* Wed Jun 12 2019 Vitaly Lipatov <lav@altlinux.ru> 3.44-alt1
- new version 3.44 (with rpmrb script)

* Mon Apr 29 2019 Vitaly Lipatov <lav@altlinux.ru> 3.42.0-alt1
- new version 3.42.0 (with rpmrb script)

* Sun Apr 21 2019 Vitaly Lipatov <lav@altlinux.ru> 3.41.3-alt1
- new version 3.41.3 (with rpmrb script) (ALT bug 36650)
- add BeautifulSoup4 require (new dep)

* Wed Mar 13 2019 Vitaly Lipatov <lav@altlinux.ru> 3.40.1-alt1
- new version 3.40.1 with rpmgs script

* Sat Feb 09 2019 Vitaly Lipatov <lav@altlinux.ru> 3.39.1-alt1
- new version 3.39.1 (with rpmrb script)

* Fri Feb 01 2019 Vitaly Lipatov <lav@altlinux.ru> 3.39.0-alt1
- new version 3.39.0 (with rpmrb script)

* Thu Jan 31 2019 Vitaly Lipatov <lav@altlinux.ru> 3.38.1-alt1
- new version 3.38.1 (with rpmrb script)

* Sun Dec 23 2018 Vitaly Lipatov <lav@altlinux.ru> 3.36.0-alt1
- new version 3.36.0 (with rpmrb script)

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 3.35.0-alt1
- new version 3.35.0 (with rpmrb script)

* Sun Nov 18 2018 Vitaly Lipatov <lav@altlinux.ru> 3.34.0-alt1
- new version 3.34.0 (with rpmrb script)

* Sat Oct 06 2018 Vitaly Lipatov <lav@altlinux.ru> 3.32.0-alt1
- new version 3.32.0 (with rpmrb script)

* Sat Sep 29 2018 Vitaly Lipatov <lav@altlinux.ru> 3.31.0-alt1
- new version 3.31.0 (with rpmrb script)

* Wed Sep 05 2018 Vitaly Lipatov <lav@altlinux.ru> 3.30.0-alt1
- new version 3.30.0 (with rpmrb script)

* Wed Aug 29 2018 Vitaly Lipatov <lav@altlinux.ru> 3.29.0-alt1
- new version 3.29.0 (with rpmrb script)
- rebuild with podofo 0.9.6

* Thu Aug 16 2018 Sergey V Turchin <zerg@altlinux.org> 3.28.0-alt2
- rebuild with new Qt

* Wed Aug 15 2018 Vitaly Lipatov <lav@altlinux.ru> 3.28.0-alt1
- new version 3.28.0 (with rpmrb script)

* Fri Jul 13 2018 Vitaly Lipatov <lav@altlinux.ru> 3.27.1-alt1
- new version 3.27.1 (with rpmrb script)

* Mon Jul 02 2018 Vitaly Lipatov <lav@altlinux.ru> 3.26.1-alt1
- new version 3.26.1 (with rpmrb script)
- drop BeautifulSoup requires (patched one used)

* Sat Jun 02 2018 Vitaly Lipatov <lav@altlinux.ru> 3.25.0-alt1
- new version 3.25.0 (with rpmrb script)

* Tue May 29 2018 Vitaly Lipatov <lav@altlinux.ru> 3.24.2-alt1
- new version 3.24.2 (with rpmrb script)

* Mon May 21 2018 Vitaly Lipatov <lav@altlinux.ru> 3.23.0-alt1
- new version 3.23.0 (with rpmrb script)

* Sat Apr 21 2018 Vitaly Lipatov <lav@altlinux.ru> 3.21.0-alt1
- new version 3.21.0 (with rpmrb script)

* Tue Mar 20 2018 Vitaly Lipatov <lav@altlinux.ru> 3.19.0-alt1
- new version 3.19.0 (with rpmrb script)

* Sun Mar 11 2018 Vitaly Lipatov <lav@altlinux.ru> 3.18.0-alt1
- new version 3.18.0 (with rpmrb script)

* Sat Feb 24 2018 Vitaly Lipatov <lav@altlinux.ru> 3.17.0-alt1
- new version 3.17.0 (with rpmrb script)

* Wed Feb 07 2018 Vitaly Lipatov <lav@altlinux.ru> 3.15.0-alt1
- new version 3.15.0 (with rpmrb script)

* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 3.14.0-alt1
- new version 3.14.0 (with rpmrb script)

* Sun Dec 03 2017 Vitaly Lipatov <lav@altlinux.ru> 3.13.0-alt1
- new version 3.13.0 (with rpmrb script)

* Sat Dec 02 2017 Vitaly Lipatov <lav@altlinux.ru> 3.12.0-alt1
- new version 3.12.0 (with rpmrb script)

* Mon Nov 06 2017 Vitaly Lipatov <lav@altlinux.ru> 3.10.0-alt1
- new version 3.10.0 (with rpmrb script)

* Thu Oct 19 2017 Sergey V Turchin <zerg@altlinux.org> 3.9.0-alt3
- build with new Qt

* Fri Oct 06 2017 Vitaly Lipatov <lav@altlinux.ru> 3.9.0-alt2
- add versioned python requires

* Fri Oct 06 2017 Vitaly Lipatov <lav@altlinux.ru> 3.9.0-alt1
- new version 3.9.0 (with rpmrb script)

* Sun Oct 01 2017 Vitaly Lipatov <lav@altlinux.ru> 3.8.0-alt1
- new version 3.8.0 (with rpmrb script)

* Tue May 23 2017 Vitaly Lipatov <lav@altlinux.ru> 2.85.1-alt1
- new version 2.85.1 (with rpmrb script)

* Wed May 10 2017 Vitaly Lipatov <lav@altlinux.ru> 2.84.0-alt1
- new version 2.84.0 (with rpmrb script)
- build with podofo 0.9.5

* Thu Mar 02 2017 Vitaly Lipatov <lav@altlinux.ru> 2.80.0-alt1
- new version 2.80.0 (with rpmrb script)

* Wed Feb 08 2017 Vitaly Lipatov <lav@altlinux.ru> 2.78.0-alt1
- new version 2.78.0 (with rpmrb script)

* Thu Jan 12 2017 Sergey V Turchin <zerg@altlinux.org> 2.69.0-alt1.1
- build with new Qt

* Tue Oct 11 2016 Vitaly Lipatov <lav@altlinux.ru> 2.69.0-alt1
- new version 2.69.0 (with rpmrb script)

* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 2.68.0-alt1
- new version 2.68.0 (with rpmrb script)
- build with podofo 0.9.4

* Fri Feb 26 2016 Vitaly Lipatov <lav@altlinux.ru> 2.35.0-alt2
- fix buildreqs
- rebuild with libicu56

* Mon Aug 24 2015 Vitaly Lipatov <lav@altlinux.ru> 2.35.0-alt1
- new version (2.35.0) with rpmgs script
- build with Qt5, update build requires

* Sun Aug 23 2015 Vitaly Lipatov <lav@altlinux.ru> 1.48.0-alt2
- rebuild with updated apws, lxml
- rebuild with new podofo 0.9.3

* Mon Oct 13 2014 Vitaly Lipatov <lav@altlinux.ru> 1.48.0-alt1
- new version 1.48.0 (with rpmrb script)

* Mon Jul 07 2014 Vitaly Lipatov <lav@altlinux.ru> 1.43.0-alt1
- new version 1.43.0 (with rpmrb script) (fix ALT bug #30128)

* Mon Apr 07 2014 Anton Farygin <rider@altlinux.ru> 1.24.0-alt2
- rebuild with new ImageMagick

* Mon Feb 17 2014 Vitaly Lipatov <lav@altlinux.ru> 1.24.0-alt1
- new version 1.24.0 (with rpmrb script)

* Sat Oct 12 2013 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- new version 1.6.0 (with rpmrb script)

* Wed Aug 28 2013 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- new version 1.0.0 (with rpmrb script)

* Tue Aug 06 2013 Vitaly Lipatov <lav@altlinux.ru> 0.9.42-alt2
- add python-module-netifaces require
- fix warning fix update_checker attribute

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.9.42-alt1
- new version 0.9.42 (with rpmrb script) (ALT bug #29056)
- rebuild with libpodofo 0.9.1
- partially added private qt4 4.8.5 headers
- add no-update patch from Fedora

* Thu Apr 18 2013 Anton Farygin <rider@altlinux.ru> 0.8.55-alt1.4
- rebuild with new ImageMagick

* Mon Apr 15 2013 Andrey Cherepanov <cas@altlinux.org> 0.8.55-alt1.3
- Correct install icons and remove rpath from plugins

* Thu Jan 17 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.55-alt1.2
- rebuild with new sip

* Thu Oct 11 2012 Sergey V Turchin <zerg@altlinux.org> 0.8.55-alt1.1
- disable xbar support

* Tue Jun 19 2012 Anton Farygin <rider@altlinux.ru> 0.8.55-alt1
- Updated to 0.8.55 release

* Wed Jun 13 2012 Vitaly Lipatov <lav@altlinux.ru> 0.8.41-alt3
- rebuild with libpodofo

* Tue Feb 28 2012 Mykola Grechukh <gns@altlinux.ru> 0.8.41-alt2
- Updated to 0.8.41 release

* Fri Nov 25 2011 Damir Shayhutdinov <damir@altlinux.ru> 0.8.27-alt2
- Fixed shebang in all executable scripts (env python2->env python)

* Thu Nov 24 2011 Damir Shayhutdinov <damir@altlinux.ru> 0.8.27-alt1
- Updated to 0.8.27 release

* Thu Mar 31 2011 Damir Shayhutdinov <damir@altlinux.ru> 0.7.50-alt2
- Dropped sphinx depends

* Wed Mar 30 2011 Damir Shayhutdinov <damir@altlinux.ru> 0.7.50-alt1
- new version
- drop bzr depends (closes #18216)
- rebuilt with new sip API (closes #24867)

* Tue Sep 14 2010 Anton Farygin <rider@altlinux.ru> 0.7.9-alt2
- rebuild with new ImageMagick

* Tue Aug 24 2010 Ildar Mulyukov <ildar@altlinux.ru> 0.7.9-alt1
- new version
- skip bundling Liberation fonts in favor of corresponding package

* Mon Feb 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.6.37-alt1
- new version (0.6.37) (fix alt bug #18217)
- add russian translation (thanks, V. Dikonov)
- fix build on x86_64, update buildreqs

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.77-alt1.1
- Rebuilt with python 2.6

* Wed Jul 16 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4.77-alt1
- initial build for ALT Linux Sisyphus
