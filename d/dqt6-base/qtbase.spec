%define IF_ver_gt() %if "%(rpmvercmp '%1' '%2')" > "0"
%define IF_ver_gteq() %if "%(rpmvercmp '%1' '%2')" >= "0"
%define IF_ver_lt() %if "%(rpmvercmp '%2' '%1')" > "0"
%define IF_ver_lteq() %if "%(rpmvercmp '%2' '%1')" >= "0"
%define IF_ver_eq() %if "%(rpmvercmp '%1' '%2')" == "0"
%define IF_ver_not_gt() %if "%(rpmvercmp '%1' '%2')" <= "0"
%define IF_ver_not_gteq() %if "%(rpmvercmp '%1' '%2')" < "0"
%define IF_ver_not_lt() %if "%(rpmvercmp '%2' '%1')" <= "0"
%define IF_ver_not_lteq() %if "%(rpmvercmp '%2' '%1')" < "0"
%define IF_ver_not_eq() %if "%(rpmvercmp '%1' '%2')" != "0"

%def_enable sql_pgsql
%def_enable sql_odbc
%def_enable sql_ibase
%def_disable sql_tds
%def_enable pulse
%def_disable journald
%def_enable vulkan
%def_enable sctp

%define platform linux-g++
#define graphicssystem raster
%ifarch %arm
%define opengl_type es2
%else
%define opengl_type opengl-desktop
%endif
%define optflags_lto %nil

%global qt_module  dqtbase
%define gname  dqt6
Name: dqt6-base
%define major  6
Version: 6.7.2
Release: alt1.dde.1
# %%if "%%version" == "%%{get_version qt6-tools-common}"
%def_disable bootstrap
# %%else
# %%def_enable bootstrap
# %%endif

Group: System/Libraries
Summary: Qt%major - QtBase components
License: LGPL-2.1 with Qt-LGPL-exception-1.1 or LGPL-3.0-only

Url: http://qt.io/

Source: %qt_module-everywhere-src-%version.tar
Source1: rpm-macros
Source2: rpm-macros-addon
# FC
Patch1: qtbase-version-check.patch
Patch2: qtbase-CMake-Install-objects-files-into-ARCHDATADIR.patch
Patch3: qtbase-use-only-major-minor-for-private-api-tag.patch
Patch4: qtbase-revert-consider-versioned-targets-when-checking-existens-in-qt-internal-walk-libs.patch
Patch5: qtbase-qgtk3theme-add-support-for-xdp-to-get-color-scheme.patch
Patch6: CVE-2024-39936.patch

# Debian
Patch100: remove_rpath_from_examples.patch
Patch101: enable_skip_plugins.patch
# ALT
Patch1000: alt-timezone.patch
Patch1001: alt-zonetab.patch
Patch1002: alt-ca-certificates-path.patch
Patch1003: alt-decrease-iconloader-fallback-depth.patch
Patch1004: alt-kernel-requires.patch
Patch1005: e2k-qt-6.patch
#
Patch2000: 9003-qt6-base-6.7.2-qmenu_fix_shortcuts.patch

# macros
%define _dqt6 %gname
%include %SOURCE1

# dynamically probing plugins
#add_findreq_skiplist %%_dqt6_plugindir/platformthemes/*.so

