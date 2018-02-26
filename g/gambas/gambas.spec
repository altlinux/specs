%def_enable firebird 
%def_enable mysql
%def_enable postgresql
%def_enable odbc
%def_enable sdl

Name: gambas
Version: 2.23.1
Release: alt1

Packager: Andrey Cherepanov <cas@altlinux.org>

Summary: Free and complete development environment based on a basic interpreter with object extensions
Group: Development/Other
License: GPL
Url: http://gambas.sourceforge.net

BuildRequires: bzlib-devel gcc-c++ imake kdelibs-devel libGL-devel
BuildRequires: libXtst-devel libcurl-devel libffi-devel libjpeg-devel 
BuildRequires: libomniORB-devel libpoppler13-devel libqt3-devel librsvg-devel 
BuildRequires: libsqlite3-devel libxslt-devel xorg-cf-files xorg-inputproto-devel
BuildRequires: libgtk+2-devel 

%if_enabled firebird 
BuildRequires: firebird-devel
%endif
%if_enabled postgresql
BuildRequires: postgresql-devel
%endif
%if_enabled mysql
BuildRequires: libMySQL-devel
%endif
%if_enabled odbc
BuildRequires: libunixODBC-devel
%endif

%if_enabled sdl
BuildRequires: libSDL-devel libSDL_image-devel libSDL_mixer-devel
%endif

Source0: %name-%version-%release.tar
Source1: %name.desktop

Patch1: gambas-2.14-alt-unresolved.patch
Patch2: gambas-2.22.0-firebird-permissive-fix.patch

%description
Gambas is a free development environment based on a Basic interpreter
with object extensions, like Visual Basic(tm) (but it is NOT a clone!).
With Gambas, you can quickly design your program GUI, access MySQL or
PostgreSQL databases, control KDE applications with DCOP, translate
your program into many languages, create network applications easily,
build RPMs of your apps automatically, and so on...

%package runtime
Summary: The Gambas runtime
Group: Development/Other

%description runtime
This package includes the Gambas interpreter needed to run Gambas applications.

%package devel
Summary: The Gambas compiler
Group: Development/Other

%description devel
This package includes the Gambas compiler, archiever and informer.

%package ide
Summary: The Gambas IDE
Group: Development/Other
Requires: %name-runtime = %version-%release
Requires: %name-devel = %version-%release
Requires: %name-gb-chart = %version-%release
Requires: %name-gb-compress = %version-%release
Requires: %name-gb-corba = %version-%release
Requires: %name-gb-crypt = %version-%release
Requires: %name-gb-db = %version-%release
Requires: %name-gb-db-form = %version-%release
Requires: %name-gb-desktop = %version-%release
Requires: %name-gb-form = %version-%release
Requires: %name-gb-form-dialog = %version-%release
Requires: %name-gb-form-mdi = %version-%release
Requires: %name-gb-gtk = %version-%release
Requires: %name-gb-gtk-ext = %version-%release
Requires: %name-gb-gtk-svg = %version-%release
Requires: %name-gb-gui = %version-%release
Requires: %name-gb-image = %version-%release
Requires: %name-gb-info = %version-%release
Requires: %name-gb-net = %version-%release
Requires: %name-gb-net-curl = %version-%release
Requires: %name-gb-net-smtp = %version-%release
Requires: %name-gb-opengl = %version-%release
Requires: %name-gb-option = %version-%release
Requires: %name-gb-pcre = %version-%release
Requires: %name-gb-pdf = %version-%release
Requires: %name-gb-qt = %version-%release
Requires: %name-gb-qt-ext = %version-%release
Requires: %name-gb-qt-kde = %version-%release
Requires: %name-gb-qt-kde-html = %version-%release
Requires: %name-gb-qt-opengl = %version-%release
Requires: %name-gb-report = %version-%release
Requires: %name-gb-sdl = %version-%release
Requires: %name-gb-sdl-sound = %version-%release
Requires: %name-gb-settings = %version-%release
Requires: %name-gb-v4l = %version-%release
Requires: %name-gb-vb = %version-%release
Requires: %name-gb-web = %version-%release
Requires: %name-gb-xml = %version-%release
Requires: %name-gb-xml-rpc = %version-%release
Requires: %name-gb-xml-xslt = %version-%release

