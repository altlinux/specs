Name: scantailor
Version: 0.9.11.1
Release: alt1

Summary: Scan processing software
License: GPL
Group: Graphics
Url: http://scantailor.sf.net

Packager: %packager
Source: %name-%version.tar
Source1: %name.desktop

# Automatically added by buildreq on Fri Apr 10 2009
BuildRequires: boost-devel boost-intrusive-devel cmake gcc-c++ glib2-devel libXfixes-devel libjpeg-devel libqt4-devel

%description
Scantailor is a book scan processing software. It
splits scanned pages, aligns, and converts to b/w from
grayscale. It has GUI interface. Analogs of this
program are ScanKromsator (written by kamerade bolega,
currently discontinued), BookRestorer.

%description -l ru_RU.UTF-8
Scantailor - программа для обработки отсканированных
книг. Эта программа может разделять развороты, выравнивать
страницы и переводить в ч/б из градаций серого. Имеет
GUI интерфейс. Наиболее известными аналогами
программы является ScanKromsator (написан камрадом bolega,
сейчас не развивается) и BookRestorer.

%prep
%setup -q

%build
cp resources/appicon.svg %name.svg
cmake -DCMAKE_INSTALL_PREFIX=/usr .
%make

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_datadir/%name/translations
install -pm755 scantailor %buildroot/%_bindir/
install -pm644 *.qm %buildroot%_datadir/%name/translations
install -pm644 -D %name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
install -pm644 -D %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/scantailor
%dir %_datadir/%name
%dir %_datadir/%name/translations
%_datadir/%name/translations/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Sat Mar 17 2012 Andrey Bergman <vkni@altlinux.org> 0.9.11.1-alt1
- update to version 0.9.11.1

* Sun Feb 05 2012 Andrey Bergman <vkni@altlinux.org> 0.9.11-alt1
- update to version 0.9.11

* Thu Aug 04 2011 Andrey Bergman <vkni@altlinux.org> 0.9.10-alt1
- update to version 0.9.10

* Wed Dec 08 2010 Andrey Bergman <vkni@altlinux.org> 0.9.9.2-alt2
- corrected desktop entry.

* Mon Oct 25 2010 Andrey Bergman <vkni@altlinux.org> 0.9.9.2-alt1
- update to version 0.9.9.2

* Mon Jul 12 2010 Andrey Bergman <vkni@altlinux.org> 0.9.9.1-alt2
- update to version 0.9.9.1

* Sat May 01 2010 Andrey Bergman <vkni@altlinux.org> 0.9.8.1-alt2
- added priority selection patch

* Mon Apr 26 2010 Andrey Bergman <vkni@altlinux.org> 0.9.8.1-alt1
- update to version 0.9.8.1

* Fri Apr 16 2010 Andrey Bergman <vkni@altlinux.org> 0.9.8-alt2
- added priority selection patch

* Sun Apr 04 2010 Andrey Bergman <vkni@altlinux.org> 0.9.8-alt1
- update to version 0.9.8

* Tue Dec 01 2009 Andrey Bergman <vkni@altlinux.org> 0.9.7.2-alt1
- update to a new version (bugfix and minor improvements)

* Sun Nov 15 2009 Andrey Bergman <vkni@altlinux.org> 0.9.7.1-alt1
- update to a new version (bugfix and minor improvements)

* Wed Nov 11 2009 Andrey Bergman <vkni@altlinux.org> 0.9.7-alt1.2
- Corrected desktop entry.

* Mon Nov 09 2009 Andrey Bergman <vkni@altlinux.org> 0.9.7-alt1.1
- Updated build requirements.

* Mon Nov 09 2009 Andrey Bergman <vkni@altlinux.org> 0.9.7-alt1
- update to a new version

* Sat Sep 05 2009 Andrey Bergman <vkni@altlinux.org> 0.9.6-alt1
- Added menu entry, icon and russian translation.

* Sun Aug 02 2009 Andrey Bergman <vkni@altlinux.org> 0.9.6-alt0.1
- update to a new version

* Thu May 21 2009 Andrey Bergman <vkni@altlinux.org> 0.9.5-alt0.4
- source update

* Mon May 04 2009 Andrey Bergman <vkni@altlinux.org> 0.9.5-alt0.1
- update to a new version (crash fix)

* Sun Apr 26 2009 Andrey Bergman <vkni@altlinux.org> 0.9.4-alt0.1
- new version

* Wed Feb 18 2009 Andrey Bergman <vkni@altlinux.org> 0.9.3-alt0.1
- update to a new version due to crash fix

* Tue Feb 17 2009 Andrey Bergman <vkni@altlinux.org> 0.9.2-alt0.1
- new version

* Sat Dec 20 2008 Andrey Bergman <vkni@altlinux.org> 0.9.1-alt0.2
- Update to version 0.9.1

* Wed Dec 11 2008 Andrey Bergman <vkni@altlinux.org> 0.9.0-alt0.1
- Initial release

