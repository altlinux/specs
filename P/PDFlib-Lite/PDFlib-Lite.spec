%define patchlevel p1
%define pythondir python%_python_version

Name: PDFlib-Lite
Version: 7.0.4
Release: alt3.p1.1

Summary: A library for on-the-fly PDF generation
License: Freely distributable, free for personal/research use and OSS development
Group: Development/Documentation

Url: http://www.pdflib.com
Source: PDFlib-Lite-%version%patchlevel.tar.gz
Patch: PDFlib-image.patch
Patch1: PDFlib-configure.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Wed Jun 03 2009
BuildRequires: perl-devel python-devel tcl-devel gcc-c++
BuildRequires: autoconf >= 2.5

%if 0
BuildRequires: python-devel
BuildRequires: perl-base, perl-devel
BuildRequires: tcl, tcl-devel
%endif

%define libname libpdflib-lite

Summary(ru_RU.KOI8-R): Библиотека для генерации PDF "на лету"

%description
Portable C library for dynamically generating PDF ("Adobe
Acrobat") files, with support for many other programming
languages.

PDFlib is a library for generating PDF files. It offers an API
with support for text, vector graphics, raster image, and
hypertext. Call PDFlib routines from within your client program
and voila: dynamic PDF files!

%description -l ru_RU.KOI8-R
Переносимая C-библиотека для динамической генерации файлов PDF
("Adobe Acrobat"), с поддержкой многих других языков
программирования.

PDFlib - бибиотека для генерации файлов PDF. Она предлагает API с
поддержкой для текста, векторной графики, растровых изображений и
гипертекста. Вызоваете подпрограммы PDFlib  из ваших приложений и
готово: динамические PDF файлы!

%package -n %libname
Summary: PDFLib shared library
Summary(ru_RU.KOI8-R): разделяемая библиотека PDFLib
Group: System/Libraries
Obsoletes: %name < 7.0.0
Provides: %name = %version-%release

%description -n %libname
PDFlib is a library for generating PDF files.

This package contains shared library.

%package -n %libname-devel
Summary: PDFLib for developers
Summary(ru_RU.KOI8-R):  PDFLib для разработчиков
Group: Development/C
Obsoletes: %name-devel < 7.0.0
Provides: %name-devel = %version-%release
Requires: %libname = %version-%release

%description -n %libname-devel
PDFlib development headers

%description -n %libname-devel -l ru_RU.KOI8-R
Заголовочные файлы PDFlib для разработчиков

%package utils
Summary: PDFLib utilities
Summary(ru_RU.KOI8-R): утилиты PDFLib
Group: File tools

%description utils
PDF library utilities

%package docs
Summary: PDFLib documentation
Summary(ru_RU.KOI8-R): документация PDFLib
Group: Documentation
BuildArch: noarch
Obsoletes: %name <= 7.0.4-alt2.p1

%description docs
PDF library documentation

%if 0
%package python
Summary: PDFLib python binding
Summary(ru_RU.KOI8-R): PDFLib для питон
Group: Development/Python

%description python
PDF library binding for python

%description python -l ru_RU.KOI8-R
Модули для языка python, позволяющие получить доступ к библиотеке

%package perl
Summary: PDFLib perl binding
Summary(ru_RU.KOI8-R):  PDFLib для perl
Group: Development/Perl
Requires: perl

%description perl
PDF library binding for perl

%description perl -l ru_RU.KOI8-R
Модули для языка perl, позволяющие получить доступ к библиотеке

%package tcl
Summary: PDFLib tcl binding
Summary(ru_RU.KOI8-R):  PDFLib для tcl
Group: Development/Tcl
Requires: tcl

%description tcl
PDF library binding for tcl

%description tcl -l ru_RU.KOI8-R
Модули для языка tcl, позволяющие получить доступ к библиотеке

%package php
Summary: PDFLib php binding
Summary(ru_RU.KOI8-R):  PDFLib для php
Group: Development/C
Requires: php-common

%description php
PDF library binding for php

%description php -l ru_RU.KOI8-R
Модули для языка php, позволяющие получить доступ к библиотеке,
требуют наличия некоторых коммерческих библиотек.
%endif

%prep
%setup -n PDFlib-Lite-%version%patchlevel
#patch1 -p1

%build
%configure \
	--with-pyincl=%python_includedir \
	--with-py=%_usr \
	--with-tclpkg=%_libdir/tcl
make all

%install
%makeinstall_std

%if 0
install -m0755 --directory      %buildroot%_includedir
install -m0755 --directory      %buildroot/usr/bin
install -m0755 --directory      %buildroot%_libdir/%pythondir/site-packages
install -m0755 --directory      %buildroot%_libdir/%pythondir/lib-dynload
install -m0755 --directory      %buildroot%_datadir/tcl/tcl8.4/pdflib
install -m0755 --directory      %buildroot$RPM_DOC_DIR/PDFLib-Lite-%version
install -m0755 --directory      %buildroot%_libdir/perl5/i386-linux/auto/pdflib_pl

/bin/install -c -m 644 libs/pdflib/pdflib.h %buildroot%_includedir
cd libs/pdflib/
../../libtool --silent /bin/install -c -m 644 libpdf.la  %buildroot%_libdir/
cd ../..

cp -af doc/*  %buildroot$RPM_DOC_DIR/PDFLib-Lite-%version

/bin/install -c -m 644 pdflib-config %buildroot%_bindir/
/bin/install -c -m 644 bind/pdflib/python/.libs/*  %buildroot%_libdir/%pythondir/lib-dynload/
/bin/install -c -m 644 bind/pdflib/tcl/.libs/*  %buildroot%_libdir/tcl/tcl8.4/pdflib/
/bin/install -c -m 644 bind/pdflib/perl/.libs/*  %buildroot%_libdir/perl5/i386-linux/auto/pdflib_pl
/bin/install -c -m 644 bind/pdflib/perl/pdflib_pl.pm  %buildroot%_libdir/perl5/i386-linux
#/bin/install -c -m 644 progs/pdflib/{pdfimage,pdfimpose,text2pdf}  %buildroot%_bindir/
/bin/install -c -m 644 progs/pdflib/{pdfimage,text2pdf}  %buildroot%_bindir/

%define samples businesscard,chartab,hello,image,invoice,pdfclock

install -m0755 --directory %buildroot$RPM_DOC_DIR/PDFLib-Lite-%version/sample/data
/bin/install -c -m 644 bind/pdflib/data/* \
	%buildroot$RPM_DOC_DIR/PDFLib-Lite-%version/sample/data

install -m0755 --directory %buildroot$RPM_DOC_DIR/PDFLib-Lite-%version/sample/tcl
/bin/install -c -m 644 bind/pdflib/tcl/{{%samples}.tcl,readme.txt} \
	%buildroot$RPM_DOC_DIR/PDFLib-Lite-%version/sample/tcl

install -m0755 --directory %buildroot$RPM_DOC_DIR/PDFLib-Lite-%version/sample/perl
/bin/install -c -m 644 bind/pdflib/perl/{{%samples}.pl,readme.txt} \
	%buildroot$RPM_DOC_DIR/PDFLib-Lite-%version/sample/perl

install -m0755 --directory %buildroot$RPM_DOC_DIR/PDFLib-Lite-%version/sample/python
/bin/install -c -m 644 bind/pdflib/python/{{%samples}.py,readme.txt} \
	%buildroot$RPM_DOC_DIR/PDFLib-Lite-%version/sample/python

install -m0755 --directory %buildroot$RPM_DOC_DIR/PDFLib-Lite-%version/sample/php
/bin/install -c -m 644  bind/pdflib/php/{{%samples}.php,readme.txt} \
	%buildroot$RPM_DOC_DIR/PDFLib-Lite-%version/sample/php
%endif

%files

%files docs
%doc doc/*
#_docdir/PDFLib-Lite-%version/sample/data

%files utils
%_bindir/pdflib-config
%_bindir/pdfimage
#_bindir/pdfimpose
%_bindir/text2pdf

%files -n %libname
%_libdir/libpdf.so*

%files -n %libname-devel
#%_libdir/libpdf.la
#_libdir/libpdf.a
%_includedir/pdflib.h

%if 0
%files python
#_libdir/%pythondir/lib-dynload/*
%_docdir/PDFLib-Lite-%version/sample/python

%files perl
%_docdir/PDFLib-Lite-%version/sample/perl
#_libdir/perl5/i386-linux/auto/pdflib_pl/*
#_libdir/perl5/i386-linux/*

%files tcl
#_datadir/tcl/tcl8.4/pdflib
%_docdir/PDFLib-Lite-%version/sample/tcl

%files php
%_docdir/PDFLib-Lite-%version/sample/php
%endif

# TODO:
# - fix bindings
# - devel-static subpackage?
# - consider http://cvs.pld-linux.org/cgi-bin/cvsweb/packages/pdflib/pdflib.spec

%changelog
* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.0.4-alt3.p1.1
- Rebuilt for debuginfo

* Sat Jul 25 2009 Michael Shigorin <mike@altlinux.org> 7.0.4-alt3.p1
- moved docs to separate noarch subpackage (repocop)

* Thu Jul 23 2009 Michael Shigorin <mike@altlinux.org> 7.0.4-alt2.p1
- applied repocop patch

* Sat Jun 06 2009 Michael Shigorin <mike@altlinux.org> 7.0.4-alt1.p1
- 7.0.4p1
- adopted an orphan (optional for grace)
- dropped all language bindings (need fixing)
- dropped sample/data from docs for now
- dropped static library for now
- fixed License:
- spec cleanup

* Thu Mar 03 2005 Andrey Orlov <cray@altlinux.ru> 6.0.1-alt2
- Adopted to use with python2.4

* Sat Jan 15 2005 Andrey Orlov <cray@altlinux.ru> 6.0.1-alt1
- New Version

* Sun Jan 11 2004 Andrey Orlov <cray@altlinux.ru> 5.0.1-alt5
- Spec remarks enhanced

* Sun Dec 21 2003 Andrey Orlov <cray@altlinux.ru> 5.0.1-alt4
- Patched

* Sun Dec 21 2003 Andrey Orlov <cray@altlinux.ru> 5.0.1-alt3
- Python23 adopted

* Tue Aug 26 2003 Andrey Orlov <cray@altlinux.ru> 5.0.1-alt2
- Tested release

* Mon Aug 25 2003 Andrey Orlov <cray@altlinux.ru> 5.0.1-alt1
- Inintial release
