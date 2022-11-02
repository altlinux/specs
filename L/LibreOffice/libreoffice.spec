# 7.4.2.3
%def_without python
%def_with parallelism
%def_without fetch
%def_enable lto
%def_enable dconf

# enable kde5 UI
%def_enable kf5

%ifarch mipsel
%def_without java
%else
%def_with java
%endif
%if_enabled kf5
%def_enable qt5
%else
%def_disable qt5
%endif
%def_disable mergelibs

Name: LibreOffice
%define hversion 7.4
%define urelease 2.3
Version: %hversion.%urelease
%define uversion %version.%urelease
%define lodir %_libdir/%name
%define uname libreoffice
%define conffile %_sysconfdir/sysconfig/%uname
Release: alt1
Summary: LibreOffice Productivity Suite
License: MPL-2.0
Group: Office
URL: http://www.libreoffice.org

Requires: %name-integrated = %EVR
Requires: %name-common = %EVR
Requires: %name-extensions = %EVR
%if_with java
Requires: libreoffice-languagetool
%endif

Provides: %name-full = %EVR
Provides: libreoffice = %EVR
Obsoletes: libreoffice < 3.99
Obsoletes: %name-full < %EVR

%define with_lang en-US ru be de fr uk pt-BR es kk tt
Requires: gst-libav

Source:         libreoffice-%version.tar.xz
Source1:        libreoffice-dictionaries-%version.tar.xz
Source2:        libreoffice-help-%version.tar.xz
Source3:        libreoffice-translations-%version.tar.xz

Source10:       libreoffice-ext_sources.%version.tar
Source100:      forky.c
Source200:      key.gpg
Source300:      libreoffice.unused

## FC patches
Patch1: FC-0001-don-t-suppress-crashes.patch
Patch2: FC-0001-disble-tip-of-the-day-dialog-by-default.patch
Patch3: FC-0001-Resolves-rhbz-1432468-disable-opencl-by-default.patch
Patch4: FC-0001-Revert-tdf-101630-gdrive-support-w-oAuth-and-Drive-A.patch
Patch5: FC-0001-disable-libe-book-support.patch

## Long-term FC patches

## ALT patches
Patch401: alt-001-MOZILLA_CERTIFICATE_FOLDER.patch
Patch402: alt-002-tmpdir.patch
#Patch403: alt-003-skia-freetype-2.11.patch
Patch404: alt-004-shortint.patch
Patch405: alt-005-svg-icons-1.patch
Patch406: alt-006-svg-icons-2.patch
Patch407: alt-007-svg-icons-3.patch

Patch500: alt-010-mips-fix-linking-with-libatomic.patch

# content of patch shared to Weblate-LibreOffice by @NeuroFreak
Patch600: LibreOffice-7.3.3.2-update-russian-translation.patch

