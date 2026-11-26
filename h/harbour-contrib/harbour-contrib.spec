%define contrib_base hbamf hbblink hbbmp hbcomio hbcomm hbct hbformat hbfoxpro hbfship hbgt hbgzio hbhttpd hbmemio hbmisc hbmzip hbnetio hbnf hboslib hbpipeio hbsms hbtcpio hbtest hbtip hbtpathy hbunix hbxpp hbzebra hbziparc rddbm rddsql xhb
%define contrib_pgsql hbpgsql sddpg
%define contrib_mysql hbmysql sddmy
%define contrib_odbc hbodbc sddodbc
%define contrib_sqlite3 hbsqlit3 sddsqlt3
%define contrib_curl hbcurl
%define contrib_ssl hbssl
%define contrib_cairo hbcairo
%define contrib_cups hbcups
%define contrib_gd hbgd
%define contrib_fbird hbfbird sddfb
%define contrib_magic hbmagic
%define contrib_bz2 hbbz2 hbbz2io
%define contrib_expat hbexpat
%define contrib_lzf hblzf
%define contrib_freeimage hbfimage
%define contrib_gs hbgs
%define contrib_allegro gtalleg

Name: harbour-contrib
Version: 3.2.0
Release: alt1
Summary: Contributed libraries for Harbour

License: GPL-2.0-or-later WITH harbour-exception AND BSD-3-Clause AND BSD-2-Clause AND ALT-Public-Domain AND CC-BY-SA-4.0
Group: Development/Other
URL: https://github.com/harbour/core
# Source-url: https://github.com/harbour/core/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

# Contribs use the separately installed compiler, headers and core libraries.
BuildRequires: libharbour-devel = %version-alt1
BuildRequires: gcc-c++ pkgconfig(minizip) pkgconfig(zlib)
BuildRequires: pkgconfig(libpq)
BuildRequires: pkgconfig(libmariadb)
BuildRequires: pkgconfig(odbc)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(cairo)
BuildRequires: libcups-devel
BuildRequires: pkgconfig(gdlib) pkgconfig(libjpeg) pkgconfig(libpng) pkgconfig(freetype2)
BuildRequires: firebird-devel
BuildRequires: libmagic-devel
BuildRequires: bzlib-devel
BuildRequires: pkgconfig(expat)
BuildRequires: liblzf-devel
BuildRequires: libfreeimage-devel
BuildRequires: libgs-devel
BuildRequires: pkgconfig(allegro)

Requires: libharbour-devel = %version-alt1
Requires: pkgconfig(minizip) pkgconfig(zlib)

%description
Contributed libraries for Harbour, including Clipper Tools and Nanforum
compatibility, networking, compression, xBase extensions and SQL RDD support.
Includes static archives, shared libraries and hbmk2 component metadata.

%package pgsql
Summary: PostgreSQL contributed libraries for Harbour

Group: Development/Other
Requires: %name = %EVR
Requires: pkgconfig(libpq)

%description pgsql
Harbour interfaces to PostgreSQL, with libraries and hbmk2 metadata.

%package mysql
Summary: MariaDB and MySQL contributed libraries for Harbour

Group: Development/Other
Requires: %name = %EVR
Requires: pkgconfig(libmariadb)

%description mysql
Harbour interfaces to MariaDB and MySQL, with libraries and hbmk2 metadata.

%package odbc
Summary: ODBC contributed libraries for Harbour

Group: Development/Other
Requires: %name = %EVR
Requires: pkgconfig(odbc)

%description odbc
Harbour interfaces to ODBC, with libraries and hbmk2 metadata.

%package sqlite3
Summary: SQLite contributed libraries for Harbour

Group: Development/Other
Requires: %name = %EVR
Requires: pkgconfig(sqlite3)

%description sqlite3
Harbour interfaces to SQLite, with libraries and hbmk2 metadata.

%package curl
Summary: curl contributed libraries for Harbour

Group: Development/Other
Requires: %name = %EVR
Requires: pkgconfig(libcurl)

%description curl
Harbour interfaces to curl, with libraries and hbmk2 metadata.

%package ssl
Summary: OpenSSL contributed libraries for Harbour

Group: Development/Other
Requires: %name = %EVR
Requires: pkgconfig(openssl)

%description ssl
Harbour interfaces to OpenSSL, with libraries and hbmk2 metadata.

%package cairo
Summary: Cairo contributed libraries for Harbour

Group: Development/Other
Requires: %name = %EVR
Requires: pkgconfig(cairo)

%description cairo
Harbour interfaces to Cairo, with libraries and hbmk2 metadata.

%package cups
Summary: CUPS contributed libraries for Harbour

Group: Development/Other
Requires: %name = %EVR
Requires: libcups-devel

%description cups
Harbour interfaces to CUPS, with libraries and hbmk2 metadata.

%package gd
Summary: GD contributed libraries for Harbour

