%define srcName leptonlib

Name: libleptonica
Version: 1.68
Release: alt1
Summary: A library for manipulating images
Summary(ru_RU.UTF-8): Библиотека для операций над изображениями
License: Leptonica license (BSD-like)
Group: System/Libraries
Url: http://www.leptonica.com
Requires: libjpeg, libtiff, libpng
BuildRequires: doxygen, libjpeg-devel, libtiff-devel, libpng-devel

Packager: %packager

Source: leptonlib-%version.tar.bz2
Patch: %name-alt-makefile.patch
Patch1: %name-alt-doc.patch

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
%_docdir/libleptonica-xxx/html_reference

%prep
%setup -q -n %srcName-%version
%patch0 -p1
%patch1 -p1

%build
doxygen Doxyfile
cd src

# Эта строка - обход ошибки с make
# В дальнейшем нужно перейти на схему с configure
mv makefile.static makefile

make -f makefile all

%install
mkdir -p %buildroot{%_libdir,%_includedir,%_includedir/leptonica}

%define docdir %_docdir/%name-%version
rm -rf %buildroot%docdir
mkdir -p %buildroot%docdir
install -pm644 leptonica-license.txt %buildroot%docdir/
install -pm644 README.html %buildroot%docdir/
install -pm644 version-notes.html %buildroot%docdir/
install -spm644 lib/shared/liblept.so.%version %buildroot%_libdir/
cp -af lib/shared/*.so %buildroot%_libdir/
install -spm644 lib/nodebug/*.a %buildroot%_libdir/
install -pm644 src/*.h %buildroot%_includedir/leptonica/
mv doc/html doc/html_reference
mv doc/html_reference %buildroot%docdir

%find_lang %name

%files
%_libdir/*.so.*
%dir %docdir
%docdir/*.html
%docdir/*.txt

%files devel
%_libdir/*.so
%_includedir/*

%files devel-static
%_libdir/*.a

%files doc
%dir %docdir/html_reference
%docdir/html_reference/*

%changelog
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