Provides: gambas = %version-%release
Provides: gambas2 = %version-%release

%description ide
This package includes the complete Gambas Development Environment, with the
database manager, the help files, and all components.

%package examples
Summary: The examples for Gambas
Group: Development/Other
Requires: %name-ide = %version-%release

%description examples
The gambas-examples package contains some examples for gambas.

%package gb-compress
Summary: The Gambas compression component
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-compress
This component allows you to compress/uncompress data or files with
the bzip2 and zip algorithms.

%package gb-chart
Summary: The Gambas chart component
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-chart
This component contains chart support.

%package gb-corba
Summary: The Gambas CORBA component
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-corba
This component contains omniORB CORBA support.

%package gb-crypt
Summary: The Gambas crypto component
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-crypt
This component contains cryptography support.

%package gb-db
Summary: The Gambas database component
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-db
This component allows you to access many databases management systems,
provided that you install the needed driver packages.

%package gb-db-form
Summary: The Gambas database component
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-db-form
This component allows you to access many databases management systems,
provided that you install the needed driver packages.

%package gb-desktop
Summary: The Gambas XDG desktop integration component
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-desktop
This component allows you to operate with XDG-compliant desktop environmnents

%package gb-form
Summary: The Gambas visual form editor
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-form
This component allows you to construct various forms

%package gb-form-dialog
Summary: The Gambas addon for visual form editor
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-form-dialog
This component allows you to ease dialog forms construction

%package gb-form-mdi
Summary: The Gambas addon for visual form editor
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-form-mdi
This component allows you to ease mdi forms construction

%package gb-gtk
Summary: The Gambas GTK2 GUI component
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-gtk
This package includes the Gambas GTK2 GUI component.

%package gb-gtk-ext
Summary: The Gambas extended GTK2 GUI component
Group: Development/Other
Requires: %name-runtime = %version-%release %name-gb-gtk = %version-%release

%description gb-gtk-ext
This component includes extra GTK controls.

%package gb-gtk-svg
Summary: The Gambas SVG component
Group: Development/Other
Requires: %name-runtime = %version-%release %name-gb-gtk = %version-%release

%description gb-gtk-svg
This component includes SVG support.

%package gb-gui
Summary: The Gambas gui component
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-gui
This component contains something

%package gb-image
Summary: The Gambas image manipulation component
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-image
This component allows you to operate with various image formats

%package gb-info
Summary: The Gambas component info browser
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-info
This component allows you to browse component info.

%package gb-net
Summary: The Gambas networking component
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-net
This component allows you to use TCP/IP and UDP sockets, and to access
any serial ports.

%package gb-net-curl
Summary: The Gambas advanced networking component
Group: Development/Other
Requires: %name-runtime = %version-%release %name-gb-net = %version-%release

%description gb-net-curl
This component allows your programs to easily become FTP or HTTP clients.

%package gb-net-smtp
Summary: The Gambas advanced networking component
Group: Development/Other
Requires: %name-runtime = %version-%release %name-gb-net = %version-%release

%description gb-net-smtp
This component allows your programs to easily become SMTP clients.

%package gb-opengl
Summary: The Gambas OpenGL component
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-opengl
This package includes OpenGL support for the Gambas.

%package gb-option
Summary: The Gambas option component
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-option
This package includes Gambas option component.

%package gb-pcre
Summary: The Gambas regular expression component
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-pcre
This package includes Gambas support for regular expressions.

%package gb-pdf
Summary: The Gambas PDF support
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-pdf
This package includes Gambas support for PDF.

