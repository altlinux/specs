# TODO: correct clip-glade linking with clip-gtk
# TODO: correct clip-gd linking with libpng, libtiff, and so on
# TODO: build clip-gd with system libgd, not internal
# TODO: what is locale.pot?

%define FCLIPDIR %_libdir/clip
%define VCLIPDIR %_localstatedir/clip

Name: libclip
Version: 1.2.0cvs
Release: alt3.qa2

Summary: XBASE/Clipper compatible program compiler - runtime library
Summary(ru_RU.KOI8-R): Совместимый с XBASE/Clipper компилятор программ -- дополнительные библиотеки

License: GPL
Group: Development/Other
Url: http://www.itk.ru

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar.bz2
#Source10: %name-%version-2005-02-03.tar.bz2
Patch: %name-%version-ezV24.patch

# TODO: fix linking
%set_verify_elf_method unresolved=relaxed
%add_findprov_lib_path %FCLIPDIR/lib


# manually removed: linux-libc-headers 
# Automatically added by buildreq on Mon Sep 11 2006
BuildRequires: bzlib-devel clip libexpat-devel libfcgi-devel libglade-devel libgpm-devel libjpeg-devel libMySQL-devel libunixODBC-devel libXpm-devel postgresql-devel libpth-devel libezV24-devel zlib-devel libssl-devel libpng-devel libtiff-devel libgd2-devel
# do not use gtk1: libgtk+extra-devel 

BuildPreReq: clip = %version

%description
This package provides runtime shared libraries for CLIP package

%description -l ru_RU.KOI8-R
Данный пакет предоставляет разделяемые библиотеки времени выполнения
для CLIP.

############################################################################
%package -n %name-all
Summary: XBASE/Clipper compatible program compiler - all additional library
Summary(ru_RU.KOI8-R): Совместимый с XBASE/Clipper компилятор программ -- все дополнительные библиотеки
Group: Development/Other

#Requires: %name-ui
Requires: %name-common = %version-%release
Requires: %name-gd = %version-%release
#Requires: %name-gtk = %version-%release
Requires: %name-gtk2 = %version-%release
#Requires: %name-interbase = %version-%release
Requires: %name-mysql = %version-%release
Requires: %name-odbc = %version-%release
Requires: %name-postgres = %version-%release

%description -n %name-all
This virtual package provides all runtime shared libraries for CLIP package
%name-common
%name-gtk
- %name-gtk
%name-gtk2
- %name-interbase
%name-mysql
%name-odbc
%name-postgres

%description -n %name-all -l ru_RU.KOI8-R
Данный виртуальный пакет предоставляет всё разделяемые библиотеки времени выполнения
для CLIP.
%name-common
%name-gd
- %name-gtk
%name-gtk2
- %name-interbase
%name-mysql
%name-odbc
%name-postgres

############################################################################
%package -n %name-common
Summary: XBASE/Clipper compatible program compiler - common library
Summary(ru_RU.KOI8-R): Совместимый с XBASE/Clipper компилятор программ -- общие библиотеки
Group: Development/Other

Requires: %name >= %version

%description -n %name-common
This package provides common runtime shared libraries for CLIP

%description -n %name-common -l ru_RU.KOI8-R
Данный пакет предоставляет общие разделяемые библиотеки времени выполнения
для CLIP.

############################################################################
%package -n %name-gtk
Summary: XBASE/Clipper compatible program compiler - gtk library
Summary(ru_RU.KOI8-R): Совместимый с XBASE/Clipper компилятор программ -- использование gtk
Group: Development/Other

Requires: %name-common = %version-%release

%description -n %name-gtk
This package provides gtk runtime shared libraries for CLIP

%description -n %name-gtk -l ru_RU.KOI8-R
Данный пакет предоставляет разделяемые библиотеки для использования gtk в CLIP.

############################################################################
%package -n %name-gd
Summary: XBASE/Clipper compatible program compiler - gd library
Summary(ru_RU.KOI8-R): Совместимый с XBASE/Clipper компилятор программ -- использование gd
Group: Development/Other

Requires: %name-common = %version-%release

%description -n %name-gd
This package provides gd runtime shared libraries for CLIP

%description -n %name-gd -l ru_RU.KOI8-R
Данный пакет предоставляет разделяемые библиотеки для использования gd в CLIP.

############################################################################
%package -n %name-gtk2
Summary: XBASE/Clipper compatible program compiler - gtk2 library
Summary(ru_RU.KOI8-R): Совместимый с XBASE/Clipper компилятор программ -- использование gtk2
Group: Development/Other

Requires: %name-common = %version-%release

%description -n %name-gtk2
This package provides gtk2 runtime shared libraries for CLIP

%description -n %name-gtk2 -l ru_RU.KOI8-R
Данный пакет предоставляет разделяемые библиотеки для использования gtk2 в CLIP.

############################################################################
%package -n %name-ui
Summary: XBASE/Clipper compatible program compiler - ui library
Summary(ru_RU.KOI8-R): Совместимый с XBASE/Clipper компилятор программ -- использование ui
Group: Development/Other

Requires: %name-common = %version-%release

