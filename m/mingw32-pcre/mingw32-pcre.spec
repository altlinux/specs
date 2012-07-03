%define __strip %_mingw32_strip
%define __objdump %_mingw32_objdump

%define origname pcre

Name: mingw32-%origname
Version: 8.12
Release: alt1

Summary: Windows MinGW Perl-compatible regular expression library
License: BSD-style
Group: System/Libraries
Url: http://www.pcre.org/
Packager: Igor Vlasenko <viy@altlinux.org>

Source: ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-%version.tar
Source1: pcre-config.1

# patch from normal alt pcre
Patch1: pcre-%version-%release.patch

Summary(ru_RU.UTF-8): Windows MinGW Библиотека для работы с Perl-совместимыми регулярными выражениями

%def_enable cpp
%define libname mingw32-lib%origname

BuildArch: noarch

BuildRequires(pre): rpm-build-mingw32
BuildRequires: mingw32-gcc
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-binutils
# we disable pcregrep-libz/pcregrep-libbz2
#BuildRequires: mingw32-zlib
#BuildRequires: mingw32-zlib-static
#BuildRequires: mingw32-bzlib

Requires: pkgconfig

%package -n %libname
Summary: Windows MinGW Perl-compatible regular expression %{?_enable_compat:compatibility }shared library
Summary(ru_RU.UTF-8): Windows MinGW Разделяемая библиотека для работы с регулярными выражениями Perl-стиля
Group: System/Libraries
Provides: %name = %version
Obsoletes: %name < %version

%package -n %libname-devel
Summary: Windows MinGW Perl-compatible regular expressions development environment
Summary(ru_RU.UTF-8): Windows MinGW Заголовочные файлы и документация для разработки с использованием библиотеки PCRE
Group: Development/C
Provides: %name-devel = %version
Obsoletes: %name-devel < %version
Requires: %libname = %version-%release

%package -n %libname-devel-static
Summary: Windows MinGW Perl-compatible regular expressions static library
Summary(ru_RU.UTF-8): Windows MinGW Вариант библиотеки PCRE для статической компоновки
Group: Development/C
Provides: %name-devel-static = %version
Obsoletes: %name-devel-static < %version
Requires: %libname-devel = %version-%release

%package -n %{libname}cpp
Summary: Windows MinGW Perl-compatible regular expressions C++ wrapper shared library
Summary(ru_RU.UTF-8): Windows MinGW Разделяемая библиотека для работы с регулярными выражениями Perl-стиля на C++
Group: System/Libraries
Requires: %libname = %version-%release

%package -n %{libname}cpp-devel
Summary: Windows MinGW Perl-compatible regular expressions C++ wrapper development library and header files
Summary(ru_RU.UTF-8): Windows MinGW Заголовочные файлы и библиотека для разработки на C++ с использованием PCRE
Group: Development/C
Requires: %{libname}cpp = %version-%release, %libname-devel = %version-%release

%package -n %{libname}cpp-devel-static
Summary: Windows MinGW Perl-compatible regular expressions C++ wrapper static library
Summary(ru_RU.UTF-8): Windows MinGW статическая библиотека для разработки на C++ с использованием PCRE
Group: Development/C
Requires: %{libname}cpp-devel = %version-%release, %libname-devel = %version-%release

%description
The PCRE library is a set of functions that implement regular expression
pattern matching using the same syntax and semantics as Perl, with
just a few differences.  The current implementation of PCRE corresponds
approximately with Perl 5.8.

%_mingw32_description

%description -l ru_RU.UTF-8
Библиотека PCRE (Perl-compatible regular expressions) предоставляет
набор функций для работы с регулярными выражениями, синтаксис и смысл
которых полностью совпадают со встроенными регулярными выражениями
языка Perl версии 5.8.

%_mingw32_description

%description -n %libname
The PCRE library is a set of functions that implement regular expression
pattern matching using the same syntax and semantics as Perl, with
just a few differences.  The current implementation of PCRE corresponds
approximately with Perl 5.8.