# Automatically added by buildreq on Fri Nov 26 2021 (-bi)
# optimized out: at-spi2-atk bash4 bashrc cmake cmake-modules debugedit elfutils fontconfig fontconfig-devel gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 icu-utils libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXmu-devel libXrender-devel libXt-devel libalsa-devel libassuan-devel libat-spi2-core libatk-devel libatomic_ops-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libcanberra-devel libcom_err-devel libcrypt-devel libctf-nobfd0 libdbus-devel libdouble-conversion3 libffi-devel libfreetype-devel libgdbm-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libglvnd-devel libgmp-devel libgpg-error libgpg-error-devel libharfbuzz-devel libicu-devel libjpeg-devel libkrb5-devel libmpfr-devel libncurses-devel libp11-kit libpango-devel libpng-devel libpopt-devel libsasl2-3 libsndfile-devel libssl-devel libstdc++-devel libtinfo-devel libudev-devel libunixODBC-devel-compat libverto-devel libvulkan-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-egl libwayland-server libxcb-devel libxcb-render-util libxcbutil-icccm libxcbutil-image libxcbutil-keysyms libxkbcommon-devel libxkbcommon-x11 perl pkg-config postgresql-devel python-modules python2-base python3 python3-base python3-module-paste rpm-build-file rpm-build-python3 rpm-macros-python sh4 tcl-devel tzdata wayland-devel xorg-proto-devel xorg-xf86miscproto-devel xxd zlib-devel zlib-devel-static
#BuildRequires: aalib-devel asio-devel binutils-devel bzlib-devel catch-devel ccmake cmark-devel drumstick-devel ebook-tools-devel eglexternalplatform-devel firebird-devel flex flite-devel frei0r-devel gambit glslang id3lib-devel ilbc-devel imlib2-devel ktoblzcheck-devel ladspa_sdk libGLU-devel libGeoIP-devel libXScrnSaver-devel libXaw-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXinerama-devel libXpm-devel libXrandr-devel libXres-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libaio-devel libarchive-devel libargon2-devel libat-spi2-core-devel libaudiofile-devel libaudit-devel libbrotli-devel libcanberra-gtk-common-devel libcap-ng-devel libcares-devel libcdaudio-devel libcdparanoia-devel libcheck-devel libchm-devel libchromaprint-devel libcmocka-devel libcrossguid-devel libcryptsetup-devel libcups-devel libdb4-devel libdca-devel libddcutil-devel libdevmapper-devel libdiscount-devel libdmtx-devel libdouble-conversion-devel libdrm-devel libedit-devel libelf-devel libenca-devel libevent-devel libexpat-devel libf2c-ng-devel libfaad-devel libfaudio-devel libfftw3-devel libfluidsynth-devel libfreetds-devel libfuse-devel libgadu-devel libgamin-devel libgbm-devel libgc-devel libgcrypt-devel libgd3-devel libgit2-devel libgmpxx-devel libgpgme-devel libgps-devel libgsm-devel libgsoap-devel libgtk+3-devel libgts-devel libhdf5-devel libid3tag-devel libidn-devel libinput-devel libkmod-devel libksba-devel liblasi-devel liblcms-devel liblcms2-devel libldap-devel liblirc-devel liblksctp-devel liblmdb-devel liblmdbxx-devel liblrdf-devel libltdl7-devel liblz4-devel liblzma-devel libmad-devel libmd-devel libmicrohttpd-devel libmng-devel libmpg123-devel libmsgpack-devel libmtdev-devel libmtp-devel libmtxclient-devel libmuparser-devel libmysqlclient21-devel libnewt-devel libnpth-devel libopenconnect-devel libopenslp-devel libpcap-devel libpciaccess-devel libpcre2-devel libportaudio2-devel libproj-devel libproxy-devel libpth-devel libpwquality-devel libqrencode4-devel libredland-devel libsamplerate-devel libscotch-devel libseccomp-devel libshape-devel libsnappy-devel libsodium-devel libsox-devel libsoxr-devel libspnav-devel libsqlite3-devel libssh2-devel libsuitesparse-devel libsystemd-devel libtar-devel libtasn1-devel libtidy-devel libtiff-devel libtimidity-devel libts-devel libturbojpeg-devel libtwolame-devel libunixODBC-devel libusb-compat-devel libusbmuxd-devel libutempter-devel libuv-devel libv4l-devel libwayland-cursor-devel libwayland-egl-devel libwayland-server-devel libwildmidi-devel libwlocate-devel libx264-devel libx265-devel libxapian-devel libxcb-render-util-devel libxcbutil-cursor-devel libxcbutil-devel libxcbutil-icccm-devel libxcbutil-image-devel libxcbutil-keysyms-devel libxine2-devel libxkbcommon-x11-devel libxkbfile-devel libxosd-devel libxvid-devel libyasm-devel libzbar-devel libzip-devel libzstd-devel libzvbi-devel lua-devel lv2-devel mpir-devel ninja-build postgresql-devel-static python-modules-compiler python3-dev swig tbb-devel tinyxml-devel tk-devel
# BuildRequires(pre): dqt6-tools-common
BuildRequires: cmake gcc-c++ ninja-build rpm-build-python3
BuildRequires: binutils-devel bzlib-devel libb2-devel libssl-devel libdbus-devel libkrb5-devel
BuildRequires: eglexternalplatform-devel flex libGLU-devel
BuildRequires: libXScrnSaver-devel libXaw-devel libXcomposite-devel libXcursor-devel libXdamage-devel
BuildRequires: libXdmcp-devel libXinerama-devel libXpm-devel libXrandr-devel libXres-devel libXtst-devel
BuildRequires: libXv-devel libXxf86misc-devel libXxf86vm-devel
BuildRequires: libcups-devel libdouble-conversion-devel libdrm-devel libelf-devel libexpat-devel libgbm-devel libgtk+3-devel
BuildRequires: libinput-devel liblz4-devel liblzma-devel libmng-devel libmtdev-devel libbrotli-devel
BuildRequires: libpcre2-devel libproxy-devel libts-devel
BuildRequires: libwayland-cursor-devel libwayland-egl-devel libwayland-server-devel
BuildRequires: libxcb-render-util-devel libxcbutil-cursor-devel libxcbutil-devel libxcbutil-icccm-devel libxcbutil-image-devel libxcbutil-keysyms-devel
BuildRequires: libxkbcommon-x11-devel libxkbfile-devel libzstd-devel
BuildRequires: libat-spi2-core-devel
%{?_enable_vulkan:BuildRequires: pkgconfig(vulkan)}
%{?_enable_pulse:BuildRequires: libpulseaudio-devel}
%{?_enable_journald:BuildRequires: pkgconfig(libsystemd-journal)}
%{?_enable_sql_tds:BuildRequires: libfreetds-devel}
%{?_enable_sql_ibase:BuildRequires: firebird-devel}
%{?_enable_sql_odbc:BuildRequires: libunixODBC-devel}
%{?_enable_sql_pgsql:BuildRequires: postgresql-devel libpq-devel libecpg-devel-static}
%{?_enable_sctp:BuildRequires: liblksctp-devel}
BuildRequires: libmysqlclient-devel
BuildRequires: libsqlite3-devel
# %%if_disabled bootstrap
# BuildRequires: dqt6-base-devel dqt6-tools
# %%endif

