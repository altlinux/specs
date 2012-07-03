%define appdir  %_datadir/%name 
%def_disable    opengl

Name:		gambas3
Version:	3.0.0
Release:	alt4

Summary:	IDE based on a basic interpreter with object extensions
Group:		Development/Tools
License:	GPLv2+

URL:		http://gambas.sourceforge.net/
Source0:	http://downloads.sourceforge.net/gambas/%name-%version.tar.bz2
Source1:	%name.desktop
Source2:	%name.watch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzlib-devel
BuildRequires:	fonts-ttf-dejavu
BuildRequires:	gettext
BuildRequires:  gcc-c++
BuildRequires:	glibc-devel
BuildRequires:	imlib2-devel
%if_enabled opengl
BuildRequires:	libGL-devel
BuildRequires:	libGLU-devel
%endif
BuildRequires:	libICE-devel
BuildRequires:	libSDL-devel
BuildRequires:	libSDL_image-devel
BuildRequires:	libSDL_mixer-devel
BuildRequires:	libSDL_ttf-devel
BuildRequires:	libXcursor-devel
BuildRequires:	libXft-devel
BuildRequires:	libXtst-devel
BuildRequires:	libcairo-devel
BuildRequires:	libcurl-devel
BuildRequires:	libdbus-devel
BuildRequires:	libffi-devel
BuildRequires:	libglew-devel
BuildRequires:	libgtk+2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl3-devel
BuildRequires:	libmysqlclient-devel
BuildRequires:	libpcre-devel
BuildRequires:	libpng-devel
BuildRequires:	libpoppler-devel
BuildRequires:	libqt4-webkit
BuildRequires:	librsvg-devel
BuildRequires:	libsqlite-devel
BuildRequires:	libsqlite3-devel
BuildRequires:	libtool
BuildRequires:	libunixODBC-devel
BuildRequires:	libv4l-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	pkg-config
BuildRequires:	postgresql9.1-devel
BuildRequires:	qt4-devel
BuildRequires:	xdg-utils
BuildRequires:	zlib-devel

Patch1:		%name-2.99.1-nolintl.patch
Patch2:		%name-2.99.1-noliconv.patch
# Use libv4l1
Patch4:		%name-2.99.1-use-libv4l1.patch

%description
Gambas3 is a free development environment based on a Basic interpreter
with object extensions, like Visual Basic (but it is NOT a clone !).
With Gambas3, you can quickly design your program GUI, access MySQL or
PostgreSQL databases, pilot KDE applications with DCOP, translate your
program into many languages, create network applications easily, and so
on...

%package runtime
Summary:	Runtime environment for Gambas3
Group:		Development/Tools

%description runtime
Gambas3 is a free development environment based on a Basic interpreter
with object extensions, like Visual Basic. This package contains the
runtime components necessary to run programs designed in Gambas3.

%package devel
Summary:	Development environment for Gambas3
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description devel
The gambas3-devel package contains the tools needed to compile Gambas3
projects without having to install the complete development environment
(gambas3-ide).

%package scripter
Summary:	Scripter program that allows the creation of Gambas3 scripts
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
Requires:	%name-devel = %version-%release

%description scripter
This package includes the scripter program that allows the user to
write script files in Gambas.

%package ide
Summary:	The complete Gambas3 Development Environment
Group:		Development/Tools
License:	GPLv2+
Provides:	%name = %version-%release
Requires:	tar, gzip, rpm-build, gettext
Requires:	%name-runtime = %version-%release
Requires:	%name-devel = %version-%release
Requires:	%name-gb-db = %version-%release
Requires:	%name-gb-db-form = %version-%release
Requires:	%name-gb-desktop = %version-%release
Requires:	%name-gb-eval-highlight = %version-%release
Requires:	%name-gb-form = %version-%release
Requires:	%name-gb-form-dialog = %version-%release
Requires:	%name-gb-form-mdi = %version-%release
Requires:	%name-gb-form-stock = %version-%release
Requires:	%name-gb-image = %version-%release
Requires:	%name-gb-image-effect = %version-%release
Requires:	%name-gb-qt4 = %version-%release
Requires:	%name-gb-qt4-ext = %version-%release
Requires:	%name-gb-qt4-webkit = %version-%release
Requires:	%name-gb-settings = %version-%release

%description ide
This package includes the complete Gambas3 Development Environment
and the database manager. Installing this package will give you all
of the Gambas3 components.

%package examples
Summary:	Example projects provided with Gambas3
Group:		Development/Tools
BuildArch:	noarch
Provides:	%name-full
# Some of the examples are GPLv2+
# Database/PictureDatabase
# Games/RobotFindsKitten
# OpenGL/GambasGears
# Printing/Printing
# Everything else is GPL+
License:	GPL+ and GPLv2+
Requires:	%name-runtime = %version-%release
Requires:	%name-ide = %version-%release
# From http://gambasdoc.org/help/howto/package#t1
# It depends on "All gambas components."
Requires:	%name-gb-cairo = %version-%release
Requires:	%name-gb-chart = %version-%release
Requires:	%name-gb-compress = %version-%release
Requires:	%name-gb-crypt = %version-%release
Requires:	%name-gb-db = %version-%release
Requires:	%name-gb-db-form = %version-%release
Requires:	%name-gb-db-mysql = %version-%release
Requires:	%name-gb-db-odbc = %version-%release
Requires:	%name-gb-db-postgresql = %version-%release
Requires:	%name-gb-db-sqlite2 = %version-%release
Requires:	%name-gb-db-sqlite3 = %version-%release
Requires:	%name-gb-desktop = %version-%release
Requires:	%name-gb-dbus = %version-%release
Requires:	%name-gb-eval-highlight = %version-%release
Requires:	%name-gb-form = %version-%release
Requires:	%name-gb-form-dialog = %version-%release
Requires:	%name-gb-form-mdi = %version-%release
Requires:	%name-gb-form-stock = %version-%release
Requires:	%name-gb-gtk = %version-%release
Requires:	%name-gb-gui = %version-%release
Requires:	%name-gb-image = %version-%release
Requires:	%name-gb-image-effect = %version-%release
Requires:	%name-gb-image-imlib = %version-%release
Requires:	%name-gb-image-io = %version-%release
Requires:	%name-gb-net = %version-%release
Requires:	%name-gb-net-curl = %version-%release
%if_enabled opengl
Requires:	%name-gb-opengl = %version-%release
Requires:	%name-gb-opengl-glu = %version-%release
Requires:	%name-gb-opengl-glsl = %version-%release
%endif
Requires:	%name-gb-option = %version-%release
Requires:	%name-gb-pcre = %version-%release
Requires:	%name-gb-pdf = %version-%release
Requires:	%name-gb-qt4 = %version-%release
Requires:	%name-gb-qt4-ext = %version-%release
Requires:	%name-gb-qt4-webkit = %version-%release
Requires:	%name-gb-qt4-opengl = %version-%release
Requires:	%name-gb-report = %version-%release
Requires:	%name-gb-sdl = %version-%release
Requires:	%name-gb-sdl-sound = %version-%release
Requires:	%name-gb-settings = %version-%release
Requires:	%name-gb-signal = %version-%release
Requires:	%name-gb-v4l = %version-%release
Requires:	%name-gb-vb = %version-%release
Requires:	%name-gb-xml = %version-%release
Requires:	%name-gb-xml-rpc = %version-%release
Requires:	%name-gb-xml-xslt = %version-%release
Requires:	%name-gb-web = %version-%release

%description examples
This package includes all the example projects provided with Gambas3.

%package gb-cairo
Summary:	Gambas3 component package for cairo
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-cairo
This package contains the Gambas Cario components.

%package gb-chart
Summary:	Gambas3 component package for chart
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-chart
This package contains the Gambas Chart components.

%package gb-compress
Summary:	Gambas3 component package for compress
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-compress
This component allows you to compress/uncompress data or files
with the bzip2 and zip algorithms.

%package gb-crypt
Summary:	Gambas3 component package for crypt
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-crypt
This component contains cryptography support.

%package gb-db
Summary:	Gambas3 component package for db
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-db
This component allows you to access many databases management
systems, provided that you install the needed driver packages.

%package gb-db-form
Summary:	Gambas3 component package for db-form
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-db-form
This package contains the Gambas Database form components.

%package gb-db-mysql
Summary:	Gambas3 component package for db-mysql
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-db-mysql
This component allows you to access MySQL databases.

%package gb-db-odbc
Summary:	Gambas3 component package for db-odbc
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-db-odbc
This component allows you to access ODBC databases.

%package gb-db-postgresql
Summary:	Gambas3 component package for db-postgresql
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-db-postgresql
This component allows you to access PostgreSQL databases.

%package gb-db-sqlite2
Summary:	Gambas3 component package for db-sqlite2
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-db-sqlite2
This component allows you to access SQLite 2 databases.

%package gb-db-sqlite3
Summary:	Gambas3 component package for db-sqlite3
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-db-sqlite3
This component allows you to access SQLite 3 databases.

%package gb-desktop
Summary:	Gambas3 component package for desktop
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-desktop
This Gambas3 component allows you to operate with XDG-compliant desktop
environmnents.

%package gb-dbus
Summary:	Gambas3 component package for dbus
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-dbus
This package contains the Gambas D-bus components.

%package gb-eval-highlight
Summary:	Gambas3 component package for eval highlight
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-eval-highlight
This component implements the eval-highlight componet.

%package gb-form
Summary:	Gambas3 component package for form
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-form
This component implements the form control.

%package gb-form-dialog
Summary:	Gambas3 component package for form-dialog
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-form-dialog
This component implements the form-dialog control.

%package gb-form-mdi
Summary:	Gambas3 component package for form-mdi
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-form-mdi
This component implements the form-mdi control.

%package gb-form-stock
Summary:	Gambas3 component package for form-stock
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-form-stock
This component implements the form-stock control.

%package gb-gtk
Summary:	Gambas3 component package for gtk
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-gtk
This package includes the Gambas GTK2 GUI component.

%package gb-gui
Summary:	Gambas3 component package for gui
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-gui
This is a component that just loads gb.qt if you are running KDE or
gb.gtk in the other cases.

%package gb-image 
Summary:	Gambas3 component package for image 
License:	GPLv2 or QPL
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-image 
Image processing component for Gambas3.

%package gb-image-effect
Summary:	Gambas3 component package for image-effect
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-image-effect
This component allows you to apply various effects to images.

%package gb-image-imlib
Summary:	Gambas3 component package for image-imlib
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-image-imlib
This component allows you to manipulate images with imlibs.

%package gb-image-io
Summary:	Gambas3 component package for image-io
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-image-io
This component allows you to perform images input output operations.

%package gb-net
Summary:	Gambas3 component package for net
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-net
This Gambas3 component allows you to use TCP/IP and UDP sockets, and to
access any serial ports.

%package gb-net-curl
Summary:	Gambas3 component package for net.curl
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-net-curl
This Gambas3 component allows your programs to easily become FTP or HTTP
clients.

