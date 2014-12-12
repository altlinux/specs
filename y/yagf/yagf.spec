%define  snapshot %nil

Name:    yagf
Version: 0.9.4.3
Release: alt1

Summary: YAGF is a graphical front-end for cuneiform and tesseract OCR tools
Summary(ru_RU.UTF-8): Оболочка YAGF предоставляет графический интерфейс для систем распознавания текста Cuneiform и Tesseract
License: GPLv3+
Group:   Office
URL:     http://symmetrica.net/cuneiform-linux/yagf-ru.html
# VCS URL: https://code.google.com/p/yagf/

Source:  %{name}-%{version}.tar
Patch:	 %{name}-%{version}.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++ libqt4-devel
BuildRequires: libaspell-devel aspell

Requires: cuneiform
Requires: libaspell
Requires: aspell-en
Requires: ImageMagick-tools

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
%patch -p1
subst "s,/usr/local,%buildroot/usr/,g" ./CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files 
%doc README COPYING DESCRIPTION AUTHORS ChangeLog
%_bindir/%name
%_libdir/%name/*.so*
%_datadir/%name
%_pixmapsdir/yagf.png
%_iconsdir/hicolor/96x96/apps/%name.png
%_desktopdir/YAGF.desktop

%changelog
* Tue Sep 02 2014 Andrey Cherepanov <cas@altlinux.org> 0.9.4.3-alt1
- New version
- Do not clean data to prevent program crash (ALT #30403)

* Thu Aug 07 2014 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1.gitbbe6842
- New version

* Thu Apr 03 2014 Andrey Cherepanov <cas@altlinux.org> 0.9.3.2-alt1.gita131416
- New version
- Multipage TIFF support
- Fix Russian translation
- Move settings to single dialog

* Wed Feb 26 2014 Andrey Cherepanov <cas@altlinux.org> 0.9.3-alt2.gitc12786e
- Build from upstream git
- Fix recognize TIFF images

* Thu Feb 20 2014 Andrey Cherepanov <cas@altlinux.org> 0.9.3-alt1
- New version

* Thu Sep 06 2012 Andrey Cherepanov <cas@altlinux.org> 0.9.2-alt1
- Version 0.9.2
  - Workspace may now be saved as a project
  - Prepare for recognition button
  - Small bug fixes and improvements

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

