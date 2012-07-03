%def_without static

Name: pstoedit
Version: 3.60
Release: alt2

Summary: converts Postscript(TM) and PDF files to other vector graphic formats
Summary(ru_RU.KOI8-R): преобразует файлы Postscript(TM) и PDF в другие векторные форматы
Copyright: GPL
Group: Graphics
URL: http://www.pstoedit.net/pstoedit
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source0: %name-%version.tar.gz

Patch0: pstoedit-3.40-alt3.3-makefile-ldl.patch
Patch1: pstoedit-3.44-alt2-pkg-config.patch

Patch10: pstoedit-3.44-cxxflags.patch
Patch11: pstoedit-3.45-quiet.patch
Patch12: pstoedit-3.45-gcc43.patch

Patch13: pstoedit-3.45-asy.patch
Patch14: pstoedit-3.45-elif.patch


Requires: lib%name = %version-%release


# Automatically added by buildreq on Tue May 30 2006
BuildRequires: fontconfig gcc-c++ ghostscript-classic libgd2-devel libImageMagick-devel libplotter-devel libpng-devel pkg-config

%package -n lib%name
Summary: Libraries for pstoedit
Summary(ru_RU.KOI8-R): Библиотеки для pstoedit
Group: Development/C

%package -n lib%name-devel
Summary: Development tools for pstoedit
Summary(ru_RU.KOI8-R): Средства разработки для pstoedit
Group: Development/C
Requires: lib%name = %version-%release
Obsoletes: pstoedit-devel
Provides: pstoedit-devel = %version

%package -n lib%name-devel-static
Summary: Static libraries for developing pstoedit addons
Summary(ru_RU.KOI8-R): Статические библиотеки для разработки дополнений к pstoedit
Group: Development/C
Requires: lib%name-devel = %version-%release
Obsoletes: pstoedit-devel-static-%version
Provides: pstoedit-devel-static

%description 
pstoedit converts PostScript and PDF files to various vector graphic
formats. The resulting files can be edited or imported into various
drawing packages. Pstoedit comes with a large set of format drivers
integrated in the binary. Additional drivers can be installed as plugins
and are available via http://www.pstoedit.net/plugins/. Just copy the
plugins to the same directory where the pstoedit binary is installed.
However, unless you also get a license key for the plugins, the
additional drivers will slightly distort the resulting graphics. See the
documentation provided with the plugins for further details.


%description -l ru_RU.KOI8-R
pstoedit преобразует файлы PostScript и PDF в другие векторные форматы.
Полученные файлы можно редактировать или импортировать в различные
графические программы. В pstoedit уже содержится большое количество
обработчиков форматов (format drivers). Другие обработчики можно
устанавливать как дополнения (plugins), они доступны по адресу
http://www.pstoedit.net/plugins/. Просто скопируйте обработчик в тот же
самый каталог, в который установлена сама программа pstoedit. Однако,
если вы не получите файл с ключем для дополнений, дополнительные
обработчики будут слегка искажать изображение на выходе. Для
дополнительной информации смотрите документацию, прилагающуюся к
обработчику. 

%description -n lib%name
Libraries for pstoedit

%description -l ru_RU.KOI8-R -n lib%name
Библиотеки для pstoedit

%description -n lib%name-devel
Development tools for pstoedit


%description -l ru_RU.KOI8-R -n lib%name-devel
Средства разработки для pstoedit


%description -n lib%name-devel-static
Static libraries for developing pstoedit addons


%description -l ru_RU.KOI8-R -n lib%name-devel-static
Статические библиотеки для разработки дополнений к pstoedit

%prep
%setup -q %name-%version
#patch0 -p1
%patch1 -p1
#patch10 -p1 -b .cxxflags
#patch11 -p1 -b .quiet
%patch12 -p1 -b .gcc43
#patch13 -p1 -b .asy
#patch14 -p1 -b .elif