%package gb-qt
Summary: The Gambas Qt GUI component
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-qt
This package includes the Gambas QT GUI component.

%package gb-qt-ext
Summary: The Gambas extended Qt GUI component
Group: Development/Other
Requires: %name-runtime = %version-%release %name-gb-qt = %version-%release

%description gb-qt-ext
This component includes somme uncommon QT controls.

%package gb-qt-kde
Summary: The Gambas KDE component
Group: Development/Other
Requires: %name-runtime = %version-%release %name-gb-qt = %version-%release

%description gb-qt-kde
This component transforms your QT application in a KDE application, and
allows you to pilot any other KDE application with the DCOP protocol.

%package gb-qt-kde-html
Summary: The Gambas KHTML component
Group: Development/Other
Requires: %name-runtime = %version-%release %name-gb-qt-kde = %version-%release

%description gb-qt-kde-html
This component allows you to use the KHTML Web Browser widget included in KDE.

%package gb-qt-opengl
Summary: The Gambas OpenGL/Qt component
Group: Development/Other
Requires: %name-runtime = %version-%release %name-gb-qt = %version-%release

%description gb-qt-opengl
This component contains support for Qt/OpenGL for Gambas.

%package gb-report
Summary: The Gambas report producing component
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-report
This component allows to produce various reports

%package gb-sdl
Summary: The Gambas SDL component
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-sdl
This component contains bindings to SDL library.

%package gb-sdl-sound
Summary: The Gambas SDL sound component
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-sdl-sound
This component contains the sound part of the SDL library. It allows you to
simultaneously play many sounds and a music stored in a file.

%package gb-settings
Summary: The another Gambas component
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-settings
This component contains something.

%package gb-v4l
Summary: The Gambas V4L component
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-v4l
This component allows access to Video4Linux devices.

%package gb-vb
Summary: The Gambas Visual Basic(tm) compatibility component
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-vb
This component aims at including some functions that imitate the behaviour
of Visual Basic(tm) functions. Use it only if you try to port some VB
projects.

%package gb-web
Summary: The Gambas Web component
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-web
This component contains Web-oriented tasks support.

%package gb-xml
Summary: The Gambas XML components based on the libxml and libxslt libraries.
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-xml
These components brings the power of the libxml and libxslt libraries to
Gambas.

%package gb-xml-rpc
Summary: The Gambas XML components based on the libxml and libxslt libraries.
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-xml-rpc
These components brings the power of the libxml and libxslt libraries to
Gambas.

%package gb-xml-xslt
Summary: The Gambas XML components based on the libxml and libxslt libraries.
Group: Development/Other
Requires: %name-runtime = %version-%release

%description gb-xml-xslt
These components brings the power of the libxml and libxslt libraries to
Gambas.

%prep
%setup
sed -i 's,lib/gambas,%_lib/gambas,' main/gbc/gbi.c main/gbx/gbx_project.c
%patch1 -p1
%patch2 -p1
cp %SOURCE1 gambas.desktop

./reconf-all

%build
%configure \
    --disable-sqlite2 \
    --disable-qte \
    %{subst_enable postgresql} \
    %{subst_enable mysql} \
    %{subst_enable odbc} \
    %{subst_enable sdl} \
    --enable-corba \
    --enable-intl \
    --enable-conv \
    --enable-qt \
    --enable-kde \
    --with-kde-includes='%_K3includedir %_includedir/tqtinterface' \
    --with-kde-libraries=%_K3libdir \
    --enable-net \
    --enable-curl \
    --enable-firebird \
    --enable-sqlite3 \
    --enable-vb \
    --enable-pdf \
    --enable-dependency-tracking 
    #

grep -rl '@QT.\+LDFLAGS@' gb.qt/ |xargs sed -i 's/@QT.\+LDFLAGS@//g'
%make_build