Group: Development/Other
Requires: %name = %EVR
Requires: pkgconfig(gdlib) pkgconfig(libjpeg) pkgconfig(libpng) pkgconfig(freetype2)

%description gd
Harbour interfaces to GD, with libraries and hbmk2 metadata.

%package fbird
Summary: Firebird contributed libraries for Harbour

Group: Development/Other
Requires: %name = %EVR
Requires: firebird-devel

%description fbird
Harbour interfaces to Firebird, with libraries and hbmk2 metadata.

%package magic
Summary: libmagic contributed libraries for Harbour

Group: Development/Other
Requires: %name = %EVR
Requires: libmagic-devel

%description magic
Harbour interfaces to libmagic, with libraries and hbmk2 metadata.

%package bz2
Summary: bzip2 contributed libraries for Harbour

Group: Development/Other
Requires: %name = %EVR
Requires: bzlib-devel

%description bz2
Harbour interfaces to bzip2, with libraries and hbmk2 metadata.

%package expat
Summary: Expat contributed libraries for Harbour

Group: Development/Other
Requires: %name = %EVR
Requires: pkgconfig(expat)

%description expat
Harbour interfaces to Expat, with libraries and hbmk2 metadata.

%package lzf
Summary: LZF contributed libraries for Harbour

Group: Development/Other
Requires: %name = %EVR
Requires: liblzf-devel

%description lzf
Harbour interfaces to LZF, with libraries and hbmk2 metadata.

%package freeimage
Summary: FreeImage contributed libraries for Harbour

Group: Development/Other
Requires: %name = %EVR
Requires: libfreeimage-devel

%description freeimage
Harbour interfaces to FreeImage, with libraries and hbmk2 metadata.

%package gs
Summary: Ghostscript contributed libraries for Harbour

Group: Development/Other
Requires: %name = %EVR
Requires: libgs-devel

%description gs
Harbour interfaces to Ghostscript, with libraries and hbmk2 metadata.

%package allegro
Summary: Allegro contributed libraries for Harbour

Group: Development/Other
Requires: %name = %EVR
Requires: pkgconfig(allegro)

%description allegro
Harbour interfaces to Allegro, with libraries and hbmk2 metadata.

%prep
%setup
# Keep only link metadata from hosted libraries. There must be no source
# fallback to a bundled dependency, even when dependency detection fails.
find contrib -path '*/3rd/*' -type f ! -name '*.hbc' -delete
rm -rf src/3rd
cat > build-env <<'ENV'
export HB_PLATFORM=linux HB_COMPILER=gcc HB_SYSLOC=yes
export HB_INSTALL_PREFIX=%_prefix HB_INSTALL_INC=%_includedir/harbour
export HB_INSTALL_LIB=%_libdir/harbour HB_INSTALL_DYN=%_libdir
export HB_BUILD_3RDEXT=no HB_BUILD_CONTRIB_DYN=yes
export HB_BUILD_SHARED=yes HB_BUILD_STRIP=no HB_BUILD_VERBOSE=yes
# Static sibling archives may also be pulled into a shared contrib (i586).
export HB_USER_CFLAGS="%optflags -ffat-lto-objects -fPIC"
export HB_USER_LDFLAGS="%optflags %{?build_ldflags}"
export HB_USER_DFLAGS="%optflags %{?build_ldflags}"
# Upstream contrib shared objects need an explicit core and math link.
export HB_USER_LIBS="harbour m"
export HB_WITH_ZLIB=%_includedir HB_WITH_MINIZIP=%_includedir/minizip
export HB_WITH_PGSQL=%_includedir/pgsql HB_WITH_MYSQL=%_includedir/mysql
export HB_WITH_ODBC=%_includedir HB_WITH_SQLITE3=%_includedir
export HB_WITH_CURL=%_includedir HB_WITH_OPENSSL=%_includedir
export HB_WITH_CAIRO=%_includedir/cairo HB_WITH_CUPS=%_includedir
export HB_WITH_GD=%_includedir HB_WITH_FIREBIRD=%_includedir
export HB_WITH_LIBMAGIC=%_includedir HB_WITH_BZIP2=%_includedir
export HB_WITH_EXPAT=%_includedir HB_WITH_LZF=%_includedir
export HB_WITH_MXML=no HB_WITH_FREEIMAGE=%_includedir
export HB_WITH_LIBHARU=no HB_WITH_GS=%_includedir/ghostscript
export HB_WITH_ALLEGRO=%_includedir
export HB_WITH_ADS=no HB_WITH_QT=no HB_WITH_OCILIB=no
export HB_WITH_MINILZO=no HB_WITH_XDIFF=no HB_WITH_TINYMT=no
ENV