%set_verify_elf_method unresolved=relaxed
%add_findreq_skiplist %lodir/share/config/webcast/*
%add_findreq_skiplist %lodir/sdk/examples/python/toolpanel/toolpanel.py 
%add_findreq_skiplist %lodir/sdk/classes
%add_findreq_skiplist %lodir/sdk/docs
%add_findreq_skiplist %lodir/sdk/idl
%add_findreq_skiplist %lodir/sdk/include
%filter_from_requires /com[.]sun[.]/d
%add_python3_req_skip pyuno strings

# Automatically added by buildreq on Wed Feb 13 2019
# optimized out: ant-lib apache-commons-logging at-spi2-atk bash4 boost-devel boost-devel-headers cppunit dconf fontconfig fontconfig-devel gcc-c++ glib-networking glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gobject-introspection gobject-introspection-devel gstreamer1.0-devel hamcrest-core icu-utils java java-headless javapackages-tools javazi kf5-kconfig-devel kf5-kcoreaddons-devel libGL-devel libICE-devel libSM-devel libX11-devel libXext-devel libXinerama-devel libXrandr-devel libXrender-devel libXt-devel libat-spi2-core libatk-devel libatk-gir-devel libboost_numpy3-1.67.0 libboost_python3-1.67.0 libcairo-devel libcairo-gobject libcairo-gobject-devel libclucene-contribs-lib libclucene-core libclucene-shared libcrypt-devel libcurl-devel libe-book libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgdk-pixbuf-gir-devel libgio-devel libglvnd-devel libgpg-error libgpg-error-devel libgraphite2-devel libgst-plugins1.0 libgtk+3-devel libharfbuzz-devel libharfbuzz-icu libicu-devel libltdl7-devel libnspr-devel libnss-devel libpango-devel libpango-gir-devel libpng-devel libpoppler-devel libpq-devel libqt5-core libqt5-gui libqt5-network libqt5-widgets libqt5-x11extras librasqal-devel librevenge-devel libsasl2-3 libstdc++-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-egl libxcb-devel libxml2-devel libxmlsec1-devel libxmlsec1-nss libxslt-devel pentaho-libxml perl pkg-config python-base python-modules python-modules-compiler python-modules-distutils python3 python3-base python3-module-lxml qt5-base-devel raptor2-devel sac sh4 termutils wayland-devel xml-common xml-utils xorg-proto-devel xz zlib-devel
BuildRequires: boost-filesystem-devel boost-locale-devel boost-signals-devel cppunit-devel doxygen flex fontforge fonts-ttf-liberation git-core gperf graphviz gst-plugins1.0-devel imake libGConf libabw-devel libavahi-devel libbluez-devel libcdr-devel libclucene-core-devel libcmis-devel libcups-devel libdbus-devel libe-book-devel libepoxy-devel libepubgen-devel libetonyek-devel libexpat-devel libexttextcat-devel libfreehand-devel libglm-devel libgpgme-devel libgtk+2-devel libgtk+3-gir-devel libhunspell-devel libhyphen-devel libjpeg-devel liblangtag-devel liblcms2-devel libldap-devel liblpsolve-devel libmspub-devel libmwaw-devel libmysqlclient-devel libmythes-devel libneon-devel libnumbertext-devel libodfgen-devel liborcus-devel libpagemaker-devel libpoppler-cpp-devel libqxp-devel libredland-devel libsane-devel libssl-devel libstaroffice-devel libunixODBC-devel libvisio-devel libwpd10-devel libwpg-devel libwps-devel libxmlsec1-nss-devel libzmf-devel mdds-devel postgresql-devel unzip xorg-cf-files xsltproc zip

# 6.4
BuildRequires: libeot-devel libqrcodegen-cpp-devel

# 7.1
BuildRequires: libbox2d-devel

# 7.2
BuildRequires: libpixman-devel

# 7.3
BuildRequires: libcuckoo-devel libopenjpeg2.0-devel libabseil-cpp-devel

# 7.4
BuildRequires: libwebp-devel libtiff-devel

%if_with java
BuildRequires: java-devel >= 9.0.0 junit ant bsh pentaho-reporting-flow-engine 
%endif

%if_enabled qt5
BuildRequires: qt5-base-devel qt5-svg-devel qt5-x11extras-devel 
BuildRequires: libxcbutil-icccm-devel
BuildRequires: libpixman-devel
%endif

%if_enabled kf5
BuildRequires: kf5-ki18n-devel kf5-kio-devel kf5-kwindowsystem-devel
%endif

%if_without python
BuildRequires: python3-dev
%endif

%if_enabled dconf
BuildRequires: libdconf-devel
%endif

%description
LibreOffice is a productivity suite that is compatible with other major
office suites.

This package provides maximum possible installation of %name along winth
other office packages, except of language packs and GNOME/KDE bindings.

%package common
Summary: Basic installation of %name
Group: Office
AutoReqProv: yes, noshell, nopython
%description common
Common part of %name that does not interfere with other packages

%package integrated
Summary: Binaries, icons and desktop files for %name
Group: Office
Provides: %uname = %EVR
Requires: %name-common = %EVR
%if_with java
Requires: pentaho-reporting-flow-engine
%endif
Provides: %name-mimetypes
%description integrated
Wrapper scripts, icons and desktop files for running %name

%package gtk3
Summary: GTK3 Extensions for %name
Group:  Office
Requires: %uname = %EVR
Requires: %name-common = %EVR
Provides: %name-gnome = %EVR
Obsoletes: %name-gnome %name-gtk %name-gtk2
%description gtk3
GTK3 extensions for %name

%if_enabled qt5
%package qt5
Summary: Qt5 Extensions for %name
Group:  Office
Requires: %uname = %EVR
Requires: %name-common = %EVR
%description qt5
qt5 extensions for %name
%endif

%if_enabled kf5
%package kde5
Summary: KDE5 Extensions for %name
Group:  Office
Requires: %uname = %EVR
Requires: %name-common = %EVR
Provides: %name-kde = %EVR
Provides: %name-kf5 = %EVR
%description kde5
KDE5 extensions for %name

%package gtk3-kde5
Summary: GTK3 Extensions for %name with KDE5 filepicker
Group:  Office
Requires: %uname = %EVR
Requires: %name-common = %EVR
%description gtk3-kde5
GTK3 Extensions for %name with KDE5 filepicker
%endif

%package -n libreofficekit
Summary: A library providing access to LibreOffice functionality
Group: Graphical desktop/GNOME
License: MPL-2.0
%description -n libreofficekit
LibreOfficeKit can be used to access LibreOffice functionality
through C/C++, without any need to use UNO.

%package -n libreofficekit-devel
Summary: Development files for libreofficekit
Group: Development/GNOME and GTK+
License: MPL-2.0
%description -n libreofficekit-devel
The libreofficekit-devel package contains libraries and header files for
developing applications that use libreofficekit.


%package extensions
Summary: Additional extensions for %name
Group:  Office
Requires: %uname = %EVR
AutoReqProv: yes, noshell, nopython
%description extensions
Additional extensions for %name.
One can choose either to install this package at once,
or to download and install (possibly newer) extensions manually.

%package sdk
Group: Development/Other
Summary: Software Development Kit for LibreOffice

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

%package postgresql
Group:  Office
Summary: PostgrSQL connector for LibreOffice
%description postgresql
%summary

# TODO redefine %%lang adding corr langpack
# define macro for quick langpack description
%define langpack(l:n:mhs:) \
%define lang %{-l:%{-l*}}%{!-l:%{error:Language code not defined}} \
%define lng %{-s:%{-s*}}%{!-s:%{lang}} \
%define pkgname langpack-%{lang} \
%define langname %{-n:%{-n*}}%{!-n:%{error:Language name not defined}} \
\
%package %{pkgname} \
Summary: %{langname} language pack for %name \
Group:  Office \
Requires: %uname = %EVR \
%{-m:Requires: mythes-%lng} \
%{-h:Requires: hyphen-%lng} \
%description %{pkgname} \
Provides additional %{langname} translations and resources for %name. \
\
%files %{pkgname} -f %{lang}.lang \
%{nil}

%prep
%setup -q -n libreoffice-%version -a10 -b1 -b2 -b3

## FC apply patches
#patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
#patch5 -p1

## Long-term FC patches applying

## ALT apply patches
%patch401 -p0
%patch402 -p1
%patch404 -p1
%patch405 -p1
##patch406 -p1 # Doesn't compile
%patch407 -p1

%patch500 -p0
# Patch with russian translation update
##patch600 -p1

# TODO move officebean to SDK or separate package
# Hack in -Wl,-rpath=/usr/lib/jvm/jre-11-openjdk/lib
sed -i 's@JAVA_HOME/lib/ -ljawt@JAVA_HOME/lib/ -Wl,-rpath=/usr/lib/jvm/jre/lib -ljawt@' configure.ac

# Hack out lowercasing install_dirname
sed -i 's/\(^INSTALLDIRNAME=\).*/\1AC_PACKAGE_NAME/' configure.ac
sed -i 's/\(^add_wrapper.*"\)libreoffice-/\1%name-/
s/\(gid_Module_Optional_Xsltfiltersamples.*\)libreoffice-/\1%name-/' bin/distro-install-desktop-integration