%package gb-net-smtp 
Summary:	Gambas3 component package for net-smtp 
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-net-smtp
This Gambas3 component allows your programs to easily become SMTP
clients.

%if_enabled opengl
%package gb-opengl 
Summary:	Gambas3 component package for opengl 
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-opengl 
This component allows you to use the Mesa libraries to do 3D operations.

%package gb-opengl-glu
Summary:	Gambas3 component package for opengl-glu
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-opengl-glu
This component allows you to use the Mesa libraries to do 3D operations.

%package gb-opengl-glsl
Summary:	Gambas3 component package for opengl-glsl
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-opengl-glsl
This component allows you to use the Mesa libraries to do 3D operations.
%endif

%package gb-option
Summary:	Gambas3 component package for option
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-option
This component allows you to interpret command-line options.

%package gb-pcre 
Summary:	Gambas3 component package for pcre 
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-pcre 
This component allows you to use Perl compatible regular expresions
within Gambas code.

%package gb-pdf
Summary:	Gambas3 component package for pdf
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-pdf
This component allows you to manipulate pdf files with Gambas code.

%package gb-qt4
Summary:	Gambas3 component package for qt4
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-qt4
This package includes Gambas QT4 GUI component.

%package gb-qt4-ext
Summary:	Gambas3 component package for qt4.ext
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-qt4-ext
This package contains the Gambas qt-ext components.

%package gb-qt4-opengl
Summary:	Gambas3 component package for qt4-opengl
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-qt4-opengl
This package contains the Gambas qt-opengl components.

%package gb-qt4-webkit
Summary:	Gambas3 component package for qt4-webkit
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-qt4-webkit
This package contains the Gambas qt-webkit components.

%package gb-report
Summary:	Gambas3 component package for report
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-report
This package contains the Gambas Report components.

%package gb-sdl
Summary:	Gambas3 component package for sdl
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
Requires:	fonts-ttf-dejavu

%description gb-sdl
This component use the sound, image and TTF fonts parts of the SDL
library. It allows you to simultaneously play many sounds and music
stored in a file. If OpenGL drivers are installed it uses them to
accelerate 2D and 3D drawing.

%package gb-sdl-sound
Summary:	Gambas3 component package for sdl-sound
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-sdl-sound
This component allows you to play sounds in Gambas. This component
manages up to 32 sound tracks that can play sounds from memory, and
one music track that can play music from a file. Everything is mixed
in real time.

%package gb-settings
Summary:	Gambas3 component package for settings
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-settings
This components allows you to deal with configuration files.

%package gb-signal
Summary:	Gambas3 component package for signal
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-signal
This package contains the Gambas Signal components.

%package gb-v4l 
Summary:	Gambas3 component package for v4l 
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-v4l 
This component allows access to Video4Linux devices.

%package gb-vb
Summary:	Gambas3 component package for vb
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-vb
This Gambas3 component aims at including some functions that imitate
the behaviour of Visual Basic(tm) functions. Use it only if you try
to port some VB projects.

%package gb-web
Summary:	Gambas3 component package for web
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-web
This components allows you to make CGI web applications using Gambas,
with an ASP-like interface.

%package gb-xml
Summary:	Gambas3 component package for xml
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-xml
These components brings the power of the libxml and libxslt libraries to
Gambas for XML processing.

%package gb-xml-rpc
Summary:	Gambas3 component package for xml.rpc
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-xml-rpc
This component allows you to use xml-rpc.

%package gb-xml-xslt
Summary:	Gambas3 component package for xml.xslt
Group:		Development/Tools
Requires:	%name-runtime = %version-%release

%description gb-xml-xslt
This component allows you to use xml-xslt.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch4 -p1
# We used to patch these out, but this is simpler.
for i in `find . |grep acinclude.m4`; do
	sed -i 's|$AM_CFLAGS -O3|$AM_CFLAGS|g' $i
	sed -i 's|$AM_CXXFLAGS -Os -fno-omit-frame-pointer|$AM_CXXFLAGS|g' $i
	sed -i 's|$AM_CFLAGS -Os|$AM_CFLAGS|g' $i
	sed -i 's|$AM_CFLAGS -O0|$AM_CFLAGS|g' $i
	sed -i 's|$AM_CXXFLAGS -O0|$AM_CXXFLAGS|g' $i
done
# Need this for gcc44
sed -i 's|-fno-exceptions||g' gb.db.sqlite3/acinclude.m4
./reconf-all

# clean up some spurious exec perms
chmod -x main/gbx/gbx_local.h
chmod -x main/gbx/gbx_subr_file.c
chmod -x gb.qt4/src/CContainer.cpp
chmod -x main/lib/option/getoptions.*
chmod -x main/lib/option/main.c

%build
# Gambas can't deal with -Wp,-D_FORTIFY_SOURCE=2
MY_CFLAGS=`echo $RPM_OPT_FLAGS | sed -e 's/-Wp,-D_FORTIFY_SOURCE=2//g'`
%configure \
	--datadir="%_datadir" \
	--enable-intl \
	--enable-conv \
	--enable-qt4 \
	--enable-kde \
	--enable-net \
	--enable-curl \
	--enable-postgresql \
	--enable-mysql \
	--enable-sqlite3 \
	--enable-sdl \
	--enable-vb \
	--enable-pdf \
	--with-bzlib2-libraries=%_libdir \
	--with-crypt-libraries=%_libdir \
	--with-curl-libraries=%_libdir \
	--with-desktop-libraries=%_libdir \
	--with-ffi-includes=`pkg-config libffi --variable=includedir` \
	--with-ffi-libraries=`pkg-config libffi --variable=libdir` \
	--with-intl-libraries=%_libdir \
	--with-conv-libraries=%_libdir \
	--with-gettext-libraries=%_libdir \
	--with-gtk-libraries=%_libdir \
	--with-gtk_svg-libraries=%_libdir \
	--with-image-libraries=%_libdir \
	--with-kde-libraries=%_libdir \
	--with-mysql-libraries=%_libdir/mysql \
	--with-net-libraries=%_libdir \
	--with-odbc-libraries=%_libdir \
%if_enabled opengl
	--with-opengl-libraries=%_libdir \
%endif
	--with-pcre-libraries=%_libdir \
	--with-poppler-libraries=%_libdir \
	--with-postgresql-libraries=%_libdir \
	--with-qt4-libraries=%_libdir \
	--with-qtopengl-libraries=%_libdir \
	--with-sdl-libraries=%_libdir \
	--with-sdl_sound-libraries=%_libdir \
	--with-smtp-libraries=%_libdir \
	--with-sqlite2-libraries=%_libdir \
	--with-sqlite3-libraries=%_libdir \
	--with-v4l-libraries=%_libdir \
	--with-xml-libraries=%_libdir \
	--with-xslt-libraries=%_libdir \
	--with-zlib-libraries=%_libdir \
	--disable-static \
	AM_CFLAGS="$MY_CFLAGS" AM_CXXFLAGS="$MY_CFLAGS"
# rpath removal
for i in main; do
	sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' $i/libtool
	sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' $i/libtool
done
make LIBTOOL=%_bindir/libtool %?_smp_mflags

%install
export PATH=%buildroot%_bindir:$PATH
make LIBTOOL=%_bindir/libtool DESTDIR=%buildroot INSTALL="install -p" install
# Yes, I know. Normally we'd nuke the .la files, but Gambas is retar^Wspecial.
# rm -rf %%buildroot%%_libdir/%%name/*.la
install -m644 -pD ./app/src/%name/.icon.png %buildroot%_pixmapsdir/%name.png
install -m644 -pD %SOURCE1 %buildroot%_desktopdir/%name.desktop

# get the buildroot out of the examples
for i in `grep -lr "%buildroot" %buildroot%appdir/examples/`; 
do
  sed -i "s|%buildroot||g" $i; 
done

# Get the SVN noise out of the main tree
#find %buildroot%appdir/ -type d -name .svn -exec rm -rf { 2>/dev/null ';' || :

# Upstream says we don't need those files. Not sure why they install them then. :/
rm -rf %buildroot%_libdir/%name/gb.la %buildroot%_libdir/%name/gb.so*