%build
. ./build-env
# Make sibling .hbc files discoverable when using the installed compiler.
export HB_INSTALL_ADDONS="$PWD/contrib"
export HB_USER_LDFLAGS="$HB_USER_LDFLAGS -L$PWD/bin/linux/gcc -L$PWD/lib/linux/gcc"
export HB_USER_DFLAGS="$HB_USER_DFLAGS -L$PWD/bin/linux/gcc -L$PWD/lib/linux/gcc"
cd contrib
failed=
for component in %contrib_base %contrib_pgsql %contrib_mysql %contrib_odbc %contrib_sqlite3 %contrib_curl %contrib_ssl %contrib_cairo %contrib_cups %contrib_gd %contrib_fbird %contrib_magic %contrib_bz2 %contrib_expat %contrib_lzf %contrib_freeimage %contrib_gs %contrib_allegro; do
    # These .hbc files supply executable-only ldflags; the shared-library
    # pass also needs their system library in HB_USER_LIBS.
    HB_USER_LIBS="harbour m"
    case "$component" in
        hbcairo) HB_USER_LIBS="$HB_USER_LIBS cairo" ;;
        gtalleg) HB_USER_LIBS="$HB_USER_LIBS alleg" ;;
    esac
    export HB_USER_LIBS
    if ! hbmk2 make.hb "$component" ||
       [ ! -s ../lib/linux/gcc/lib$component.a ] ||
       [ ! -s ../bin/linux/gcc/lib$component.so.3.2.0 ]; then
        echo "BUILD_FAILED_COMPONENT=$component"
        failed="$failed $component"
    fi
done
[ -z "$failed" ] || { echo "Failed contribs:$failed"; exit 1; }

%install
mkdir -p %buildroot%_libdir/harbour %buildroot%_datadir/harbour/contrib
for group in base pgsql mysql odbc sqlite3 curl ssl cairo cups gd fbird magic bz2 expat lzf freeimage gs allegro; do
    case "$group" in
        base) components="%contrib_base" ;;
        pgsql) components="%contrib_pgsql" ;;
        mysql) components="%contrib_mysql" ;;
        odbc) components="%contrib_odbc" ;;
        sqlite3) components="%contrib_sqlite3" ;;
        curl) components="%contrib_curl" ;;
        ssl) components="%contrib_ssl" ;;
        cairo) components="%contrib_cairo" ;;
        cups) components="%contrib_cups" ;;
        gd) components="%contrib_gd" ;;
        fbird) components="%contrib_fbird" ;;
        magic) components="%contrib_magic" ;;
        bz2) components="%contrib_bz2" ;;
        expat) components="%contrib_expat" ;;
        lzf) components="%contrib_lzf" ;;
        freeimage) components="%contrib_freeimage" ;;
        gs) components="%contrib_gs" ;;
        allegro) components="%contrib_allegro" ;;
    esac
    for component in $components; do
        install -m644 lib/linux/gcc/lib$component.a %buildroot%_libdir/harbour/
        cp -a bin/linux/gcc/lib$component.so* %buildroot%_libdir/
        target=%buildroot%_datadir/harbour/contrib/$component
        mkdir -p "$target"
        for extension in hbc hbx ch h api; do
            for file in contrib/$component/*.$extension; do
                [ ! -f "$file" ] || install -m644 "$file" "$target/"
            done
        done
        # Retain nested .hbc files for system dependencies (no source copies).
        if [ -d contrib/$component/3rd ]; then
            (cd contrib/$component && find 3rd -name '*.hbc' -print) | while read file; do
                install -Dm644 contrib/$component/$file "$target/$file"
            done
        fi
        echo %_libdir/harbour/lib$component.a >> "$group.files"
        echo %_libdir/lib$component.so* >> "$group.files"
        echo %_datadir/harbour/contrib/$component >> "$group.files"
    done
done
# Both SQLite wrappers reference this common system-library link metadata.
install -Dm644 contrib/3rd/sqlite3/sqlite3.hbc %buildroot%_datadir/harbour/contrib/3rd/sqlite3/sqlite3.hbc
# Shared build helper metadata belongs to the contrib distribution.
install -m644 contrib/hbpre.hbm contrib/hbpost.hbm %buildroot%_datadir/harbour/contrib/

%files -f base.files
%doc LICENSE.txt README.md contrib/hbunix/daemon.c
%dir %_datadir/harbour
%dir %_datadir/harbour/contrib
%_datadir/harbour/contrib/*.hbm

%files pgsql -f pgsql.files

%files mysql -f mysql.files

%files odbc -f odbc.files

%files sqlite3 -f sqlite3.files
%_datadir/harbour/contrib/3rd

%files curl -f curl.files

%files ssl -f ssl.files

%files cairo -f cairo.files

%files cups -f cups.files

%files gd -f gd.files

%files fbird -f fbird.files

%files magic -f magic.files

%files bz2 -f bz2.files

%files expat -f expat.files

%files lzf -f lzf.files

%files freeimage -f freeimage.files

%files gs -f gs.files

%files allegro -f allegro.files

%changelog
* Thu Nov 26 2026 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt1
- initial build for ALT Linux.