%install
%make DESTDIR=%buildroot libdir=%_libdir install
install -pD -m644 app/src/gambas2/img/16/gambas.png %buildroot%_miconsdir/gambas.png
install -pD -m644 app/src/gambas2/img/32/gambas.png %buildroot%_niconsdir/gambas.png
install -pD -m644 gambas.desktop %buildroot%_desktopdir/gambas2.desktop
%set_compress_method skip

%files runtime
%doc README COPYING
%_bindir/gbr2
%_bindir/gbx2
%_bindir/gbs2*

%dir %_libdir/gambas2
%dir %_datadir/gambas2
%dir %_datadir/gambas2/info

%_libdir/gambas2/gb.component
%_datadir/gambas2/info/gb.info
%_datadir/gambas2/info/gb.list

%_libdir/gambas2/gb.debug.component
%_libdir/gambas2/gb.debug.so*
%_libdir/gambas2/gb.debug.la
%_datadir/gambas2/info/gb.debug.info
%_datadir/gambas2/info/gb.debug.list

%_libdir/gambas2/gb.eval.component
%_libdir/gambas2/gb.eval.so*
%_libdir/gambas2/gb.eval.la
%_datadir/gambas2/info/gb.eval.info
%_datadir/gambas2/info/gb.eval.list

# wtf there for ?
%_libdir/gambas2/gb.draw.so*
%_libdir/gambas2/gb.draw.la

%files devel
%_bindir/gba2
%_bindir/gbc2
%_bindir/gbi2

%files ide
%_bindir/gambas2
%_bindir/gambas2.gambas
%_bindir/gambas2-database-manager*
%_datadir/gambas2/help
%_miconsdir/gambas.png
%_niconsdir/gambas.png
%_desktopdir/gambas2.desktop

%files examples
%_datadir/gambas2/examples

%files gb-compress
%_libdir/gambas2/gb.compress.*
%_datadir/gambas2/info/gb.compress.*

%files gb-corba
%_libdir/gambas2/gb.corba.component
%_libdir/gambas2/gb.corba.la
%_libdir/gambas2/gb.corba.so*
%_datadir/gambas2/info/gb.corba.info
%_datadir/gambas2/info/gb.corba.list

%files gb-crypt
%_libdir/gambas2/gb.crypt.*
%_datadir/gambas2/info/gb.crypt.*

%files gb-chart
%_libdir/gambas2/gb.chart.*
%_datadir/gambas2/info/gb.chart.*

%files gb-db
%_libdir/gambas2/gb.db.component
%_libdir/gambas2/gb.db.la
%_libdir/gambas2/gb.db.so*

%_libdir/gambas2/gb.db.sqlite3.*

%if_enabled firebird
%_libdir/gambas2/gb.db.firebird.*
%endif

%if_enabled mysql
%_libdir/gambas2/gb.db.mysql.*
%endif

%if_enabled postgresql
%_libdir/gambas2/gb.db.postgresql.*
%endif

%if_enabled odbc
%_libdir/gambas2/gb.db.odbc.*
%endif

%_datadir/gambas2/info/gb.db.info
%_datadir/gambas2/info/gb.db.list

%files gb-db-form
%_libdir/gambas2/gb.db.form.component
%_libdir/gambas2/gb.db.form.gambas
%_datadir/gambas2/info/gb.db.form.info
%_datadir/gambas2/info/gb.db.form.list

%files gb-desktop
%_libdir/gambas2/gb.desktop.component
%_libdir/gambas2/gb.desktop.gambas
%_libdir/gambas2/gb.desktop.so*
%_libdir/gambas2/gb.desktop.la
%_datadir/gambas2/info/gb.desktop.info
%_datadir/gambas2/info/gb.desktop.list

%files gb-form
%_libdir/gambas2/gb.form.component
%_libdir/gambas2/gb.form.gambas
%_datadir/gambas2/info/gb.form.info
%_datadir/gambas2/info/gb.form.list