%__chmod 644 doc/*
%__chmod 644 examples/*
%__chmod 644 contrib/java/java1/*
%__chmod 644 contrib/java/java2/*
%__chmod 644 othersrc/gsdllinc/*

%build
%configure
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS"


%install
%makeinstall pkgdatadir=$RPM_BUILD_ROOT%_datadir/pstoedit
%__install -d $RPM_BUILD_ROOT%_man1dir
%__install -m 664 doc/pstoedit.1 $RPM_BUILD_ROOT%_man1dir

# remove non-packaged files
%__rm -f %buildroot%_libdir/*.la
%__rm -f %buildroot%_libdir/pstoedit/*.la
%if_without static
%__rm -f %buildroot%_libdir/*.a
%__rm -f %buildroot%_libdir/pstoedit/*.a
%endif

%files
%_bindir/pstoedit
%_man1dir/*
%doc doc/changelog.htm doc/index.htm doc/readme.txt doc/pstoedit.tex doc/pstoedit.htm doc/pstoedit.trans examples contrib/java

%files -n lib%name
%_libdir/*.so.*
%dir %_libdir/pstoedit
%_libdir/pstoedit/*
%dir %_datadir/pstoedit
%_datadir/pstoedit/*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_datadir/aclocal/*
%_libdir/pkgconfig/*

%if_with static
%files -n lib%name-devel-static
%_libdir/*.a
%dir %_libdir/pstoedit
%_libdir/pstoedit/*.a
%endif

%changelog
* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 3.60-alt2
- Rebuild with new libImageMagick

* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.60-alt1.1
- Removed bad RPATH

* Sun Sep 04 2011 Ilya Mashkin <oddity@altlinux.ru> 3.60-alt1
- 3.60 (Closes: #28428)

* Tue Sep 14 2010 Anton Farygin <rider@altlinux.ru> 3.50-alt1.2
- NMU: rebuild with new libImageMagick

* Fri Sep 03 2010 Anton Farygin <rider@altlinux.ru> 3.50-alt1.1
- NMU: rebuild with new libImageMagick

* Tue Aug 11 2009 Ilya Mashkin <oddity@altlinux.ru> 3.50-alt1
- 3.50

* Fri Jul 10 2009 Ilya Mashkin <oddity@altlinux.ru> 3.45-alt3
- fix build, update patches

* Sat Nov 08 2008 Ilya Mashkin <oddity@altlinux.ru> 3.45-alt2
- update patches, fix gcc4.3 build

* Wed Oct 08 2008 Ilya Mashkin <oddity@altlinux.ru> 3.45-alt1
- 3.45

* Thu Jan 11 2007 Yury A. Zotov <yz@altlinux.ru> 3.44-alt2
- bug #10622 is fixed (pkg-config --libs pstoedit now gives only -lpstoedit)

* Tue May 30 2006 Yury A. Zotov <yz@altlinux.ru> 3.44-alt1
- new version
- BuilsRequires is updated

* Sat Apr 15 2006 Yury A. Zotov <yz@altlinux.ru> 3.40-alt4
- added pstoedit-3.40-alt3.3-makefile-ldl.patch -- link 
  libpstoedit.so with libdl explicitly
- BuildRequires is updated

* Thu Sep 15 2005 Anton Farygin <rider@altlinux.ru> 3.40-alt3.2
- rebuild with libMagick.so.9

* Mon Sep 12 2005 Anton Farygin <rider@altlinux.ru> 3.40-alt3.1
- fixed rebuild

* Sat May 28 2005 Yury A. Zotov <yz@altlinux.ru> 3.40-alt3
- build with libplotter #6142, #6788

* Sat Apr 09 2005 Yury A. Zotov <yz@altlinux.ru> 3.40-alt2
- fixed bug #6461

* Thu Jan 20 2005 Stanislav Ievlev <inger@altlinux.org> 3.40-alt1
- 3.40

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 3.33-alt5.1
- Rebuilt with libtiff.so.4.

* Wed May 26 2004 Yury A. Zotov <yz@altlinux.ru> 3.33-alt5
- buildreq libtiff-devel

* Tue Dec 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 3.33-alt4
- do not package .la files.
- do not build libpstoedit-devel-static subpackage by default.

* Wed Oct 08 2003 Yury A. Zotov <yz@altlinux.ru> 3.33-alt3
- BuildRequires updates for Sisyphus 20031005
- pstoedit-3.32-alt1-configure-libtool_program.patch removed
- rebuild with hasher

* Sat Jan 25 2003 Yury A. Zotov <yz@altlinux.ru> 3.33-alt2
- libpstoedit-devel: provides/obsoletes pstoedit-devel
- libpstoedit-devel-static: provides/obsoletes pstoedit-devel-static

* Mon Jan 13 2003 Yury A. Zotov <yz@altlinux.ru> 3.33-alt1
- new version
- package split: pstoedit, libpstoedit, libpstoedit-{devel,devel-static}

* Sat Oct 26 2002 Yury A. Zotov <yz@altlinux.ru> 3.32-alt1
- new version
- split into pstoedit, pstoedit-devel, pstoedit-devel-static

* Fri Feb 1 2002 Yury Zotov <yz@altlinux.ru> 3.31-alt1
- initial release
