%define _unpackaged_files_terminate_build 1

%def_without python
%def_with parallelism
%def_without fetch
%def_enable lto
%def_with dconf
%def_with mdds
%def_with orcus
# Uncompatible with zxing-cpp >= 2.2.1
%def_with zxing
# check
%def_with openssl

# Attention! Use only one UI: kde5 or kde6
# enable kde5 UI
%def_disable kde5
# enable kde6 UI
%def_enable kde6

%ifarch mipsel
%def_without java
%else
%def_with java
%endif
%if_enabled kde5
%define enable_kde 1
%def_enable qt5
%else
%def_disable qt5
%if_enabled kde6
%define enable_kde 1
%else
%define enable_kde 0
%endif
%endif
%if_enabled kde6
%def_enable qt6
%else
%def_disable qt6
%endif
%def_enable mergelibs
%def_disable gtk4

# build scripts don't need any help in enabling LTO
%define optflags_lto %nil

# with the default -g2 %%name-common-debuginfo
# doesn't fit into 4Gb limit of the payload
%define optflags_debug -g1

Name: libreoffice
%define hversion 26.2
%define urelease 3.2
Version: %hversion.%urelease
Release: alt1
%define uversion %version.%urelease
%define lodir %_libdir/%name
%define uname libreoffice5
%define conffile %_sysconfdir/sysconfig/%uname

Summary: LibreOffice Productivity Suite
# default new files are: MPLv2
# older files are typically: MPLv2 incorporating work under ASLv2
# nlpsolver is: LGPLv3
# icon-themes/karasa_jaga/COPYING: LGPLv3+
# icon-themes/colibre/COPYING-ICONS: CC0
# lotuswordpro is: Either LGPL 2.1 or SISSL 1.1
# wizards/source/access2base: Either MPLv2 or LGPLv3+
# writerperfect/source/common/DirectoryStream.cxx: MPLv2 or LGPLv2+
# extras/source/autocorr/lang/hr/license.md: GPL 2.0 or LGPL2 or MPLv1.1
# odk/examples/java/...: 3 clause BSD
License: MPL-2.0 AND Apache-2.0 AND LGPL-3.0-only AND LGPL-3.0-or-later AND CC0-1.0 AND BSD-3-Clause AND (LGPL-2.1-only OR SISSL) AND (MPL-2.0 OR LGPL-3.0-or-later) AND (MPL-2.0 OR LGPL-2.1-or-later) AND (MPL-1.1 OR GPL-2.0-only OR LGPL-2.1-only) AND MIT
Group: Office
URL: http://www.libreoffice.org

ExcludeArch: armh

%define with_lang ru be de fr uk pt-BR es kk tr tt el uz ky

Source:	libreoffice-%version.tar.xz
Source1: libreoffice-dictionaries-%version.tar.xz
Source2: libreoffice-help-%version.tar.xz
Source3: libreoffice-translations-%version.tar.xz
#Source4: libreoffice-%version-ru.tar

Source10: libreoffice-ext_sources-%version.tar
Source200: key.gpg
Source300: libreoffice.unused

# Icons
Source400: libreoffice-icons-oxygen.zip
# Scalable symbolic icons from https://raw.githubusercontent.com/gnome-design-team/gnome-icons/master/apps-symbolic/Adwaita/scalable/apps/
Source401: libreoffice-icons-symbolic.tar

## FC patches
Patch1: FC-0001-don-t-suppress-crashes.patch
Patch2: FC-0001-disble-tip-of-the-day-dialog-by-default.patch
Patch3: FC-0001-Resolves-rhbz-1432468-disable-opencl-by-default.patch

## ALT patches
Patch401: alt-001-MOZILLA_CERTIFICATE_FOLDER.patch
Patch402: alt-002-tmpdir.patch
Patch403: alt-003-shortint.patch
Patch404: alt-004-unversioned-desktop-files.patch
Patch405: alt-005-mkdir-for-external-project.patch
Patch407: alt-007-vnd.ms-word-mimetype.patch
Patch410: alt-010-svg-icons-1.patch
Patch411: alt-011-svg-icons-2.patch
Patch412: alt-012-svg-icons-3.patch

Patch500: alt-010-mips-fix-linking-with-libatomic.patch
Patch501: 64c7eac.diff

# make -j32 fails without this patch
Patch700: alt-700-external-project-concurrency.patch