%files gb-form-dialog
%_libdir/gambas2/gb.form.dialog.component
%_libdir/gambas2/gb.form.dialog.gambas
%_datadir/gambas2/info/gb.form.dialog.info
%_datadir/gambas2/info/gb.form.dialog.list

%files gb-form-mdi
%_libdir/gambas2/gb.form.mdi.component
%_libdir/gambas2/gb.form.mdi.gambas
%_datadir/gambas2/info/gb.form.mdi.info
%_datadir/gambas2/info/gb.form.mdi.list

%files gb-gtk
%_libdir/gambas2/gb.gtk.component
%_libdir/gambas2/gb.gtk.gambas
%_libdir/gambas2/gb.gtk.so*
%_libdir/gambas2/gb.gtk.la
%_datadir/gambas2/info/gb.gtk.info
%_datadir/gambas2/info/gb.gtk.list

%files gb-gtk-ext
%_libdir/gambas2/gb.gtk.ext.component
%_libdir/gambas2/gb.gtk.ext.so*
%_libdir/gambas2/gb.gtk.ext.la
%_datadir/gambas2/info/gb.gtk.ext.info
%_datadir/gambas2/info/gb.gtk.ext.list

%files gb-gtk-svg
%_libdir/gambas2/gb.gtk.svg.component
%_libdir/gambas2/gb.gtk.svg.so*
%_libdir/gambas2/gb.gtk.svg.la
%_datadir/gambas2/info/gb.gtk.svg.info
%_datadir/gambas2/info/gb.gtk.svg.list

%files gb-gui
%_libdir/gambas2/gb.gui.component
%_libdir/gambas2/gb.gui.so*
%_libdir/gambas2/gb.gui.la
%_datadir/gambas2/info/gb.gui.info
%_datadir/gambas2/info/gb.gui.list

%files gb-image
%_libdir/gambas2/gb.image.component
%_libdir/gambas2/gb.image.so*
%_libdir/gambas2/gb.image.la
%_datadir/gambas2/info/gb.image.info
%_datadir/gambas2/info/gb.image.list

%files gb-info
%_libdir/gambas2/gb.info.component
%_libdir/gambas2/gb.info.gambas
%_datadir/gambas2/info/gb.info.info
%_datadir/gambas2/info/gb.info.list

%files gb-net
%_libdir/gambas2/gb.net.component
%_libdir/gambas2/gb.net.so*
%_libdir/gambas2/gb.net.la
%_datadir/gambas2/info/gb.net.info
%_datadir/gambas2/info/gb.net.list

%files gb-net-curl
%_libdir/gambas2/gb.net.curl.component
%_libdir/gambas2/gb.net.curl.so*
%_libdir/gambas2/gb.net.curl.la
%_datadir/gambas2/info/gb.net.curl.info
%_datadir/gambas2/info/gb.net.curl.list

%files gb-net-smtp
%_libdir/gambas2/gb.net.smtp.component
%_libdir/gambas2/gb.net.smtp.so*
%_libdir/gambas2/gb.net.smtp.la
%_datadir/gambas2/info/gb.net.smtp.info
%_datadir/gambas2/info/gb.net.smtp.list

%files gb-opengl
%_libdir/gambas2/gb.opengl.component
%_libdir/gambas2/gb.opengl.so*
%_libdir/gambas2/gb.opengl.la
%_datadir/gambas2/info/gb.opengl.info
%_datadir/gambas2/info/gb.opengl.list

%files gb-option
%_libdir/gambas2/gb.option.component
%_libdir/gambas2/gb.option.so*
%_libdir/gambas2/gb.option.la
%_datadir/gambas2/info/gb.option.info
%_datadir/gambas2/info/gb.option.list

%files gb-pcre
%_libdir/gambas2/gb.pcre.component
%_libdir/gambas2/gb.pcre.so*
%_libdir/gambas2/gb.pcre.la
%_datadir/gambas2/info/gb.pcre.info
%_datadir/gambas2/info/gb.pcre.list

