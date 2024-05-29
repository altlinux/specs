%define _name liba52

%def_disable static

Name: a52dec
Version: 0.8.0
Release: alt1

Summary: Library for decoding ATSC A/52 streams
Summary(ru_RU.UTF-8): Библиотека для декодирования потоков ATSC A/52
Group: Sound
License: GPL-2.0
URL: https://git.adelielinux.org/community/a52dec

Source: %name-%version.tar
Requires: %_name = %version-%release

%if_enabled static
BuildRequires: glibc-devel-static
%endif

%description
liba52 is a free library for decoding ATSC A/52 streams. It is released
under the terms of the GPL license. The A/52 standard is used in a
variety of applications, including digital television and DVD. It is
also known as AC-3.

a52dec is a test program for liba52. It decodes ATSC A/52 streams, and
also includes a demultiplexer for mpeg-1 and mpeg-2 program streams.

%description -l ru_RU.UTF8
liba52 - свободная библиотека для декодирования потоков ATSC A/52,
выпущенная под лицензией GPL. Стандарт A/52 используется в различных
областях, включая цифровое телевидение и DVD. Он также известен как AC-3.

a52dec - программа для тестирования библиотеки liba52. Она декодирует
потоки ATSC A/52, а также содержит демультиплексор для потоков mpeg-1 и mpeg-2.

%package -n %_name
Summary: %_name shared libraries
Group: System/Libraries

%description -n %_name
This package contains shared version of %_name.

%description -n %_name -l ru_RU.UTF8
Этот пакет сожержит разделяемые библиотеки %_name.

%package -n %_name-devel
Summary: %_name header files and development libraries
Group: Development/C
Requires: %_name = %version-%release

%description -n %_name-devel
Header files and development libraries for %_name.

%description -n %_name-devel -l ru_RU.UTF8
Заголовочные файлы и библиотеки для разработки с %_name.

%if_enabled static
%package -n %_name-devel-static
Summary: %_name static libraries
Group: Development/C
Requires: %_name-devel = %version-%release

%description -n %_name-devel-static
Static version of %_name libraries.

%description -n %_name-devel-static -l ru_RU.UTF8
Статическая версия библиотек %_name.

%endif

%prep
%setup

%build
%add_optflags %optflags_shared

%autoreconf
%configure \
	--enable-shared \
	%{subst_enable static}

%make_build

%install
%makeinstall

# remove non-packaged files
rm -f %buildroot%_libdir/*.la

%files
%_bindir/*
%_man1dir/*
%doc README ChangeLog AUTHORS HISTORY TODO

%files -n %_name
%_libdir/*.so.*

%files -n %_name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/%_name.pc
%doc doc/%_name.txt

%if_enabled static
%files -n %_name-devel-static
%_libdir/*.a
%endif

%changelog
* Wed May 29 2024 Grigory Ustinov <grenka@altlinux.org> 0.8.0-alt1
- Build new version.

* Wed Jun 06 2018 Grigory Ustinov <grenka@altlinux.org> 0.7.4-alt9
- Add russian descriptions (Closes: #22773).

* Mon Apr 09 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.4-alt8
- drop pointless libtool_1.5 BR

* Mon Jul 23 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.4-alt7.1
- Fixed build

* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.4-alt7
- Rebuilt for debuginfo

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.4-alt6
- Rebuilt for soname set-versions

* Fri Nov 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.7.4-alt5.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for liba52
  * postun_ldconfig for liba52
  * postclean-05-filetriggers for spec file

* Fri Jan 05 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.7.4-alt5
- Fixed #8639 (proper packaging of %%_bindir).
- Changed packager field.
- Disable static library build.

* Tue Oct 17 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.7.4-alt4
- use libtool-1.5.
- use autoreconf.

* Fri Nov 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.7.4-alt3
- use libtool-1.4
- do not package .la files.
- fix TEXTREL bug.

* Sun Oct 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.7.4-alt2
- Rebuild with gcc-3.2. 

* Tue Aug 20 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.7.4-alt1
- 0.7.4

* Thu Apr 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.7.3-alt1
- First build for Sisyphus.
