#set_verify_elf_method none

Name: tesseract
Version: 5.3.0
Release: alt1

Summary: Tesseract Open Source OCR Engine
Summary(ru_RU.UTF-8): Движок распознавания текста с открытым исходным кодом

License: Apache-2.0
Group: Graphics
Url: https://github.com/tesseract-ocr

Packager: Andrey Cherepanov <cas@altlinux.org>

# Source-url: https://github.com/tesseract-ocr/tesseract/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

# installing language files /usr/share/tesseract/tessdata
Patch: tesseract-5.1.0-alt-makefile.patch

BuildRequires: gcc-c++
BuildRequires: libtiff-devel
BuildRequires: libleptonica-devel >= 1.74
BuildRequires: autoconf-archive
BuildRequires: libpango-devel
BuildRequires: libcairo-devel
BuildRequires: libicu-devel
BuildRequires: doxygen

Requires: %name-langpack-en >= 4.1.0
Requires: %name-langpack-ru >= 4.1.0

%description
This package contains an OCR engine - libtesseract and a command line
program - tesseract. Tesseract has unicode (UTF-8) support, and can recognize
more than 100 languages "out of the box". Tesseract supports various output
formats: plain text, hOCR (HTML), PDF, TSV. To improve OCR, you need to improve
the quality of the analyzed image.

%description -l ru_RU.UTF-8
Этот пакет содержит движок распознавания текста - libtesseract и программу
командной строки - tesseract. Tesseract поддерживает юникод (UTF-8) и может
распознавать более 100 языков "из коробки". Tesseract поддерживает различные
форматы вывода: txt, ocr (HTML), PDF, TSV. Чтобы улучшить распознавание текста,
необходимо улучшить качество анализируемого изображения.

%package devel
Summary: Development files for tesseract
Summary(ru_RU.UTF-8): Файлы разработки для tesseract
Group: Development/C
Requires: %name
Requires: libleptonica-devel >= 1.74

%description devel
The %name-devel package contains header file for
developing applications that use %name.

%description devel -l ru_RU.UTF-8
Пакет %name-devel содержит файлы заголовка для
разработки приложений, использующих %name.

%package doc
Summary: Tesseract OCR Tool Documentation
Summary(ru_RU.UTF-8): Документация по движку Tesseract OCR
Group: Documentation
BuildArch: noarch

%description doc
The documentation contains a description of the library functions and the
tesseract utilities. The development section has examples of teaching language
models.

%description doc -l ru_RU.UTF-8
Документация содержит описание функций библиотеки и утилит %name В разделе
разработки есть примеры обучения языковых моделей.

%prep
%setup
%patch -p2
%ifarch %e2k
# LCC autovectorization perform better than these brief SIMD snippets
sed -i "/CHECK_COMPILE_FLAG/{N;/_OPT/s/=true/=false/}" configure.ac
%add_optflags -mno-sse
%endif

%build
%autoreconf
%configure --disable-static
%make_build

# for teaching language models (dev)
%make_build training

doxygen doc/Doxyfile

%install
%makeinstall_std
%makeinstall_std training-install

# link to a non-existent file
rm -I %buildroot%_libdir/*.la

%files
%doc AUTHORS ChangeLog README.md LICENSE
%_bindir/*
%_datadir/%name/tessdata/configs
%_datadir/%name/tessdata/tessconfigs
%_datadir/%name/tessdata/pdf.ttf
%_libdir/lib*.so.5*

%files devel
%_includedir/%name
%_libdir/lib*.so
%_pkgconfigdir/%name.pc

%files doc
%doc doc/html/*

%changelog
* Fri Dec 23 2022 Evgeny Chuck <koi@altlinux.org> 5.3.0-alt1
- new version (5.3.0) with rpmgs script

* Sun Jul 10 2022 Evgeny Chuck <koi@altlinux.org> 5.2.0-alt1
- Build new version (Closes: 43192)
- new version (5.2.0) with rpmgs script

* Sat May 21 2022 Evgeny Chuck <koi@altlinux.org> 5.1.0-alt1
- new version (5.1.0) with rpmgs scrip
- Fixed path to "tessdata" directory

* Mon Jan 10 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 4.1.3-alt1.1
- fixed build for Elbrus

* Fri Dec 31 2021 Evgeny Chuck <koi@altlinux.org> 4.1.3-alt1
- new version (4.1.3) with rpmgs script
- Correct license installed
- Changing the installation path of language files
- Adaptation of the specification to version 4.1.3

* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 3.04.01-alt2
- build with libleptonica

* Thu Aug 25 2016 Vitaly Lipatov <lav@altlinux.ru> 3.04.01-alt1
- new version 3.04.01 (with rpmrb script)
- fix previous broken build

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 3.04.00-alt1
- new version 3.04.00 (with rpmrb script)

* Mon Dec 09 2013 Andrey Cherepanov <cas@altlinux.org> 3.02.02-alt1
- New version

* Thu May 03 2012 Andrey Cherepanov <cas@altlinux.org> 3.02-alt1.r723
- New version 3.02
- Major changes:
  * Added simultaneous multi-language capability.
  * Added experimental equation detector.
  * Improved handling of resolution from input images.
  * Major improvements to layout analysis for better image detection,
    diacritic detection, better textline finding, better tabstop finding.
  * Improved line detection and removal.
  * Many other fixes, including the way in which the chopper finds chops
    and messes with the outline while it does so.
- Build both executables and dictionaries from one package

* Wed Aug 31 2011 Andrey Cherepanov <cas@altlinux.org> 3.00-alt1
- New version 3.00 (closes: #25477)
- Add optflags_shared for build (closes: #25249)

* Tue Apr 26 2011 Fr. Br. George <george@altlinux.ru> 2.04-alt2
- Fix debuginfo

* Wed Sep 23 2009 Fr. Br. George <george@altlinux.ru> 2.04-alt1
- Version up

* Sat Nov 08 2008 Vitaly Lipatov <lav@altlinux.ru> 2.03-alt2
- fix build with gcc 4.3

* Fri May 09 2008 Vitaly Lipatov <lav@altlinux.ru> 2.03-alt1
- new version 2.03 (with rpmrb script)

* Wed Oct 24 2007 Vitaly Lipatov <lav@altlinux.ru> 2.01-alt1
- new version 2.01 (with rpmrb script)

* Tue Jul 24 2007 Vitaly Lipatov <lav@altlinux.ru> 2.00-alt1
- initial build for Sisyphus