%description -n %name-ui
This package provides ui runtime shared libraries for CLIP

%description -n %name-ui -l ru_RU.KOI8-R
Данный пакет предоставляет разделяемые библиотеки для использования ui в CLIP.

############################################################################
%package -n %name-interbase
Summary: XBASE/Clipper compatible program compiler - library for database Interbase
Summary(ru_RU.KOI8-R): Совместимый с XBASE/Clipper компилятор программ -- библиотека для базы данных Interbase
Group: Development/Other

Requires: %name-common = %version-%release

%description -n %name-interbase
This package provides library for using database Interbase in CLIP.

%description -n %name-interbase -l ru_RU.KOI8-R
Данный пакет предоставляет библиотеку для использования базы данных Interbase в CLIP.

############################################################################
%package -n %name-mysql
Summary: XBASE/Clipper compatible program compiler - library for database MySQL
Summary(ru_RU.KOI8-R): Совместимый с XBASE/Clipper компилятор программ -- библиотека для базы данных MySQL
Group: Development/Other

Requires: %name-common = %version-%release

%description -n %name-mysql
This package provides library for using database MySQL in CLIP.

%description -n %name-mysql -l ru_RU.KOI8-R
Данный пакет предоставляет библиотеку для использования базы данных MySQL в CLIP.

############################################################################
%package -n %name-odbc
Summary: XBASE/Clipper compatible program compiler - library for ODBC
Summary(ru_RU.KOI8-R): Совместимый с XBASE/Clipper компилятор программ -- библиотека для ODBC
Group: Development/Other

Requires: %name-common = %version-%release

%description -n %name-odbc
This package provides library for using ODBC in CLIP.

%description -n %name-odbc -l ru_RU.KOI8-R
Данный пакет предоставляет библиотеку для использования баз данных через ODBC в CLIP.

############################################################################
%package -n %name-postgres
Summary: XBASE/Clipper compatible program compiler - library for database Postgre
Summary(ru_RU.KOI8-R): Совместимый с XBASE/Clipper компилятор программ -- библиотека для базы данных Postgre
Group: Development/Other

Requires: %name-common = %version-%release

%description -n %name-postgres
This package provides library for using database Postgre in CLIP.

%description -n %name-postgres -l ru_RU.KOI8-R
Данный пакет предоставляет библиотеку для использования баз данных Postgre в CLIP.

############################################################################

%package -n %name-fcgi
Summary: XBASE/Clipper compatible program compiler - fcgi library
Summary(ru_RU.KOI8-R): Совместимый с XBASE/Clipper компилятор программ -- использование fcgi
Group: Development/Other

Requires: %name-common = %version-%release

%description -n %name-fcgi
This package provides fcgi runtime shared libraries for CLIP

%description -n %name-fcgi -l ru_RU.KOI8-R
Данный пакет предоставляет разделяемые библиотеки для использования fcgi в CLIP.

%prep
%setup -q
%patch
# incorrect checking
echo > clip-ui/configure
cp clip-ui/Makefile.in clip-ui/Makefile
# fix /usr/lib
%__subst "s|/usr/lib|%_libdir|g" clip-gd/gd/configure

%build
# for locale.pot
export CLIP_LOCALE_ROOT=`pwd`

make CLIPROOT=%FCLIPDIR

%install
mkdir -p %buildroot%FCLIPDIR/{include,etc,cliprc,lib}
make install DESTDIR=%buildroot CLIPROOT=%FCLIPDIR
mkdir -p %buildroot%VCLIPDIR
cp -rf locale.pot %buildroot%VCLIPDIR/

# fix broken installer in source
mkdir -p %buildroot%_docdir
mv %buildroot%FCLIPDIR/doc %buildroot%_docdir/%name-%version
mv %buildroot%FCLIPDIR/locale.po %buildroot%VCLIPDIR

%files -n %name-all

%files -n %name-gd
%_docdir/%name-%version/clip-gd
%_docdir/%name-%version/example/clip-gd
%FCLIPDIR/include/gd*
%FCLIPDIR/lib/%name-gd.so

%files -n %name-gtk2
%_docdir/%name-%version/example/clip-gtk2
%FCLIPDIR/include/*gtk2*
%config %FCLIPDIR/cliprc/clip-gtk2.cliprc
%FCLIPDIR/lib/%name-gtk2.so
%FCLIPDIR/lib/%name-glade2.so
%VCLIPDIR/locale.pot/clip-gtk2

%files -n %name-ui
%_docdir/%name-%version/example/clip-ui
%FCLIPDIR/include/clip-ui*
#%config %FCLIPDIR/cliprc/clip-gtk2.cliprc
%FCLIPDIR/lib/%name-ui.so
%FCLIPDIR/lib/drivers
%VCLIPDIR/locale.po/*/*
%VCLIPDIR/locale.pot/clip-ui

%define build_interbase 0
%if %build_interbase
%files -n %name-interbase
%_docdir/%name-%version/clip-interbase
%_docdir/%name-%version/example/clip-interbase
%FCLIPDIR/include/interbase*
%FCLIPDIR/lib/%name-interbase.so
%endif