This package contains PCRE shared libraries.
%_mingw32_description

%description -n %libname -l ru_RU.UTF-8
Библиотека PCRE (Perl-compatible regular expressions) предоставляет
набор функций для работы с регулярными выражениями, синтаксис и смысл
которых полностью совпадают со встроенными регулярными выражениями
языка Perl версии 5.8.

Данный пакет содержит динамическую разделяемую библиотеку PCRE.

%_mingw32_description

%description -n %{libname}cpp
The PCRE library is a set of functions that implement regular expression
pattern matching using the same syntax and semantics as Perl, with
just a few differences.  The current implementation of PCRE corresponds
approximately with Perl 5.8.

This package contains PCRE C++ wrapper shared library.

%_mingw32_description

%description -n %{libname}cpp -l ru_RU.UTF-8
Библиотека PCRE (Perl-compatible regular expressions) предоставляет набор
функций для работы с регулярными выражениями, синтаксис и смысл которых
полностью совпадают со встроенными регулярными выражениями языка Perl
версии 5.8.

Данный пакет содержит динамическую разделяемую библиотеку PCRE для C++.

%_mingw32_description

%description -n %libname-devel
The PCRE library is a set of functions that implement regular expression
pattern matching using the same syntax and semantics as Perl, with
just a few differences.  The current implementation of PCRE corresponds
approximately with Perl 5.8.

This package contains development libraries, include files and development
documentation required for developing applications which use perl-style
regular expressions.

%_mingw32_description

%description -n %libname-devel -l ru_RU.UTF-8
Библиотека PCRE (Perl-compatible regular expressions) предоставляет набор
функций для работы с регулярными выражениями, синтаксис и смысл которых
полностью совпадают со встроенными регулярными выражениями языка Perl
версии 5.8.

Данный пакет содержит средства разработки: заголовочные файлы и
документацию, необходимые для написания и сборки программ, использующих
библиотеку PCRE.

%_mingw32_description

%description -n %{libname}cpp-devel
The PCRE library is a set of functions that implement regular expression
pattern matching using the same syntax and semantics as Perl, with
just a few differences.  The current implementation of PCRE corresponds
approximately with Perl 5.8.

This package contains development libraries, include files and development
documentation required for developing C++ applications which use
perl-style regular expressions.

%_mingw32_description

%description -n %{libname}cpp-devel -l ru_RU.UTF-8
Библиотека PCRE (Perl-compatible regular expressions) предоставляет набор
функций для работы с регулярными выражениями, синтаксис и смысл которых
полностью совпадают со встроенными регулярными выражениями языка Perl
версии 5.8.

Данный пакет содержит средства разработки: заголовочные файлы и
документацию, необходимые для написания и сборки программ на C++,
использующих библиотеку PCRE.

%_mingw32_description

%description -n %libname-devel-static
The PCRE library is a set of functions that implement regular expression
pattern matching using the same syntax and semantics as Perl, with
just a few differences.  The current implementation of PCRE corresponds
approximately with Perl 5.8.

This package contains static development libraries required for developing
statically linked applications which use perl-style regular expressions.

%_mingw32_description

%description -n %libname-devel-static -l ru_RU.UTF-8
Библиотека PCRE (Perl-compatible regular expressions) предоставляет набор
функций для работы с регулярными выражениями, синтаксис и смысл которых
полностью совпадают со встроенными регулярными выражениями языка Perl
версии 5.8.

Данный пакет содержит библиотеку для статической компоновки программ,
использующих функции PCRE.

%_mingw32_description

%description -n %{libname}cpp-devel-static
The PCRE library is a set of functions that implement regular expression
pattern matching using the same syntax and semantics as Perl, with
just a few differences.  The current implementation of PCRE corresponds
approximately with Perl 5.8.

This package contains static development libraries required for developing
statically linked C++ applications which use perl-style regular expressions.

%_mingw32_description