%filter_from_requires /libjawt[.]so/d

# Choose right path to kcoreaddons_version.h
if [ -e "%_includedir/KF5/KCoreAddons/kcoreaddons_version.h" ]; then  
    sed -i -e 's|kf5_test_include="KF5/kcoreaddons_version.h"|kf5_test_include="KF5/KCoreAddons/kcoreaddons_version.h"|' configure.ac
fi

# Hack in ALT pixman path
sed -i 's@ -I@ -I /usr/include/pixman-1 -I@' canvas/Library_cairocanvas.mk

# Hack in python shebang
find . -name \*.py | while read F; do
    sed -i '1i#!/usr/bin/python3
/^#!.*python/d' "$F"
done

# Hack in proper LibreOffice PATH in libreofficekit
sed -i 's@/libreoffice/@/LibreOffice/@g' libreofficekit/Library_libreofficekitgtk.mk

# Hack hardcoded lsattr path
for f in `grep -rl '/usr/sbin/lsattr' *`; do sed -i 's@/usr/sbin/lsattr@/usr/bin/lsattr@g' $f; done

# Hack in MimeType=application/vnd.ms-visio.drawing.main+xml
grep -Fq "application/vnd.ms-visio.drawing.main+xml" sysui/desktop/menus/draw.desktop || sed -i 's@MimeType=@MimeType=application/vnd.ms-visio.drawing.main+xml;@' sysui/desktop/menus/draw.desktop

