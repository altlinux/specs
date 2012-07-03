Name: libteckit
Version: 2.5.1
Release: alt2.1
Summary: Conversion library and mapping compiler
Summary(ru_RU.UTF-8): Библиотека для перекодирования текстовых файлов и компилятор таблиц соответствия для неё
License: LGPLv2+ or CPL
Group: System/Libraries
Url: http://scripts.sil.org/teckit
Packager: Andrey Bergman <vkni@altlinux.org>

Source: TECkit_2_5_1.tar.bz2
Patch: %name-alt-gcc4.4.patch

BuildRequires: gcc-c++ libexpat-devel zlib-devel

%description
TECkit is a low-level toolkit intended to be used by other
applications that need to perform encoding conversions (e.g., when
importing legacy data into a Unicode-based application). The
primary component of the TECkit package is therefore a library that
performs conversions; this is the "TECkit engine". The engine
relies on mapping tables in a specific binary format (for which
documentation is available); there is a compiler that creates such
tables from a human-readable mapping description (a simple text file).

%description -l ru_RU.UTF-8
TECkit - это низкоуровневая библиотека, предназначенная для использования
программами, требующими перевода текстов из одной кодировки в другую 
(например, в случаях, когда приложение, работающее с данными в формате 
Unicode получает 8-ми битные данные). Основной частью пакета TECkit является 
программная библиотека, осуществляющая перекодирование, так называемая
"TECkit engine". Помимо неё пакет включает в себя таблицы соответствия 
между кодировками в специальном бинарном формате. Они преобразуются специальным
компилятором из текствого формата.

%package devel
Summary: Conversion library and mapping compiler
Summary(ru_RU.UTF-8): Заголовочные файлы библиотеки для перекодирования текстовых файлов
Group: Development/C++
Requires: %name = %version-%release
Provides: %name-devel = %version-%release

%description devel
TECkit is a low-level toolkit intended to be used by other
applications that need to perform encoding conversions (e.g., when
importing legacy data into a Unicode-based application). The
primary component of the TECkit package is therefore a library that
performs conversions; this is the "TECkit engine". The engine
relies on mapping tables in a specific binary format (for which
documentation is available); there is a compiler that creates such
tables from a human-readable mapping description (a simple text file).

%description -l ru_RU.UTF-8 devel
TECkit - это низкоуровневая библиотека, предназначенная для использования
программами, требующими перевода текстов из одной кодировки в другую 
(например, в случаях, когда приложение, работающее с данными в формате 
Unicode получает 8-ми битные данные). Основной частью пакета TECkit является 
программная библиотека, осуществляющая перекодирование, так называемая
"TECkit engine". Помимо неё пакет включает в себя таблицы соответствия 
между кодировками в специальном бинарном формате. Они преобразуются специальным
компилятором из текстового формата.

Этот пакет содержит заголовочные файлы, требуемые для подключения
библиотеки и компилятора к программам, написанным на языке С. Кроме
того, в пакете содержится документация по использованию библиотеки.

%package utils
Summary: Utils for conversion library and mapping compiler
Summary(ru_RU.UTF-8): Утилиты, идущие в поставке с библиотекой для перекодирования текстовых файлов
Group: Text tools
Requires: %name = %version-%release
Provides: %name-devel = %version-%release

%description utils
Programs that come with TECkit encoding conversion library.

%description -l ru_RU.UTF-8 utils
Программы, идущие в поставке с библиотекой TECkit, перекодирующей
тексты.

%prep
%setup -q -n TECkit_2_5_1
%patch0 -p1

%__chmod 0755 ./autogen.sh
%__chmod 0755 ./configure
%__rm -r zlib*

%build
./autogen.sh
%configure --disable-static
make %_smp_mflags

%install
%__rm -rf %buildroot
%make_install install DESTDIR=%buildroot
rm -f %buildroot%_libdir/*.la

%find_lang %name

%files

%doc AUTHORS COPYING INSTALL NEWS README
%doc license/{LICENSING.txt,License_CPLv05.txt,License_LGPLv21.txt}
%_libdir/libTECkit.so.*
%_libdir/libTECkit_Compiler.so.*

%files devel

%doc docs/*.pdf
%_includedir/teckit/
%_libdir/libTECkit.so
%_libdir/libTECkit_Compiler.so

%files utils
%_bindir/sfconv
%_bindir/teckit_compile
%_bindir/txtconv

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 2.5.1-alt2.1
- rebuilt for debuginfo and soname set-versions

* Fri May 08 2009 Andrey Bergman <vkni@altlinux.org> 2.5.1-alt2
- patch for gcc 4.4

* Thu Dec 11 2008 Andrey Bergman <vkni@altlinux.org> 2.5.1-alt1
- new version

* Sat Mar 15 2008 Andrey Bergman <vkni@altlinux.org> 2.2.1-alt1
- initial release for Sisyphus