%files gb-pdf
%_libdir/gambas2/gb.pdf.component
%_libdir/gambas2/gb.pdf.so*
%_libdir/gambas2/gb.pdf.la
%_datadir/gambas2/info/gb.pdf.info
%_datadir/gambas2/info/gb.pdf.list

%files gb-qt
%_libdir/gambas2/gb.qt.component
%_libdir/gambas2/gb.qt.gambas
%_libdir/gambas2/gb.qt.so*
%_libdir/gambas2/gb.qt.la
%_datadir/gambas2/info/gb.qt.info
%_datadir/gambas2/info/gb.qt.list

%files gb-qt-ext
%_libdir/gambas2/gb.qt.ext.component
%_libdir/gambas2/gb.qt.ext.so*
%_libdir/gambas2/gb.qt.ext.la
%_datadir/gambas2/info/gb.qt.ext.info
%_datadir/gambas2/info/gb.qt.ext.list

%files gb-qt-kde
%_libdir/gambas2/gb.qt.kde.component
%_libdir/gambas2/gb.qt.kde.so*
%_libdir/gambas2/gb.qt.kde.la
%_datadir/gambas2/info/gb.qt.kde.info
%_datadir/gambas2/info/gb.qt.kde.list

%files gb-qt-kde-html
%_libdir/gambas2/gb.qt.kde.html.component
%_libdir/gambas2/gb.qt.kde.html.so*
%_libdir/gambas2/gb.qt.kde.html.la
%_datadir/gambas2/info/gb.qt.kde.html.info
%_datadir/gambas2/info/gb.qt.kde.html.list

%files gb-qt-opengl
%_libdir/gambas2/gb.qt.opengl.component
%_libdir/gambas2/gb.qt.opengl.so*
%_libdir/gambas2/gb.qt.opengl.la
%_datadir/gambas2/info/gb.qt.opengl.info
%_datadir/gambas2/info/gb.qt.opengl.list

%files gb-report
%_libdir/gambas2/gb.report.component
%_libdir/gambas2/gb.report.gambas
%_datadir/gambas2/info/gb.report.info
%_datadir/gambas2/info/gb.report.list

%if_enabled sdl
%files gb-sdl
%_libdir/gambas2/gb.sdl.component
%_libdir/gambas2/gb.sdl.so
%_libdir/gambas2/gb.sdl.so.*
%_libdir/gambas2/gb.sdl.la
%_datadir/gambas2/info/gb.sdl.info
%_datadir/gambas2/info/gb.sdl.list

%files gb-sdl-sound
%_libdir/gambas2/gb.sdl.sound.component
%_libdir/gambas2/gb.sdl.sound.so*
%_libdir/gambas2/gb.sdl.sound.la
%_datadir/gambas2/info/gb.sdl.sound.info
%_datadir/gambas2/info/gb.sdl.sound.list
%endif

%files gb-settings
%_libdir/gambas2/gb.settings.component
%_libdir/gambas2/gb.settings.gambas
%_datadir/gambas2/info/gb.settings.info
%_datadir/gambas2/info/gb.settings.list

%files gb-v4l
%_libdir/gambas2/gb.v4l.component
%_libdir/gambas2/gb.v4l.so*
%_libdir/gambas2/gb.v4l.la
%_datadir/gambas2/info/gb.v4l.info
%_datadir/gambas2/info/gb.v4l.list

%files gb-vb
%_libdir/gambas2/gb.vb.la
%_libdir/gambas2/gb.vb.so*
%_libdir/gambas2/gb.vb.component
%_datadir/gambas2/info/gb.vb.info
%_datadir/gambas2/info/gb.vb.list

%files gb-web
%_libdir/gambas2/gb.web.component
%_libdir/gambas2/gb.web.gambas
%_datadir/gambas2/info/gb.web.info
%_datadir/gambas2/info/gb.web.list

