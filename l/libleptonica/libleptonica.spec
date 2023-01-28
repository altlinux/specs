%define srcName leptonlib

Name: libleptonica
Version: 1.83.1
Release: alt1

Summary: A library for manipulating images
Summary(ru_RU.UTF-8): Библиотека для операций над изображениями

License: BSD-2-Clause
Group: System/Libraries
Url: http://www.leptonica.com

# Source-url: https://github.com/DanBloomberg/leptonica/releases/download/%version/leptonica-%version.tar.gz
Source: leptonlib-%version.tar.bz2

Patch: %name-1.69-alt-debuginfo.patch
Patch1: %name-alt-makefile.patch

BuildRequires: doxygen
BuildRequires: libjpeg-devel
BuildRequires: libtiff-devel
BuildRequires: libpng-devel
BuildRequires: libgif-devel
BuildRequires: libwebp-devel
BuildRequires: libopenjpeg2.0-devel

%package devel
Summary: Development files for programs which will use the Leptonica library
Summary(ru_RU.UTF-8): Заголовочные файлы для программ, использующих библиотеку Leptonica
Group: Development/C
Requires: %name = %version-%release glibc-devel libcurl-devel libssl-devel zlib-devel libjpeg-devel libtiff-devel libpng-devel

%package devel-static
Summary: Static Leptonica library
Summary(ru_RU.UTF-8): Версия библиотеки Leptonica для статического связывания
Group: Development/C
Requires: %name-devel = %version-%release

%package doc
Summary: Documentation prepared with Doxygen
Group: Development/C
Requires: %name-devel = %version-%release
BuildArch: noarch

%description
This package contains a Leptonica shared library of functions for loading,
manipulating and saving image files.

%description -l ru_RU.UTF-8
Библиотека Leptonica предназначена для создания программ, обрабатывающих
цветные и чёрно-белые изображения. Она содержит большое количество
низкоуровневых процедур обработки изображений. В частности, процедуры,
осуществляющие изменение контрастности, яркости, построение гистограмм,
различные морфологические процедуры. Библиотека написана на языке C.
Обязательно следует отметить, что новые версии библиотеки выходят довольно часто,
примерно раз в месяц, и не всегда полностью совместимы друг с другом.

%description devel
This package includes development files necessary for developing programs
which use Leptonica library

%description -l ru_RU.UTF-8 devel
Этот пакет содержит заголовочные файлы для библиотеки Leptonica -
библиотеки, предназначенной для создания программ, обрабатывающих изображения.

%description devel-static
This package includes static library necessary for developing statically
which use Leptonica library

%description -l ru_RU.UTF-8 devel-static
Этот пакет содержит версию библиотеки Leptonica для статического связывания.
Использование статической версии библиотеки зачастую оправдано, поскольку
обратная совместимость между версиями библиотеки не сохраняется, а
новые выпуски появляются примерно раз в месяц.

%description doc
This package includes Leptonica library documentation prepared with Doxygen.
The documentation is in html format.

%description -l ru_RU.UTF-8 doc
В этом пакете содержится автоматически сгенерированная с помощью пакета
Doxygen документация в html формате по функциям библиотеки Leptonica. Все функции библиотеки,
которые можно использовать из программ, имеют краткое описание и определение
параметров. Другой документации, к сожалению, не существует.
Файлы с описаниями библиотеки расположены в каталоге
%_docdir/libleptonica-xxx/html

%prep
%setup -n %srcName-%version
%autopatch -p1

%build
# Packaging static libraries lto * .a
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%autoreconf
%configure
%make_build

doxygen Doxyfile

