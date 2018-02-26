%define srcName minidjvu

Name: minidjvu
Version: 0.8
Release: alt1.1
Summary: A program to create bitonal djvu files.
Summary(ru_RU.UTF-8): Программа для создания чёрно-белых файлов djvu.
License: GPLv2
Group: System/Libraries
Url: http://minidjvu.sourceforge.net/
Requires: libminidjvu = %version-%release

Packager: %packager

Source: minidjvu-%version.tar.bz2

# Automatically added by buildreq on Sun Apr 18 2010
BuildRequires: gcc-c++ libjpeg-devel libtiff-devel recode zlib-devel

%package -n libminidjvu
Summary: Minidjvu library
Summary(ru_RU.UTF-8): Библиотека minidjvu
Group: Development/C

%package -n libminidjvu-devel
Summary: Development files for programs which will use the Minidjvu library
Summary(ru_RU.UTF-8): Заголовочные файлы для программ, использующих библиотеку minidjvu
Group: Development/C
Requires: libminidjvu = %version-%release

%package -n libminidjvu-devel-static
Summary: Static Minidjvu library
Summary(ru_RU.UTF-8): Версия библиотеки Minidjvu для статического связывания
Group: Development/C
Requires: libminidjvu-devel = %version-%release

%description
A simple program to make a pack bitonal graphical files
into djvu file. It is very useful for creating typical
djvu scientific book from the output of ScanTailor.

%description -l ru_RU.UTF-8
Простая программа для создания djvu файла из набора
чёрно-белых изображений. Крайне полезна при создании
отсканированных научно-технических книг в формате djvu
после обработки сканов программой ScanTailor.

%description -n libminidjvu
Shared library contaiting functions and algorithms
for creating djvu files from bitonal graphical files.

%description -n libminidjvu -l ru_RU.UTF-8
Разделяемая библиотека, содержащая функции для
перепаковки чёрно-белых графических файлов в формат djvu.

%description -n libminidjvu-devel
Header files for Minidjvu library.

%description -n libminidjvu-devel -l ru_RU.UTF-8
Заголовочные файлы для библиотеки Minidjvu.

%description -n libminidjvu-devel-static
Static version of Minidjvu library.

%description -l ru_RU.UTF-8 -n libminidjvu-devel-static
Статическая версия библиотеки Minidjvu.

%prep
%setup -q -n %srcName-%version

%build
# Перекодируем страницу man из UTF8 в кодировку KOI8-R.
recode utf-8..koi8-r doc/ru/minidjvu.1

%configure
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make

%install
%define docdir %_docdir/%name-%version
mkdir -p %buildroot{%_bindir,%_libdir,%_includedir,%_includedir/minidjvu,%docdir}
mkdir -p %buildroot%_includedir/minidjvu/{alg,alg/patterns,base,formats,jb2}

%makeinstall
install -pm644 NEWS %buildroot%docdir/
install -pm644 README %buildroot%docdir/
install -pm644 COPYING %buildroot%docdir/
install -pm644 doc/decode.html %buildroot%docdir/
install -pm644 doc/encode.html %buildroot%docdir/

install -pm644 minidjvu/alg/*.h %buildroot%_includedir/minidjvu/alg/
install -pm644 minidjvu/alg/patterns/*.h %buildroot%_includedir/minidjvu/alg/patterns
install -pm644 minidjvu/base/*.h %buildroot%_includedir/minidjvu/base/
install -pm644 minidjvu/formats/*.h %buildroot%_includedir/minidjvu/formats/
install -pm644 minidjvu/jb2/*.h %buildroot%_includedir/minidjvu/jb2/

install -pm644 minidjvu.h %buildroot%_includedir/minidjvu/

%find_lang %name

%files -f %name.lang
%_bindir/*
%dir %docdir
%docdir/*
%_mandir/man?/*
%_mandir/ru/man?/*

%files -n libminidjvu
%_libdir/*.so.*

%files -n libminidjvu-devel
%_libdir/*.so
%dir %_includedir/minidjvu
%_includedir/*

%files -n libminidjvu-devel-static
%_libdir/*.a

%changelog
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1.1
- Removed bad RPATH

* Wed Dec 08 2010 Andrey Bergman <vkni@altlinux.org> 0.8-alt1
- Added russian manual. 

* Sun Apr 18 2010 Andrey Bergman <vkni@altlinux.org> 0.8-alt0.5
- Initial release of the package.

