Name: unpaper
Version: 0.4
Release: alt2
License: GPLv2
Group: Publishing
# URL: http://unpaper.berlios.de
Url: https://github.com/Flameeyes/unpaper/tree/unpaper-0.4

Packager: Yury Aliaev <mutabor@altlinux.ru>

# Source: http://download.berlios.de/%name/%name-%version.tar.gz
Source: %name-%version.tar

Summary: unpaper is a post-processing tool for scanned sheets of paper
Summary(ru_RU.UTF-8): unpaper есть программа для обработки страниц после сканирования

BuildPreReq: docbook-style-xsl
# Automatically added by buildreq on Fri May 25 2012
# optimized out: libgpg-error xml-common
BuildRequires: libdb4-devel libnss-mdns netpbm xsltproc

%description
unpaper is a post-processing tool for scanned sheets of paper,
especially for book pages that have been scanned from previously created
photocopies. The main purpose is to make scanned book pages better
readable on screen after conversion to PDF or DJVU. unpaper tries to
clean scanned images by removing dark edges that appeared through
scanning or copying on areas outside the actual page content.
The program also tries to detect disaligned centering and rotation
of pages and will automatically straighten each page by rotating it
to the correct angle.

%description -l ru_RU.UTF-8
unpaper есть программа для обработки страниц после сканирования,
особенно в тех случаях, когда была отсканирована фотокопия книги.
Основная её цель есть улучшить читаемость с экрана после преобразования
в форматы PDF и DJVU. Программа unpaper пытается убрать тёмное
окаймление, появляющуюся за пределами содержимого страницы
при сканировании или копировании. Программа также пытается определить
нарушения центровки страниц и их наклон и автоматически выпрямляет
страницы, поворачивая их на соответствующий угол.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS COPYING INSTALL NEWS README TODO doc/* html/*

%changelog
* Sat May 26 2012 Malo Skryleve <malo@altlinux.org> 0.4-alt2
- Fixed some errors

* Fri May 25 2012 Malo Skryleve <malo@altlinux.org> 0.4-alt1
- updated to version 0.4, changed source host because of a new author

* Thu Jun 26 2008 Yury Aliaev <mutabor@altlinux.org> 0.3-alt1
- version 0.3

* Sun Jun 01 2007 Yury Aliaev <mutabor@altlinux.org> 0.2-alt1
- Initial build