%description -n %{libname}cpp-devel-static -l ru_RU.UTF-8
Библиотека PCRE (Perl-compatible regular expressions) предоставляет набор
функций для работы с регулярными выражениями, синтаксис и смысл которых
полностью совпадают со встроенными регулярными выражениями языка Perl
версии 5.8.

Данный пакет содержит библиотеку для статической компоновки C++ программ,
использующих функции PCRE.

%_mingw32_description

%prep
%setup -q -n %origname-%version
%patch1 -p1

%build
mkdir -p m4
autoreconf -fisv
%define docdir %_docdir/%name
%_mingw32_configure \
	--includedir=%_mingw32_includedir/pcre \
	%{subst_enable cpp} \
	--enable-utf8 \
	--enable-unicode-properties \
	#
#make_build
make

%install
%make_install install DESTDIR=%buildroot

# No need to distribute manpages which appear in the native packages already
#install -pm644 %_sourcedir/pcre-config.1 %buildroot%_mingw32_mandir/man1
rm -rf %buildroot%_mingw32_mandir
# the same
rm -rf %buildroot%_mingw32_docdir



#bzip2 -9 %buildroot%docdir/ChangeLog
#install -pm644 HACKING pcredemo.c %buildroot%docdir/

#rm %buildroot%_mingw32_bindir/pcregrep
#rm %buildroot%_mingw32_mandir/man1/pcregrep.*
#rm %buildroot%_mingw32_libdir/*.la

%files -n %libname
%_mingw32_bindir/libpcreposix-3.dll
%_mingw32_bindir/libpcre-3.dll
#%dir %docdir
#%docdir/[ACLN]*
%doc AUTHORS COPYING NEWS ChangeLog LICENCE NON-UNIX-USE

%files -n %libname-devel
%_mingw32_libdir/libpcreposix.la
%_mingw32_libdir/libpcre.la
#%_mingw32_bindir/*
%_mingw32_bindir/pcretest.exe
%_mingw32_bindir/pcre-config
%_mingw32_bindir/pcregrep.exe
%_mingw32_libdir/pkgconfig/libpcre.pc
#%_mingw32_mandir/man1/*
#%_mingw32_mandir/man3/*
%_mingw32_includedir/pcre
%if_enabled cpp
%exclude %_mingw32_includedir/pcre/pcrecpp*.h
%exclude %_mingw32_includedir/pcre/pcre_*.h
#%exclude %_mingw32_mandir/man3/pcrecpp.*
%endif #cpp
#%dir %docdir
#%docdir/H*
#%docdir/*.c

%if_enabled cpp
%files -n %{libname}cpp
%_mingw32_bindir/libpcrecpp-1.dll

%files -n %{libname}cpp-devel
%_mingw32_libdir/libpcrecpp.la
%dir %_mingw32_includedir/pcre
%_mingw32_includedir/pcre/pcrecpp*.h
%_mingw32_includedir/pcre/pcre_*.h
%_mingw32_libdir/pkgconfig/libpcrecpp.pc
#%_mingw32_mandir/man3/pcrecpp.*
%endif #cpp

%files -n %libname-devel-static
#%_mingw32_libdir/*.a
%_mingw32_libdir/libpcreposix.a
%_mingw32_libdir/libpcre.a
%_mingw32_libdir/libpcreposix.dll.a
%_mingw32_libdir/libpcre.dll.a

%files -n %{libname}cpp-devel-static
%_mingw32_libdir/libpcrecpp.a
%_mingw32_libdir/libpcrecpp.dll.a

%changelog
* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 8.12-alt1
- new version

* Sun Aug 23 2009 Igor Vlasenko <viy@altlinux.ru> 7.9-alt2
- applied pcre-7.9-deb-alt-shlib.patch (soname 3).
  it seems to be a good tradition in that world too.

* Sat Aug 22 2009 Igor Vlasenko <viy@altlinux.ru> 7.9-alt1
- MinGW 32 build