# hack hardcoded libodbc version
sed -i 's/libodbc.so.1/libodbc.so.2/g' connectivity/source/drivers/odbc/OFunctions.cxx

# Hack in relative ln -s
sed -i '/program.soffice/s/ln -sf \("*\$\)/ln --relative -sf $DESTDIR\1/' sysui/desktop/share/create_tree.sh
sed -i '/share.xdg/s/ln -sf \("*\$\)/cp -va $DESTDIR\1/' sysui/desktop/share/create_tree.sh
sed -i 's/ln -sf \("*\$\)/ln --relative -sf $DESTDIR\1/' bin/distro-install-sdk
sed -i 's/ln -sf \("*\$\)/ln --relative -sf $DESTDIR\1/' bin/distro-install-desktop-integration

rm -fr %name-tnslations/git-hooks

# Now create a config file
grep -r getenv * | sed -n 's/.*getenv *( *"\([^"]*\).*/\1/p' | sort -u | grep -E 'STAR_|SAL_|OOO_' > %name.config.ENV

sed -n '/# STAR_PROFILE_LOCKING_DISABLED/,/#.*JITC_PROCESSOR_TYPE_EXPORT/p' < desktop/scripts/soffice.sh > libreoffice.config
test -n "libreoffice.config"
sed -i '/# STAR_PROFILE_LOCKING_DISABLED/i\
test -r %conffile && . %conffile ||:
/# STAR_PROFILE_LOCKING_DISABLED/,/#.*JITC_PROCESSOR_TYPE_EXPORT/d' desktop/scripts/soffice.sh

%build
grep -l GCC_VERSION configure* | while read F; do
        sed -i '/GCC_VERSION=.*AWK/s/.*/GCC_VERSION="${_gcc_version%%%%.*}"/' $F
done
%ifarch mipsel
export CFLAGS="-Os --param ggc-min-expand=20 --param ggc-min-heapsize=32768 -g1"
export CXXFLAGS="$CFLAGS"
%endif

# XXX no "thin" LTO option in GCC!
sed -i 's/-flto=thin/-flto=jobserver/g' solenv/gbuild/platform/com_GCC_defs.mk

PARALLEL=$(nproc)

%ifarch ppc64le
# reduce excessive resource use
if [ "$PARALLEL" -gt 24 ] ; then
        PARALLEL=24
fi
%endif