# No need for the static libs
rm -rf %buildroot%_libdir/%name/*.a

# Replace the bundled font with a symlink to our system copy
pushd %buildroot%appdir/gb.sdl/
rm -f DejaVuSans.ttf
ln -s ../../fonts/ttf/dejavu/DejaVuSans.ttf DejaVuSans.ttf
popd

chmod -x %buildroot%appdir/gb.sdl/LICENSE

# Mime types.
mkdir -p %buildroot%_datadir/mime/packages/
install -m 0644 -p app/mime/application-x-gambasscript.xml %buildroot%_xdgmimedir/packages/
install -m 0644 -p main/mime/application-x-gambas3.xml %buildroot%_xdgmimedir/packages/

%files runtime
%doc COPYING INSTALL README
%dir %_libdir/%name/
%_libdir/%name/gb.component
%_libdir/%name/gb.debug.*
%_libdir/%name/gb.draw.*
%_libdir/%name/gb.eval.component
%_libdir/%name/gb.eval.so*
%_bindir/gbr3
%_bindir/gbx3
%_datadir/pixmaps/%name.png
%_datadir/applications/*.desktop
%dir %appdir/
%dir %appdir/info/
%appdir/info/gb.debug.*
%appdir/info/gb.eval.list
%appdir/info/gb.eval.info
%appdir/info/gb.info
%appdir/info/gb.list
%dir %appdir/icons/
%appdir/icons/application-x-gambas3.png
%_xdgmimedir/packages/application-x-gambas3.xml
%appdir/icons/application-x-gambasserverpage.png

%files devel
%doc COPYING
%_bindir/gbc3
%_bindir/gba3
%_bindir/gbi3

%files scripter
%_bindir/gbs3
%_bindir/gbs3.gambas
%_bindir/gbw3
%appdir/icons/application-x-gambasscript.png
%_xdgmimedir/packages/application-x-gambasscript.xml

%files ide
%_bindir/%name
%_bindir/%name.gambas
# The IDE crashes if it can't find this directory.
# Since -examples Requires: -ide, this is okay.
%dir %appdir/examples/

%files examples
%dir %appdir/examples/Automation/
%dir %appdir/examples/Basic/
%dir %appdir/examples/Control/
%dir %appdir/examples/Database/
%dir %appdir/examples/Drawing/
%dir %appdir/examples/Games/
%dir %appdir/examples/Image/
%dir %appdir/examples/Misc/
%dir %appdir/examples/Networking/
%dir %appdir/examples/OpenGL/
%dir %appdir/examples/Printing/
%dir %appdir/examples/Sound/
%dir %appdir/examples/Video/
%dir %appdir/examples/Automation/DBusExplorer/
%appdir/examples/Automation/DBusExplorer/dbus*.png
%appdir/examples/Automation/DBusExplorer/DBusExplorer.gambas
%appdir/examples/Automation/DBusExplorer/.directory
%appdir/examples/Automation/DBusExplorer/.gambas/
%appdir/examples/Automation/DBusExplorer/.hidden
%appdir/examples/Automation/DBusExplorer/.icon.png
%appdir/examples/Automation/DBusExplorer/method.png
%appdir/examples/Automation/DBusExplorer/.project
%appdir/examples/Automation/DBusExplorer/property.png
%appdir/examples/Automation/DBusExplorer/.settings
%appdir/examples/Automation/DBusExplorer/signal.png
%appdir/examples/Automation/DBusExplorer/.src/
%appdir/examples/Automation/DBusExplorer/.startup

%dir %appdir/examples/Basic/Blights/
%dir %appdir/examples/Basic/Blights/.lang/
%appdir/examples/Basic/Blights/.directory
%appdir/examples/Basic/Blights/.gambas/
%appdir/examples/Basic/Blights/.hidden
%appdir/examples/Basic/Blights/.icon*
%appdir/examples/Basic/Blights/.project
%appdir/examples/Basic/Blights/.src/
%appdir/examples/Basic/Blights/.startup
%appdir/examples/Basic/Blights/Blights.gambas
%appdir/examples/Basic/Blights/ampoule.png
%appdir/examples/Basic/Blights/bloff.xpm
%appdir/examples/Basic/Blights/blon.xpm

%dir %appdir/examples/Basic/Collection/
%dir %appdir/examples/Basic/Collection/.lang/
%appdir/examples/Basic/Collection/.directory
%appdir/examples/Basic/Collection/.gambas/
%appdir/examples/Basic/Collection/.hidden
%appdir/examples/Basic/Collection/.icon*
%appdir/examples/Basic/Collection/.project
%appdir/examples/Basic/Collection/.startup
%appdir/examples/Basic/Collection/.src/
%appdir/examples/Basic/Collection/Collection.gambas
%appdir/examples/Basic/Collection/collection.png

%dir %appdir/examples/Basic/DragNDrop/
%appdir/examples/Basic/DragNDrop/.directory
%appdir/examples/Basic/DragNDrop/.gambas/
%appdir/examples/Basic/DragNDrop/.hidden
%appdir/examples/Basic/DragNDrop/.icon*
%appdir/examples/Basic/DragNDrop/.project
%appdir/examples/Basic/DragNDrop/.startup
%appdir/examples/Basic/DragNDrop/DragNDrop.gambas
%appdir/examples/Basic/DragNDrop/.src/
%appdir/examples/Basic/DragNDrop/drop.png

%dir %appdir/examples/Basic/Object/
%dir %appdir/examples/Basic/Object/.lang/
%appdir/examples/Basic/Object/.directory
%appdir/examples/Basic/Object/.gambas/
%appdir/examples/Basic/Object/.hidden
%appdir/examples/Basic/Object/.icon*
%appdir/examples/Basic/Object/.project
%appdir/examples/Basic/Object/.startup
%appdir/examples/Basic/Object/.src/
%appdir/examples/Basic/Object/Object.gambas
%appdir/examples/Basic/Object/object.png

%dir %appdir/examples/Basic/Timer/
%dir %appdir/examples/Basic/Timer/.lang/
%appdir/examples/Basic/Timer/.directory
%appdir/examples/Basic/Timer/.gambas/
%appdir/examples/Basic/Timer/.hidden
%appdir/examples/Basic/Timer/.icon*
%appdir/examples/Basic/Timer/.project
%appdir/examples/Basic/Timer/.startup
%appdir/examples/Basic/Timer/.src/
%appdir/examples/Basic/Timer/Timer.gambas
%appdir/examples/Basic/Timer/timer.png

%dir %appdir/examples/Control/ArrayOfControls/
%dir %appdir/examples/Control/ArrayOfControls/.lang/
%appdir/examples/Control/ArrayOfControls/.directory
%appdir/examples/Control/ArrayOfControls/.gambas/
%appdir/examples/Control/ArrayOfControls/.hidden
%appdir/examples/Control/ArrayOfControls/.icon*
%appdir/examples/Control/ArrayOfControls/.project
%appdir/examples/Control/ArrayOfControls/.startup
%appdir/examples/Control/ArrayOfControls/.src/
%appdir/examples/Control/ArrayOfControls/green1.png
%appdir/examples/Control/ArrayOfControls/green.png
%appdir/examples/Control/ArrayOfControls/phone.png
%appdir/examples/Control/ArrayOfControls/red1.png
%appdir/examples/Control/ArrayOfControls/red.png
%appdir/examples/Control/ArrayOfControls/ArrayOfControls.gambas

%dir %appdir/examples/Control/Embedder/
%dir %appdir/examples/Control/Embedder/.lang/
%appdir/examples/Control/Embedder/.directory
%appdir/examples/Control/Embedder/.gambas/
%appdir/examples/Control/Embedder/.hidden
%appdir/examples/Control/Embedder/.icon*
%appdir/examples/Control/Embedder/.project
%appdir/examples/Control/Embedder/.settings
%appdir/examples/Control/Embedder/.startup
%appdir/examples/Control/Embedder/.src/
%appdir/examples/Control/Embedder/Embedder.gambas
%appdir/examples/Control/Embedder/embedder.png

%dir %appdir/examples/Control/HighlightEditor/
%dir %appdir/examples/Control/HighlightEditor/.lang/
%appdir/examples/Control/HighlightEditor/.directory
%appdir/examples/Control/HighlightEditor/.gambas/
%appdir/examples/Control/HighlightEditor/.hidden
%appdir/examples/Control/HighlightEditor/.icon*
%appdir/examples/Control/HighlightEditor/.project
%appdir/examples/Control/HighlightEditor/.startup
%appdir/examples/Control/HighlightEditor/.src/
%appdir/examples/Control/HighlightEditor/HighlightEditor.gambas
%appdir/examples/Control/HighlightEditor/download.html
%appdir/examples/Control/HighlightEditor/editor.png

%dir %appdir/examples/Control/TextEdit/
%dir %appdir/examples/Control/TextEdit/.lang/
%appdir/examples/Control/TextEdit/.directory
%appdir/examples/Control/TextEdit/.gambas/
%appdir/examples/Control/TextEdit/.hidden
%appdir/examples/Control/TextEdit/.icon*
%appdir/examples/Control/TextEdit/.project
%appdir/examples/Control/TextEdit/.startup
%appdir/examples/Control/TextEdit/.src/
%appdir/examples/Control/TextEdit/TextEdit.gambas
%appdir/examples/Control/TextEdit/edit.png
%appdir/examples/Control/TextEdit/text.html

%dir %appdir/examples/Control/TreeView/
%dir %appdir/examples/Control/TreeView/.lang/
%appdir/examples/Control/TreeView/.directory
%appdir/examples/Control/TreeView/.gambas/
%appdir/examples/Control/TreeView/.hidden
%appdir/examples/Control/TreeView/.icon*
%appdir/examples/Control/TreeView/.project
%appdir/examples/Control/TreeView/.startup
%appdir/examples/Control/TreeView/.src/
%appdir/examples/Control/TreeView/Female.png
%appdir/examples/Control/TreeView/Male.png
%appdir/examples/Control/TreeView/treeview.png
%appdir/examples/Control/TreeView/TreeView.gambas

%dir %appdir/examples/Control/Wizard/
%dir %appdir/examples/Control/Wizard/.lang/
%appdir/examples/Control/Wizard/.directory
%appdir/examples/Control/Wizard/.gambas/
%appdir/examples/Control/Wizard/.hidden
%appdir/examples/Control/Wizard/.icon*
%appdir/examples/Control/Wizard/.project
%appdir/examples/Control/Wizard/.startup
%appdir/examples/Control/Wizard/.src/
%appdir/examples/Control/Wizard/Wizard.gambas
%appdir/examples/Control/Wizard/wizard.png

%dir %appdir/examples/Database/Database/
%dir %appdir/examples/Database/Database/.lang/
%appdir/examples/Database/Database/.component
%appdir/examples/Database/Database/.directory
%appdir/examples/Database/Database/.gambas/
%appdir/examples/Database/Database/.hidden
%appdir/examples/Database/Database/.icon*
%appdir/examples/Database/Database/.project
%appdir/examples/Database/Database/.startup
%appdir/examples/Database/Database/.src/
%appdir/examples/Database/Database/Database.gambas
%appdir/examples/Database/Database/database.png

%dir %appdir/examples/Database/MySQLExample/
%dir %appdir/examples/Database/MySQLExample/.lang/
%appdir/examples/Database/MySQLExample/.action
%appdir/examples/Database/MySQLExample/.directory
%appdir/examples/Database/MySQLExample/.gambas/
%appdir/examples/Database/MySQLExample/.hidden
%appdir/examples/Database/MySQLExample/.icon*
%appdir/examples/Database/MySQLExample/icons/
%appdir/examples/Database/MySQLExample/MySQLExample.gambas
%appdir/examples/Database/MySQLExample/.project
%appdir/examples/Database/MySQLExample/.src/
%appdir/examples/Database/MySQLExample/.startup

%dir %appdir/examples/Database/PictureDatabase/
%dir %appdir/examples/Database/PictureDatabase/.lang/
%appdir/examples/Database/PictureDatabase/.directory
%appdir/examples/Database/PictureDatabase/.gambas/
%appdir/examples/Database/PictureDatabase/.hidden
%appdir/examples/Database/PictureDatabase/.icon*
%appdir/examples/Database/PictureDatabase/.project
%appdir/examples/Database/PictureDatabase/.startup
%appdir/examples/Database/PictureDatabase/.src/
%appdir/examples/Database/PictureDatabase/Images/
%appdir/examples/Database/PictureDatabase/PictureDatabase.gambas

%dir %appdir/examples/Drawing/AnalogWatch/
%appdir/examples/Drawing/AnalogWatch/.directory
%appdir/examples/Drawing/AnalogWatch/.gambas/
%appdir/examples/Drawing/AnalogWatch/.hidden
%appdir/examples/Drawing/AnalogWatch/.icon*
%appdir/examples/Drawing/AnalogWatch/.project
%appdir/examples/Drawing/AnalogWatch/.startup
%appdir/examples/Drawing/AnalogWatch/AnalogWatch.gambas
%appdir/examples/Drawing/AnalogWatch/.src/
%appdir/examples/Drawing/AnalogWatch/timer.png

%dir %appdir/examples/Drawing/Barcode/
%dir %appdir/examples/Drawing/Barcode/.lang/
%appdir/examples/Drawing/Barcode/.directory
%appdir/examples/Drawing/Barcode/.gambas/
%appdir/examples/Drawing/Barcode/.hidden
%appdir/examples/Drawing/Barcode/.icon*
%appdir/examples/Drawing/Barcode/.project
%appdir/examples/Drawing/Barcode/.settings
%appdir/examples/Drawing/Barcode/.startup
%appdir/examples/Drawing/Barcode/.src/
%appdir/examples/Drawing/Barcode/Barcode.gambas
%appdir/examples/Drawing/Barcode/barcode.png

%dir %appdir/examples/Drawing/Chart/
%dir %appdir/examples/Drawing/Chart/.lang/
%appdir/examples/Drawing/Chart/.directory
%appdir/examples/Drawing/Chart/.gambas/
%appdir/examples/Drawing/Chart/.hidden
%appdir/examples/Drawing/Chart/.icon*
%appdir/examples/Drawing/Chart/.project
%appdir/examples/Drawing/Chart/.src/
%appdir/examples/Drawing/Chart/.startup
%appdir/examples/Drawing/Chart/Chart.gambas
%appdir/examples/Drawing/Chart/graph.png

%dir %appdir/examples/Drawing/Clock/
%dir %appdir/examples/Drawing/Clock/.lang/
%appdir/examples/Drawing/Clock/.directory
%appdir/examples/Drawing/Clock/.gambas/
%appdir/examples/Drawing/Clock/.hidden
%appdir/examples/Drawing/Clock/.icon*
%appdir/examples/Drawing/Clock/.project
%appdir/examples/Drawing/Clock/.startup
%appdir/examples/Drawing/Clock/.src/
%appdir/examples/Drawing/Clock/Clock.gambas
%appdir/examples/Drawing/Clock/img/

%dir %appdir/examples/Drawing/Gravity/
%dir %appdir/examples/Drawing/Gravity/.lang/
%appdir/examples/Drawing/Gravity/.directory
%appdir/examples/Drawing/Gravity/.gambas/
%appdir/examples/Drawing/Gravity/.hidden
%appdir/examples/Drawing/Gravity/.icon*
%appdir/examples/Drawing/Gravity/.project
%appdir/examples/Drawing/Gravity/.startup
%appdir/examples/Drawing/Gravity/.src/
%appdir/examples/Drawing/Gravity/Gravity.gambas
%appdir/examples/Drawing/Gravity/gravity.png

%dir %appdir/examples/Drawing/OnScreenDisplay/
%dir %appdir/examples/Drawing/OnScreenDisplay/.lang/
%appdir/examples/Drawing/OnScreenDisplay/.directory
%appdir/examples/Drawing/OnScreenDisplay/.gambas/
%appdir/examples/Drawing/OnScreenDisplay/.hidden
%appdir/examples/Drawing/OnScreenDisplay/.icon*
%appdir/examples/Drawing/OnScreenDisplay/.project
%appdir/examples/Drawing/OnScreenDisplay/.startup
%appdir/examples/Drawing/OnScreenDisplay/.src/
%appdir/examples/Drawing/OnScreenDisplay/OnScreenDisplay.gambas
%appdir/examples/Drawing/OnScreenDisplay/icon.png

%dir %appdir/examples/Drawing/Painting/
%dir %appdir/examples/Drawing/Painting/.lang
%appdir/examples/Drawing/Painting/.directory
%appdir/examples/Drawing/Painting/.gambas/
%appdir/examples/Drawing/Painting/.hidden
%appdir/examples/Drawing/Painting/.icon*
%appdir/examples/Drawing/Painting/.project
%appdir/examples/Drawing/Painting/.startup
%appdir/examples/Drawing/Painting/.src/
%appdir/examples/Drawing/Painting/Example*
%appdir/examples/Drawing/Painting/clovis.jpg
%appdir/examples/Drawing/Painting/gambas.*svg
%appdir/examples/Drawing/Painting/icon.png
%appdir/examples/Drawing/Painting/image.jpg
%appdir/examples/Drawing/Painting/Painting.gambas

%dir %appdir/examples/Drawing/GSLSpline/
%appdir/examples/Drawing/GSLSpline/.directory
%appdir/examples/Drawing/GSLSpline/.gambas/
%appdir/examples/Drawing/GSLSpline/.icon*
%appdir/examples/Drawing/GSLSpline/.project
%appdir/examples/Drawing/GSLSpline/.src/
%appdir/examples/Drawing/GSLSpline/.startup
%appdir/examples/Drawing/GSLSpline/GSLSpline.gambas
%appdir/examples/Drawing/GSLSpline/spline.png

%dir %appdir/examples/Games/BeastScroll/
%appdir/examples/Games/BeastScroll/.dir_icon.png
%appdir/examples/Games/BeastScroll/.directory
%appdir/examples/Games/BeastScroll/.gambas/
%appdir/examples/Games/BeastScroll/.hidden
%appdir/examples/Games/BeastScroll/.icon*
%appdir/examples/Games/BeastScroll/.project
%appdir/examples/Games/BeastScroll/.startup
%appdir/examples/Games/BeastScroll/.src/
%appdir/examples/Games/BeastScroll/BeastScroll.gambas
%appdir/examples/Games/BeastScroll/b-title.mod
%appdir/examples/Games/BeastScroll/bgd*.png
%appdir/examples/Games/BeastScroll/fireworks.png
%appdir/examples/Games/BeastScroll/logo.png
%appdir/examples/Games/BeastScroll/scrolltext.png
%appdir/examples/Games/BeastScroll/sprite*.png

%dir %appdir/examples/Games/Concent/
%dir %appdir/examples/Games/Concent/.lang/
%appdir/examples/Games/Concent/.directory
%appdir/examples/Games/Concent/.gambas/
%appdir/examples/Games/Concent/.hidden
%appdir/examples/Games/Concent/.icon*
%appdir/examples/Games/Concent/.project
%appdir/examples/Games/Concent/.settings
%appdir/examples/Games/Concent/.startup
%appdir/examples/Games/Concent/*.wav
%appdir/examples/Games/Concent/CHANGELOG
%appdir/examples/Games/Concent/Concent.gambas
%appdir/examples/Games/Concent/.src/
%appdir/examples/Games/Concent/imagenes/

%dir %appdir/examples/Games/DeepSpace/
%dir %appdir/examples/Games/DeepSpace/.lang/
%appdir/examples/Games/DeepSpace/.directory
%appdir/examples/Games/DeepSpace/.gambas/
%appdir/examples/Games/DeepSpace/.hidden
%appdir/examples/Games/DeepSpace/.icon*
%appdir/examples/Games/DeepSpace/.project
%appdir/examples/Games/DeepSpace/.startup
%appdir/examples/Games/DeepSpace/.src/
%appdir/examples/Games/DeepSpace/DeepSpace.gambas
%appdir/examples/Games/DeepSpace/doc/
%appdir/examples/Games/DeepSpace/images/
%appdir/examples/Games/DeepSpace/object.data/

%dir %appdir/examples/Games/GameOfLife/
%dir %appdir/examples/Games/GameOfLife/.lang/
%appdir/examples/Games/GameOfLife/.debug
%appdir/examples/Games/GameOfLife/.directory
%appdir/examples/Games/GameOfLife/.gambas/
%appdir/examples/Games/GameOfLife/.hidden
%appdir/examples/Games/GameOfLife/.icon*
%appdir/examples/Games/GameOfLife/.project
%appdir/examples/Games/GameOfLife/.settings
%appdir/examples/Games/GameOfLife/.startup
%appdir/examples/Games/GameOfLife/.src/
%appdir/examples/Games/GameOfLife/GameOfLife.gambas
%appdir/examples/Games/GameOfLife/glob2*.png

%dir %appdir/examples/Games/GNUBoxWorld/
%dir %appdir/examples/Games/GNUBoxWorld/.lang/
%appdir/examples/Games/GNUBoxWorld/.directory
%appdir/examples/Games/GNUBoxWorld/.gambas/
%appdir/examples/Games/GNUBoxWorld/.hidden
%appdir/examples/Games/GNUBoxWorld/.icon*
%appdir/examples/Games/GNUBoxWorld/License
%appdir/examples/Games/GNUBoxWorld/.project
%appdir/examples/Games/GNUBoxWorld/.startup
%appdir/examples/Games/GNUBoxWorld/.src/
%appdir/examples/Games/GNUBoxWorld/GNUBoxWorld.gambas
%appdir/examples/Games/GNUBoxWorld/abajo.png
%appdir/examples/Games/GNUBoxWorld/arriba.png
%appdir/examples/Games/GNUBoxWorld/derecha.png
%appdir/examples/Games/GNUBoxWorld/destino.png
%appdir/examples/Games/GNUBoxWorld/ganador.png
%appdir/examples/Games/GNUBoxWorld/izquierda.png
%appdir/examples/Games/GNUBoxWorld/logo.png
%appdir/examples/Games/GNUBoxWorld/movibleendestino.png
%appdir/examples/Games/GNUBoxWorld/movible.png
%appdir/examples/Games/GNUBoxWorld/obstaculo*.png
%appdir/examples/Games/GNUBoxWorld/piso.png

%dir %appdir/examples/Games/Puzzle1To8
%dir %appdir/examples/Games/Puzzle1To8/.lang/
%appdir/examples/Games/Puzzle1To8/.directory
%appdir/examples/Games/Puzzle1To8/.gambas/
%appdir/examples/Games/Puzzle1To8/.hidden
%appdir/examples/Games/Puzzle1To8/.icon*
%appdir/examples/Games/Puzzle1To8/.project
%appdir/examples/Games/Puzzle1To8/.startup
%appdir/examples/Games/Puzzle1To8/.src/
%appdir/examples/Games/Puzzle1To8/ejemplo1.png
%appdir/examples/Games/Puzzle1To8/ejemplo2.png
%appdir/examples/Games/Puzzle1To8/logo.png
%appdir/examples/Games/Puzzle1To8/Licence
%appdir/examples/Games/Puzzle1To8/Puzzle*.gambas

%dir %appdir/examples/Games/RobotFindsKitten/
%dir %appdir/examples/Games/RobotFindsKitten/.lang/
%appdir/examples/Games/RobotFindsKitten/.directory
%appdir/examples/Games/RobotFindsKitten/.gambas/
%appdir/examples/Games/RobotFindsKitten/.hidden
%appdir/examples/Games/RobotFindsKitten/.icon*
%appdir/examples/Games/RobotFindsKitten/.project
%appdir/examples/Games/RobotFindsKitten/.startup
%appdir/examples/Games/RobotFindsKitten/.src/
%appdir/examples/Games/RobotFindsKitten/COPYING
%appdir/examples/Games/RobotFindsKitten/RobotFindsKitten.gambas
%appdir/examples/Games/RobotFindsKitten/heart.png
%appdir/examples/Games/RobotFindsKitten/nkis.txt
%appdir/examples/Games/RobotFindsKitten/readme.txt

%dir %appdir/examples/Games/Snake/
%dir %appdir/examples/Games/Snake/.lang/
%appdir/examples/Games/Snake/.directory
%appdir/examples/Games/Snake/.gambas/
%appdir/examples/Games/Snake/.hidden
%appdir/examples/Games/Snake/.icon*
%appdir/examples/Games/Snake/.project
%appdir/examples/Games/Snake/.startup
%appdir/examples/Games/Snake/.src/
%appdir/examples/Games/Snake/Snake.gambas
%appdir/examples/Games/Snake/apple.png
%appdir/examples/Games/Snake/body.png
%appdir/examples/Games/Snake/*.wav
%appdir/examples/Games/Snake/head.png

%dir %appdir/examples/Games/Solitaire/
%dir %appdir/examples/Games/Solitaire/.lang/
%appdir/examples/Games/Solitaire/.directory
%appdir/examples/Games/Solitaire/.gambas/
%appdir/examples/Games/Solitaire/.hidden
%appdir/examples/Games/Solitaire/.icon*
%appdir/examples/Games/Solitaire/.project
%appdir/examples/Games/Solitaire/.startup
%appdir/examples/Games/Solitaire/.src/
%appdir/examples/Games/Solitaire/Solitaire.gambas
%appdir/examples/Games/Solitaire/ball.png
%appdir/examples/Games/Solitaire/new.png
%appdir/examples/Games/Solitaire/quit.png
%appdir/examples/Games/Solitaire/redo.png
%appdir/examples/Games/Solitaire/undo.png

%dir %appdir/examples/Games/StarField/
%appdir/examples/Games/StarField/.directory
%appdir/examples/Games/StarField/.gambas/
%appdir/examples/Games/StarField/.icon*
%appdir/examples/Games/StarField/.project
%appdir/examples/Games/StarField/.src/
%appdir/examples/Games/StarField/.startup
%appdir/examples/Games/StarField/StarField.gambas
%appdir/examples/Games/StarField/enterprise.png
%appdir/examples/Games/StarField/logo.png

%dir %appdir/examples/Image/ImageViewer/
%dir %appdir/examples/Image/ImageViewer/.lang/
%appdir/examples/Image/ImageViewer/.directory
%appdir/examples/Image/ImageViewer/.gambas/
%appdir/examples/Image/ImageViewer/.hidden
%appdir/examples/Image/ImageViewer/.icon*
%appdir/examples/Image/ImageViewer/image.png
%appdir/examples/Image/ImageViewer/ImageViewer.gambas
%appdir/examples/Image/ImageViewer/.project
%appdir/examples/Image/ImageViewer/.startup
%appdir/examples/Image/ImageViewer/.src/

%dir %appdir/examples/Image/Lighttable/
%dir %appdir/examples/Image/Lighttable/.lang/
%appdir/examples/Image/Lighttable/.action/
%appdir/examples/Image/Lighttable/.gambas/
%appdir/examples/Image/Lighttable/.src/
%appdir/examples/Image/Lighttable/.directory
%appdir/examples/Image/Lighttable/.hidden
%appdir/examples/Image/Lighttable/.icon*
%appdir/examples/Image/Lighttable/.project
%appdir/examples/Image/Lighttable/.settings
%appdir/examples/Image/Lighttable/.startup
%appdir/examples/Image/Lighttable/CHANGELOG
%appdir/examples/Image/Lighttable/close.png
%appdir/examples/Image/Lighttable/FStart.*
%appdir/examples/Image/Lighttable/hand1.png
%appdir/examples/Image/Lighttable/help-contents.png
%appdir/examples/Image/Lighttable/Help*.html
%appdir/examples/Image/Lighttable/Liesmich.txt
%appdir/examples/Image/Lighttable/Lighttable.gambas
%appdir/examples/Image/Lighttable/lighttable.png
%appdir/examples/Image/Lighttable/LTicon.png
%appdir/examples/Image/Lighttable/move.png
%appdir/examples/Image/Lighttable/Readme.txt
%appdir/examples/Image/Lighttable/zoom-in.png

%dir %appdir/examples/Misc/Console/
%dir %appdir/examples/Misc/Console/.lang/
%appdir/examples/Misc/Console/.directory
%appdir/examples/Misc/Console/.gambas/
%appdir/examples/Misc/Console/.hidden
%appdir/examples/Misc/Console/.icon*
%appdir/examples/Misc/Console/.project
%appdir/examples/Misc/Console/.startup
%appdir/examples/Misc/Console/Console.gambas
%appdir/examples/Misc/Console/terminal.png
%appdir/examples/Misc/Console/.src/

%dir %appdir/examples/Misc/Evaluator/
%dir %appdir/examples/Misc/Evaluator/.lang/
%appdir/examples/Misc/Evaluator/.directory
%appdir/examples/Misc/Evaluator/.gambas/
%appdir/examples/Misc/Evaluator/.hidden
%appdir/examples/Misc/Evaluator/.icon*
%appdir/examples/Misc/Evaluator/.project
%appdir/examples/Misc/Evaluator/.startup
%appdir/examples/Misc/Evaluator/Evaluator.gambas
%appdir/examples/Misc/Evaluator/.src/
%appdir/examples/Misc/Evaluator/calculator.png

%dir %appdir/examples/Misc/Explorer/
%dir %appdir/examples/Misc/Explorer/.lang/
%appdir/examples/Misc/Explorer/.directory
%appdir/examples/Misc/Explorer/.gambas/
%appdir/examples/Misc/Explorer/.hidden
%appdir/examples/Misc/Explorer/.icon*
%appdir/examples/Misc/Explorer/.project
%appdir/examples/Misc/Explorer/.startup
%appdir/examples/Misc/Explorer/Explorer.gambas
%appdir/examples/Misc/Explorer/.src/
%appdir/examples/Misc/Explorer/folder.png

%dir %appdir/examples/Misc/Notepad/
%dir %appdir/examples/Misc/Notepad/.lang/
%appdir/examples/Misc/Notepad/.directory
%appdir/examples/Misc/Notepad/.gambas/
%appdir/examples/Misc/Notepad/.hidden
%appdir/examples/Misc/Notepad/.icon*
%appdir/examples/Misc/Notepad/.project
%appdir/examples/Misc/Notepad/.startup
%appdir/examples/Misc/Notepad/.src/
%appdir/examples/Misc/Notepad/Notepad.gambas
%appdir/examples/Misc/Notepad/notepad.png

%dir %appdir/examples/Misc/PDFViewer/
%dir %appdir/examples/Misc/PDFViewer/.lang/
%appdir/examples/Misc/PDFViewer/.directory
%appdir/examples/Misc/PDFViewer/.gambas/
%appdir/examples/Misc/PDFViewer/.hidden
%appdir/examples/Misc/PDFViewer/.icon*
%appdir/examples/Misc/PDFViewer/.project
%appdir/examples/Misc/PDFViewer/.startup
%appdir/examples/Misc/PDFViewer/.src/
%appdir/examples/Misc/PDFViewer/PDFViewer.gambas
%appdir/examples/Misc/PDFViewer/pdf.png

%dir %appdir/examples/Networking/ClientSocket/
%dir %appdir/examples/Networking/ClientSocket/.lang/
%appdir/examples/Networking/ClientSocket/.directory
%appdir/examples/Networking/ClientSocket/.gambas/
%appdir/examples/Networking/ClientSocket/.hidden
%appdir/examples/Networking/ClientSocket/.icon*
%appdir/examples/Networking/ClientSocket/.project
%appdir/examples/Networking/ClientSocket/.startup
%appdir/examples/Networking/ClientSocket/ClientSocket.gambas
%appdir/examples/Networking/ClientSocket/.src/
%appdir/examples/Networking/ClientSocket/socket.png

%dir %appdir/examples/Networking/DnsClient/
%dir %appdir/examples/Networking/DnsClient/.lang/
%appdir/examples/Networking/DnsClient/.directory
%appdir/examples/Networking/DnsClient/.gambas/
%appdir/examples/Networking/DnsClient/.hidden
%appdir/examples/Networking/DnsClient/.icon*
%appdir/examples/Networking/DnsClient/.project
%appdir/examples/Networking/DnsClient/.startup
%appdir/examples/Networking/DnsClient/DnsClient.gambas
%appdir/examples/Networking/DnsClient/.src/
%appdir/examples/Networking/DnsClient/dnsclient.png

%dir %appdir/examples/Networking/HTTPGet/
%dir %appdir/examples/Networking/HTTPGet/.lang/
%appdir/examples/Networking/HTTPGet/.directory
%appdir/examples/Networking/HTTPGet/.gambas/
%appdir/examples/Networking/HTTPGet/.hidden
%appdir/examples/Networking/HTTPGet/.icon*
%appdir/examples/Networking/HTTPGet/.project
%appdir/examples/Networking/HTTPGet/.startup
%appdir/examples/Networking/HTTPGet/.src/
%appdir/examples/Networking/HTTPGet/HTTPGet.gambas
%appdir/examples/Networking/HTTPGet/httpclient.png

%dir %appdir/examples/Networking/HTTPPost/
%dir %appdir/examples/Networking/HTTPPost/.lang/
%appdir/examples/Networking/HTTPPost/.directory
%appdir/examples/Networking/HTTPPost/.gambas/
%appdir/examples/Networking/HTTPPost/.hidden
%appdir/examples/Networking/HTTPPost/.icon*
%appdir/examples/Networking/HTTPPost/.project
%appdir/examples/Networking/HTTPPost/.startup
%appdir/examples/Networking/HTTPPost/.src/
%appdir/examples/Networking/HTTPPost/HTTPPost.gambas
%appdir/examples/Networking/HTTPPost/httpclient.png

%dir %appdir/examples/Networking/SerialPort/
%dir %appdir/examples/Networking/SerialPort/.lang/
%appdir/examples/Networking/SerialPort/.directory
%appdir/examples/Networking/SerialPort/.gambas/
%appdir/examples/Networking/SerialPort/.hidden
%appdir/examples/Networking/SerialPort/.icon*
%appdir/examples/Networking/SerialPort/.project
%appdir/examples/Networking/SerialPort/.startup
%appdir/examples/Networking/SerialPort/.src/
%appdir/examples/Networking/SerialPort/SerialPort.gambas
%appdir/examples/Networking/SerialPort/serialport.png

%dir %appdir/examples/Networking/ServerSocket/
%dir %appdir/examples/Networking/ServerSocket/.lang/
%appdir/examples/Networking/ServerSocket/.directory
%appdir/examples/Networking/ServerSocket/.gambas/
%appdir/examples/Networking/ServerSocket/.hidden
%appdir/examples/Networking/ServerSocket/.icon*
%appdir/examples/Networking/ServerSocket/.project
%appdir/examples/Networking/ServerSocket/.startup
%appdir/examples/Networking/ServerSocket/.src/
%appdir/examples/Networking/ServerSocket/ServerSocket.gambas
%appdir/examples/Networking/ServerSocket/serversocket.png

%dir %appdir/examples/Networking/UDPServerClient/
%dir %appdir/examples/Networking/UDPServerClient/.lang/
%appdir/examples/Networking/UDPServerClient/.directory
%appdir/examples/Networking/UDPServerClient/.gambas/
%appdir/examples/Networking/UDPServerClient/.hidden
%appdir/examples/Networking/UDPServerClient/.icon*
%appdir/examples/Networking/UDPServerClient/.project
%appdir/examples/Networking/UDPServerClient/.startup
%appdir/examples/Networking/UDPServerClient/.src/
%appdir/examples/Networking/UDPServerClient/UDPServerClient.gambas
%appdir/examples/Networking/UDPServerClient/udpsocket.png

%dir %appdir/examples/Networking/WebBrowser/
%dir %appdir/examples/Networking/WebBrowser/.lang/
%appdir/examples/Networking/WebBrowser/.directory
%appdir/examples/Networking/WebBrowser/.gambas/
%appdir/examples/Networking/WebBrowser/.hidden
%appdir/examples/Networking/WebBrowser/.icon*
%appdir/examples/Networking/WebBrowser/.project
%appdir/examples/Networking/WebBrowser/.startup
%appdir/examples/Networking/WebBrowser/.src/
%appdir/examples/Networking/WebBrowser/WebBrowser.gambas
%appdir/examples/Networking/WebBrowser/konqueror.png
%appdir/examples/Networking/WebBrowser/list-*.png

%dir %appdir/examples/OpenGL/3DWebCam/
%appdir/examples/OpenGL/3DWebCam/.directory
%appdir/examples/OpenGL/3DWebCam/.gambas/
%appdir/examples/OpenGL/3DWebCam/.hidden
%appdir/examples/OpenGL/3DWebCam/.icon*
%appdir/examples/OpenGL/3DWebCam/.project
%appdir/examples/OpenGL/3DWebCam/.startup
%appdir/examples/OpenGL/3DWebCam/3DWebCam.gambas
%appdir/examples/OpenGL/3DWebCam/.src/
%appdir/examples/OpenGL/3DWebCam/webcam.png

%dir %appdir/examples/OpenGL/GambasGears/
%appdir/examples/OpenGL/GambasGears/.directory
%appdir/examples/OpenGL/GambasGears/.gambas/
%appdir/examples/OpenGL/GambasGears/.hidden
%appdir/examples/OpenGL/GambasGears/.icon*
%appdir/examples/OpenGL/GambasGears/.project
%appdir/examples/OpenGL/GambasGears/.startup
%appdir/examples/OpenGL/GambasGears/GambasGears.gambas
%appdir/examples/OpenGL/GambasGears/.src/
%appdir/examples/OpenGL/GambasGears/gears.png

%dir %appdir/examples/OpenGL/NeHeTutorial/
%appdir/examples/OpenGL/NeHeTutorial/.directory
%appdir/examples/OpenGL/NeHeTutorial/.gambas/
%appdir/examples/OpenGL/NeHeTutorial/.icon*
%appdir/examples/OpenGL/NeHeTutorial/.project
%appdir/examples/OpenGL/NeHeTutorial/.src/
%appdir/examples/OpenGL/NeHeTutorial/.startup
%appdir/examples/OpenGL/NeHeTutorial/NeHe.png
%appdir/examples/OpenGL/NeHeTutorial/NeHeTutorial.gambas
%appdir/examples/OpenGL/NeHeTutorial/*.txt
%appdir/examples/OpenGL/NeHeTutorial/Star.png
%appdir/examples/OpenGL/NeHeTutorial/barrel.png
%appdir/examples/OpenGL/NeHeTutorial/ceiling.png
%appdir/examples/OpenGL/NeHeTutorial/crate.jpeg
%appdir/examples/OpenGL/NeHeTutorial/floor.png
%appdir/examples/OpenGL/NeHeTutorial/glass.png
%appdir/examples/OpenGL/NeHeTutorial/icon.png
%appdir/examples/OpenGL/NeHeTutorial/wall.jpeg

%dir %appdir/examples/OpenGL/NeHeTutorialShell/
%appdir/examples/OpenGL/NeHeTutorialShell/.directory
%appdir/examples/OpenGL/NeHeTutorialShell/.gambas/
%appdir/examples/OpenGL/NeHeTutorialShell/.icon*
%appdir/examples/OpenGL/NeHeTutorialShell/.project
%appdir/examples/OpenGL/NeHeTutorialShell/.src/
%appdir/examples/OpenGL/NeHeTutorialShell/.startup
%appdir/examples/OpenGL/NeHeTutorialShell/NeHeTutorialShell.gambas
%appdir/examples/OpenGL/NeHeTutorialShell/icon.png
%appdir/examples/OpenGL/NeHeTutorialShell/nehe.png

%dir %appdir/examples/OpenGL/PDFPresentation/
%appdir/examples/OpenGL/PDFPresentation/.directory
%appdir/examples/OpenGL/PDFPresentation/.gambas/
%appdir/examples/OpenGL/PDFPresentation/.hidden
%appdir/examples/OpenGL/PDFPresentation/.icon*
%appdir/examples/OpenGL/PDFPresentation/.project
%appdir/examples/OpenGL/PDFPresentation/.settings
%appdir/examples/OpenGL/PDFPresentation/.startup
%appdir/examples/OpenGL/PDFPresentation/.src/
%appdir/examples/OpenGL/PDFPresentation/PDFPresentation.gambas
%appdir/examples/OpenGL/PDFPresentation/icon.png
%appdir/examples/OpenGL/PDFPresentation/logo.png
%appdir/examples/OpenGL/PDFPresentation/music.xm

%dir %appdir/examples/OpenGL/TunnelSDL/
%appdir/examples/OpenGL/TunnelSDL/.dir_icon.png
%appdir/examples/OpenGL/TunnelSDL/.directory
%appdir/examples/OpenGL/TunnelSDL/.gambas/
%appdir/examples/OpenGL/TunnelSDL/.icon*
%appdir/examples/OpenGL/TunnelSDL/.project
%appdir/examples/OpenGL/TunnelSDL/.src/
%appdir/examples/OpenGL/TunnelSDL/.startup
%appdir/examples/OpenGL/TunnelSDL/CHANGELOG
%appdir/examples/OpenGL/TunnelSDL/TunnelSDL.gambas
%appdir/examples/OpenGL/TunnelSDL/texture.png
%appdir/examples/OpenGL/TunnelSDL/tunnelsdl.png

%dir %appdir/examples/Printing/Printing/
%appdir/examples/Printing/Printing/.directory
%appdir/examples/Printing/Printing/.gambas/
%appdir/examples/Printing/Printing/.hidden
%appdir/examples/Printing/Printing/.icon*
%appdir/examples/Printing/Printing/.project
%appdir/examples/Printing/Printing/.startup
%appdir/examples/Printing/Printing/molly-malone.txt
%appdir/examples/Printing/Printing/printer-laser.png
%appdir/examples/Printing/Printing/.src/
%appdir/examples/Printing/Printing/Printing.gambas

%dir %appdir/examples/Printing/ReportExample/
%appdir/examples/Printing/ReportExample/.connection/
%appdir/examples/Printing/ReportExample/.directory
%appdir/examples/Printing/ReportExample/.gambas/
%appdir/examples/Printing/ReportExample/.hidden/
%appdir/examples/Printing/ReportExample/.icon*
%appdir/examples/Printing/ReportExample/.project
%appdir/examples/Printing/ReportExample/.settings
%appdir/examples/Printing/ReportExample/.src/
%appdir/examples/Printing/ReportExample/.startup
%appdir/examples/Printing/ReportExample/ReportExample.gambas
%appdir/examples/Printing/ReportExample/gambas.svg

%dir %appdir/examples/Sound/CDPlayer/
%dir %appdir/examples/Sound/CDPlayer/.lang/
%appdir/examples/Sound/CDPlayer/.directory
%appdir/examples/Sound/CDPlayer/.gambas/
%appdir/examples/Sound/CDPlayer/.hidden
%appdir/examples/Sound/CDPlayer/.icon*
%appdir/examples/Sound/CDPlayer/.project
%appdir/examples/Sound/CDPlayer/.startup
%appdir/examples/Sound/CDPlayer/CDPlayer.gambas
%appdir/examples/Sound/CDPlayer/cdrom.png
%appdir/examples/Sound/CDPlayer/.src/

%dir %appdir/examples/Sound/MusicPlayer/
%dir %appdir/examples/Sound/MusicPlayer/.lang/
%appdir/examples/Sound/MusicPlayer/.directory
%appdir/examples/Sound/MusicPlayer/.gambas/
%appdir/examples/Sound/MusicPlayer/.hidden
%appdir/examples/Sound/MusicPlayer/.icon*
%appdir/examples/Sound/MusicPlayer/.project
%appdir/examples/Sound/MusicPlayer/.startup
%appdir/examples/Sound/MusicPlayer/.src/
%appdir/examples/Sound/MusicPlayer/MusicPlayer.gambas
%appdir/examples/Sound/MusicPlayer/sound.png

%dir %appdir/examples/Video/MoviePlayer/
%dir %appdir/examples/Video/MoviePlayer/.lang/
%appdir/examples/Video/MoviePlayer/.directory
%appdir/examples/Video/MoviePlayer/.gambas/
%appdir/examples/Video/MoviePlayer/.hidden
%appdir/examples/Video/MoviePlayer/.icon*
%appdir/examples/Video/MoviePlayer/.project
%appdir/examples/Video/MoviePlayer/.startup
%appdir/examples/Video/MoviePlayer/.src/
%appdir/examples/Video/MoviePlayer/MoviePlayer.gambas
%appdir/examples/Video/MoviePlayer/video.png

%dir %appdir/examples/Video/MyWebCam/
%dir %appdir/examples/Video/MyWebCam/.lang/
%appdir/examples/Video/MyWebCam/.directory
%appdir/examples/Video/MyWebCam/.gambas/
%appdir/examples/Video/MyWebCam/.hidden
%appdir/examples/Video/MyWebCam/.icon*
%appdir/examples/Video/MyWebCam/.project
%appdir/examples/Video/MyWebCam/.startup
%appdir/examples/Video/MyWebCam/.src/
%appdir/examples/Video/MyWebCam/MyWebCam.gambas
%appdir/examples/Video/MyWebCam/camera.png

%dir %appdir/examples/Video/WebCam/
%appdir/examples/Video/WebCam/.directory
%appdir/examples/Video/WebCam/.gambas/
%appdir/examples/Video/WebCam/.hidden
%appdir/examples/Video/WebCam/.icon*
%appdir/examples/Video/WebCam/.project
%appdir/examples/Video/WebCam/.startup
%appdir/examples/Video/WebCam/.src/
%appdir/examples/Video/WebCam/camera.png
%appdir/examples/Video/WebCam/settings.png
%appdir/examples/Video/WebCam/WebCam.gambas

# Translation files
%lang(ca) %appdir/examples/Basic/Blights/.lang/ca.*o
%lang(cs) %appdir/examples/Basic/Blights/.lang/cs.*o
%lang(de) %appdir/examples/Basic/Blights/.lang/de.*o
%lang(es) %appdir/examples/Basic/Blights/.lang/es.*o
%lang(fr) %appdir/examples/Basic/Blights/.lang/fr.*o
%lang(sv) %appdir/examples/Basic/Blights/.lang/sv.*o
%lang(ca) %appdir/examples/Basic/Collection/.lang/ca.*o
%lang(cs) %appdir/examples/Basic/Collection/.lang/cs.*o
%lang(de) %appdir/examples/Basic/Collection/.lang/de.*o
%lang(es) %appdir/examples/Basic/Collection/.lang/es.*o
%lang(ca) %appdir/examples/Basic/Object/.lang/ca.*o
%lang(cs) %appdir/examples/Basic/Object/.lang/cs.*o
%lang(de) %appdir/examples/Basic/Object/.lang/de.*o
%lang(es) %appdir/examples/Basic/Object/.lang/es.*o
%lang(ca) %appdir/examples/Basic/Timer/.lang/ca.*o
%lang(cs) %appdir/examples/Basic/Timer/.lang/cs.*o
%lang(de) %appdir/examples/Basic/Timer/.lang/de.*o
%lang(es) %appdir/examples/Basic/Timer/.lang/es.*o
%lang(ca) %appdir/examples/Control/ArrayOfControls/.lang/ca.*o
%lang(cs) %appdir/examples/Control/ArrayOfControls/.lang/cs.*o
%lang(de) %appdir/examples/Control/ArrayOfControls/.lang/de.*o
%lang(ca) %appdir/examples/Control/Embedder/.lang/ca.*o
%lang(cs) %appdir/examples/Control/Embedder/.lang/cs.*o
%lang(de) %appdir/examples/Control/Embedder/.lang/de.*o
%lang(es) %appdir/examples/Control/Embedder/.lang/es.*o
%lang(ca) %appdir/examples/Control/HighlightEditor/.lang/ca.*o
%lang(cs) %appdir/examples/Control/HighlightEditor/.lang/cs.*o
%lang(de) %appdir/examples/Control/HighlightEditor/.lang/de.*o
%lang(es) %appdir/examples/Control/HighlightEditor/.lang/es.*o
%lang(ca) %appdir/examples/Control/TextEdit/.lang/ca.*o
%lang(cs) %appdir/examples/Control/TextEdit/.lang/cs.*o
%lang(de) %appdir/examples/Control/TextEdit/.lang/de.*o
%lang(es) %appdir/examples/Control/TextEdit/.lang/es.*o
%lang(fr) %appdir/examples/Control/TextEdit/.lang/fr.*o
%lang(sv) %appdir/examples/Control/TextEdit/.lang/sv.*o
%lang(ca) %appdir/examples/Control/TreeView/.lang/ca.*o
%lang(cs) %appdir/examples/Control/TreeView/.lang/cs.*o
%lang(de) %appdir/examples/Control/TreeView/.lang/de.*o
%lang(es) %appdir/examples/Control/TreeView/.lang/es.*o
%lang(ca) %appdir/examples/Control/Wizard/.lang/ca.*o
%lang(cs) %appdir/examples/Control/Wizard/.lang/cs.*o
%lang(de) %appdir/examples/Control/Wizard/.lang/de.*o
%lang(ca) %appdir/examples/Database/Database/.lang/ca.*o
%lang(cs) %appdir/examples/Database/Database/.lang/cs.*o
%lang(de) %appdir/examples/Database/Database/.lang/de.*o
%lang(es) %appdir/examples/Database/Database/.lang/es.*o
%lang(ca) %appdir/examples/Database/MySQLExample/.lang/ca.*o
%lang(cs) %appdir/examples/Database/MySQLExample/.lang/cs.*o
%lang(de) %appdir/examples/Database/MySQLExample/.lang/de.*o
%lang(es) %appdir/examples/Database/MySQLExample/.lang/es.*o
%lang(fr) %appdir/examples/Database/MySQLExample/.lang/fr.*o
%lang(ca) %appdir/examples/Database/PictureDatabase/.lang/ca.*o
%lang(cs) %appdir/examples/Database/PictureDatabase/.lang/cs.*o
%lang(de) %appdir/examples/Database/PictureDatabase/.lang/de.*o
%lang(es) %appdir/examples/Database/PictureDatabase/.lang/es.*o
%lang(ca) %appdir/examples/Drawing/Barcode/.lang/ca.*o
%lang(cs) %appdir/examples/Drawing/Barcode/.lang/cs.*o
%lang(de) %appdir/examples/Drawing/Barcode/.lang/de.*o
%lang(ca) %appdir/examples/Drawing/Chart/.lang/ca.*o
%lang(cs) %appdir/examples/Drawing/Chart/.lang/cs.*o
%lang(de) %appdir/examples/Drawing/Chart/.lang/de.*o
%lang(es) %appdir/examples/Drawing/Chart/.lang/es.*o
%lang(ca) %appdir/examples/Drawing/Clock/.lang/ca.*o
%lang(cs) %appdir/examples/Drawing/Clock/.lang/cs.*o
%lang(de) %appdir/examples/Drawing/Clock/.lang/de.*o
%lang(es) %appdir/examples/Drawing/Clock/.lang/es.*o
%lang(ca) %appdir/examples/Drawing/Gravity/.lang/ca.*o
%lang(cs) %appdir/examples/Drawing/Gravity/.lang/cs.*o
%lang(de) %appdir/examples/Drawing/Gravity/.lang/de.*o
%lang(es) %appdir/examples/Drawing/Gravity/.lang/es.*o
%lang(ca) %appdir/examples/Drawing/OnScreenDisplay/.lang/ca.*o
%lang(cs) %appdir/examples/Drawing/OnScreenDisplay/.lang/cs.*o
%lang(de) %appdir/examples/Drawing/OnScreenDisplay/.lang/de.*o
%lang(es) %appdir/examples/Drawing/OnScreenDisplay/.lang/es.*o
%lang(ca) %appdir/examples/Drawing/Painting/.lang/ca.*o
%lang(cs) %appdir/examples/Drawing/Painting/.lang/cs.*o
%lang(de) %appdir/examples/Drawing/Painting/.lang/de.*o
%lang(ca) %appdir/examples/Games/Concent/.lang/ca.*o
%lang(cs) %appdir/examples/Games/Concent/.lang/cs.*o
%lang(de) %appdir/examples/Games/Concent/.lang/de.*o
%lang(en) %appdir/examples/Games/Concent/.lang/en.*o
%lang(es) %appdir/examples/Games/Concent/.lang/es.*o
%lang(fr) %appdir/examples/Games/Concent/.lang/fr.*o
%lang(ca) %appdir/examples/Games/DeepSpace/.lang/ca.*o
%lang(cs) %appdir/examples/Games/DeepSpace/.lang/cs.*o
%lang(de) %appdir/examples/Games/DeepSpace/.lang/de.*o
%lang(es) %appdir/examples/Games/DeepSpace/.lang/es.*o
%lang(ca) %appdir/examples/Games/GameOfLife/.lang/ca.*o
%lang(cs) %appdir/examples/Games/GameOfLife/.lang/cs.*o
%lang(de) %appdir/examples/Games/GameOfLife/.lang/de.*o
%lang(ca) %appdir/examples/Games/GNUBoxWorld/.lang/ca.*o
%lang(cs) %appdir/examples/Games/GNUBoxWorld/.lang/cs.*o
%lang(de) %appdir/examples/Games/GNUBoxWorld/.lang/de.*o
%lang(es) %appdir/examples/Games/GNUBoxWorld/.lang/es*.*o
%lang(ca) %appdir/examples/Games/Puzzle1To8/.lang/ca.*o
%lang(cs) %appdir/examples/Games/Puzzle1To8/.lang/cs.*o
%lang(de) %appdir/examples/Games/Puzzle1To8/.lang/de.*o
%lang(es) %appdir/examples/Games/Puzzle1To8/.lang/es*.*o
%lang(ca) %appdir/examples/Games/RobotFindsKitten/.lang/ca.*o
%lang(cs) %appdir/examples/Games/RobotFindsKitten/.lang/cs.*o
%lang(de) %appdir/examples/Games/RobotFindsKitten/.lang/de.*o
%lang(es) %appdir/examples/Games/RobotFindsKitten/.lang/es.*o
%lang(ca) %appdir/examples/Games/Snake/.lang/ca.*o
%lang(cs) %appdir/examples/Games/Snake/.lang/cs.*o
%lang(de) %appdir/examples/Games/Snake/.lang/de.*o
%lang(ca) %appdir/examples/Games/Solitaire/.lang/ca.*o
%lang(cs) %appdir/examples/Games/Solitaire/.lang/cs.*o
%lang(de) %appdir/examples/Games/Solitaire/.lang/de.*o
%lang(es) %appdir/examples/Games/Solitaire/.lang/es.*o
%lang(ca) %appdir/examples/Image/ImageViewer/.lang/ca.*o
%lang(cs) %appdir/examples/Image/ImageViewer/.lang/cs.*o
%lang(de) %appdir/examples/Image/ImageViewer/.lang/de.*o
%lang(es) %appdir/examples/Image/ImageViewer/.lang/es.*o
%lang(ca) %appdir/examples/Image/Lighttable/.lang/ca.*o
%lang(cs) %appdir/examples/Image/Lighttable/.lang/cs.*o
%lang(de) %appdir/examples/Image/Lighttable/.lang/de.*o
%lang(en) %appdir/examples/Image/Lighttable/.lang/en.*o
%lang(fr) %appdir/examples/Misc/Console/.lang/fr.*o
%lang(ca) %appdir/examples/Misc/Evaluator/.lang/ca.*o
%lang(cs) %appdir/examples/Misc/Evaluator/.lang/cs.*o
%lang(de) %appdir/examples/Misc/Evaluator/.lang/de.*o
%lang(es) %appdir/examples/Misc/Evaluator/.lang/es.*o
%lang(ca) %appdir/examples/Misc/Explorer/.lang/ca.*o
%lang(cs) %appdir/examples/Misc/Explorer/.lang/cs.*o
%lang(de) %appdir/examples/Misc/Explorer/.lang/de.*o
%lang(es) %appdir/examples/Misc/Explorer/.lang/es.*o
%lang(ca) %appdir/examples/Misc/Notepad/.lang/ca.*o
%lang(cs) %appdir/examples/Misc/Notepad/.lang/cs.*o
%lang(de) %appdir/examples/Misc/Notepad/.lang/de.*o
%lang(es) %appdir/examples/Misc/Notepad/.lang/es.*o
%lang(ca) %appdir/examples/Misc/PDFViewer/.lang/ca.*o
%lang(cs) %appdir/examples/Misc/PDFViewer/.lang/cs.*o
%lang(de) %appdir/examples/Misc/PDFViewer/.lang/de.*o
%lang(es) %appdir/examples/Misc/PDFViewer/.lang/es.*o
%lang(ca) %appdir/examples/Networking/ClientSocket/.lang/ca.*o
%lang(cs) %appdir/examples/Networking/ClientSocket/.lang/cs.*o
%lang(de) %appdir/examples/Networking/ClientSocket/.lang/de.*o
%lang(es) %appdir/examples/Networking/ClientSocket/.lang/es.*o
%lang(ca) %appdir/examples/Networking/DnsClient/.lang/ca.*o
%lang(cs) %appdir/examples/Networking/DnsClient/.lang/cs.*o
%lang(de) %appdir/examples/Networking/DnsClient/.lang/de.*o
%lang(es) %appdir/examples/Networking/DnsClient/.lang/es.*o
%lang(ca) %appdir/examples/Networking/HTTPGet/.lang/ca.*o
%lang(cs) %appdir/examples/Networking/HTTPGet/.lang/cs.*o
%lang(de) %appdir/examples/Networking/HTTPGet/.lang/de.*o
%lang(es) %appdir/examples/Networking/HTTPGet/.lang/es.*o
%lang(ca) %appdir/examples/Networking/HTTPPost/.lang/ca.*o
%lang(cs) %appdir/examples/Networking/HTTPPost/.lang/cs.*o
%lang(de) %appdir/examples/Networking/HTTPPost/.lang/de.*o
%lang(es) %appdir/examples/Networking/HTTPPost/.lang/es.*o
%lang(ca) %appdir/examples/Networking/SerialPort/.lang/ca.*o
%lang(cs) %appdir/examples/Networking/SerialPort/.lang/cs.*o
%lang(es) %appdir/examples/Networking/SerialPort/.lang/es.*o
%lang(ca) %appdir/examples/Networking/ServerSocket/.lang/ca.*o
%lang(cs) %appdir/examples/Networking/ServerSocket/.lang/cs.*o
%lang(es) %appdir/examples/Networking/ServerSocket/.lang/es.*o
%lang(ca) %appdir/examples/Networking/UDPServerClient/.lang/ca.*o
%lang(cs) %appdir/examples/Networking/UDPServerClient/.lang/cs.*o
%lang(es) %appdir/examples/Networking/UDPServerClient/.lang/es.*o
%lang(ca) %appdir/examples/Networking/WebBrowser/.lang/ca.*o
%lang(cs) %appdir/examples/Networking/WebBrowser/.lang/cs.*o
%lang(de) %appdir/examples/Networking/WebBrowser/.lang/de.*o
%lang(es) %appdir/examples/Networking/WebBrowser/.lang/es.*o
%lang(ca) %appdir/examples/Sound/CDPlayer/.lang/ca.*o
%lang(cs) %appdir/examples/Sound/CDPlayer/.lang/cs.*o
%lang(es) %appdir/examples/Sound/CDPlayer/.lang/es.*o
%lang(ca) %appdir/examples/Sound/MusicPlayer/.lang/ca.*o
%lang(cs) %appdir/examples/Sound/MusicPlayer/.lang/cs.*o
%lang(es) %appdir/examples/Sound/MusicPlayer/.lang/es.*o
%lang(fr) %appdir/examples/Sound/MusicPlayer/.lang/fr.*o
%lang(ca) %appdir/examples/Video/MoviePlayer/.lang/ca.*o
%lang(cs) %appdir/examples/Video/MoviePlayer/.lang/cs.*o
%lang(es) %appdir/examples/Video/MoviePlayer/.lang/es.*o
%lang(ca) %appdir/examples/Video/MyWebCam/.lang/ca.*o
%lang(cs) %appdir/examples/Video/MyWebCam/.lang/cs.*o
%lang(es) %appdir/examples/Video/MyWebCam/.lang/es.*o

%files gb-cairo
%_libdir/%name/gb.cairo.*
%appdir/info/gb.cairo.*

%files gb-chart
%_libdir/%name/gb.chart.*
%appdir/info/gb.chart.*

%files gb-compress
%_libdir/%name/gb.compress.*
%appdir/info/gb.compress.*

%files gb-crypt
%_libdir/%name/gb.crypt.*
%appdir/info/gb.crypt.*

%files gb-db
%_libdir/%name/gb.db.component
%_libdir/%name/gb.db.gambas
%_libdir/%name/gb.db.la
%_libdir/%name/gb.db.so*
%appdir/info/gb.db.info
%appdir/info/gb.db.list

%files gb-db-form
%_libdir/%name/gb.db.form.*
%appdir/control/gb.db.form/
%appdir/info/gb.db.form.*

%files gb-db-mysql
%_libdir/%name/gb.db.mysql.*
%_libdir/%name/gb.mysql.*
%appdir/info/gb.db.mysql.*
%appdir/info/gb.mysql.*

%files gb-db-odbc
%_libdir/%name/gb.db.odbc.*
%appdir/info/gb.db.odbc.*

%files gb-db-postgresql
%_libdir/%name/gb.db.postgresql.*
%appdir/info/gb.db.postgresql.*

%files gb-db-sqlite2
%_libdir/%name/gb.db.sqlite2.*
%appdir/info/gb.db.sqlite2.*

%files gb-db-sqlite3
%_libdir/%name/gb.db.sqlite3.*
%appdir/info/gb.db.sqlite3.*

%files gb-dbus
%_libdir/%name/gb.dbus.*
%appdir/info/gb.dbus.*

%files gb-desktop
%_libdir/%name/gb.desktop.*
%appdir/control/gb.desktop/
%appdir/info/gb.desktop.*

%files gb-eval-highlight
%_libdir/%name/gb.eval.highlight.*
%appdir/info/gb.eval.highlight.*

%files gb-form
%_libdir/%name/gb.form.component
%_libdir/%name/gb.form.gambas
%appdir/control/gb.form/
%appdir/info/gb.form.info
%appdir/info/gb.form.list

%files gb-form-dialog
%_libdir/%name/gb.form.dialog.component
%_libdir/%name/gb.form.dialog.gambas
%appdir/info/gb.form.dialog.info
%appdir/info/gb.form.dialog.list

%files gb-form-mdi
%_libdir/%name/gb.form.mdi.component
%_libdir/%name/gb.form.mdi.gambas
%appdir/control/gb.form.mdi/
%appdir/info/gb.form.mdi.info
%appdir/info/gb.form.mdi.list

%files gb-form-stock
%_libdir/%name/gb.form.stock.component
%_libdir/%name/gb.form.stock.gambas
%appdir/info/gb.form.stock.info
%appdir/info/gb.form.stock.list

%files gb-gtk
%_libdir/%name/gb.gtk.component
%_libdir/%name/gb.gtk.gambas
%_libdir/%name/gb.gtk.so*
%_libdir/%name/gb.gtk.la
%appdir/info/gb.gtk.info
%appdir/info/gb.gtk.list

%files gb-gui
%_libdir/%name/gb.gui.*
%appdir/info/gb.gui.*

%files gb-image
%_libdir/%name/gb.image.component
%_libdir/%name/gb.image.so*
%_libdir/%name/gb.image.la
%appdir/info/gb.image.info
%appdir/info/gb.image.list

%files gb-image-effect
%_libdir/%name/gb.image.effect.*
%appdir/info/gb.image.effect.*

%files gb-image-imlib
%_libdir/%name/gb.image.imlib.*
%appdir/info/gb.image.imlib.*

%files gb-image-io
%_libdir/%name/gb.image.io.*
%appdir/info/gb.image.io.*

%files gb-net
%_libdir/%name/gb.net.component
%_libdir/%name/gb.net.so*
%_libdir/%name/gb.net.la
%appdir/info/gb.net.info
%appdir/info/gb.net.list

%files gb-net-curl
%_libdir/%name/gb.net.curl.*
%appdir/info/gb.net.curl.*

%files gb-net-smtp
%_libdir/%name/gb.net.smtp.*
%appdir/info/gb.net.smtp.*

%if_enabled opengl
%files gb-opengl
%_libdir/%name/gb.opengl.component
%_libdir/%name/gb.opengl.so*
%_libdir/%name/gb.opengl.la
%appdir/info/gb.opengl.info
%appdir/info/gb.opengl.list

%files gb-opengl-glu
%_libdir/%name/gb.opengl.glu.*
%appdir/info/gb.opengl.glu.*

%files gb-opengl-glsl
%_libdir/%name/gb.opengl.glsl.*
%appdir/info/gb.opengl.glsl.*
%endif

%files gb-option
%_libdir/%name/gb.option.*
%appdir/info/gb.option.*

%files gb-pcre
%_libdir/%name/gb.pcre.*
%appdir/info/gb.pcre.*

%files gb-pdf
%_libdir/%name/gb.pdf.component
%_libdir/%name/gb.pdf.so*
%_libdir/%name/gb.pdf.la
%appdir/info/gb.pdf.info
%appdir/info/gb.pdf.list

%files gb-qt4 
%_libdir/%name/gb.qt4.component
%_libdir/%name/gb.qt4.gambas 
%_libdir/%name/gb.qt4.so* 
%_libdir/%name/gb.qt4.la 
%appdir/info/gb.qt4.info 
%appdir/info/gb.qt4.list

%files gb-qt4-ext
%_libdir/%name/gb.qt4.ext.*
%appdir/info/gb.qt4.ext.*

%files gb-qt4-opengl
%_libdir/%name/gb.qt4.opengl.*
%appdir/info/gb.qt4.opengl.*

%files gb-qt4-webkit
%_libdir/%name/gb.qt4.webkit.*
%appdir/info/gb.qt4.webkit.*

%files gb-report
%_libdir/%name/gb.report.*
%appdir/control/gb.report/
%appdir/info/gb.report.*

%files gb-sdl
%_libdir/%name/gb.sdl.component
%_libdir/%name/gb.sdl.so
%_libdir/%name/gb.sdl.so.*
%_libdir/%name/gb.sdl.la
%appdir/info/gb.sdl.info
%appdir/info/gb.sdl.list
%appdir/gb.sdl/

%files gb-sdl-sound
%_libdir/%name/gb.sdl.sound.*
%appdir/info/gb.sdl.sound.*

%files gb-settings
%_libdir/%name/gb.settings.*
%appdir/info/gb.settings.*

%files gb-signal
%_libdir/%name/gb.signal.*
%appdir/info/gb.signal.*

%files gb-v4l
%_libdir/%name/gb.v4l.*
%appdir/info/gb.v4l.*

%files gb-vb
%_libdir/%name/gb.vb.*
%appdir/info/gb.vb.*

%files gb-web
%_libdir/%name/gb.web.*
%appdir/info/gb.web.*

%files gb-xml
%_libdir/%name/gb.xml.component
%_libdir/%name/gb.xml.so*
%_libdir/%name/gb.xml.la
%appdir/info/gb.xml.info
%appdir/info/gb.xml.list

%files gb-xml-rpc
%_libdir/%name/gb.xml.rpc.*
%appdir/info/gb.xml.rpc.*

%files gb-xml-xslt
%_libdir/%name/gb.xml.xslt.*
%appdir/info/gb.xml.xslt.*

%changelog
* Wed Feb 01 2012 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt4
- gambas3-examples  provides gambas3-full to complete installation

* Tue Jan 31 2012 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt3
- Disable OpenGL support

* Wed Jan 25 2012 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt2
- Set gambas3-examples as noarch
- Fix dependences on DejaVu font

* Mon Jan 23 2012 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus
