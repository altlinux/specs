# -*- coding: utf-8 -*-
Name: calibre
Version: 7.5.1
Release: alt1.2

Summary: A e-book library management application
Summary(ru_RU.UTF8): Программа для работы с личной электронной библиотекой

License: GPLv2
Group: File tools
Url: http://calibre-ebook.com/

Packager: Vitaly Lipatov <lav@altlinux.ru>

#Source-url: https://github.com/kovidgoyal/calibre/archive/refs/tags/v%version.tar.gz
# Source-url: https://download.calibre-ebook.com/%version/calibre-%version.tar.xz
Source: %name-%version.tar

Patch1: calibre-no-update.patch
Patch2: calibre-nodisplay.patch
Patch3: calibre-alt-loongarch64-and-riscv64-support.patch

AutoProv:no

ExclusiveArch: %qt6_qtwebengine_arches

Requires: fonts-ttf-core
#Requires: xkeyboard-config

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro >= 1.9.19
BuildRequires(pre): rpm-macros-qt6-webengine

%define calibredir %_datadir/calibre

# Windows's modules
%add_python3_req_skip calibre_extensions.winsapi

# internal extensions?
%add_python3_req_skip calibre_extensions calibre_extensions.fast_css_transform calibre_extensions.freetype calibre_extensions.progress_indicator calibre_extensions.speedup

%add_python3_path %_libdir/%name

#BuildRequires: chrpath
#BuildRequires: /proc

#BuildRequires: gcc-c++ libX11-devel libXext-devel libXrender-devel libjpeg-devel libsqlite3-devel
BuildRequires: gcc-c++
BuildRequires: cmake

BuildRequires: xdg-utils >= 1.0.2

BuildRequires(pre): rpm-macros-qt6
BuildRequires: qt6-base-devel
# Project MESSAGE: This project is using private headers and will therefore be tied to this specific Qt module build version.
# Project MESSAGE: Running this project against other versions of the Qt modules may crash at any arbitrary point.
# Project MESSAGE: This is not a bug, but a result of using Qt internals. You have been warned!
#BuildRequires: qt6-qtbase-private-devel

BuildRequires: qt6-svg-devel
BuildRequires: qt6-charts-devel
BuildRequires: qt6-webengine-devel
BuildRequires: qt6-imageformats
# WebView support: Quick QuickWidgets WaylandCompositor
BuildRequires: qt6-declarative-devel
BuildRequires: qt6-wayland-devel
# needs for smiles and emojicons
Requires: qt6-imageformats


#BuildRequires: libpoppler-qt5-devel >= 0.20.2
#BuildRequires: libwmf-devel >= 0.2.8

#py3_use dbus >= 1.2.16

# missed in the official list
#BuildRequires: libudev-devel
#BuildRequires: python3-modules-curses
#BuildRequires: libmtdev-devel libts-devel libinput-devel
BuildRequires: libxkbcommon-devel

BuildRequires: python3
Requires: python3


# Checked 02.03.2024 with
# https://github.com/kovidgoyal/calibre/blob/master/bypy/sources.json
# calibre/bypy/sources.json
BuildRequires: zlib-devel
# >= 1.3
BuildRequires: bzlib-devel >= 1.0.8
# xz
BuildRequires: liblzma-devel
#>= 5.4.4
#BuildRequires: libunrar-devel >= 6.2.11
BuildRequires: libunrar-devel >= 6.1.7
BuildRequires: libbrotli-devel >= 1.1.0
BuildRequires: libzstd-devel >= 1.5.5

BuildRequires: libexpat >= 2.5.0
BuildRequires: libsqlite3-devel
BuildRequires: libffi-devel
#>= 3.4.4
BuildRequires: libhyphen-devel >= 2.8.8
BuildRequires: libssl-devel >= 3.1.3
#BuildRequires: libncursesw-devel >= 6.4
BuildRequires: libncursesw-devel >= 6.3
BuildRequires: libreadline-devel >= 8.2
BuildRequires: libicu-devel >= 7.3
# TODO:
BuildRequires: libstemmer-devel
#>= 2.2.0
BuildRequires: libjpeg-devel >= 3.0.0
BuildRequires: libpng-devel >= 1.6.40
BuildRequires: libjbig-devel >= 2.1
BuildRequires: libtiff-devel
#>= 4.6.0
BuildRequires: libwebp-devel >= 1.3.2
BuildRequires: libfreetype-devel >= 2.13.2
BuildRequires: libgraphite2-devel >= 1.3.4
BuildRequires: fontconfig-devel >= 2.14.2
# iconv (in glibc)
BuildRequires: libxml2-devel >= 2.12.1
BuildRequires: libxslt-devel
#>= 1.1.39
BuildRequires: libchm-devel >= 0.40
BuildRequires: optipng >= 0.7.7
Requires: optipng >= 0.7.7
# TODO: mozjpeg 4.1.4
BuildRequires: libusb-devel >= 1.0.26
BuildRequires: libmtp-devel >= 1.1.21
BuildRequires: libopenjpeg2.0-devel >= 2.5.0
BuildRequires: libpoppler-devel >= 23.08.0
BuildRequires: libpodofo-devel >= 0.10.3
BuildRequires: libgpg-error-devel >= 1.47
BuildRequires: libgcrypt-devel >= 1.10.2
BuildRequires: glib2-devel >= 2.78.0