%files gb-xml
%_libdir/gambas2/gb.xml.so*
%_libdir/gambas2/gb.xml.la
%_libdir/gambas2/gb.xml.component
%_datadir/gambas2/info/gb.xml.info
%_datadir/gambas2/info/gb.xml.list

%files gb-xml-rpc
%_libdir/gambas2/gb.xml.rpc.component
%_libdir/gambas2/gb.xml.rpc.gambas
%_datadir/gambas2/info/gb.xml.rpc.info
%_datadir/gambas2/info/gb.xml.rpc.list

%files gb-xml-xslt
%_libdir/gambas2/gb.xml.xslt.so*
%_libdir/gambas2/gb.xml.xslt.la
%_libdir/gambas2/gb.xml.xslt.component
%_datadir/gambas2/info/gb.xml.xslt.info
%_datadir/gambas2/info/gb.xml.xslt.list

%changelog
* Wed Nov 16 2011 Andrey Cherepanov <cas@altlinux.org> 2.23.1-alt1
- New version 2.23.1

* Fri May 06 2011 Andrey Cherepanov <cas@altlinux.org> 2.23.0-alt2
- Add all modules as gambas-ide requires (closes: #17042)
- gambas-ide provides both gambas and gambas2

* Wed May 04 2011 Andrey Cherepanov <cas@altlinux.org> 2.23.0-alt1
- New version 2.23.0
- Add Firebird support to gambas-gb-db
- Adapt to new KDE3 placement

* Thu Oct 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.18.0-alt1.2
- Rebuilt with libomniORB 4.2.0

* Tue Aug 03 2010 Sergey V Turchin <zerg@altlinux.org> 2.18.0-alt1.1
- rebuilt with new poppler

* Mon Nov 23 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 2.18.0-alt1
- 2.18.0

* Sun Oct 25 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 2.17.0-alt1
- 2.17.0

* Tue Sep 15 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 2.16.0-alt2
- Rebuild with new poppler

* Thu Sep 10 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 2.16.0-alt1
- 2.16.0

* Sun Aug 16 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 2.15.2-alt1
- 2.15.2

* Mon Jul 27 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 2.15.0-alt1
- 2.15.0 (ALT #20233)

* Thu Jul 16 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 2.14.0-alt1
- 2.14.0

* Mon May 12 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.0-alt1
- 2.6.0 released

* Mon Apr 28 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.0-alt1
- 2.5.0 released

* Sat Mar 29 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.1-alt1
- 2.4.1 released

* Fri Jan  4 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.0-alt1
- 2.0.0 released

* Fri Nov 16 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.9.91-alt1
- 1.9.91

* Thu Oct 18 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.9.90-alt1
- 1.9.90

* Tue Jul 10 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.9.49-alt1
- 1.9.49

* Thu Jul  5 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.18-alt1
- 1.0.18

* Fri Sep 02 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.11-alt1
- 1.0.11

* Mon Aug 15 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.10-alt1
- 1.0.10

* Sat Jul 23 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.9-alt1
- 1.0.9

* Tue Jul 12 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Mon Jul 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Mon May 30 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.6-alt2
- fixed buildrequires

* Wed May 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Thu Mar 10 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Thu Jan 13 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Wed Jan 05 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Tue Dec 21 2004 Valery Inozemtsev <shrek@altlinux.ru> 0.99.RC5-alt1
- 1.0.RC5

* Fri Nov 12 2004 Valery Inozemtsev <shrek@altlinux.ru> 0.99.RC2-alt2
- fixed requires (#5486)
- fixed examples (#5487)

* Mon Nov 08 2004 Valery Inozemtsev <shrek@altlinux.ru> 0.99.RC2-alt1
- 1.0.RC2

* Sun Nov 07 2004 Valery Inozemtsev <shrek@altlinux.ru> 0.99.RC1-alt1
- new version

* Thu Jun 03 2004 Valery Inozemtsev <shrek@altlinux.ru> 0.93b-alt1
- initial release 