# find libraries
%add_findprov_lib_path %_dqt6_libdir

%description
Qt is a software toolkit for developing applications.

This package contains base tools, like string, xml, and network
handling.

%package common
Summary: Common package for Qt%major
Group: System/Configuration/Other
Requires: common-licenses
%description common
Common package for Qt%major

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
Requires: pkgconfig(xkbcommon) pkgconfig(gl) pkgconfig(egl)
Requires: rpm-macros-%gname
Requires: gcc-c++
Requires: rpm-build-ninja
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
Requires: %name-devel
%description devel-static
%summary.

%package -n rpm-macros-%gname
Summary: Set of RPM macros for packaging Qt%major-based applications
Group: Development/KDE and QT
BuildArch: noarch
#Requires: %name-common
%description -n rpm-macros-%gname
Set of RPM macros for packaging Qt%major-based applications for %distribution
Install this package if you want to create RPM packages that use Qt%major

%package static
Group: Development/KDE and QT
Summary: Static library files for %name
Requires: %name-devel
Requires: pkgconfig(fontconfig)
Requires: pkgconfig(glib-2.0)
Requires: pkgconfig(zlib)
%description static
%summary.

%package doc
Summary: Document for developing apps which will use Qt%major
Group: Development/KDE and QT
Requires: %name-common
#Requires: %gname-assistant
%description doc
This package contains documentation and sources for example programs.

%package -n %gname-qtbase
Summary: qtbase compatibility package
Group: System/Libraries
BuildArch: noarch
Requires: lib%gname-concurrent
Requires: lib%gname-core
Requires: lib%gname-dbus
Requires: lib%gname-network
Requires: lib%gname-sql
Requires: lib%gname-test
Requires: lib%gname-xml
%description -n %gname-qtbase
qtbase compatibility package

%package -n %gname-qtbase-gui
Summary: qtbase-gui compatibility package
Group: System/Libraries
BuildArch: noarch
Requires: lib%gname-gui
Requires: lib%gname-opengl
Requires: lib%gname-printsupport
Requires: lib%gname-widgets
Requires: lib%gname-xcbqpa
Provides: qt6-qtbase-x11 = %version-%release
%description -n %gname-qtbase-gui
qtbase-gui compatibility package

%package -n %gname-sql
BuildArch: noarch
Group: System/Libraries
Summary: Meta-package for SQL support of Qt%major GUI toolkit
Requires: %name-common
Requires: %gname-sql-mysql
Requires: %gname-sql-sqlite
%{?_enable_sql_ibase:Requires: %gname-sql-interbase}
%{?_enable_sql_pgsql:Requires: %gname-sql-postgresql}
%{?_enable_sql_odbc:Requires: %gname-sql-odbc}
%{?_enable_sql_tds:Requires: %gname-sql-tds}
%description -n %gname-sql
Meta-package for SQL support of Qt%major GUI toolkit

%package -n %gname-sql-odbc
Summary: ODBC drivers for Qt%major SQL classes
Group: System/Libraries
Requires: %name-common
Provides: %gname-plugin-sql = %EVR
%description -n %gname-sql-odbc
ODBC driver for Qt's SQL classes (QODBC)

%package -n %gname-sql-tds
Summary: FreeTDS(Sybase) driver for Qt%major SQL classes
Group: System/Libraries
Requires: %name-common
Provides: %gname-plugin-sql = %EVR
%description -n %gname-sql-tds
FreeTDS(Sybase) driver for Qt's SQL classes (QTDS)

%package -n %gname-sql-mysql
Summary: MySQL driver for Qt%major SQL classes
Group: System/Libraries
Requires: %name-common
Provides: %gname-plugin-sql = %EVR
%description -n %gname-sql-mysql
MySQL driver for Qt's SQL classes (QMYSQL)

%package -n %gname-sql-postgresql
Summary: PostgreSQL drivers for Qt%major SQL classes
Group: System/Libraries
Requires: %name-common
Provides: %gname-plugin-sql = %EVR
%description -n %gname-sql-postgresql
PostgreSQL driver for Qt's SQL classes (QPSQL)

%package -n %gname-sql-interbase
Summary: InterBase drivers for Qt%major SQL classes
Group: System/Libraries
Requires: %name-common
Provides: %gname-plugin-sql = %EVR
%description -n %gname-sql-interbase
InterBase driver for Qt's SQL classes (QIBASE)

#%package -n %gname-sql-sqlite
#Summary: SQLite driver for Qt%major SQL classes
#Group: System/Libraries
#Requires: %name-common
#Provides: %gname-plugin-sql = %EVR
#%description -n %gname-sql-sqlite
#SQLite driver for Qt's SQL classes (QSQLITE)