%set_verify_elf_method unresolved=relaxed
%add_findreq_skiplist %lodir/share/config/webcast/*
%add_findreq_skiplist %lodir/sdk/examples/python/DocumentHandling/*.py
%add_findprov_skiplist %lodir/sdk/examples/python/DocumentHandling/*.py
%add_findreq_skiplist %lodir/sdk/examples/python/toolpanel/toolpanel.py
%add_findreq_skiplist %lodir/sdk/examples/DevelopersGuide/FirstSteps/*/python/*.py
%add_findreq_skiplist %lodir/sdk/classes
%add_findreq_skiplist %lodir/sdk/docs
%add_findreq_skiplist %lodir/sdk/idl
%add_findreq_skiplist %lodir/sdk/include
%filter_from_requires /com[.]sun[.]/d
%filter_from_requires /open/d
%filter_from_requires /valgrind/d
%add_python3_req_skip pyuno strings officehelper uno unohelper
%add_python3_req_skip usr.src.tmp.libreoffice-buildroot.usr.%_lib.libreoffice.program.wizards.ui.event.ListDataListener

BuildRequires(pre): rpm-build-python3
BuildRequires: cppunit-devel flex fonts-ttf-liberation gcc-c++ git-core gperf gst-plugins1.0-devel hunspell-en imake libGConf-devel libGLEW-devel libabw-devel libbluez-devel libcdr-devel libclucene-core-devel libcmis-devel libcups-devel libdbus-devel libetonyek-devel libexpat-devel libexttextcat-devel libfreehand-devel libglm-devel libharfbuzz-devel libhunspell-devel libhyphen-devel libjpeg-devel liblangtag-devel liblcms2-devel libldap-devel liblpsolve-devel libmspub-devel libmwaw-devel libmythes-devel libneon-devel libnss-devel libodfgen-devel libredland-devel libsane-devel libvigra-devel libvisio-devel libwpd10-devel libwpg-devel libwps-devel libxslt-devel perl-Archive-Zip postgresql-devel python3-dev unzip xorg-cf-files zip
BuildRequires: mdds-devel >= 3.0.0
BuildRequires: python2.7(distutils) libunixODBC-devel libX11-devel libXext-devel libXinerama-devel libXrandr-devel libXrender-devel libXt-devel
%if_with openssl
BuildRequires: libssl-devel
%endif
%if_enabled gtk4
BuildRequires: libgtk4-devel
%else
BuildRequires: libgtk+3-devel
%endif
BuildRequires: xsltproc

# 4.4
BuildRequires: libavahi-devel libpagemaker-devel boost-signals-devel
BuildRequires: libe-book-devel
# 5.1
%if_with java
BuildRequires: junit xsltproc
BuildRequires: ant apache-commons-httpclient apache-commons-lang bsh
BuildRequires: pentaho-reporting-flow-engine
%endif
# 5.1.2
BuildRequires: libgtk+3-gir-devel
# 5.2.0
#BuildRequires: libCoinMP-devel
# 5.3.0
BuildRequires: libzmf-devel libstaroffice-devel libepoxy-devel libmysqlcppconn-devel libmysqlclient-devel
# 5.3.3
BuildRequires: doxygen e2fsprogs
# 5.4.0
BuildRequires: libxmlsec1-nss-devel libgpgme-devel
# 6.0.1
BuildRequires: libepubgen-devel libqxp-devel boost-locale-devel boost-filesystem-devel
# 6.0.5
%if_enabled qt5
BuildRequires: qt5-base-devel
%endif
%if_enabled qt6
BuildRequires: qt6-base-devel
BuildRequires: qt6-multimedia-devel
%endif
# 6.1.0
BuildRequires: libnumbertext-devel
# 6.1.1
BuildRequires: python3-module-setuptools
# 6.1.3.1 kde5 UI
%if_enabled kde5
BuildRequires: qt5-base-devel qt5-x11extras-devel
BuildRequires: kf5-kconfig-devel kf5-kcoreaddons-devel
BuildRequires: kf5-ki18n-devel kf5-kio-devel kf5-kwindowsystem-devel
BuildRequires: kf5-kdelibs4support-devel
BuildRequires: libgtk+3-devel
%endif
# kde6 UI
%if_enabled kde6
BuildRequires: kf6-kconfig-devel kf6-kcoreaddons-devel
BuildRequires: kf6-ki18n-devel kf6-kio-devel kf6-kwindowsystem-devel
%endif
# 6.1.5.2
#BuildRequires: libpoppler-devel
# 6.3.5.2
BuildRequires: fontforge
# 6.4.5.2
%if_with orcus
# Build with system liborcus
BuildRequires: liborcus-devel >= 0.20.2
%else
# Build with bundled liborcus
BuildRequires: boost-devel-headers boost-interprocess-devel boost-program_options-devel gcc-c++ zlib-devel boost-filesystem-devel mdds-devel python3-devel
%endif
BuildRequires: libqrcodegen-cpp-devel
BuildRequires: libxcbutil-icccm-devel
BuildRequires: libeot-devel
BuildRequires: libgraphite2-devel
%if_with java
# 7.0.4.2
# java.lang.SecurityManager is missing in Java 25
BuildRequires: java-17-openjdk-devel
%endif
# 7.1.5.2
BuildRequires: libbox2d-devel
BuildRequires: libpixman-devel
# 7.2.5.2
%if_with zxing
BuildRequires: libzxing-cpp-devel
%endif
# 7.3.5.2
BuildRequires: libcuckoo-devel
BuildRequires: libopenjpeg2.0-devel
BuildRequires: libabseil-cpp-devel
# 7.4
BuildRequires: libwebp-devel libtiff-devel
# 7.6
BuildRequires: frozen-devel
# 24.2
BuildRequires: libargon2-devel
# 24.8
BuildRequires: rhino
# 25.8
BuildRequires: libzstd-devel
# 26.2
BuildRequires: libmd4c-devel
BuildRequires: libfast_float-devel
BuildRequires: perl-Time-Piece

%if_without python
BuildRequires: python3-dev
%endif
%if_with dconf
BuildRequires: libdconf-devel
%endif
BuildRequires: gnu-config

AutoReqProv: yes, noshell, nopython

Provides: %name-full = %EVR
Obsoletes: %name-full < %EVR
Obsoletes: LibreOffice4
Provides: LibreOffice = %EVR
Provides: LibreOffice-still = %EVR
Obsoletes: LibreOffice < %EVR
Obsoletes: LibreOffice-still < %EVR
# common
Obsoletes: LibreOffice4-common
Provides: LibreOffice-common = %EVR
Provides: LibreOffice-still-common = %EVR
Obsoletes: LibreOffice-common < %EVR
Obsoletes: LibreOffice-still-common < %EVR
# Strict requirements
# integrated
Provides: LibreOffice-integrated = %EVR
Provides: LibreOffice-still-integrated = %EVR
Obsoletes: LibreOffice-integrated < %EVR
Obsoletes: LibreOffice-still-integrated < %EVR
Obsoletes: LibreOffice4-integrated
# mimetypes
Provides: LibreOffice-mimetypes = %EVR
Provides: LibreOffice-still-mimetypes = %EVR
Obsoletes: LibreOffice-mimetypes < %EVR
Obsoletes: LibreOffice-still-mimetypes < %EVR
Obsoletes: LibreOffice4-mimetypes
# Other runtime requirements
Requires: gst-libav
%if_with java
Requires: java-headless >= 9.0.0
Requires: pentaho-reporting-flow-engine
Requires: %name-extensions = %EVR

%package extensions
Summary: Java extensions for LibreOffice
Group: Office
Requires: java-headless >= 9.0.0
Provides: LibreOffice-extensions = %EVR
Obsoletes: LibreOffice-extensions < %EVR
Provides: LibreOffice-still-extensions = %EVR
Obsoletes: LibreOffice-still-extensions < %EVR
Obsoletes: LibreOffice4-extensions

%description extensions
%{summary}.
%endif

%package core
Summary: Core part for LibreOffice (without Java)
Group: Office

%description core
%{summary}.

%description
LibreOffice is a productivity suite that is compatible with other major
office suites.

This package provides maximum possible installation of %name along winth
other office packages, except of language packs and GNOME/KDE bindings.

%package gtk3
Summary: GTK3 GUI for %name
Group:  Office
Requires: %name-core = %EVR
Provides: LibreOffice-gtk3 = %EVR
Provides: LibreOffice-still-gtk3 = %EVR
Obsoletes: LibreOffice-gtk3 < %EVR
Obsoletes: LibreOffice-still-gtk3 < %EVR
Provides: LibreOffice-gnome = %EVR
Provides: %name-gnome = %EVR
Obsoletes: %name-gnome < %EVR
%description gtk3
GTK3 GUI for %name

%package gtk4
Summary: GTK4 GUI for %name
Group:  Office
Requires: %name-core = %EVR
Provides: LibreOffice-gtk4 = %EVR
Provides: LibreOffice-still-gtk4 = %EVR
Obsoletes: LibreOffice-gtk4 < %EVR
Obsoletes: LibreOffice-still-gtk4 < %EVR
%description gtk4
GTK4 GUI for %name

%if %{enable_kde}
%package qt
Summary: Qt GUI for %name
Group:  Office
Requires: %name-core = %EVR
Obsoletes: LibreOffice-qt5 < %EVR
Obsoletes: LibreOffice-qt6 < %EVR
Obsoletes: LibreOffice-still-qt5 < %EVR
Obsoletes: LibreOffice-still-qt6 < %EVR
Obsoletes: libreoffice-qt5 < %EVR
Obsoletes: libreoffice-qt6 < %EVR
Provides:  LibreOffice-qt5 = %EVR
Provides:  LibreOffice-qt6 = %EVR
Provides:  LibreOffice-still-qt5 = %EVR
Provides:  LibreOffice-still-qt6 = %EVR
Provides:  libreoffice-qt5 = %EVR
Provides:  libreoffice-qt6 = %EVR
%description qt
Qt GUI for %name

%package kde
Summary: KDE GUI for %name
Group:  Office
Requires: %name-core = %EVR
Obsoletes: %name-kde4 < %EVR
Obsoletes: %name-kde4 < %EVR
Obsoletes: LibreOffice-kde5 < %EVR
Obsoletes: LibreOffice-kde6 < %EVR
Obsoletes: LibreOffice-still-kde5 < %EVR
Obsoletes: LibreOffice-still-kde6 < %EVR
Obsoletes: LibreOffice4-kde4 < %EVR
Obsoletes: LibreOffice4-kde4 < %EVR
Obsoletes: libreoffice-kde5 < %EVR
Obsoletes: libreoffice-kde6 < %EVR
Provides:  %name-kde4 = %EVR
Provides:  %name-kde4 = %EVR
Provides:  LibreOffice-kde5 = %EVR
Provides:  LibreOffice-kde6 = %EVR
Provides:  LibreOffice-still-kde5 = %EVR
Provides:  LibreOffice-still-kde6 = %EVR
Provides:  LibreOffice4-kde4 = %EVR
Provides:  LibreOffice4-kde4 = %EVR
Provides:  libreoffice-kde5 = %EVR
Provides:  libreoffice-kde6 = %EVR
%description kde
KDE GUI for %name
%endif

%package -n libreofficekit
Summary: A library providing access to LibreOffice functionality
Group: Graphical desktop/GNOME
License: MPL-2.0
Provides: libreofficekit-still = %EVR
Obsoletes: libreofficekit-still < %EVR
%description -n libreofficekit
LibreOfficeKit can be used to access LibreOffice functionality
through C/C++, without any need to use UNO.

%package -n libreofficekit-devel
Summary: Development files for libreofficekit
Group: Development/GNOME and GTK+
Provides: libreofficekit-still-devel = %EVR
Obsoletes: libreofficekit-still-devel < %EVR
License: MPL-2.0
%description -n libreofficekit-devel
The libreofficekit-devel package contains libraries and header files for
developing applications that use libreofficekit.

%package sdk
Group: Development/Other
Summary: Software Development Kit for LibreOffice
Provides: LibreOffice-sdk = %EVR
Provides: LibreOffice-still-sdk = %EVR
Obsoletes: LibreOffice-sdk < %EVR
Obsoletes: LibreOffice-still-sdk < %EVR

%description sdk
The SDK is a development kit for LibreOffice 5.3, which
eases the development of office components. It provides a set of
libraries, binaries, header, and IDL files which have final API's
and can only be extended with new functionality. This set of libraries
and binaries is the minimum set of functions needed to use system
abstraction for base functionality and for using UNO (Universal
Network Objects) component technology. The UNO component model is the
base of the whole Office API. The SDK provides everything necessary
to use the Office API from external programs (e.g. Java, C++) or to
extend the Office functionality with new components (e.g. new filter
components, CalcAddin functions). It is compatible over several
versions because the API remains unaffected and will only be extended
with new functions.

# define macro for quick langpack description
%define langpack(l:n:s:mh) \
%define lang %{-l:%{-l*}}%{!-l:%{error:Language code not defined}} \
%define pkgname langpack-%{lang} \
%define langname %{-n:%{-n*}}%{!-n:%{error:Language name not defined}} \
%define spellname %{-s:%{-s*}}%{!-s:%{error:Spell dictionary is not defined}} \
\
%package %{pkgname} \
Summary: %{langname} language pack for %name \
Group:  Office \
Requires: %name-core = %EVR \
%{-m:Requires: mythes-%lang} \
%{-h:Requires: hyphen-%lang} \
%{-s:Requires: hunspell-%spellname} \
Provides: LibreOffice-%{pkgname} = %EVR \
Provides: LibreOffice-still-%{pkgname} = %EVR \
Obsoletes: LibreOffice-%{pkgname} < %EVR \
Obsoletes: LibreOffice-still-%{pkgname} < %EVR \
Obsoletes: LibreOffice4-%{pkgname} \
%description %{pkgname} \
Provides additional %{langname} translations and resources for %name. \
\
%files %{pkgname} -f %{lang}.lang \
%{nil}

%prep
echo Direct build
%setup -q -n libreoffice-%version -a10 -b1 -b2 -b3
#tar xf %SOURCE4 --strip-components=1 -C translations/source/ru

## FC apply patches
#patch1 -p1
%patch2 -p1
%patch3 -p1

## ALT apply patches
%patch401 -p0
%patch402 -p1
%patch403 -p1
%patch404 -p1
%patch405 -p1
%patch407 -p1
#patch410 -p1
#patch411 -p1
#patch412 -p1

%patch500 -p0
%patch501 -p1
%patch700 -p1

# TODO move officebeans to SDK or separate package
# Hack in -Wl,-rpath=/usr/lib/jvm/jre-11-openjdk/lib
sed -i 's@JAVA_HOME/lib/ -ljawt@JAVA_HOME/lib/ -Wl,-rpath=/usr/lib/jvm/jre/lib -ljawt@' configure.ac
%filter_from_requires /libjawt[.]so/d

%if_enabled kde5
# Choose right path to kcoreaddons_version.h
if [ -e "%_includedir/KF5/KCoreAddons/kcoreaddons_version.h" ]; then
    sed -i -e 's|kf5_test_include="KF5/kcoreaddons_version.h"|kf5_test_include="KF5/KCoreAddons/kcoreaddons_version.h"|' configure.ac
fi
%endif

# Hack in proper LibreOffice PATH in libreofficekit
sed -i 's@/libreoffice/@/LibreOffice/@g' libreofficekit/Library_libreofficekitgtk.mk

# Hack hardcoded lsattr path
for f in `grep -rl '/usr/sbin/lsattr' *`; do sed -i 's@/usr/sbin/lsattr@/usr/bin/lsattr@g' $f; done

# Hack in MimeType=application/vnd.ms-visio.drawing.main+xml
fgrep -q "application/vnd.ms-visio.drawing.main+xml" sysui/desktop/menus/draw.desktop || sed -i 's@MimeType=@MimeType=application/vnd.ms-visio.drawing.main+xml;@' sysui/desktop/menus/draw.desktop

rm -fr %name-tnslations/git-hooks

# create shell wrappers
for n in office writer impress calc base draw math qstart; do
	oname=lo$n
	case "$n" in
		office) opt=""; oname=libreoffice;;
		qstart) opt="--quickstart --nologo --nodefault";;
		*) opt="--$n";;
	esac
	cat > $oname.sh <<@@@
#!/bin/sh
exec %lodir/program/soffice $opt "\$@"
@@@
done

# Now create a config file
grep -r getenv * | sed -n 's/.*getenv *( *"\([^"]*\).*/\1/p' | sort -u | egrep 'STAR_|SAL_|OOO_' > %name.config.ENV