BuildRequires: libdbus-devel
#>= 1.15.8
# https://bugzilla.altlinux.org/show_bug.cgi?id=39224
BuildRequires: libdbus-glib-devel
#>= 0.112

BuildRequires: libhunspell-devel >= 1.7.2


# Checked 02.03.2024 with
# https://github.com/kovidgoyal/calibre/blob/master/bypy/sources.json
# calibre/bypy/sources.json

%py3_use six >= 1.16.0
%py3_use unrardll >= 0.1.7
%py3_use lxml >= 4.9.3
%py3_use pychm >= 0.8.6
%py3_use html5-parser >= 0.4.12
%py3_use css-parser >= 1.0.10
%py3_use dateutil >= 2.8.2
%py3_use jeepney >= 0.8.0
%py3_use dns >= 2.4.2
%py3_use mechanize >= 0.4.8
%py3_use feedparser >= 6.0.10
# sgmllib is needed for feedparser parsing malformed feeds
#py3_use sgmllib3k >= 1.0.0
%py3_use markdown >= 3.4.4
%py3_use html2text >= 2020.1.16
# no need really
#py3_use soupsieve
#>= 2.5
%py3_use beautifulsoup4 >= 4.12.2
%py3_use regex >= 2023.8.8
%py3_use chardet >= 5.2.0
BuildRequires: libuchardet-devel
# >= 0.0.8
%py3_use msgpack >= 1.0.7
%py3_use Pygments >= 2.16.1
%py3_use pycryptodome >= 3.19.0
%py3_use apsw > 3.43.0.0
%py3_use webencodings >= 0.5.1
%py3_use html5lib >= 1.1
%py3_use Pillow >= 10.0.1
%py3_use netifaces >= 0.11.0
%py3_use psutil >= 5.9.5
%py3_use ifaddr >= 0.2.0

# needed for py7zr
#py3_use texttable >= 1.6.7
#py3_use multivolumefile 0.2.3
#py3_use brotli 1.1.0
#py3_use pyzstd 0.15.9
#py3_use pypmd 1.0.0
#py3_use inflate64 0.3.1
# TODO: build py7zr
#py3_use py7zr >= 0.20.6

%py3_use fonttools >= 4.47.0
%py3_use zeroconf >= 0.115.0

#py3_use toml >= 0.10.1
#py3_use pyparsing >= 2.4.7
%py3_use packaging >= 23.1


%py3_buildrequires sip6 >= 6.7.11
%py3_buildrequires PyQt-builder
# >= 1.15.2
%py3_buildrequires PyQt6-sip >= 13.5.2
BuildRequires: python3-module-PyQt6-devel
%py3_use PyQt6 >= 6.5.2
%py3_use PyQt6-WebEngine >= 6.5.0

BuildRequires: libspeechd-devel
#>= 0.11.5
BuildRequires: libxxhash-devel
#>= 3.3.0

%py3_use jeepney
%py3_use xxhash

Requires:       udisks2
Requires:       /usr/bin/jpegtran

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

%patch1 -p1
%patch2 -p1
%patch3 -p1

# TODO: remove or replace with python
find -type f -name "*.py" | xargs %__subst "s|^#!/usr/bin/env python$|#!/usr/bin/python3|"
find -type f -name "*.py" | xargs %__subst "s|^#!/usr/bin/python2$|#!/usr/bin/python3|"

# fix default libdir
%__subst "s|/usr/lib|%_libdir|" setup/build_environment.py

# setup QMAKE compile flags
#sed -i 's|^\(.*QMAKE_LIBS_PRIVATE.*\+=.*glib.*fontconfig.*\)$|\1\n            QMAKE_CXXFLAGS += %optflags|' setup/build.py

