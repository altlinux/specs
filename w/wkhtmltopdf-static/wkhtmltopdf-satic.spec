Name: wkhtmltopdf-static
Version: 0.10.0
Release: alt1.rc2

Summary: Shell utility to convert html to pdf using the webkit rendering engine and qt
License: %lgpl3plus
Group: Publishing
URL: http://code.google.com/p/wkhtmltopdf/
Packager: Sergey Kurakin <kurakin@altlinux.org>

# git://github.com/antialize/wkhtmltopdf.git
Source: wkhtmltopdf-%version.tar

# hardly patched qt version is able to function without X-server running
# git://gitorious.org/+wkhtml2pdf/qt/wkhtmltopdf-qt.git
# with unused components deleted
Source2: qts-%version.tar

Conflicts: wkhtmltopdf

BuildPreReq: rpm-build-licenses gzip

# Automatically added by buildreq on Tue Mar 08 2011
BuildRequires: fontconfig-devel gcc-c++ libXext-devel libXrender-devel libfreetype-devel libssl-devel

%description
wkhtmltopdf is a command line tool to create a pdf from an url,
a local html file or stdin. It produces a pdf like rendred with
the WebKit engine.

This static build does not requires an X11 server to run
and have some extra features.

%package -n wkhtmltoimage-static
Group: Publishing
Summary: Shell utility to convert html to raster image using the webkit rendering engine and qt
%description -n wkhtmltoimage-static
wkhtmltoimage is a command line tool to create a raster image
from an url, a local html file or stdin. It produces an image
like rendred with the WebKit engine.

This static build does not requires an X11 server to run
and have some extra features.

%prep
%setup -D -a 2 -n wkhtmltopdf-%version
# remove rpath
echo "QMAKE_LFLAGS_RPATH =" >> common.pri

%build

# build qt without x-server
pushd qts

# accept the software license
sed -i s/OPT_CONFIRM_LICENSE=no/OPT_CONFIRM_LICENSE=yes/g configure

./configure \
-prefix $(pwd) \
-release \
-static \
-fast \
-exceptions \
-no-accessibility \
-no-stl \
-no-sql-ibase \
-no-sql-mysql \
-no-sql-odbc \
-no-sql-psql \
-no-sql-sqlite \
-no-sql-sqlite2 \
-no-qt3support \
-xmlpatterns \
-no-phonon \
-no-phonon-backend \
-webkit \
-no-scripttools \
-no-mmx \
-no-3dnow \
-no-sse \
-no-sse2 \
-qt-zlib \
-qt-gif \
-qt-libtiff \
-qt-libpng \
-qt-libmng \
-qt-libjpeg \
-graphicssystem raster \
-opensource \
-nomake tools \
-nomake examples \
-nomake demos \
-nomake docs \
-nomake translations \
-no-opengl \
-no-dbus \
-no-multimedia \
-openssl \
-no-declarative \
-largefile \
-no-nis \
-no-cups \
-no-iconv \
-no-pch \
-no-gtkstyle \
-no-nas-sound \
-no-sm \
-no-xshape \
-no-xinerama \
-no-xcursor \
-no-xfixes \
-no-xrandr \
-no-mitshm \
-no-xinput \
-no-xkb \
-no-glib \
-no-openvg \
-no-xsync \
-no-audio-backend \
-no-sse3 \
-no-ssse3 \
-no-sse4.1 \
-no-sse4.2 \
#

%make_build
%make_install
cp src/3rdparty/webkit/JavaScriptCore/release/* lib

popd
# patched qt build comleted

# build static wkhtmltopdf itself
qts/bin/qmake
%make_build
bin/wkhtmltopdf --manpage | gzip > wkhtmltopdf.1.gz
bin/wkhtmltoimage --manpage | gzip > wkhtmltoimage.1.gz

%install
#make_install INSTALL_ROOT=%buildroot%prefix install
install -D -m 755 bin/wkhtmltopdf %buildroot%_bindir/wkhtmltopdf
install -D -m 755 bin/wkhtmltoimage %buildroot%_bindir/wkhtmltoimage
install -D -m 644 wkhtmltopdf.1.gz %buildroot%_man1dir/wkhtmltopdf.1.gz
install -D -m 644 wkhtmltoimage.1.gz %buildroot%_man1dir/wkhtmltoimage.1.gz

%files
%doc README_WKHTMLTOPDF
%_bindir/wkhtmltopdf
%_man1dir/wkhtmltopdf*

%files -n wkhtmltoimage-static
%doc README_WKHTMLTOIMAGE
%_bindir/wkhtmltoimage
%_man1dir/wkhtmltoimage*

%changelog
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
