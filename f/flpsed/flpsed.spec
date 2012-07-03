Name: flpsed
Version: 0.7.0
Release: alt2
Packager: Fr. Br. George <george@altlinux.ru>
Summary: Add arbitrary text lines to existing PostScript document
Summary(ru_RU.UTF-8): Добавление и редактирование текстовых полей в готовый PostScript-документ
Group: Publishing
License: GPL

Source: %name-%version.tar.gz
Url: http://www.ecademix.com/JohannesHofmann/

# Automatically added by buildreq on Fri Oct 07 2011
# optimized out: fontconfig libX11-devel libstdc++-devel xorg-xproto-devel
BuildRequires: gcc-c++ libXext-devel libXft-devel libXinerama-devel libcairo-devel libfltk-devel libpixman-devel

%description
flpsed is a WYSIWYG pseudo PostScript1 editor. "Pseudo", because you
can't remove or modify existing elements of a document. But flpsed lets
you add arbitrary text lines to existing PostScript1 documents. Added
lines can later be reedited with flpsed. Using pdftops, which is part of
xpdf one can convert PDF documents to PostScript and also add text to
them. flpsed is useful for filling in forms, adding notes etc.

%description -l ru_RU.UTF-8
flpsed -- это псевдоредактор PostScript1-файлов в стиле WYSIWYG.
Приставка "псевдо" означает, что редактировать сам PS-документ или его
части flpsed не позволяет. Всё, что можно -- это добавлять любое
количество текстовых полей поверх имеющейся картинки; вот эти-то поля
и можно будет редактировать по новой. PDF-документы можно
преобразовывать в PS с помощью pdftops (часть пакета xpdf).

%prep
%setup
cat > %name.desktop <<@@@
[Desktop Entry]
Encoding=UTF-8
Name=flpsed
Name[ru]=flpsed
Comment=Add arbitrary text lines to existing PostScript document
Comment[ru]=Добавление текстовыхкомментариев в готовый PostScript документ
GenericName=WYSIWYG pseudo PostScript editor
GenericName[ru]=Псевдо-редактор PostScript файлов
Exec=flpsed
Terminal=false
Type=Application
Categories=Graphics;Publishing;
@@@

%build
#autoreconf
%configure
%make

%install
%makeinstall
install -D %name.desktop %buildroot%_desktopdir/%name.desktop

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%_bindir/*
%_desktopdir/*
%_man1dir/*

%changelog
* Thu Jun 21 2012 Fr. Br. George <george@altlinux.ru> 0.7.0-alt2
- Fix repocop warnings

* Fri Oct 07 2011 Fr. Br. George <george@altlinux.ru> 0.7.0-alt1
- Autobuild version bump to 0.7.0
- Fix dependencies

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.5.2-alt1.2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for flpsed
  * postclean-03-private-rpm-macros for the spec file

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.2
- Rebuilt with FLTK 1.3.0.r8575

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.1
- Rebuilt with libfltk13 and for debuginfo

* Fri Oct 09 2009 Fr. Br. George <george@altlinux.ru> 0.5.2-alt1
- Version up

* Thu Jan 24 2008 Fr. Br. George <george@altlinux.ru> 0.5.0-alt1
- Version up to 0.5.0
- FC8 synchronization
- desktop file added

* Sun May 14 2006 Fr. Br. George <george@altlinux.ru> 0.3.7-alt1
- Up to 0.3.7 version

* Thu Aug 18 2005 Fr. Br. George <george@altlinux.ru> 0.3.5-alt1
- Version upping
- Russian description added

* Sun Feb 20 2005 Fr. Br. George <george@altlinux.ru> 0.3.2-alt1
- Initial build