sed -e "s/^Name=calibre/Name=Calibre/g" \
    -i src/calibre/linux.py

%build
export LANG='en_US.UTF-8'
#python3 setup.py build
#python3 setup.py iso639
#python3 setup.py iso3166
#python3 setup.py translations
#python3 setup.py liberation_fonts --system-liberation_fonts --path-to-liberation_fonts %_ttffontsdir/liberation

# TODO:
# https://bugs.launchpad.net/calibre/+bug/2005955
#python3 setup.py hyphenation --hyphenation-url="%SOURCE2"

# TODO: /usr/share/javascript/mathjax/core.js
#python3 setup.py mathjax --system-mathjax --path-to-mathjax /usr/share/javascript/mathjax
# FIXME: Downloading MathJax: https://github.com/mathjax/MathJax/archive/3.1.4.tar.gz
#python3 setup.py mathjax

#$ grep sub_commands setup/resources.py
#    sub_commands = ['kakasi', 'liberation_fonts', 'mathjax', 'rapydscript', 'hyphenation']
#python3 setup.py resources

#python3 setup.py gui

%install
export LANG='en_US.UTF-8'

python3 setup.py install \
    --staging-root=%buildroot%_prefix --prefix=%_prefix \
    --staging-libdir=%buildroot%_libdir --libdir=%_libdir \
    --system-plugins-location=%calibredir/system-plugins \
    %nil

cp -a man-pages/ %buildroot%_mandir

%find_lang --with-man --all-name %name

#rm -rv %buildroot%calibredir/rapydscript/

rm -rv %buildroot%_datadir/bash-completion
rm -rv %buildroot%_libdir/calibre/tinycss/tests

#chrpath -d %buildroot%_libdir/%name/%name/plugins/*.so

#rm -v %buildroot%_bindir/calibre-uninstall
rm -rv %buildroot%_datadir/%name/fonts/liberation/
rm -v %buildroot%_datadir/%name/calibre-portable.*

rm -v %buildroot%_libdir/calibre/calibre/translations/msgfmt.py


#	rm debian/tmp/usr/share/calibre/calibre-portable.*
#	rm debian/tmp/usr/lib/python*/site-packages/init_calibre.py
#	rmdir debian/tmp/usr/share/desktop-directories
#
#	# do not install developer's script
#	rm debian/tmp/usr/lib/calibre/calibre/devices/mtp/unix/upstream/update.py
#
# 	# Replace "python" to "python3" in shebang
#	find debian/tmp/usr/lib/calibre debian/tmp/usr/share/calibre -name '*.py' -print | xargs --no-run-if-empty sed --separate --file=debian/fix-python-shebang.sed --in-place
#
#	# Remove source path name from pyuic6 outputs
#	find debian/tmp/usr/lib/calibre/calibre/gui2 -name '*_ui.py' -print | xargs --no-run-if-empty sed --separate --file=debian/remove-ui-basepath.sed --in-place


%check
#export LANG='en_US.UTF-8'
#python3 -m unittest discover


%files -f %name.lang
%doc README.md Changelog.txt
#/etc/bash_completion.d/%name
%_bindir/*
%_man1dir/*
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
* Wed Aug 28 2024 Sergey V Turchin <zerg@altlinux.org> 7.5.1-alt1.2
- NMU: clean build requires

* Mon Mar 04 2024 Ivan A. Melnikov <iv@altlinux.org> 7.5.1-alt1.1
- NMU: fix build on loongarch64

* Sat Mar 02 2024 Vitaly Lipatov <lav@altlinux.ru> 7.5.1-alt1
- new version 7.5.1
- build with PyQt6

* Wed Jul 13 2022 Vitaly Lipatov <lav@altlinux.ru> 5.44.0-alt1
- new version 5.44.0 (with rpmrb script)

* Tue Jun 07 2022 Vitaly Lipatov <lav@altlinux.ru> 5.43.0-alt1
- new version 5.43.0 (with rpmrb script)

* Tue May 24 2022 Vitaly Lipatov <lav@altlinux.ru> 5.42.0-alt1
- new version 5.42.0 (with rpmrb script)
- update build requires

* Sat Apr 02 2022 Vitaly Lipatov <lav@altlinux.ru> 5.40.0-alt1
- new version 5.40.0 (with rpmrb script)

* Fri Feb 18 2022 Sergey V Turchin <zerg@altlinux.org> 5.36.0-alt1.1
- NMU: using not_qt5_qtwebengine_arches macro

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
