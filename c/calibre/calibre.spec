# -*- coding: utf-8 -*-
Name: calibre
Version: 0.8.55
Release: alt1
Summary: A e-book library management application
Summary(ru_RU.UTF8): Программа для работы с личной электронной библиотекой
License: GPL
Group: File tools
Url: http://calibre-ebook.com/
Packager: Damir Shayhutdinov <damir@altlinux.ru>
Source: http://sourceforge.net/projects/%name/files/%version/%name-%version.tar
#.gz
Requires: fonts-ttf-liberation

%add_python_req_skip win32serviceutil win32service win32event win32con win32com win32api pythoncom usbobserver

# Automatically added by buildreq on Thu Aug 26 2010 (-bi)
BuildRequires: gcc-c++ libImageMagick-devel libX11-devel libXext-devel libchm-devel libjpeg-devel libpodofo-devel libpoppler-qt4-devel libqt4-devel python-module-PyQt4-devel python-module-cssutils python-module-dateutil python-module-imaging python-module-lxml python-module-mechanize python-module-sip-devel python-modules-compiler python-modules-curses python-modules-encodings

BuildRequires: libicu-devel libsqlite3-devel python-modules-json libqt4-devel libqt4-core python-module-PyQt4

BuildRequires: /proc

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
%setup -n %name
sed -i "s/env python2/env python/" setup/install.py

%build
%python_build
%__python setup.py resources

%install
#python_install (not use due skip-build unsupported)
python setup.py install --staging-libdir=%buildroot%_libdir --libdir=%_libdir --prefix=%_prefix --root=%buildroot --staging-root=%buildroot/%_prefix
%find_lang --with-kde %name
mv %buildroot{/usr,}/etc

%files -f %name.lang
%doc README Changelog.yaml
/etc/bash_completion.d/%name
%_bindir/*
%exclude %_bindir/%name-uninstall
%_libdir/%name/
%exclude %_libdir/%name/%name/trac
%_datadir/%name/
%exclude %_datadir/%name/fonts/liberation/

%changelog
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