sed -n '/# STAR_PROFILE_LOCKING_DISABLED/,/#.*JITC_PROCESSOR_TYPE_EXPORT/p' < desktop/scripts/soffice.sh > libreoffice.config
test -n "libreoffice.config"
sed -i '/# STAR_PROFILE_LOCKING_DISABLED/i\
test -r %conffile && . %conffile ||:
/# STAR_PROFILE_LOCKING_DISABLED/,/#.*JITC_PROCESSOR_TYPE_EXPORT/d' desktop/scripts/soffice.sh

# Put Python3 shebang
subst '1i#!/usr/bin/python3' `find odk/examples/ -name \*.py`

# Guess Kyrgyz localization as complete
subst '/ks /a ky \\' solenv/inc/langlist.mk

# Remove wrong mime-type application/vnd.ms-word
rm -f sysui/desktop/mimetypes/ms-word-document2.desktop

%build
export CC=%_target_platform-gcc
export CXX=%_target_platform-g++

%ifarch mipsel
export CFLAGS="-Os --param ggc-min-expand=20 --param ggc-min-heapsize=32768 -g1"
%else
export CFLAGS="-fPIC %optflags"
%endif
%ifarch loongarch64
export CFLAGS="$CFLAGS -flax-vector-conversions"
%endif
%if_disabled gtk4
export CFLAGS="$CFLAGS -I%_includedir/gtk-3.0"
%endif

export CXXFLAGS="$CFLAGS"
export LDFLAGS="$CFLAGS"


# XXX no "thin" LTO option in GCC!
sed -i 's/-flto=thin/-flto=jobserver/g' solenv/gbuild/platform/com_GCC_defs.mk

# new libcmis
sed -i "s@libcmis-0.5@libcmis-0.6@g" configure.ac

PARALLEL=${NPROCS:-%__nprocs}
%ifarch ppc64le
# reduce excessive resource use
if [ "$PARALLEL" -gt 24 ] ; then
        PARALLEL=24
fi
%endif

cp -af /usr/share/gnu-config/config.guess .
cp -af /usr/share/gnu-config/config.sub .

export ac_cv_prog_LO_CLANG_CXX=""
export ac_cv_prog_LO_CLANG_CC=""
./autogen.sh \
        --prefix=%_prefix \
        --libdir=%_libdir \
        %{subst_enable lto} \
        --with-vendor="ALT Linux Team" \
        %{?_without_mdds:--without-system-mdds } \
        %{?_without_orcus:--without-system-orcus } \
        %{?_without_zxing:--without-system-zxing } \
        %{subst_enable mergelibs} \
        --with-system-libcmis \
        --disable-firebird-sdbc \
        --disable-coinmp \
        --enable-dbus \
