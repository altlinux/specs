Name: kakasi
Version: 2.3.4
Release: alt3

Summary: A Japanese character set conversion filter
Summary(ru_RU.UTF-8): Преобразователь японского текста
License: GPL
Group: Text tools
URL: http://kakasi.namazu.org/
Source: %name-%version.tar.bz2
Patch: kakasi-2.3.4-fixdict.patch

# Automatically added by buildreq on Sun Oct 16 2011
BuildRequires: glibc-devel-static

%description
KAKASI is a filter for converting Kanji characters to Hiragana or
Katakana characters, or into Romaji (phonetic transcription of
Japanese pronunciation).

%description -l ru_RU.UTF-8
KAKASI - фильтр для преобразования Канджи в Хирагана, Катакана
или Ромаджи (фонетическая транскрипция японского произношения).

%package devel
Summary: Files for development of applications which will use KAKASI
Summary(ru_RU.UTF-8): Файлы для написания программ, использующих KAKASI
Group: Development/C
Requires: %name = %version-%release

%description devel
The kakasi-devel package contains the header file and library for
developing applications which will use the KAKASI Japanese character
set filter.

%description devel -l ru_RU.UTF-8
Пакeт kakasi-devel файлы заголовков и библиотеку для написания
программ, использующих преобразователь японского текста KAKASI.

%prep
%setup -q
%patch -p1

%build
%configure --disable-static
%make

%install
%makeinstall
install -pD -m644 doc/kakasi.1 $RPM_BUILD_ROOT%_mandir/ja/man1/kakasi.1

%files
%_bindir/atoc_conv
%_bindir/kakasi
%_bindir/mkkanwa
%_bindir/rdic_conv
%_bindir/wx2_conv
%_libdir/libkakasi.so.*
%dir %_datadir/kakasi
%_datadir/kakasi/itaijidict
%_datadir/kakasi/kanwadict
%_mandir/ja/man1/kakasi.1*
%doc AUTHORS ChangeLog NEWS README README-ja

%files devel
%_bindir/kakasi-config
%_includedir/libkakasi.h
%_libdir/libkakasi.so

%changelog
* Sun Oct 16 2011 Alexey Tourbin <at@altlinux.ru> 2.3.4-alt3
- rebuilt for debuginfo

* Sun Nov 14 2010 Denis Smirnov <mithraen@altlinux.ru> 2.3.4-alt2.qa1.1
- rebuild (with the help of girar-nmu utility)

* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 2.3.4-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for kakasi
  * postun_ldconfig for kakasi
  * postclean-05-filetriggers for spec file

* Sat Apr 02 2005 Vyacheslav Dikonov <slava@altlinux.ru> 2.3.4-alt2
- minor fixes

* Sun Mar 27 2005 Vyacheslav Dikonov <slava@altlinux.ru> 2.3.4-alt1
- ALTLinux build (for xmltv tv_grab_jp)