%files -n %name-mysql
%_docdir/%name-%version/clip-mysql
%_docdir/%name-%version/example/clip-mysql
%FCLIPDIR/include/mysql*
%FCLIPDIR/lib/%name-mysql.so

%files -n %name-odbc
#%_docdir/%name-%version/example/clip-odbc
#%FCLIPDIR/include/clip-odbc
%FCLIPDIR/lib/%name-odbc.so

%files -n %name-postgres
%_docdir/%name-%version/clip-postgres
%_docdir/%name-%version/example/clip-postgres
%FCLIPDIR/include/postgres*
%FCLIPDIR/lib/%name-postgres.so

%files -n %name-fcgi
%_docdir/%name-%version/example/clip-fcgi
%FCLIPDIR/include/fcgi.ch
%FCLIPDIR/lib/%name-fcgi.so

%files -n %name-common
%dir %_docdir/%name-%version
%_docdir/%name-%version/clip-com/
#%_docdir/%name-%version/example/clip-fw
%dir %_docdir/%name-%version/example/
%_docdir/%name-%version/example/clip-gzip
%_docdir/%name-%version/example/clip-bzip2
%_docdir/%name-%version/example/clip-com
%_docdir/%name-%version/example/clip-crypto
#%_docdir/%name-%version/example/clip-cti
%_docdir/%name-%version/example/clip-rtf
%_docdir/%name-%version/example/clip-xml
%_docdir/%name-%version/example/clip-postscript
%FCLIPDIR/include/clip-expat*
%FCLIPDIR/include/clip-postscript*
#%FCLIPDIR/include/fwin
#%FCLIPDIR/include/cti
#%FCLIPDIR/include/cti.ch
%FCLIPDIR/include/bggraph.ch
%FCLIPDIR/include/nanfor
%FCLIPDIR/include/netto
%FCLIPDIR/include/object*
%FCLIPDIR/include/rich*
#%FCLIPDIR/include/bg*
%FCLIPDIR/include/r2d2*
#%FCLIPDIR/etc/.calendar
%FCLIPDIR/lib/libclip-bzip2.so
%FCLIPDIR/lib/libclip-com.so
%FCLIPDIR/lib/libclip-crypto.so
%FCLIPDIR/lib/libclip-postscript.so
#%FCLIPDIR/lib/libclip-fw.so
#%FCLIPDIR/lib/libclip-cti.so
%FCLIPDIR/lib/libclip-gzip.so
%FCLIPDIR/lib/libclip-nanfor.so
%FCLIPDIR/lib/libclip-netto.so
%FCLIPDIR/lib/libclip-rtf.so
%FCLIPDIR/lib/libclip-r2d2.so
%FCLIPDIR/lib/libclip-xml.so
#%config %FCLIPDIR/cliprc/*
%VCLIPDIR/locale.pot/clip-r2d2
%exclude %FCLIPDIR/lib/*.a

%changelog
* Wed Sep 28 2011 Andrey Cherepanov <cas@altlinux.org> 1.2.0cvs-alt3.qa2
- Remove wrong directory attributes 

* Tue May 03 2011 Andrey Cherepanov <cas@altlinux.org> 1.2.0cvs-alt3.qa1
- Rebuild for set-versioning

* Mon Apr 18 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.0cvs-alt3
- fix build

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 1.2.0cvs-alt2.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.0cvs-alt2.1
- Automated rebuild due to libcrypto.so.6 -> libcrypto.so.7 soname change.

* Tue Jul 01 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.0cvs-alt2
- fix packing
- build with external libezV24

* Mon Jul 30 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.0cvs-alt1
- new version from CVS 2007-07-31
- remove unneeded ldconfig from post/preun sections
- fix locale.po packaging
- fix lib detecting in clip-gd

* Sat Nov 18 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version (-fw, -cti modules is left)

* Sun Nov 12 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.16-alt1
- remove gtk1 package - build without gdk-pixbuf-devel, gtk+

* Mon Sep 11 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.16-alt0.2
- unresolved=relaxed :(
- add fixes, update buildreq

* Wed May 24 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.16-alt0.1
- new version

* Sun Dec 18 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.15-alt0.1
- new version

* Fri May 27 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.14-alt2
- fix libpq-devel build require

* Fri Apr 08 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.14-alt1.1
- fix build req for clip

* Mon Mar 07 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.14-alt1
- new version

* Thu Feb 03 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.13-alt2
- last patch (03.02.2005) with clip-ui

* Sun Dec 19 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.13-alt1
- new version

* Mon Dec 06 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.12-alt1
- new version + last patches (07.12.2004)

* Sat Sep 18 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.11-alt0.1
- new version
- really use post(un)_ldconfig macro

* Mon Jul 19 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.10-alt2
- do not require -interbase now in libclip-all
- apply last patches (19.07.04)

* Mon Jun 21 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.10-alt1
- new version
- apply last patches (21.06.04)
- use a macro for ldconfig

* Tue Apr 06 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.9-alt0.2
- release to Sisyphus

* Fri Feb 27 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.9-alt0.1
- new version
- split in to different packages

* Fri Feb 20 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.8-alt0.1
- first build for Sisyphus