%install
%makeinstall_std
# link to a non-existent file
rm -f %buildroot%_libdir/*.la

%files
%doc README.html
%doc version-notes.html
%doc leptonica-license.txt
%_libdir/*.so.*
# utilities for working with files
# without them, the work with the program will be incomplete
%_bindir/*

%files devel
%_includedir/leptonica
%_libdir/libleptonica.so
%_pkgconfigdir/lept.pc
%_libdir/cmake/LeptonicaConfig-version.cmake
%_libdir/cmake/LeptonicaConfig.cmake

%files devel-static
%_libdir/*.a

%files doc
%doc doc/html/*

%changelog
* Sat Jan 28 2023 Evgeny Chuck <koi@altlinux.org> 1.83.1-alt1
- new version (1.83.1) with rpmgs script

* Wed Dec 21 2022 Evgeny Chuck <koi@altlinux.org> 1.83.0-alt1
- new version (1.83.0) with rpmgs script

* Sun Feb 13 2022 Evgeny Chuck <koi@altlinux.org> 1.82.0-alt2
- Restoring deleted patches:
  + libleptonica-alt-makefile.patch
  + libleptonica-1.69-alt-debuginfo.patch
- cleanup spec

* Thu Dec 16 2021 Evgeny Chuck <koi@altlinux.org> 1.82.0-alt1
- new version (1.82.0) with rpmgs script
- Added OpenJPEG codec for working with jpeg images
- minor fixes in spec

* Mon Aug 17 2020 Pavel Vasenkov <pav@altlinux.org> 1.73-alt3
- NMU: correct license information 

* Tue Aug 30 2016 Vitaly Lipatov <lav@altlinux.ru> 1.73-alt2
- pack lept.pc (ALT bug #32432)

* Wed Feb 10 2016 Andrey Bergman <vkni@altlinux.org> 1.73-alt1
- update to version 1.73

* Thu Jun 04 2015 Andrey Bergman <vkni@altlinux.org> 1.72-alt1
- update to version 1.72

* Sun Oct 19 2014 Andrey Bergman <vkni@altlinux.org> 1.71-alt1
- update to version 1.71

* Tue Jan 28 2014 Andrey Bergman <vkni@altlinux.org> 1.70-alt1
- update to version 1.70

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.69-alt2.3
- Rebuilt with libpng15

* Tue Sep 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.69-alt2.2
- Rebuilt for debuginfo

* Sun Sep 02 2012 Dmitry V. Levin <ldv@altlinux.org> 1.69-alt2.1
- Built with libtiff.so.5.

* Sat Aug 04 2012 Andrey Bergman <vkni@altlinux.org> 1.69-alt2
- corrected BuildRequires

* Thu Jul 19 2012 Andrey Bergman <vkni@altlinux.org> 1.69-alt1
- update to version 1.69

* Wed Apr 20 2011 Andrey Bergman <vkni@altlinux.org> 1.68-alt1
- update to version 1.68

* Wed Dec 01 2010 Andrey Bergman <vkni@altlinux.org> 1.67-alt1
- update to version 1.67

* Tue Aug 10 2010 Andrey Bergman <vkni@altlinux.org> 1.66-alt1
- update to version 1.66

* Thu Apr 08 2010 Andrey Bergman <vkni@altlinux.org> 1.65-alt1
- update to version 1.65

* Wed Jan 06 2010 Andrey Bergman <vkni@altlinux.org> 1.64-alt1
- update to version 1.64

* Mon Nov 09 2009 Andrey Bergman <vkni@altlinux.org> 1.63-alt1
- update to version 1.63

* Fri Aug 07 2009 Andrey Bergman <vkni@altlinux.org> 1.62-alt1
- update to version 1.62

* Fri May 08 2009 Andrey Bergman <vkni@altlinux.org> 1.61-alt2
- Architecture fix. Shared lib policy fix.

* Tue Apr 28 2009 Andrey Bergman <vkni@altlinux.org> 1.61-alt1
- update to version 1.61. Architecture correction.

* Mon Jan 19 2009 Andrey Bergman <vkni@altlinux.org> 1.60-alt1
- rapid update to version 1.60 (fixed bug introduced in 1.59)

* Mon Jan 12 2009 Andrey Bergman <vkni@altlinux.org> 1.59-alt1
- update to version 1.59

* Fri Nov 07 2008 Andrey Bergman <vkni@altlinux.org> 1.58-alt1
- update to version 1.58

* Sun Aug 10 2008 Andrey Bergman <vkni@altlinux.org> 1.57-alt1
- update to version 1.57

* Thu May 15 2008 Andrey Bergman <vkni@altlinux.org> 1.56-alt1
- update to version 1.56

* Fri Mar 21 2008 Andrey Bergman <vkni@altlinux.org> 1.55-alt1
- update to version 1.55

* Wed Mar 05 2008 Andrey Bergman <vkni@altlinux.org> 1.54-alt1
- initial release
