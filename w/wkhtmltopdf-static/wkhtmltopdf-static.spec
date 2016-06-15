# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.1
Name: wkhtmltopdf-static
Version: 0.12.2.4
#Release: alt1

Summary: Shell utility to convert html to pdf using the QT webkit rendering engine
License: %lgpl3plus
Group:   Publishing
URL:     http://wkhtmltopdf.org/
#URL:    https://github.com/wkhtmltopdf/
Packager: Sergey Kurakin <kurakin@altlinux.org>

# https://github.com/wkhtmltopdf/wkhtmltopdf
Source: wkhtmltopdf-%version.tar

# hardly patched qt version is able to function without X-server running
# https://github.com/wkhtmltopdf/qt
Source2: qt-wk-%version.tar

Conflicts: wkhtmltopdf

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Sep 06 2015
# optimized out: fontconfig libX11-devel libXext-devel libcom_err-devel libfreetype-devel libkrb5-devel libstdc++-devel pkg-config xorg-renderproto-devel xorg-videoproto-devel xorg-xextproto-devel xorg-xproto-devel zlib-devel
BuildRequires: fontconfig-devel gcc-c++ libXrender-devel libXv-devel libicu-devel libjpeg-devel libpng-devel libssl-devel ruby

BuildRequires: glibc-devel-static libssl-devel-static

%description
wkhtmltopdf is a command line tool to create a pdf from an url,
a local html file or stdin. It produces a pdf like rendred with
the WebKit engine.

This static build does not requires an X11 server to run
and have some extra features.

%package -n wkhtmltoimage-static
Group: Publishing
Conflicts: wkhtmltopdf
Summary: Shell utility to convert html to raster image using the webkit rendering engine and qt
%description -n wkhtmltoimage-static
wkhtmltoimage is a command line tool to create a raster image
from an url, a local html file or stdin. It produces an image
like rendred with the WebKit engine.

This static build does not requires an X11 server to run
and have some extra features.

%package -n libwkhtmltox-static
Summary: Shared library of wkhtmltox-static
Conflicts: libwkhtmltox
Group: System/Libraries

%description -n libwkhtmltox-static
libwkhtmltox is a shared library which permits to create a pdf or raster
image from an url, a local html file or stdin. It produces a pdf like
rendred with the WebKit engine.

This package contains shared library libwkhtmltox-static, that
does not requires an X11 server to run and have some extra features.

%package -n libwkhtmltox-static-devel
Summary: Development files of libwkhtmltox-static
Group: Development/C++
Requires: %name = %version-%release
Conflicts: libwkhtmltox-devel

%description -n libwkhtmltox-static-devel
libwkhtmltox is a shared library which permits to create a pdf or raster
image from an url, a local html file or stdin. It produces a pdf like
rendred with the WebKit engine.

This package contains development files of libwkhtmltox-static, that
does not requires an X11 server to run and have some extra features.


####### Patched QT configuration
# Flags from scripts/build.py
%define common_qt_flags        \\\
        -opensource            \\\
        -confirm-license       \\\
        -fast                  \\\
        -release               \\\
        -static                \\\
        -graphicssystem raster \\\
        -webkit                \\\
        -exceptions            \\\
        -xmlpatterns           \\\
        -system-zlib           \\\
        -system-libpng         \\\
        -system-libjpeg        \\\
        -no-libmng             \\\
        -no-libtiff            \\\
        -no-accessibility      \\\
        -no-stl                \\\
        -no-qt3support         \\\
        -no-phonon             \\\
        -no-phonon-backend     \\\
        -no-opengl             \\\
        -no-declarative        \\\
        -no-script             \\\
        -no-scripttools        \\\
        -no-sql-ibase          \\\
        -no-sql-mysql          \\\
        -no-sql-odbc           \\\
        -no-sql-psql           \\\
        -no-sql-sqlite         \\\
        -no-sql-sqlite2        \\\
        -no-mmx                \\\
        -no-3dnow              \\\
        -no-sse                \\\
        -no-sse2               \\\
        -no-multimedia         \\\
        -nomake demos          \\\
        -nomake docs           \\\
        -nomake examples       \\\
        -nomake tools          \\\
        -nomake tests          \\\
        -nomake translations

# without: -no-rpath, -silent
%define posix_qt_flags         \\\
        -xrender               \\\
        -largefile             \\\
        -iconv                 \\\
        -openssl               \\\
        -no-dbus               \\\
        -no-nis                \\\
        -no-cups               \\\
        -no-pch                \\\
        -no-gtkstyle           \\\
        -no-nas-sound          \\\
        -no-sm                 \\\
        -no-xshape             \\\
        -no-xinerama           \\\
        -no-xcursor            \\\
        -no-xfixes             \\\
        -no-xrandr             \\\
        -no-mitshm             \\\
        -no-xinput             \\\
        -no-xkb                \\\
        -no-glib               \\\
        -no-gstreamer          \\\
        -D ENABLE_VIDEO=0      \\\
        -no-openvg             \\\
        -no-xsync              \\\
        -no-audio-backend      \\\
        -no-sse3               \\\
        -no-ssse3              \\\
        -no-sse4.1             \\\
        -no-sse4.2             \\\
        -no-avx                \\\
        -no-neon


%prep
%setup -D -a 2 -n wkhtmltopdf-%version
# remove rpath
echo "QMAKE_LFLAGS_RPATH =" >> common.pri

%build
# build qt without x-server
pushd qt-wk
./configure -prefix $(pwd) %common_qt_flags %posix_qt_flags
%make_build
%make_install
popd
# patched qt build comleted

# build static wkhtmltopdf itself
qt-wk/bin/qmake
%make_build

%install
%make_install INSTALL_ROOT=%buildroot%prefix install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%files
%doc README.md CHANGELOG.md AUTHORS
%_bindir/wkhtmltopdf
%_man1dir/wkhtmltopdf*

%files -n wkhtmltoimage-static
%doc README.md CHANGELOG.md AUTHORS
%_bindir/wkhtmltoimage
%_man1dir/wkhtmltoimage*

%files -n libwkhtmltox-static
%_libdir/*.so.*

%files -n libwkhtmltox-static-devel
%_includedir/*
%_libdir/*.so


%changelog
* Wed Jun 15 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.12.2.4-alt1.1
- (AUTO) subst_x86_64.

* Sun Sep 06 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.12.2.4-alt1
- New version based on patched QT 4.8
- Subpackages for libwkhtmltox-static library

* Wed Mar 06 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.10.0-alt1.rc2.1
- Updating BuildRequires to enable https:// support

* Wed Mar  9 2011 Sergey Kurakin <kurakin@altlinux.org> 0.10.0-alt1.rc2
- forked static build to function without X-server running
- 0.10.0 rc2 features wkhtmltoimage
- license changed to LGPL3 (was GPL3)

* Sun Jul 25 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.9.9-alt1
- update to 0.9.9
- add Debian patch to fix some typos

* Fri Mar 26 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.9.5-alt1
- update to 0.9.5
- don't package COPYING file (according to Docs Policy)

* Tue Nov 24 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.8.3-alt2
- fix build with new %%cmake macro

* Sun Oct 18 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.8.3-alt1
- initial build for Sisyphus