export ac_cv_prog_LO_CLANG_CXX=""
export ac_cv_prog_LO_CLANG_CC=""
./autogen.sh \
        --prefix=%_prefix \
        --libdir=%_libdir \
        --with-vendor="ALT Linux Team" \
        %{subst_enable lto} \
        %{subst_enable mergelibs} \
        --enable-odk \
        --disable-firebird-sdbc \
        --disable-coinmp \
        --enable-dbus \
        --enable-evolution2 \
        --enable-gio \
        --enable-build-opensymbol \
        --enable-avahi \
        %{subst_with java} \
        --without-fonts \
        --without-myspell-dicts \
        \
        --with-external-dict-dir=%_datadir/myspell \
        --with-external-hyph-dir=%_datadir/hyphen \
        --with-external-thes-dir=%_datadir/mythes \
        --with-lang="%with_lang" \
        --with-external-tar=`pwd`/ext_sources \
        \
        --enable-ext-nlpsolver \
        --enable-ext-numbertext \
        --enable-ext-wiki-publisher \
  \
        --enable-release-build \
        --with-help \
  \
        %{subst_enable kf5} \
        %{subst_enable qt5} \
        %{subst_enable dconf} \
        --enable-gtk3 \
%if_enabled kf5 \
        --enable-gtk3-kde5 \
%endif
        --enable-introspection \
        --enable-cipher-openssl-backend \
        --enable-eot \
        --enable-formula-logger \
        --disable-zxing \
  \
%if_with parallelism
        --with-parallelism="$PARALLEL" \
%else   
        --without-parallelism \
%endif
%if_with python
        --enable-python=internal \
%endif
%if_with fetch
        --enable-fetch-external
%else
        --with-system-libs \
        --without-system-poppler \
        --without-system-dragonbox \
        --without-system-libfixmath \
        --disable-fetch-external
%endif

        ## --without-system-libtiff \

# TODO  --enable-vlc --enable-zxing --with-system-dragonbox

%make bootstrap

%if_with parallelism
export _JAVA_OPTIONS="-XX:ParallelGCThreads=4 $_JAVA_OPTIONS"
%endif

%make verbose=true build

export DESTDIR=../output
export KDEMAINDIR=/usr
export GNOMEDIR=/usr
export GNOME_MIME_THEME=hicolor
export PREFIXDIR=/usr
. ./bin/get_config_variables PRODUCTVERSIONSHORT PRODUCTVERSION SRCDIR WORKDIR PKG_CONFIG INSTDIR
export PRODUCTVERSIONSHORT PRODUCTVERSION SRCDIR WORKDIR PKG_CONFIG INSTDIR
$WORKDIR/CustomTarget/sysui/share/libreoffice/create_tree.sh

%install
unset RPM_PYTHON

%make DESTDIR=%buildroot INSTALLDIR=%lodir distro-pack-install
rm -f %buildroot%lodir/sdk/config.*

# XXX create versioned links (mentioned in desktop files)
ln -sr %buildroot%lodir/program/soffice %buildroot%_bindir/%uname%hversion
for F in `find %buildroot%_iconsdir/*/*/apps -type f -name "%name-*.*"`; do
        ll=`echo "$F" | sed "s@apps/%name-@apps/%uname%hversion-@"`
        ln -sr "$F" "$ll"
done

# Pick up LOO-generated file lists
for l in %with_lang; do
        ll="`echo "$l" | tr '-' '_'`"
        grep -v '^%%dir' file-lists/lang_${ll}_list.txt > $ll.lang
done

# Reuse upstream SDK plugin list
grep -vh '^%%dir' file-lists/sdk_doc_list.txt file-lists/sdk_list.txt | grep -vF '/sdk/config.' > files.sdk

# Reuse upstream "GNOME" plugin list
grep -vh '^%%dir' file-lists/gnome_list.txt > files.gtk3

# Create qt5 plugin list
find %buildroot%lodir -name "*qt5*"   | sed 's@^%buildroot@@' > files.qt5

# Create kde5 plugin list
find %buildroot%lodir -name "*kf5*" | sed 's@^%buildroot@@' > files.kde5

# Create gkt3-kde5 plugin list
find %buildroot%lodir -name "*kde5*" | sed 's@^%buildroot@@' > files.gtk3-kde5