%package -n lib%gname-sql
Summary: SQL support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common
# sqlite plugin included
Provides: %gname-plugin-sql = %EVR
Provides: %gname-sql-sqlite = %EVR
%description -n lib%gname-sql
SQL support library for the Qt%major toolkit

%package -n lib%gname-core
Summary: Core library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common
Requires: glibc-gconv-modules
%description -n lib%gname-core
Core library for the Qt%major toolkit

%package -n lib%gname-gui
Summary: GUI support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%gname-gui
GUI support library for the Qt%major toolkit

%package -n lib%gname-dbus
Summary: DBus support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%gname-dbus
DBus support library for the Qt%major toolkit

%package -n lib%gname-network
Summary: Network support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common
Requires: ca-certificates
%description -n lib%gname-network
Network support library for the Qt%major toolkit

%package -n lib%gname-opengl
Summary: OpenGL support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%gname-opengl
OpenGL support library for the Qt%major toolkit

%package -n lib%gname-xml
Summary: XML support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%gname-xml
XML support library for the Qt%major toolkit

%package -n lib%gname-concurrent
Summary: Multi-threading concurrence support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%gname-concurrent
Multi-threading concurrence support library for the Qt%major toolkit

%package -n lib%gname-printsupport
Summary: Printing support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%gname-printsupport
Printing support library for the Qt%major toolkit

%package -n lib%gname-test
Summary: Testing support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%gname-test
Testing support library for the Qt%major toolkit

%package -n lib%gname-widgets
Summary: Widgets library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%gname-widgets
Widgets library for the Qt%major toolkit

%package -n lib%gname-eglfsdeviceintegration
Summary: EGL integration library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common
Requires: tslib
%description -n lib%gname-eglfsdeviceintegration
EGL integration library for the Qt%major toolkit

%package -n lib%gname-xcbqpa
Summary: EGL integration library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%gname-xcbqpa
EGL integration library for the Qt%major toolkit

%package -n lib%gname-eglfskmssupport
Summary: EGL integration library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%gname-eglfskmssupport
EGL integration library for the Qt%major toolkit

%package -n lib%gname-eglfskmsgbmsupport
Summary: EGL integration library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%gname-eglfskmsgbmsupport
EGL integration library for the Qt%major toolkit

%package -n lib%gname-openglwidgets
Summary: OpenGL widgets library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%gname-openglwidgets
OpenGL widgets library for the Qt%major toolkit

%prep
%setup -n %qt_module-everywhere-src-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
#
%patch100 -p1
%patch101 -p1
#
%patch1000 -p1
%patch1001 -p1
%patch1002 -p1
%patch1003 -p1
%patch1004 -p1
%ifarch %e2k
%patch1005 -p1
%endif
#
%patch2000 -p1

# install optflags
%add_optflags %optflags_shared
sed -i "s|^\s*QMAKE_CFLAGS_OPTIMIZE\s*=.*$|QMAKE_CFLAGS_OPTIMIZE = %optflags|" mkspecs/common/gcc-base.conf
QMAKE_CFLAGS_OPTIMIZE_FULL=`echo %optflags | sed 's|-O[[:digit:]]||'`
QMAKE_CFLAGS_OPTIMIZE_FULL+=" -O3"
sed -i "s|^\s*QMAKE_CFLAGS_OPTIMIZE_FULL\s*=.*$|QMAKE_CFLAGS_OPTIMIZE_FULL = $QMAKE_CFLAGS_OPTIMIZE_FULL|" mkspecs/common/gcc-base.conf

# remove some bundled libs to ensure they're not accidentally used
pushd src/3rdparty
rm -rf freetype/include libjpeg libpng zlib xcb harfbuzz-ng
popd

# exclude from build
sed -i '/^qt_internal_add_example.*htmlinfo.*/d' examples/xml/CMakeLists.txt

# remove unused rpath
sed -i '/CMAKE_INSTALL_RPATH/s|$ORIGIN $ORIGIN/${__qt_relDir}|%_dqt6_libdir|' \
  src/corelib/Qt6CoreMacros.cmake