%if_with openssl
        --enable-openssl \
        --enable-cipher-openssl-backend \
%else
        --disable-openssl \
%endif
        --disable-pdfium \
%ifarch %ix86
        --disable-skia \
%else
        --enable-skia \
%endif
        --enable-evolution2 \
        --enable-introspection \
        --enable-odk \
        --enable-gio \
        --enable-symbols \
        --enable-build-opensymbol \
        --enable-avahi \
        %{subst_with java} \
        --without-fonts \
        --without-myspell-dicts \
        --without-doxygen \
        --without-system-poppler \
        --without-system-dragonbox \
        --without-system-libfixmath \
        --with-system-libs \
        --without-export-validation \
        --without-lxml \
        --without-system-libfixmath \
        --with-rhino-jar=/usr/share/java/rhino/rhino.jar \
        \
        --with-external-dict-dir=%_datadir/myspell \
        --with-external-hyph-dir=%_datadir/hyphen \
        --with-external-thes-dir=%_datadir/mythes \
        --with-lang="en-US %with_lang" \
        --with-external-tar=`pwd`/ext_sources \
        --without-system-java-websocket \
        --with-rhino-jar=%_datadir/java/rhino.jar \
        \
        --enable-ext-nlpsolver \
        --enable-ext-wiki-publisher \
  \
        --enable-release-build \
        --with-help \
  \
        %{subst_enable qt5} \
        %{subst_enable qt6} \
%if_enabled gtk4
        --enable-gtk4 \
%else
        --enable-gtk3 \
%endif
%if_enabled kde5
        --enable-gtk3-kde5 \
%endif
%if_enabled kde6
        --enable-kf6 \
        --enable-qt6 \
%endif
        --without-system-zxcvbn \
%if_with parallelism
        --with-parallelism="$PARALLEL" \
%else
        --without-parallelism \
%endif
%if_with python
        --enable-python=internal \
%else
        --enable-python=system \
%endif
%if_with dconf
        --enable-dconf \
%endif
        --enable-introspection \
        --enable-eot \
        --enable-formula-logger \
%if_with fetch
        --enable-fetch-external
%else
        --with-system-libs \
        --disable-fetch-external
%endif

%make bootstrap

%if_with parallelism
export _JAVA_OPTIONS="-XX:ParallelGCThreads=4 $_JAVA_OPTIONS"
%endif

%make build AR=/usr/bin/ar RANLIB=/usr/bin/ranlib verbose=true

# Generate typelib files
## TODO us
export DESTDIR=../output
export KDEMAINDIR=/usr
export GNOMEDIR=/usr
export GNOME_MIME_THEME=hicolor
export PREFIXDIR=/usr
. ./bin/get_config_variables PRODUCTVERSIONSHORT PRODUCTVERSION SRCDIR WORKDIR PKG_CONFIG INSTDIR
export PRODUCTVERSIONSHORT PRODUCTVERSION SRCDIR WORKDIR PKG_CONFIG INSTDIR
cd $WORKDIR/CustomTarget/sysui/share/libreoffice
./create_tree.sh

%install
%makeinstall DESTDIR=%buildroot INSTALLDIR=%lodir

%if_with python
# Ignore dull /usr/local/bin/python hack
chmod -x %buildroot%lodir/program/python-core*/lib/cgi.py
%endif

# Pick up LOO-generated file lists
for l in %with_lang; do
	ll="`echo "$l" | tr '-' '_'`"
	cat %buildroot/gid_*_$ll | sort -u > $l.lang
done

# Create gtk3 plugin list
find %buildroot%lodir -name "*_gtk3lo.so" | sed 's@^%buildroot@@' > files.gtk3

# Create gtk4 plugin list
find %buildroot%lodir -name "*_gtk4lo.so" | sed 's@^%buildroot@@' > files.gtk4

# Create qt5 plugin list
find %buildroot%lodir -name "*qt5*"   | sed 's@^%buildroot@@' > files.qt5

# Create kde5 plugin list
find %buildroot%lodir -name "*_kde5*" | sed 's@^%buildroot@@' > files.kde5

# Create qt6 plugin list
find %buildroot%lodir -name "*qt6*"   | sed 's@^%buildroot@@' > files.qt6

# Create kde6 plugin list
find %buildroot%lodir -name "*_kf6*" | sed 's@^%buildroot@@' > files.kde6

# Generate base filelist by removing files from  separated packages
%define nolang_remove /share/extensions/.|%lodir/sdk/.|share/Scripts/java/.|/program/classes/.
{ cat %buildroot/gid_* | sort -u
  cat *.lang files.gtk3 files.gtk4 files.kde5 files.qt5 files.kde6 files.qt6
  echo %lodir/program/liblibreofficekitgtk.so
} | sort | uniq -u | egrep -v '~$|%nolang_remove' > files.nolang

# Return Oxygen icon theme from LibreOffice 5.3 (see https://bugs.documentfoundation.org/show_bug.cgi?id=110353 for details)
install -D %SOURCE400 %buildroot%lodir/share/config/images_oxygen.zip
echo "%lodir/share/config/images_oxygen.zip" >> files.nolang

unset RPM_PYTHON

# Install wrappers
for n in lo*.sh; do install -m755 -D $n %buildroot%_bindir/${n%%.sh}; done
install -Dm755 libreoffice.sh %buildroot%_bindir/libreoffice
install -Dm755 libreoffice.sh %buildroot%_bindir/loffice
ln -s loffice %buildroot%_bindir/soffice
ln -s ../%_lib/%name/program/unopkg %buildroot%_bindir/unopkg

# Install icons
for f in `( cd sysui/desktop/icons; find hicolor -type f )`; do
	d=`dirname "$f"`; n=`basename "$f"`
	if [[ "$d" == *apps ]]; then
		# Add prefix to apps icons
		install -D sysui/desktop/icons/$f %buildroot%_iconsdir/$d/libreoffice-$n
	else
		install -D sysui/desktop/icons/$f %buildroot%_iconsdir/$d/$n
	fi
done