grep %lodir file-lists/common_list.txt | \
        grep -Ev '/share/extensions/.|%lodir/sdk/.|so[.]debug$|libreofficekit' | \
        cat > files.common
# TODO lo5 or something for stand-alone

grep -v %lodir file-lists/common_list.txt | \
        sed -E 's@(/man/.*)[.]gz@\1.*@' | \
        cat > files.integrated

# Hack out "Education" category from Math
sed -i 's/Education;//' %buildroot%lodir/share/xdg/math.desktop

# TODO some other hack with sysui/desktop/ stuff ?
mkdir %buildroot%_datadir/mimelnk
install sysui/desktop/mimetypes/*.desktop %buildroot%_datadir/mimelnk/
find %buildroot%_iconsdir -type f -name LibreOffice-oasis-\* | while read File; do
        Name=`basename $File`
        Dir=`dirname $File`
        Ext=${File##*.}
        Target=""
        case $Name in
               LibreOffice-oasis-web.*) Target=text-html;;
               LibreOffice-oasis-drawing.*) Target=image-x-generic;;
               LibreOffice-oasis-document.*) Target=x-office-document;;
               LibreOffice-oasis-presentation.*) Target=x-office-presentation;;
               LibreOffice-oasis-spreadsheet.*) Target=x-office-spreadsheet;;
        esac
        test -z "$Target" || ln -sr "$Dir/$Name" "$Dir/$Target.$Ext"
done

# Config file
install -D libreoffice.config %buildroot%conffile

# Typelib/GIR stuff

install -D workdir/CustomTarget/sysui/share/libreofficedev/*.typelib %buildroot%_typelibdir/LOKDocView-0.1.typelib
install -D workdir/CustomTarget/sysui/share/libreofficedev/*.gir %buildroot%_girdir/LOKDocView-0.1.gir
ln -s --relative %buildroot%lodir/program/liblibreofficekitgtk.so %buildroot%_libdir/
mkdir -p %buildroot%_includedir/LibreOfficeKit
install -p include/LibreOfficeKit/* %{buildroot}%{_includedir}/LibreOfficeKit

%files

%files sdk -f files.sdk

%files postgresql -f file-lists/postgresql_list.txt

%files common -f files.common
%config %conffile
%_bindir/%uname%hversion
%_iconsdir/*/*/apps/%uname%hversion-*
%if_with java
%lodir/program/classes/ScriptProviderForBeanShell.jar
%lodir/program/services/scriptproviderforbeanshell.rdb
%endif

%files integrated -f files.integrated
%_datadir/metainfo/LibreOffice*
%_datadir/mimelnk/*
%_iconsdir/*/*/mimetypes/[^Ll]*.*
%_bindir/%name

%files gtk3 -f files.gtk3

%if_enabled qt5
%files qt5 -f files.qt5
%endif