%build
%define qdoc_found %{expand:%%(if [ -e %_dqt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
unset QTDIR QTLIB QTINC
export QT_DIR="$PWD"
export PATH=$QT_DIR/bin:$PATH
export LD_LIBRARY_PATH=$QT_DIR/lib:$LD_LIBRARY_PATH
export QT_PLUGIN_PATH=$QT_DIR/plugins
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"

mkdir -p BUILD
pushd BUILD
#    -DCMAKE_INSTALL_PREFIX=%_dqt6_prefix \
cmake .. \
    -DCMAKE_INSTALL_PREFIX:STRING=%prefix \
    -DINSTALL_ARCHDATADIR:STRING=%_dqt6_archdatadir \
    -DINSTALL_BINDIR:STRING=%_dqt6_bindir \
    -DINSTALL_DATADIR:STRING=%_dqt6_datadir \
    -DINSTALL_DOCDIR:STRING=%_dqt6_docdir \
    -DINSTALL_EXAMPLESDIR:STRING=%_dqt6_examplesdir \
    -DINSTALL_INCLUDEDIR:STRING=%_dqt6_headerdir \
    -DINSTALL_QMLDIR:STRING=%_dqt6_qmldir \
    -DINSTALL_LIBDIR:STRING=%_dqt6_libdir \
    -DINSTALL_LIBEXECDIR:STRING=%_dqt6_libexecdir \
    -DINSTALL_PLUGINSDIR:STRING=%_dqt6_plugindir \
    -DINSTALL_SYSCONFDIR:STRING=%_dqt6_sysconfdir \
    -DINSTALL_TRANSLATIONSDIR:STRING=%_dqt6_translationdir \
    -DINSTALL_MKSPECSDIR:STRING=%_dqt6_mkspecsdir \
    \
    -GNinja \
    -DCMAKE_BUILD_TYPE:STRING=%_dqt6_build_type \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DBUILD_WITH_PCH:BOOL=OFF \
    -DQT_QMAKE_TARGET_MKSPEC:STRING=%platform \
    \
    -DQT_FEATURE_enable_new_dtags:BOOL=ON \
    -DQT_FEATURE_reduce_relocations:BOOL=OFF \
    -DQT_FEATURE_relocatable:BOOL=OFF \
    -DQT_FEATURE_separate_debug_info:BOOL=OFF \
    -DQT_FEATURE_rpath:BOOL=OFF \
    -DQT_DISABLE_RPATH:BOOL=OFF \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
    -DCMAKE_INSTALL_RPATH:STRING=%_dqt6_libdir \
    -DQT_FEATURE_use_gold_linker:BOOL=OFF \
    -DQT_CREATE_VERSIONED_HARD_LINK:BOOL=OFF \
%ifnarch ppc64le
    -DCMAKE_INTERPROCEDURAL_OPTIMIZATION:BOOL=ON \
%endif
    \
    -DQT_BUILD_EXAMPLES:BOOL=ON \
    -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON \
    -DQT_BUILD_TESTS:BOOL=OFF \
    -DQT_BUILD_STANDALONE_TESTS:BOOL=OFF \
    -DQT_FEATURE_journald:BOOL=OFF \
    -DQT_FEATURE_openssl_linked:BOOL=ON \
    -DQT_FEATURE_openssl_hash:BOOL=ON \
    -DQT_FEATURE_accessibility:BOOL=ON \
    -DQT_FEATURE_fontconfig:BOOL=ON \
    -DQT_FEATURE_glib:BOOL=ON \
%ifarch x86_64 %e2k
    -DQT_FEATURE_sse2:BOOL=ON \
%endif
    -DQT_FEATURE_icu:BOOL=ON \
    -DQT_FEATURE_system_jpeg:BOOL=ON \
    -DQT_FEATURE_system_png:BOOL=ON \
    -DQT_FEATURE_system_zlib:BOOL=ON \
    -DQT_FEATURE_dbus_linked:BOOL=ON \
    -DQT_FEATURE_system_pcre2:BOOL=ON \
    -DQT_FEATURE_libproxy:BOOL=ON \
    -DQT_FEATURE_sctp:BOOL=%{?_enable_sctp:ON}%{!?_enable_sctp:OFF} \
    -DQT_FEATURE_mimetype:BOOL=ON \
    -DQT_FEATURE_mimetype_database:BOOL=OFF \
    \
    -DQT_FEATURE_sql_odbc:BOOL=ON \
    -DQT_FEATURE_sql_sqlite:BOOL=ON \
    -DQT_FEATURE_system_sqlite:BOOL=ON \
    -DQT_FEATURE_sql_mysql:BOOL=ON \
    -DQT_FEATURE_sql_tds:BOOL=%{?_enable_sql_tds:ON}%{!?_enable_sql_tds:OFF} \
    -DQT_FEATURE_sql_ibase:BOOL=%{?_enable_sql_ibase:ON}%{!?_enable_sql_ibase:OFF} \
    -DQT_FEATURE_sql_odbc:BOOL=%{?_enable_sql_odbc:ON}%{!?_enable_sql_odbc:OFF} \
    -DQT_FEATURE_sql_psql:BOOL=%{?_enable_sql_pgsql:ON}%{!?_enable_sql_pgsql:OFF} \
    \
    -DQT_FEATURE_xcb:BOOL=ON \
    -DQT_FEATURE_system_xcb_xinput:BOOL=ON \
    -DQT_FEATURE_xkbcommon:BOOL=ON \
    -DQT_FEATURE_opengl:BOOL=ON \
    -DQT_FEATURE_eglfs:BOOL=ON \
    -DQT_FEATURE_egl:BOOL=ON \
    -DQT_FEATURE_kms:BOOL=ON \
%if "%opengl_type" == "es2"
     -DINPUT_opengl:STRING=es2 \
     -DFEATURE_opengles3:BOOL=ON \
%endif
    #
popd
cmake --build BUILD %_smp_mflags --verbose
%if %qdoc_found
cmake --build BUILD --target docs
%endif

%install
DESTDIR="%buildroot" cmake --install BUILD
%if %qdoc_found
DESTDIR=%buildroot cmake --build BUILD --target install_docs
%endif

# install private qtxcb headers
mkdir -p %buildroot/%_dqt6_headerdir/QtXcb
install -m 0644 src/plugins/platforms/xcb/*.h %buildroot/%_dqt6_headerdir/QtXcb/

# uninstall optflags
sed -i "s|^\s*QMAKE_CFLAGS_OPTIMIZE\s*=.*$|QMAKE_CFLAGS_OPTIMIZE = -O2|" %buildroot%_dqt6_archdatadir/mkspecs/common/gcc-base.conf
sed -i "s|^\s*QMAKE_CFLAGS_OPTIMIZE_FULL\s*=.*$|QMAKE_CFLAGS_OPTIMIZE_FULL = -O3|" %buildroot%_dqt6_archdatadir/mkspecs/common/gcc-base.conf

# remove macos staff
rm -rf %buildroot/%_dqt6_archdatadir/mkspecs/features/uikit ||:

# create/own dirs
mkdir -p %buildroot/{%_dqt6_archdatadir/mkspecs/modules,%_dqt6_importdir,%_dqt6_qmldir,%_dqt6_libexecdir,%_dqt6_translationdir,%_dqt6_docdir,%_dqt6_examplesdir}
mkdir -p %buildroot/%_dqt6_plugindir/{accessible,iconengines,script,styles}/

# debug logging config
mkdir -p %buildroot/%_sysconfdir/dqt6/
cat >%buildroot/%_sysconfdir/dqt6/qtlogging.ini <<__EOF__
[Rules]
*.debug=false
qt.qpa.xcb.xcberror.warning=false
__EOF__
ln -s `relative %_sysconfdir/dqt6/qtlogging.ini %_dqt6_datadir/qtlogging.ini` %buildroot/%_dqt6_datadir/qtlogging.ini

# cleanup
rm -rf %buildroot/%_dqt6_libdir/*.la
rm -rf %buildroot/%_dqt6_examplesdir/corelib/serialization/cbordump

# .pc
mkdir -p %buildroot/%_dqt6_libdir/pkgconfig/
cat >%buildroot/%_dqt6_libdir/pkgconfig/Qt%major.pc<<__EOF__
prefix=%_dqt6_prefix
archdatadir=%_dqt6_archdatadir
bindir=%_dqt6_bindir
datadir=%_dqt6_datadir

docdir=%_dqt6_docdir
examplesdir=%_dqt6_examplesdir
headerdir=%_dqt6_headerdir
importdir=%_dqt6_importdir
qmldir=%_dqt6_qmldir
libdir=%_dqt6_libdir
libexecdir=%_dqt6_libexecdir
moc=%_dqt6_bindir/moc
plugindir=%_dqt6_plugindir
settingsdir=%_dqt6_settingsdir
sysconfdir=%_dqt6_sysconfdir
translationdir=%_dqt6_translationdir

Name: Qt%major
Description: Qt%major Configuration
%{nil}Version: %version
__EOF__

# rpm macros
install -d -m 0755 %buildroot/%_rpmmacrosdir/
cat >%buildroot/%_rpmmacrosdir/%gname <<__EOF__
%%_dqt6 %_dqt6
%%_dqt6_epoch %{?epoch}%{!?epoch:0}
%%_dqt6_version %version
%%_dqt6_evr %EVR
__EOF__
cat %SOURCE1 | sed 's|define[[:space:]][[:space:]]*||' >>%buildroot/%_rpmmacrosdir/%gname
cat %SOURCE2 >>%buildroot/%_rpmmacrosdir/%gname

# create compatibility symlinks to dirs
for d in imports libexec mkspecs plugins ; do
ln -s `relative %_dqt6_archdatadir/$d %_dqt6_prefix/$d` %buildroot/%_dqt6_prefix/$d
done
ln -s `relative %_dqt6_docdir %_dqt6_prefix/doc` %buildroot/%_dqt6_prefix/doc

# install binaries to %_bindir
mkdir %buildroot/%_bindir
ls -1d %buildroot/%_dqt6_bindir/* | \
while read f ; do
    [ -f "$f" ] || continue
    [ -x "$f" ] || continue
    fname=`basename $f`
    mv $f %buildroot/%_bindir/$fname-%gname
    ln -s `relative %_bindir/$fname-%gname %_dqt6_bindir/$fname-%gname` %buildroot/%_dqt6_bindir/$fname
    if echo "$fname" | grep -qe '6$'  ; then
	ln -s $fname-%gname %buildroot/%_bindir/$fname
    fi
done

## .prl/.la files
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %buildroot/%_dqt6_libdir
for prl_file in libQt%{major}*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd

# install libs into qt prefix
mkdir -p %buildroot/%_dqt6_prefix/lib
ls -1d %buildroot/%_dqt6_libdir/*.{a,so,prl} 2>/dev/null | \
while read f ; do
    [ -d "$f" ] && continue
    fname=`basename $f`
    ln -s `relative $f %buildroot/%_dqt6_prefix/lib/$fname` %buildroot/%_dqt6_prefix/lib/$fname
done
# link includes into qt prefix
ln -s `relative %buildroot/%_dqt6_headerdir %buildroot/%_dqt6_prefix/include` %buildroot/%_dqt6_prefix/include

# relax depends on sql plugins files
for f in %buildroot/%_dqt6_libdir/cmake/Qt?Sql/Qt*DriverPluginTargets.cmake ; do
    sed -i '/message.*FATAL_ERROR.*target.* references the file/s|FATAL_ERROR|WARNING|' $f
done

%files -n dqt6-qtbase
%files -n dqt6-qtbase-gui
%files common
%doc LICENSES/*
%dir %_sysconfdir/dqt6/
%dir %_dqt6_docdir/
%dir %_dqt6_archdatadir/
%dir %_dqt6_examplesdir/
%dir %_dqt6_importdir/
%dir %_dqt6_qmldir/
%dir %_dqt6_translationdir/
%dir %_dqt6_prefix/
%dir %_dqt6_prefix/doc/
%dir %_dqt6_prefix/imports/
%dir %_dqt6_prefix/lib/
%dir %_dqt6_prefix/libexec/
%dir %_dqt6_prefix/plugins/
%if "%_dqt6_prefix" != "%_dqt6_datadir"
%dir %_dqt6_datadir/
%endif
%dir %_dqt6_libexecdir/
%dir %_dqt6_plugindir/
%dir %_dqt6_plugindir/accessible/
#%dir %_dqt6_plugindir/bearer/
%dir %_dqt6_plugindir/egldeviceintegrations/
%dir %_dqt6_plugindir/generic/
%dir %_dqt6_plugindir/iconengines/
%dir %_dqt6_plugindir/imageformats/
%dir %_dqt6_plugindir/networkinformation/
%dir %_dqt6_plugindir/platforminputcontexts/
%dir %_dqt6_plugindir/platforms/
%dir %_dqt6_plugindir/platformthemes/
%dir %_dqt6_plugindir/printsupport/
%dir %_dqt6_plugindir/script/
%dir %_dqt6_plugindir/sqldrivers/
%dir %_dqt6_plugindir/styles/
%dir %_dqt6_plugindir/tls/
%dir %_dqt6_plugindir/xcbglintegrations/
%config(noreplace) %_sysconfdir/dqt6/qtlogging.ini
%_dqt6_datadir/qtlogging.ini

%files doc
%if %qdoc_found
%doc %_dqt6_docdir/*
%exclude %_dqt6_docdir/config/
%exclude %_dqt6_docdir/global/
%endif
%_dqt6_examplesdir/*

%files -n rpm-macros-%gname
%_rpmmacrosdir/%gname

%files devel
%_dqt6_docdir/config/
%_dqt6_docdir/global/
%dir %_dqt6_bindir
#
%_bindir/androiddeployqt*
%_dqt6_bindir/androiddeployqt*
%_bindir/androidtestrunner*
%_dqt6_bindir/androidtestrunner*
%_bindir/qt-cmake*
%_dqt6_bindir/qt-cmake*
%_bindir/qt-configure-module*
%_dqt6_bindir/qt-configure-module*
%_bindir/qtpaths*
%_dqt6_bindir/qtpaths*
%_bindir/qdbuscpp2xml*
%_dqt6_bindir/qdbuscpp2xml*
%_bindir/qdbusxml2cpp*
%_dqt6_bindir/qdbusxml2cpp*
%_bindir/qmake*
%_dqt6_bindir/qmake*
#
%_dqt6_libexecdir/moc
%_dqt6_libexecdir/rcc
%_dqt6_libexecdir/syncqt
%_dqt6_libexecdir/uic
%_dqt6_libexecdir/qlalr
%_dqt6_libexecdir/qvkgen
%_dqt6_libexecdir/tracegen
%_dqt6_libexecdir/cmake_automoc_parser
%_dqt6_libexecdir/ensure_pro_file.cmake
%_dqt6_libexecdir/qt-internal-configure-*
%_dqt6_libexecdir/qt-cmake-private*
%_dqt6_libexecdir/qt-cmake-standalone-test
%_dqt6_libexecdir/qt-testrunner.py
%_dqt6_libexecdir/sanitizer-testrunner.py
%_dqt6_libexecdir/tracepointgen
#
%dir %_dqt6_headerdir
%dir %_dqt6_prefix/include/
%_dqt6_headerdir/Qt*/
%dir %_dqt6_prefix/mkspecs/
%_dqt6_archdatadir/mkspecs/
%_dqt6_prefix/lib/libQt%{major}*.prl
%_dqt6_libdir/libQt%{major}*.prl
%_dqt6_prefix/lib/libQt%{major}*.so
%_dqt6_libdir/libQt%{major}*.so
%_dqt6_prefix/lib/libQt%{major}*.a
%_dqt6_libdir/libQt%{major}*.a
%dir %_dqt6_libdir/cmake/
%_dqt6_libdir/cmake/Qt%{major}*/
%_dqt6_archdatadir/metatypes/
%_dqt6_archdatadir/modules/
%_dqt6_libdir/pkgconfig/Qt%{major}*.pc

%files devel-static

%files -n %gname-sql
# packaged with sql library
#%if_enabled sql_sqlite
#%files -n %gname-sql-sqlite
#%_dqt6_plugindir/sqldrivers/libqsqlite.so
#%endif

%if_enabled sql_ibase
%files -n %gname-sql-interbase
%_dqt6_plugindir/sqldrivers/libqsqlibase.so
%endif

%files -n %gname-sql-mysql
%_dqt6_plugindir/sqldrivers/libqsqlmysql.so

%if_enabled sql_odbc
%files -n %gname-sql-odbc
%_dqt6_plugindir/sqldrivers/libqsqlodbc.so
%endif

%if_enabled sql_pgsql
%files -n %gname-sql-postgresql
%_dqt6_plugindir/sqldrivers/libqsqlpsql.so
%endif

%if_enabled sql_tds
%files -n %gname-sql-tds
%_dqt6_plugindir/sqldrivers/libqsqltds.so
%endif

%if_enabled sql_sqlite2
%files -n %gname-sql-sqlite2
%_dqt6_plugindir/sqldrivers/libqsqlite2.so
%endif

%files -n lib%gname-core
%_dqt6_libdir/libQt%{major}Core.so.*

%files -n lib%gname-concurrent
%_dqt6_libdir/libQt%{major}Concurrent.so.*

%files -n lib%gname-dbus
%_dqt6_libdir/libQt%{major}DBus.so.*

%files -n lib%gname-gui
%_dqt6_libdir/libQt%{major}Gui.so.*
%_dqt6_plugindir/egldeviceintegrations/*
%_dqt6_plugindir/generic/*
%_dqt6_plugindir/imageformats/*
%_dqt6_plugindir/platforminputcontexts/*
%_dqt6_plugindir/platforms/*
%_dqt6_plugindir/platformthemes/*
%_dqt6_plugindir/xcbglintegrations/*

%files -n lib%gname-network
%_dqt6_libdir/libQt%{major}Network.so.*
%_dqt6_plugindir/networkinformation/*
%_dqt6_plugindir/tls/*

%files -n lib%gname-opengl
%_dqt6_libdir/libQt%{major}OpenGL.so.*

%files -n lib%gname-printsupport
%_dqt6_libdir/libQt%{major}PrintSupport.so.*
%_dqt6_plugindir/printsupport/*

%files -n lib%gname-sql
%_dqt6_libdir/libQt%{major}Sql.so.*
%_dqt6_plugindir/sqldrivers/libqsqlite.so

%files -n lib%gname-test
%_dqt6_libdir/libQt%{major}Test.so.*

%files -n lib%gname-widgets
%_dqt6_libdir/libQt%{major}Widgets.so.*
#%_dqt6_plugindir/accessible/*

%files -n lib%gname-xml
%_dqt6_libdir/libQt%{major}Xml.so.*

%files -n lib%gname-eglfsdeviceintegration
%_dqt6_libdir/libQt%{major}EglFSDeviceIntegration.so.*

%files -n lib%gname-xcbqpa
%_dqt6_libdir/libQt%{major}XcbQpa.so.*

%files -n lib%gname-eglfskmssupport
%_dqt6_libdir/libQt%{major}EglFsKmsSupport.so.*

%files -n lib%gname-eglfskmsgbmsupport
%_dqt6_libdir/libQt%{major}EglFsKmsGbmSupport.so.*

%files -n lib%gname-openglwidgets
%_dqt6_libdir/libQt%{major}OpenGLWidgets.so.*

%changelog
* Wed Oct 02 2024 Leontiy Volodin <lvol@altlinux.org> 6.7.2-alt1.dde.1
- fork qt6 for separate deepin packaging (ALT #48138)

* Tue Sep 03 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt2
- restore qmenu_fix_shortcuts.patch (thanks Corwin)

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Jul 22 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt4
- add patch for keyboard shortcuts from Corwin

* Mon Feb 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt3
- fix iconloader fallback (closes: 49503)

* Thu Feb 22 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt2
- set C.UTF-8 locale for qmake

* Mon Feb 19 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt1
- new version

* Tue Dec 05 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.1-alt1
- new version

* Tue Nov 28 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt3
- remove rpath from examples
- turn off build dependencies on plugins by default

* Wed Nov 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt2
- fix build docs

* Tue Oct 31 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

* Tue Jun 13 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt3
- fixed compilation on LoongArch (thanks asheplyakov@alt) (closes: 46477)

* Thu Apr 13 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt2
- fix to build docs

* Wed Feb 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Fri Dec 09 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt4
- automate bootstrap mode

* Wed Jun 15 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt3
- move some altlinux fixes from Qt5
- build docs

* Thu Jun 02 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt2
- fix parse timezones

* Wed May 25 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Mon Apr 18 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt2
- fix requires (closes: 42468)

* Tue Dec 07 2021 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

* Thu Nov 25 2021 Sergey V Turchin <zerg@altlinux.org> 6.2.1-alt0.1
- initial build
