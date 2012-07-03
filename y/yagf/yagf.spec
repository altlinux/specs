Name:    yagf
Version: 0.9.1
Release: alt1

Summary: YAGF is a graphical front-end for cuneiform and tesseract OCR tools
Summary(ru_RU.UTF-8): Оболочка YAGF предоставляет графический интерфейс для консольных программ распознавания тектов cuneiform и tesseract
License: GPLv3+
Group:   Office
URL:     http://symmetrica.net/cuneiform-linux/yagf-ru.html

Source:  http://symmetrica.net/cuneiform-linux/yagf-%{version}-Source.tar.gz
Source1: YAGF.desktop

BuildRequires: gcc-c++ libqt4-devel
BuildRequires: cmake libaspell-devel aspell
Requires:      cuneiform libaspell aspell-en

Packager: Andrey Cherepanov <cas@altlinux.org>

%description
YAGF is a graphical front-end for cuneiform and tesseract OCR tools.
With YAGF you can open already scanned image files or obtain new images
via XSane (scanning results are automatically passed to YAGF).
Once you have a scanned image you can prepare it for recognition, select
particular image areas for recognition, set the recognition language and
so no. Recognized text is displayed in a editor window where it can be
corrected, saved to disk or copied to clipboard.
YAGF also provides some facilities for a multi-page recognition (see
the online help for more details).

%description -l ru_RU.UTF-8
Оболочка YAGF предоставляет графический интерфейс для консольных
программ распознавания тектов cuneiform и tesseract на платформе Linux.
Кроме того, YAGF позволяет управлять сканированием изображений, импортом
страниц из документов PDF, их предварительной обработкой и собственно
распознаванием из единого центра. Программа YAGF также упрощает
последовательное распознавание большого числа отсканированных страниц.

%prep
%setup -q
cp -f %SOURCE1 .
subst "s,/usr/local,%buildroot/usr/,g" ./CMakeLists.txt

%build
cmake ./
%make

%install
make install DESTDIR=%buildroot

%files 
%doc README COPYING DESCRIPTION AUTHORS ChangeLog
%_bindir/%name
%dir %_libdir/%name
%_libdir/%name/*.so*
%_datadir/%name
%_datadir/pixmaps/yagf.png
%_datadir/icons/hicolor/96x96/apps/%name.png
%_datadir/applications/YAGF.desktop

%changelog
* Mon Apr 23 2012 Andrey Cherepanov <cas@altlinux.org> 0.9.1-alt1
- Version 0.9.1
- Changes:
  - Text-splitting capability for splitting ext into blocks
    automatically is added
  - Toolbar icons size togling options is added
  - YAGF now stores its private data in a FeeDesktop conformat way
  - Some minor bug fixes and improvements

* Tue Mar 06 2012 Andrey Cherepanov <cas@altlinux.org> 0.9-alt1
- Version 0.9
- Changes:
  - Automatic removal of black edges appearing while scanning small
    documents is added. This option may be turned off in the settings dialog.
  - Images are loaded and processed a bit faster.
  - Deskewing is improved.
  - New recognition languages are added (require tesseract 3+).

* Fri Jan 13 2012 Andrey Cherepanov <cas@altlinux.org> 0.8.9-alt1
- Version 0.8.9
- Change group to Office

* Thu Oct 27 2011 Andrey Cherepanov <cas@altlinux.org> 0.8.7-alt4
- Install aspell for build with cmake

* Mon Aug 29 2011 Andrey Cherepanov <cas@altlinux.org> 0.8.7-alt3
- Add unowned pathes

* Mon Aug 29 2011 Andrey Cherepanov <cas@altlinux.org> 0.8.7-alt2
- Clarify license number
- Set Cuneiform as default engine
- Set Russian-English for Russian as default

* Mon Aug 29 2011 Andrey Cherepanov <cas@altlinux.org> 0.8.7-alt1
- Version 0.8.7

* Sun Aug 14 2011 Andrey Cherepanov <cas@altlinux.org> 0.8.6-alt3
- Show absent Aspell dictionary in dialog
- Install English dictionary as required second dictionary (closes: #25881)

* Tue May 31 2011 Andrey Cherepanov <cas@altlinux.org> 0.8.6-alt2
- Localize for XFCE menu

* Tue Feb 22 2011 Andrey Cherepanov <cas@altlinux.org> 0.8.6-alt1
- Version 0.8.6

* Fri Jan 28 2011 Andrey Cherepanov <cas@altlinux.org> 0.8.5-alt1
- Version 0.8.5

* Mon Jan 17 2011 Andrey Cherepanov <cas@altlinux.org> 0.8.3-alt1
- Version 0.8.3

* Tue Aug 18 2009 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt1
- Version 0.8.1

* Mon Jul 06 2009 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1
- First version for Sisyphus