%if_enabled kf5
%files kde5 -f files.kde5
%_datadir/metainfo/*kde*

%files gtk3-kde5 -f files.gtk3-kde5
%endif

%files extensions
%lodir/share/extensions/*

%langpack -m -h -l en_US -s en -n English
%langpack -m -h -l ru          -n Russian
%langpack    -h -l be          -n Belorussian
%langpack -m -h -l de          -n German
%langpack -m -h -l fr          -n French
%langpack -m -h -l uk          -n Ukrainian
%langpack -m -h -l pt_BR -s pt -n Brazilian Portuguese
%langpack -m -h -l es          -n Espanian
%langpack       -l kk          -n Kazakh
%langpack    -h -l tt          -n Tatar

%files -n libreofficekit
%_typelibdir/LOKDocView-*.typelib
%lodir/program/liblibreofficekitgtk.so
%_libdir/liblibreofficekitgtk.so
%lodir/share/libreofficekit

%files -n libreofficekit-devel
%_girdir/LOKDocView-*.gir
%_includedir/LibreOfficeKit

%changelog
* Wed Nov 02 2022 Fr. Br. George <george@altlinux.ru> 7.4.2.3-alt1
- Update to 7.4.2.3
- Fix desktop binary naming (Closes: #44176)

* Sun Oct 23 2022 Fr. Br. George <george@altlinux.ru> 7.4.2.1-alt1
- Update to 7.4.2.1
- Use install scheme provided by upstream

* Tue Jul 05 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 7.3.3.2-alt2
- NMU: Update russian translation for 7.3.3.2

* Fri May 20 2022 Fr. Br. George <george@altlinux.ru> 7.3.3.2-alt1
- Update to 7.3.3.2

* Wed Apr 13 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 7.3.2.1-alt3
- NMU: Update russian translation patch for 7.3.2.1

* Thu Mar 31 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 7.3.2.1-alt2
- NMU: Update russian translation for 7.3.2.1

* Mon Mar 21 2022 Andrey Cherepanov <cas@altlinux.org> 7.3.2.1-alt1
- NMU: Update to 7.3.2.1
- Fix insert symbols in Math (ALT #41969)

* Thu Mar 10 2022 Fr. Br. George <george@altlinux.ru> 7.3.1.3-alt1
- Update to 7.3.1.3

* Wed Feb 23 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 7.3.0.3-alt4
- NMU: - adapted spec for kf5-kcoreaddons-devel-5.91.0-alt1 and kf5-kcoreaddons-devel-5.90.0-alt1

* Mon Feb 22 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 7.3.0.3-alt3
- NMU:
  + Update russian translation for 7.3.0.3
  + FTBFS: Fix build

* Thu Feb 17 2022 Fr. Br. George <george@altlinux.ru> 7.3.0.3-alt2
- Fix build

* Thu Feb 03 2022 Fr. Br. George <george@altlinux.ru> 7.3.0.3-alt1
- Update to 7.3.0.3 (7.3.0 release)

* Sat Jan 15 2022 Fr. Br. George <george@altlinux.ru> 7.3.0.1-alt1
- Update to 7.3.0.1
- Update buildreq (Closes: #40915, #37391)
- Remove forky.c support

* Thu Jan 13 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 7.2.0.1-alt3
- Enabled SVG icon themes by default for Qt5 and KF5 backends (Closes: #35436).

* Sat Jan 01 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 7.2.0.1-alt2
- Update russian translation for 7.2.0.1

* Tue Aug 03 2021 Andrey Cherepanov <cas@altlinux.org> 7.2.0.1-alt1.1
- FTBFS: patch bundled Skia for freetype 2.11 (ALT #40642)

* Thu Jul 15 2021 Fr. Br. George <george@altlinux.ru> 7.2.0.1-alt1
- Update to 7.2.0.1

* Sun May 16 2021 Fr. Br. George <george@altlinux.ru> 7.1.3.2-alt1
- Update to 7.1.3.2

* Thu May 13 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 7.0.1.2-alt4
- Switched python scripts to python-3.

* Tue Mar 16 2021 Fr. Br. George <george@altlinux.ru> 7.1.1.2-alt1
- Update to 7.1.1.2

* Sat Feb 13 2021 Fr. Br. George <george@altlinux.ru> 7.1.0.3-alt3
- Update to 7.1.0.3
- Remove antic LanguageTool from ext_source
- Bundle Python3.8

* Thu Jan 21 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 7.0.1.2-alt3
- Reduced build workers count for ppc64le.

* Wed Oct 14 2020 Ivan A. Melnikov <iv@altlinux.org> 7.0.1.2-alt2
- Drop LanguageTool dependency for java-less build

* Wed Sep 23 2020 Fr. Br. George <george@altlinux.ru> 7.0.1.2-alt1
- Update to 7.0.1.2

* Sun Aug 30 2020 Fr. Br. George <george@altlinux.ru> 7.0.0.3-alt2
- Avoid qt5 dependency build

* Wed Aug 26 2020 Fr. Br. George <george@altlinux.ru> 7.0.0.3-alt1
- Update to 7.0.0.3
- Drop GTK2 and KDE4 support

* Fri Aug 07 2020 Andrey Cherepanov <cas@altlinux.org> 6.3.0.3-alt6
- Use bundled liborcus-0.14.
- Install mime package bundle for LibreOffice MIME types.

* Fri Jul 24 2020 Andrey Bychkov <mrdrew@altlinux.org> 6.3.0.3-alt5
- Rebuild with dconf enabled (Closes: 38752).

* Mon Jun 01 2020 Ivan A. Melnikov <iv@altlinux.org> 6.3.0.3-alt4
- Fix build with poppler 0.86.0 (see
  https://bugs.documentfoundation.org/show_bug.cgi?id=131353).
- Get rid of java BRs in no-java build.
- Fix build on mipsel:
  + fix linking with libatomic;
  + adjust building options.

* Tue Feb 04 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.3.0.3-alt3
- Rebuilt with new poppler and boost.

* Wed Dec 04 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 6.3.0.3-alt2
- Rebuilt with mdds-1.5.0 and boost-1.71.0.

* Mon Aug 05 2019 Fr. Br. George <george@altlinux.ru> 6.3.0.3-alt1
- Version up to 6.3.0.3
- Require pentaho-reporting-flow-engine (Closes: #36900)

* Mon May 27 2019 Fr. Br. George <george@altlinux.ru> 6.2.4.2-alt1
- Verion up (Closes: #36635, #35896)

* Mon Apr 08 2019 Fr. Br. George <george@altlinux.ru> 6.2.2.2-alt1.1
- Build with internal python

* Mon Mar 25 2019 Fr. Br. George <george@altlinux.ru> 6.2.2.2-alt1
- Update to 6.2.2.2

* Sun Mar 03 2019 Nikolai Kostrigin <nickel@altlinux.org> 6.2.1.1-alt2
- Fix FTBFS against libmysqlclient21

* Mon Feb 18 2019 Fr. Br. George <george@altlinux.ru> 6.2.1.1-alt1
- Update to 6.2.1.1 (Closes: #36107, #35504, #35420, #35292)
- Move KDE-depended library to -kde5 package (Closes: #36100)

* Tue Feb 12 2019 Fr. Br. George <george@altlinux.ru> 6.2.0.3-alt1
- Update to 6.2.0.3
- Build with native kde5 SAL instead of gtk3/kde5

* Wed Nov 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.3.1-alt3
- NMU: fixed build with new poppler.

* Mon Oct 22 2018 Ivan Razzhivin <underwit@altlinux.org> 6.1.3.1-alt2
- build with gtk3/kde5 UI

* Wed Oct 17 2018 Fr. Br. George <george@altlinux.ru> 6.1.3.1-alt1
- Update to 6.1.3.1

* Tue Sep 25 2018 Fr. Br. George <george@altlinux.ru> 6.1.2.1-alt1
- Update to 6.1.2.1

* Mon Sep 17 2018 Fr. Br. George <george@altlinux.ru> 6.1.1.2-alt1
- Update to 6.1.1.2

* Mon Aug 20 2018 Fr. Br. George <george@altlinux.ru> 6.1.0.3-alt1
- Update to 6.1.0.3 (Closes: #35135)
- MIPS port, thanks to iv@ (Closes: #35171)

* Wed Jun 06 2018 Fr. Br. George <george@altlinux.ru> 6.0.5.1-alt1
- Update to 6.0.5.1 (Closes: #34765)
- Introduce Qt5 chooser (Closes: #33136)
- Provide libreoffice binary (Closes: #34825)
- Add application/vnd.ms-visio.drawing.main+xml to mimetypes (Closes: #32699)

* Wed May 23 2018 Fr. Br. George <george@altlinux.ru> 6.0.4.2-alt1
- Update to 6.0.4.2

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.0.1.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Feb 14 2018 Fr. Br. George <george@altlinux.ru> 6.0.1.1-alt1
- Update to 6.0.1.1

* Thu Nov 30 2017 Fr. Br. George <george@altlinux.ru> 5.4.3.2-alt1
- Update to 5.4.3.2

* Mon Nov 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.4.2.2-alt2
- Rebuilt with libCoinMP-1.8.3.

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