# Install desktop files
# Hack out "Education" category from Math
subst 's/Education;//' %buildroot%lodir/share/xdg/math.desktop
mkdir -p %buildroot%_desktopdir
for f in %buildroot%lodir/share/xdg/*.desktop; do
	# Use GenericName values as Names (replace application name by its role,
	# for example, LibreOffice Impress by Presentation)
	n=`basename "$f"`
	awk '/^Name/ {next} /^GenericName/ {print;sub(/^GenericName/, "Name");print;next} {print}' "$f" > %buildroot%_desktopdir/libreoffice-$n
done

# TODO some other hack with .mime (?)
mkdir -p %buildroot%_datadir/mimelnk/application
install sysui/desktop/mimetypes/*.desktop %buildroot%_datadir/mimelnk/application/

# Install mime package bundle for LibreOffice MIME types
install -Dm0644 workdir/CustomTarget/sysui/share/output/usr/share/mime/packages/libreoffice%hversion.xml %buildroot%_datadir/mime/packages/libreoffice%hversion.xml

# Config file
install -D libreoffice.config %buildroot%conffile

# Typelib/GIR stuff
#install -D workdir/CustomTarget/sysui/share/output/girepository-1.0/LOKDocView-0.1.typelib %buildroot%_typelibdir/LOKDocView-0.1.typelib
#install -D workdir/CustomTarget/sysui/share/output/usr/share/gir-1.0/LOKDocView-0.1.gir %buildroot%_girdir/LOKDocView-0.1.gir
mv %buildroot%lodir/program/liblibreofficekitgtk.so %buildroot%_libdir/
mkdir -p %buildroot%_includedir/LibreOfficeKit
install -p include/LibreOfficeKit/* %{buildroot}%{_includedir}/LibreOfficeKit

# Make symlinks for x-office-* icons
# oasis-text -> x-office-document
# oasis-spreadsheet -> x-office-spreadsheet
# oasis-presentation -> x-office-presentation
# oasis-drawing -> image-x-generic
for dir in `ls -d %buildroot%_iconsdir/hicolor/*`; do
	for type in text spreadsheet presentation drawing; do
		target="$type"
		if [ "$type" == "text" ]; then
			target="x-office-document"
		elif ["$type" == "drawing" ]; then
			target="image-x-generic"
		else
			target="x-office-$type"
		fi
		for format in png svg; do
			if [ -e $dir/mimetypes/oasis-$type.$format ]; then
				ln -s oasis-$type.$format $dir/mimetypes/$target.$format
			fi
		done
	done
done

# Install appdata files
mkdir -p %buildroot%_datadir/metainfo
cp -a sysui/desktop/appstream-appdata/*.xml %buildroot%_datadir/metainfo

# Install man pages
install -Dpm0644 sysui/desktop/man/libreoffice.1 %buildroot%_man1dir/libreoffice.1
install -Dpm0644 sysui/desktop/man/unopkg.1 %buildroot%_man1dir/unopkg.1

# Install symbolc icons
mkdir -p %buildroot%_iconsdir/hicolor/symbolic/apps
tar xf %SOURCE401 -C %buildroot%_iconsdir/hicolor/symbolic/apps

# Fix shebang for python3
find %buildroot%lodir -name "__init__.py" -size 0 -exec bash -c 'echo "#!/usr/bin/python3" > "$1"' _ {} \;
find %buildroot%lodir -name \*.py > py.files
cat py.files | xargs grep -l '^#!/usr/bin/python3' > py_with_shebang.files
comm -23 <(sort py.files) <(sort py_with_shebang.files) | xargs subst '1i #!%__python3'

%files
%if_with java
%lodir/share/Scripts/java
%lodir/program/classes
%endif

%files core -f files.nolang
%exclude /gid_Module*
%_bindir/*
%config %conffile
%_datadir/metainfo/*.appdata.xml
%_desktopdir/libreoffice-*.desktop
%_iconsdir/*/*/mimetypes/*
%_iconsdir/*/*/apps/*
%_datadir/mime/packages/libreoffice%hversion.xml
%_datadir/mimelnk/application/*
%_man1dir/libreoffice.1*
%_man1dir/unopkg.1*

%files extensions
%if_with java
%lodir/share/extensions
%endif

%files sdk
%lodir/sdk

%files gtk3 -f files.gtk3

%if_enabled gtk4
%files gtk4 -f files.gtk4
%endif

%if_enabled qt5
%files qt -f files.qt5
%endif

%if_enabled kde5
%files kde -f files.kde5
%_datadir/metainfo/org.libreoffice.kde.metainfo.xml
%endif

%if_enabled qt6
%files qt -f files.qt6
%endif

%if_enabled kde6
%files kde -f files.kde6
%_datadir/metainfo/org.libreoffice.kde.metainfo.xml
%endif

%langpack -m -h -l ru -s ru-lebedev -n Russian
%langpack    -h -l be -s be -n Belorussian
%langpack -m -h -l de -s de -n German
%langpack -m -h -l fr -s fr -n French
%langpack -m -h -l uk -s uk -n Ukrainian
%langpack       -l pt-BR -s pt -n Brazilian Portuguese
%langpack -m -h -l es -s es -n Espanian
%langpack       -l kk -s kk -n Kazakh
%langpack       -l tr       -n Turkish
%langpack    -h -l tt -s tt -n Tatar
%langpack -m -h -l el -s el -n Greek
%langpack       -l uz -s uz -n Uzbek
%langpack       -l ky -s ky -n Kyrgyz

%files -n libreofficekit
#_typelibdir/LOKDocView-*.typelib
%_libdir/liblibreofficekitgtk.so

%files -n libreofficekit-devel
#_girdir/LOKDocView-*.gir
%_includedir/LibreOfficeKit

%changelog
* Thu Apr 30 2026 Andrey Cherepanov <cas@altlinux.org> 26.2.3.2-alt1
- New version.

* Mon Apr 27 2026 Andrey Cherepanov <cas@altlinux.org> 26.2.2.2-alt5
- libreoffice: require libreoffice-extension to avoid missing parts on update.

* Fri Apr 24 2026 Fr. Br. George <george@altlinux.org> 26.2.2.2-alt4
- Split to main and Java-free core packages.

* Mon Apr 13 2026 Andrey Cherepanov <cas@altlinux.org> 26.2.2.2-alt3
- Removed open and valgrind from requirements (ALT #58645).
- Did not split to main and core packages.

* Wed Apr 08 2026 Andrey Cherepanov <cas@altlinux.org> 26.2.2.2-alt2
- Fix some post-install unowned files (ALT #58587) (thanks andy@).
- Exclude core part without Java (ALT #58514).

* Fri Mar 27 2026 Andrey Cherepanov <cas@altlinux.org> 26.2.2.2-alt1
- New version.

* Fri Feb 27 2026 Andrey Cherepanov <cas@altlinux.org> 26.2.1.2-alt1
- New version.
- Fixed insert audio files using qt6/kf6 VCL (ALT #57028).

* Mon Feb 23 2026 Andrey Cherepanov <cas@altlinux.org> 26.2.0.3-alt3
- Complete GUI translation on Russian (thanks Olesya Gerasimenko).

* Mon Feb 08 2026 Ilya Sorochan <k0tran@altlinux.org> 26.2.0.3-alt2
- Add `-flax-vector-conversions` flag for loongarch64 (Fixes FTBFS).

* Wed Feb 04 2026 Andrey Cherepanov <cas@altlinux.org> 26.2.0.3-alt1
- New version.

* Tue Jan 13 2026 Andrey Cherepanov <cas@altlinux.org> 25.8.4.2-alt3
- Returned build Qt6 and KDE6.

* Thu Jan 08 2026 Andrey Cherepanov <cas@altlinux.org> 25.8.4.2-alt2
- Packaged libreoffice-qt and libreoffice-kde without its major version.
- Built with Qt5 and KDE5 (ALT #57028).

* Fri Dec 19 2025 Andrey Cherepanov <cas@altlinux.org> 25.8.4.2-alt1
- New version (closes: CVE-2025-14714).

* Wed Dec 17 2025 Andrey Cherepanov <cas@altlinux.org> 25.8.3.2-alt3
- FTBFS: built with Java 17 because Java 25 does not support SecurityManager
  for bundled hsqldb.

* Tue Nov 25 2025 Ivan A. Melnikov <iv@altlinux.org> 25.8.3.2-alt2
- Drop loongarch64-specific patch 501 from spec, as upstream is
  patching skia in the same way now (fixes building on loongarch64).

* Wed Nov 19 2025 Andrey Cherepanov <cas@altlinux.org> 25.8.3.2-alt1
- New version.
- Fixed typo in libreoffice-kde6 summary (ALT #56930).

* Mon Oct 27 2025 Andrey Cherepanov <cas@altlinux.org> 25.8.2.2-alt1
- New version.
- Renamed to libreoffice.

* Thu Sep 11 2025 Andrey Cherepanov <cas@altlinux.org> 25.2.6.2-alt1
- New version.
- Replaced application name by its role in desktop files.

* Thu Jul 17 2025 Andrey Cherepanov <cas@altlinux.org> 25.2.4.3-alt1
- New version.
- Enabled dbus support.
- Enabled skia support.

* Sat Jun 07 2025 Andrey Cherepanov <cas@altlinux.org> 24.8.7.2-alt1
- New version (fixes: CVE-2025-2866 PDF signature forgery with adbe.pkcs7.sha1 SubFilter)
- Complete Russian translation.

* Wed Apr 23 2025 Andrey Cherepanov <cas@altlinux.org> 24.8.6.2-alt1
- New version.

* Thu Apr 10 2025 Ivan A. Melnikov <iv@altlinux.org> 24.8.5.2-alt3
- Generate more full debuginfo
  + reduce optflags_debug to -g1 to fit into 4Gb payload limit.
- Enable mergelibs (gives measurable performance improvements
  on certain tests).
- Respect %%__nprocs.

* Sat Mar 08 2025 Andrey Cherepanov <cas@altlinux.org> 24.8.5.2-alt2
- Mention security fix in 24.8.5:
  + CVE-2025-1080 Macro URL arbitrary script execution

* Fri Feb 28 2025 Andrey Cherepanov <cas@altlinux.org> 24.8.5.2-alt1
- New version.

* Fri Jan 31 2025 Andrey Cherepanov <cas@altlinux.org> 24.8.4.2-alt1
- New version.
- Security fixes:
  + CVE-2024-12425 Path traversal leading to arbitrary .ttf file write
  + CVE-2024-12426 URL fetching can be used to exfiltrate arbitrary INI file values and environment variables

* Fri Dec 20 2024 Andrey Cherepanov <cas@altlinux.org> 24.8.3.2-alt1
- New version.

* Mon Dec 16 2024 Andrey Cherepanov <cas@altlinux.org> 24.2.7.2-alt1
- New version.
- Provide LibreOffice-still-qt5 and LibreOffice-still-kde5 to upgrade from KDE5.

* Tue Dec 10 2024 Andrey Cherepanov <cas@altlinux.org> 24.2.6.2-alt3
- Build with KDE6 (ALT #52386).
- Build with Turkish localization.

* Sat Nov 16 2024 Andrey Cherepanov <cas@altlinux.org> 24.2.6.2-alt2
- Remove wrong mime-type application/vnd.ms-word to fix open .doc from network shares.
- Use system libcmis.

* Thu Oct 03 2024 Andrey Cherepanov <cas@altlinux.org> 24.2.6.2-alt1
- New version.
- Security fixes (for 24.8.0/24.2.5):
  + CVE-2024-7788 Signatures in "repair mode" should not be trusted

* Fri Aug 23 2024 Andrey Cherepanov <cas@altlinux.org> 24.2.5.2-alt1
- New version.
- Security fixes:
  + CVE-2024-6472 Ability to trust not validated macro signatures removed in high security mode
  + CVE-2024-5261 TLS certificate are not properly verified when utilizing LibreOfficeKit
  + CVE-2024-3044 Graphic on-click binding allows unchecked script execution.

* Wed Jul 10 2024 Andrey Cherepanov <cas@altlinux.org> 24.2.4.2-alt1
- New version.

* Sun May 12 2024 Andrey Cherepanov <cas@altlinux.org> 7.6.7.2-alt1
- New version.

* Wed Apr 24 2024 Andrey Cherepanov <cas@altlinux.org> 7.6.6.3-alt1
- New version.

* Sat Feb 24 2024 Andrey Cherepanov <cas@altlinux.org> 7.6.5.2-alt1
- New version.

* Thu Feb 01 2024 Andrey Cherepanov <cas@altlinux.org> 7.6.4.1-alt1
- New version.
- Built with GTK4 VCL and unify build flags with Fedora.

* Mon Dec 18 2023 Andrey Cherepanov <cas@altlinux.org> 7.5.9.2-alt2
- FTBFS: fixed build with libxml2 2.12 (ALT #48841).

* Thu Dec 07 2023 Andrey Cherepanov <cas@altlinux.org> 7.5.9.2-alt1
- New version (fixes CVE-2023-6186 and CVE-2023-6185).

* Wed Dec 06 2023 Andrey Cherepanov <cas@altlinux.org> 7.5.8.2-alt4
- Added Kyrgyz localization.

* Wed Nov 22 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 7.5.8.2-alt3
- NMU: rebuilt with libcmis-0.6

* Wed Nov 22 2023 Andrey Cherepanov <cas@altlinux.org> 7.5.8.2-alt2
- FTBFS: fixed build with icu 74 (https://bugs.documentfoundation.org/show_bug.cgi?id=158108)
- Reduced log output.

* Sat Nov 04 2023 Andrey Cherepanov <cas@altlinux.org> 7.5.8.2-alt1
- New version.

* Fri Sep 29 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 7.5.7.1-alt3
- Support LoongArch architecture (lp64d ABI).

* Fri Sep 29 2023 Andrey Cherepanov <cas@altlinux.org> 7.5.7.1-alt2
- Rebuilt with bundled mdds and orcus.

* Wed Sep 27 2023 Andrey Cherepanov <cas@altlinux.org> 7.5.7.1-alt1
- New version.
- Add LibreOffice-still-langpack-uz with Uzbek localization.

* Tue Sep 12 2023 Andrey Cherepanov <cas@altlinux.org> 7.5.6.2-alt2
- Complete Russian localization of interface.

* Tue Sep 12 2023 Andrey Cherepanov <cas@altlinux.org> 7.5.6.2-alt1
- New version.

* Mon Aug 21 2023 Andrey Cherepanov <cas@altlinux.org> 7.5.5.2-alt1
- New version.

* Sun Jul 30 2023 Andrey Cherepanov <cas@altlinux.org> 7.4.7.2-alt2
- Fixed build with Boost 1.82.

* Wed May 31 2023 Andrey Cherepanov <cas@altlinux.org> 7.4.7.2-alt1
- New version (ALT #46320).
- Security fixes:
  + CVE-2023-2255 Remote documents loaded without prompt via IFrame
  + CVE-2023-0950 Array Index UnderFlow in Calc Formula Parsing
- Built with KDE5 support.

* Sun Mar 26 2023 Andrey Cherepanov <cas@altlinux.org> 7.4.6.2-alt1
- New version.

* Thu Feb 02 2023 Andrey Cherepanov <cas@altlinux.org> 7.4.5.1-alt1
- New version.

* Tue Dec 06 2022 Andrey Cherepanov <cas@altlinux.org> 7.3.7.2-alt2
- Required spell dictionary for langpack (ALT #42242).

* Sat Nov 05 2022 Andrey Cherepanov <cas@altlinux.org> 7.3.7.2-alt1
- New version.

* Fri Oct 14 2022 Andrey Cherepanov <cas@altlinux.org> 7.3.6.2-alt2
- Security fixes in 7.3.6.2:
  + CVE-2022-3140 Macro URL arbitrary script execution

* Wed Sep 14 2022 Andrey Cherepanov <cas@altlinux.org> 7.3.6.2-alt1
- New version.

* Sun Aug 21 2022 Andrey Cherepanov <cas@altlinux.org> 7.3.5.2-alt1
- New version.
- Security fixes:
  + CVE-2022-26305 Execution of Untrusted Macros Due to Improper Certificate Validation
  + CVE-2022-26306 Static Initialization Vector Allows to Recover Passwords for Web Connections Without Knowing the Master Password
  + CVE-2022-26307 Weak Master Keys

* Fri May 27 2022 Andrey Cherepanov <cas@altlinux.org> 7.2.7.2-alt1
- New version.

* Mon Mar 14 2022 Andrey Cherepanov <cas@altlinux.org> 7.2.6.2-alt1
- New version.

* Wed Feb 23 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 7.2.5.2-alt4
- NMU: - adapted spec for kf5-kcoreaddons-devel-5.91.0-alt1 and kf5-kcoreaddons-devel-5.90.0-alt1
- Security fixes:
  + CVE-2021-25636 Incorrect trust validation of signature with ambiguous KeyInfo children

* Wed Feb 23 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 7.2.5.2-alt3
- NMU: Fix build (ftbfs)

* Fri Feb 04 2022 Andrey Cherepanov <cas@altlinux.org> 7.2.5.2-alt2
- Fix id and add icons to appdata metainfo.

* Wed Feb 02 2022 Andrey Cherepanov <cas@altlinux.org> 7.2.5.2-alt1
- New Still version.
- Add information about Still version and package names to appdata files.

* Fri Jan 14 2022 Fr. Br. George <george@altlinux.ru> 7.1.8.1-alt2.1
- Use bundled liborcus

* Fri Jan 14 2022 Andrey Cherepanov <cas@altlinux.org> 7.1.8.1-alt2
- Use bundled mdds-1.5.

* Mon Dec 06 2021 Andrey Cherepanov <cas@altlinux.org> 7.1.8.1-alt1
- New version.

* Mon Nov 22 2021 Andrey Cherepanov <cas@altlinux.org> 7.1.7.2-alt2
- Exclude libvclplug_gtk3_kde5lo.so from LibreOffice-still-gtk3.

* Fri Nov 05 2021 Andrey Cherepanov <cas@altlinux.org> 7.1.7.2-alt1
- New version.

* Mon Sep 13 2021 Andrey Cherepanov <cas@altlinux.org> 7.1.6.2-alt1
- New version.
- Security fixes:
  + CVE-2021-25633 Content Manipulation with Double Certificate Attack
  + CVE-2021-25634 Timestamp Manipulation with Signature Wrapping
  + CVE-2021-25635 Content Manipulation with Certificate Validation Attack

* Fri Aug 20 2021 Andrey Cherepanov <cas@altlinux.org> 7.1.5.2-alt1
- New version.
- Use gtk3-kde5 vcl instead of kde5 due to incorrect icon scaling.

* Wed May 19 2021 Andrey Cherepanov <cas@altlinux.org> 7.0.6.2-alt2
- Build with bundled liborcus-0.15.

* Mon May 17 2021 Andrey Cherepanov <cas@altlinux.org> 7.0.6.2-alt1
- New version.

* Tue May 04 2021 Andrey Cherepanov <cas@altlinux.org> 7.0.5.2-alt3
- Use python3 autoreq for python scripts.

* Fri Apr 09 2021 Andrey Cherepanov <cas@altlinux.org> 7.0.5.2-alt2
- docxexport: export russianUpper/russianLower numbering.

* Mon Mar 29 2021 Andrey Cherepanov <cas@altlinux.org> 7.0.5.2-alt1
- New version.
- Use -fPIC for build on any architectures.

* Thu Feb 18 2021 Ivan A. Melnikov <iv@altlinux.org> 7.0.4.2-alt2
- Remove BR: openjdk-devel from non-java builds.

* Fri Feb 05 2021 Andrey Cherepanov <cas@altlinux.org> 7.0.4.2-alt1
- New version.
- Add Greek languagepack (ALT #39636).
- Use all available processors for build.

* Mon Nov 09 2020 Ivan A. Melnikov <iv@altlinux.org> 6.4.7.2-alt3
- Get rid of java-related BRs in non-java builds.
- Fix build on mipsel.

* Sun Nov 08 2020 Andrey Cherepanov <cas@altlinux.org> 6.4.7.2-alt2
- Do not provide liblibreofficekitgtk.so (ALT #39219).

* Fri Oct 23 2020 Andrey Cherepanov <cas@altlinux.org> 6.4.7.2-alt1
- New Still version 6.4.7.2.

* Sat Sep 05 2020 Andrey Cherepanov <cas@altlinux.org> 6.4.6.2-alt2
- Package KDE5-specific libraries to LibreOffice-still-kde5.

* Fri Aug 21 2020 Andrey Cherepanov <cas@altlinux.org> 6.4.6.2-alt1
- New version 6.4.6.2 (Still).

* Fri Aug 14 2020 Andrey Cherepanov <cas@altlinux.org> 6.4.5.2-alt2
- Remove deprecated package LibreOffice-still-gtk2.

* Fri Aug 07 2020 Andrey Cherepanov <cas@altlinux.org> 6.4.5.2-alt1
- New version 6.4.5.2 (Still).
- Fixed:
  + CVE-2020-12801 Crash-recovered MSOffice encrypted documents defaulted to not to using encryption on next save
  + CVE-2020-12802 remote graphics contained in docx format retrieved in 'stealth mode'
  + CVE-2020-12803 XForms submissions could overwrite local files
- Install mime package bundle for LibreOffice MIME types.

* Mon Jul 27 2020 Andrey Bychkov <mrdrew@altlinux.org> 6.3.6.2-alt4
- Rebuild with dconf enabled (Closes: 38753).

* Wed May 27 2020 Andrey Cherepanov <cas@altlinux.org> 6.3.6.2-alt3
- Remove deprecated libtelepathy-devel.

* Thu May 14 2020 Andrey Cherepanov <cas@altlinux.org> 6.3.6.2-alt2
- Put libreoffice- prefix to icons and desktop files (ALT #38480).

* Thu Apr 30 2020 Andrey Cherepanov <cas@altlinux.org> 6.3.6.2-alt1
- New version 6.3.6.2 (Still).

* Fri Feb 28 2020 Andrey Cherepanov <cas@altlinux.org> 6.3.5.2-alt1
- New version 6.3.5.2 (Still).
- Set MOZILLA_CERTIFICATE_FOLDER as default Firefox profile.
- Remove version from Name and icon names in desktop files.
- Remove old scalable icons.
- Do not use version suffux for icons and in desktop files.

* Wed Dec 04 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.8.2-alt2
- Rebuilt with mdds-1.5.0 and boost-1.71.0.

* Mon Oct 28 2019 Andrey Cherepanov <cas@altlinux.org> 6.2.8.2-alt1
- New version 6.2.8.2 (Still).

* Thu Sep 19 2019 Andrey Cherepanov <cas@altlinux.org> 6.2.7.1-alt1
- New version 6.2.7.1 (Still).
- Fixed:
  + CVE-2019-9849 Disabled fetching remote bullet graphics in 'stealth mode'
  + CVE-2019-9850 Fixed insufficient URL validation that allowed LibreLogo script execution
  + CVE-2019-9851 Fixed LibreLogo global-event script execution issue
  + CVE-2019-9852 Fixed insufficient URL encoding flaw in allowed script location check
  + CVE-2019-9854 Fixed unsafe URL assembly flaw
  + CVE-2019-9855 Fixed path equivalence handling flaw

* Tue Aug 13 2019 Andrey Cherepanov <cas@altlinux.org> 6.2.6.2-alt1
- New version 6.2.6.2 (Still).
- Fixed:
  + CVE-2019-9848 Fixed an arbitrary script execution via LibreLogo

* Sun Jun 16 2019 Andrey Cherepanov <cas@altlinux.org> 6.1.6.3-alt3
- Require pentaho-reporting-flow-engine only if build with java
  support.

* Fri Jun 14 2019 Andrey Cherepanov <cas@altlinux.org> 6.1.6.3-alt2
- Requires pentaho-reporting-flow-engine for queries in Base.

* Sun May 05 2019 Andrey Cherepanov <cas@altlinux.org> 6.1.6.3-alt1
- New version 6.1.6.3 (Still).

* Mon Apr 29 2019 Andrey Cherepanov <cas@altlinux.org> 6.1.6.2-alt1
- New version 6.1.6.2 (Still).

* Sat Mar 09 2019 Andrey Cherepanov <cas@altlinux.org> 6.1.5.2-alt1
- New version 6.1.5.2 (Still).

* Fri Feb 08 2019 Andrey Cherepanov <cas@altlinux.org> 6.0.7.3-alt1
- New version 6.0.7.3 (Still).
- Link with bundled poppler-0.66.

* Tue Oct 23 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.7.2-alt1
- New version 6.0.7.2 (Still).
- Unexpected abort fixed (bug #35444) by mrdrew@.

* Mon Oct 08 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.7.1-alt1
- New version 6.0.7.1 (Still).

* Tue Sep 18 2018 Fr. Br. George <george@altlinux.ru> 6.0.6.2-alt2
- Build with bundled old mdds/orcus

* Fri Sep 07 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.6.2-alt1
- New version 6.0.6.2 (Still).
- Disable CoinMP.
- Use simplified scalable desktop icons from LibreOffice 6.1.

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.4.7.2-alt1.1
- NMU: rebuilt with boost-1.67.0

* Fri May 18 2018 Andrey Cherepanov <cas@altlinux.org> 5.4.7.2-alt1
- New version 5.4.7.2 (Still).

* Wed May 09 2018 Andrey Cherepanov <cas@altlinux.org> 5.4.7.1-alt1
- New package LibreOffice-still with Still version of LibreOffice for Sisyphus.

* Tue May 08 2018 Andrey Cherepanov <cas@altlinux.org> 5.4.7.1-alt0.M80P.1
- New version 5.4.7.1 (Still).

* Wed Mar 28 2018 Andrey Cherepanov <cas@altlinux.org> 5.4.6.2-alt0.M80P.1
- New version 5.4.6.2 (Still) (ALT #34502)
- Return Oxygen icon theme from LibreOffice 5.3.

* Thu Nov 30 2017 Fr. Br. George <george@altlinux.ru> 5.4.3.2-alt1
- Update to 5.4.3.2

* Mon Nov 27 2017 Fr. Br. George <george@altlinux.ru> 5.3.7.2-alt0.M80P.1
- Version up

* Mon Nov 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.4.2.2-alt2
- Rebuilt with libCoinMP-1.8.3.

* Sat Nov 11 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.7.2-alt0.M80P.1
- New stable version 5.3.7.2

* Thu Oct 05 2017 Fr. Br. George <george@altlinux.ru> 5.4.2.2-alt1
- Update to 5.4.2.2

* Tue Sep 12 2017 Fr. Br. George <george@altlinux.ru> 5.4.1.2-alt1
- Update to 5.4.1.2

* Mon Jul 31 2017 Fr. Br. George <george@altlinux.ru> 5.4.0.3-alt1
- Update to 5.4.0.3

* Wed Jun 07 2017 Fr. Br. George <george@altlinux.ru> 5.3.3.2-alt2
- Enable languagetool extension

* Wed May 17 2017 Fr. Br. George <george@altlinux.ru> 5.3.3.2-alt1
- Update to 5.3.3.2
- Build SDK

* Wed Apr 12 2017 Fr. Br. George <george@altlinux.ru> 5.3.2.2-alt1
- Update to 5.3.2.2

* Thu Feb 09 2017 Fr. Br. George <george@altlinux.ru> 5.3.0.3-alt1
- Update to 5.3.0.3
- Change versioning scheme

* Mon Oct 17 2016 Fr. Br. George <george@altlinux.ru> 5.2-alt4
- Update to 5.2.3.1

* Wed Aug 24 2016 Fr. Br. George <george@altlinux.ru> 5.2-alt3
- Update to 5.2.1.1

* Tue Jul 19 2016 Fr. Br. George <george@altlinux.ru> 5.2-alt2
- Update to 5.2.0.2
- (closes: #31953)

* Mon Jul 11 2016 Fr. Br. George <george@altlinux.ru> 5.2-alt1
- Update to 5.2.0.1

* Thu Jun 02 2016 Fr. Br. George <george@altlinux.ru> 5.1-alt4
- Update to 5.1.3.2
- Fix buildreqs

* Thu Mar 31 2016 Fr. Br. George <george@altlinux.ru> 5.1-alt3
- Update to 5.1.2.1
- Build with system python again

* Thu Mar 10 2016 Fr. Br. George <george@altlinux.ru> 5.1-alt2
- Update to 5.1.1.3
- Build without forky (turns out -XX:ParallelGCThreads=2 fixes OOM)

* Wed Feb 10 2016 Fr. Br. George <george@altlinux.ru> 5.1-alt1
- Update to 5.1.1.1
- Build with internal Python3

* Wed Nov 04 2015 Fr. Br. George <george@altlinux.ru> 5.0-alt2
- Update to 5.0.3.2

* Wed Sep 16 2015 Fr. Br. George <george@altlinux.ru> 5.0-alt1
- Update to 5.0.3.1
- Rename package
- Remove -standalone package

* Tue Feb 24 2015 Fr. Br. George <george@altlinux.ru> 4.4-alt2
- Update to 4.4.1.2

* Thu Feb 05 2015 Fr. Br. George <george@altlinux.ru> 4.4-alt1
- Update to 4.4.0.3
- Turn tt and be langpacks on

* Mon Dec 01 2014 Fr. Br. George <george@altlinux.ru> 4.3-alt3
- Update to 4.3.5.1

* Wed Nov 19 2014 Fr. Br. George <george@altlinux.ru> 4.3-alt2
- Update to 4.3.4.1

* Wed Nov 12 2014 Fr. Br. George <george@altlinux.ru> 4.3-alt1
- Update to 4.3.3.2
- Provide loffice binary (Closes: #30044)
- Reqiure gst-libav (Closes: #30015)

* Fri Jun 06 2014 Alexey Shabalin <shaba@altlinux.ru> 4.3-alt0.beta2.buildfix1
- 4.3.0.0.beta2-buildfix1
- update BR:
- switch to librevenge-based import libs

* Wed Apr 30 2014 Fr. Br. George <george@altlinux.ru> 4.2-alt3
- Version up to 4.2.4.1

* Wed Apr 16 2014 Fr. Br. George <george@altlinux.ru> 4.2-alt2
- Version up to 4.2.3.3

* Wed Mar 19 2014 Fr. Br. George <george@altlinux.ru> 4.2-alt1
- Version up

* Tue Feb 04 2014 Fr. Br. George <george@altlinux.ru> 4.1-alt9
- Merge -full package into general one
- Buld with help (closes: #29735)
- Require gst1.0 plugins to install (closes: #29782)

* Thu Dec 26 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt8
- Build with --enable-release-build

* Thu Dec 19 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt7
- Version up to officially corporative stable 4.1.4.2
- Disable applied patches

* Mon Nov 25 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt6
- Version up to officially stable 4.1.3.2
- More accurate forky utilization

* Tue Oct 01 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt5
- Version up to 4.1.2.3

* Fri Sep 27 2013 Yuri N. Sedunov <aris@altlinux.org> 4.1-alt4
- rebuild against libharfbuzz-icu

* Wed Sep 04 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt3
- Version up to 4.1.1.2
- Refresh FC patchset
- Un-hardcode /tmp usage (Closes: 29267)

* Tue Aug 13 2013 Alexey Shabalin <shaba@altlinux.ru> 4.1-alt2
- fixed gnome file list
- fixed kde file list
- drop use gnome-open in gnome-open-url.sh
- build with gstreamer-1.0
- build with system libraries (libodfgen,libcdr,libmspub,libmwaw,libvisio,libcmis,libexttextcat)
- build with system jar files
- changed configure options --with-system-* to --with-system-libs

* Tue Jul 30 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt1
- Version up to 4.1.0.4
- Renew FC patchset (previous ones are pushed to upstream)

*  Wed May 15 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt8
- Version up to 4.0.3.3
- Drop some RH patches accepted by upstream

* Wed Apr 24 2013 Sergey V Turchin <zerg@altlinux.org> 4.0-alt7.1
- NMU: rebuilt with new poppler

* Mon Apr 22 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt7
- Closes: 28883
- Drop some internal libraries build

* Thu Apr 18 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt6
- Version up to 4.0.2.2
- Incoprporate useful RH patches

* Thu Mar 21 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt5
- Introduce Kazakh locale
- Fix common binary displacement

* Tue Mar 19 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt4
- Fix conflicts with LO3
- Introduce "full" package (without langpacks and GNOME/KDE stuff)

* Wed Mar 06 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt3
- Update to 4.0.2.1
- Introduce extra extensions
- Separate %name-standalone and %name-integrated packages
- Introduce %name-mimetype

* Tue Mar 05 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt2
- Separate KDE4 plugins
- Apply Firefox certificates import patch

* Tue Feb 19 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt1
Initial test build

