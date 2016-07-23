#
# spec file for package tqt3 (version R14)
#
# Copyright (c) 2014 Trinity Desktop Environment
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#
# Vendor:		Trinity Project

# TDE variables
%define tde_version 14.0.3
%define tqtdir	%_libdir/tqt3-%tde_version
%define tdir tqt3-%tde_version
%define kdedir  %prefix
%define libname	libtqt
%define tqinclude %_includedir/tqt3
%define tqdoc %_docdir/%name-%tde_version

# Versions
%define rname	tqt
# %%define major	3.5
%define minor	3
%define bugfix	8

Name: trinity-tqt3
Version: 3.5.0
Release: alt1
Summary: TQt GUI Library, Version 3
Group: System/Libraries
Url: http://www.trinitydesktop.org/

License: GPLv2+

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name-%tde_version%{?preversion:~%preversion}.tar
Source1: build-examples.sh

%define with_settings 0
%define build_qsa 0

%define with_ibase 1
%define debug 0
%define qt_copy 0
%define building 0

%define _keep_libtool_files 1
%define _optlevel s
%define static_nonthr 0
%define shared_nonthr 0
%define build_xt 0

%define build_qsa 0
%define build_odbc 1
%define with_settings 0
%define with_nas 0
%define versioning_hack 0

%if %with_settings
Source121: qtX-set-tqtdir-environment-csh
Source122: qtX-set-tqtdir-environment-sh
%endif
#
Source5: qtX-designer-sh
Source6: qtX-assistant-sh
Source8: qtX-README.distribution
Source9: qtX-linguist-sh
%if %with_settings
Source10: qtrc
%endif
Source11: qt-ru-3.3.2-20040604.tar
Source12: wrap_kde_malloc.cpp
#
Source21: qt3-assistant.desktop
Source22: qt3-designer.desktop
Source23: qt3-linguist.desktop
Source24: qt3-qtconfig.desktop

Source101: qt.16.png
Source102: qt.32.png
Source103: qt.48.png

#Source200: Xinerama.tar
%if %build_qsa
Source1000: qsa-x11-free-%qsa_ver.tar
%endif

Source111: tqassistant.desktop
Source112: tqdesigner.desktop
Source113: tqlinguist.desktop
Source114: tqtconfig.desktop

# FC
Patch2: qt-3.0.5-nodebug.patch
Patch3: qt-3.3.8d-xim.patch
Patch4: qt-3.1.0-makefile.patch
Patch5: qt-x11-free-3.1.0-editor.patch
Patch6: qt-x11-free-3.1.0-assistant.patch
Patch7: qt-x11-free-3.2.2-designer.patch
Patch8: qt-x11-free-3.1.1-qmotif.patch
Patch9: qt-x11-free-3.3.8b-uic-multilib-ALT.patch
Patch10: qt-x11-free-3.1.0-header.patch
Patch11: qt-x11-free-3.3.4-mono.patch
Patch12: qt-x11-free-3.3.8d-strip.patch
Patch13: qt-x11-free-3.3.4-qfontdatabase_x11.patch
Patch14: qt-x11-free-3.3.8d-gcc4-buildkey.patch
Patch15: qt-visibility-alt.patch
Patch16: qt-x11-free-3.3.7-umask.patch
Patch17: qt-3.3.6-fontrendering-214371.patch
Patch18: qt-3.3.8-fontrendering-#214570.patch
Patch19: qt-3.3.8-fontrendering-as_IN-209972.patch

# MDK
Patch21: qt-3.0.5-fix-pyqt-config.patch
Patch22: qt3-opentype-aliasing.patch

# SuSE
Patch30: qt3-never-strip.diff
Patch31: shut-up.diff
#
Patch33: lib64-plugin-support.diff
Patch34: pluginmanager-fix.diff
#
Patch38: kmenu-search-fix.diff

# Qt-copy
Patch51: 0046-qiconview-no-useless-scrollbar.diff
Patch52: 0078-argb-visual-hack.patch
Patch53: 0088-fix-xinput-clash.diff

# ALT
Patch100: qt-3.3.3-alt-homedir.patch
Patch101: qt-3.3.0-alt-honor-SUSv3-locales.patch %{nil by raorn@alt}
Patch102: qt-3.2.3-alt-designer_add_translator.patch
Patch103: qt-3.2.3-alt-qtconfig_add_translator.patch
Patch104: qt-3.3.5-alt-buildkey-nomachine.patch
Patch105: qt-3.3.0-alt-shared_libs.patch
Patch106: qt-3.3.1-alt-iso_c_extension.patch
Patch107: qt-x11-free-3.3.6-alt-maccyrillic.patch
Patch108: qt-3.3.8d-alt-arm-no-packed-pointers.patch
Patch109: qt-x11-free-3.3.8d-Lib64.patch
Patch110: qt-3.3.8d-full-hiden-item-QIconView.patch

# Sergey A. Sukiyazov <sukiyazov@mail.ru>
Patch9000: 9000-qt-x11-free-3.3.3-menubar.patch
Patch9001: 9001-qt-x11-free-3.3.3-psprinter-ALT.patch
Patch9002: 9002-qt-x11-free-3.3.6-strlist.patch
Patch9003: 9003-qt-x11-free-3.3.3-textstream.patch
Patch9004: 9004-qt-x11-free-3.3.4-uridrag.patch
Patch9005: 9005-qt-x11-free-3.3.8b-codecs.patch
Patch9006: 9006-qt-x11-free-3.3.3-codecs-utf8.patch
Patch9007: 9100-qt-x11-free-3.3.8-fix_shortcuts.patch

Patch400: trinnity-tqt3_DEFAULT_SOURCE-3.5.patch

# Automatically added by buildreq on Sat Jul 23 2016
# optimized out: fontconfig fontconfig-devel libGL-devel libICE-devel libSM-devel libX11-devel libXext-devel libXrender-devel libXt-devel libfreetype-devel libjpeg-devel libpq-devel libstdc++-devel libunixODBC-devel-compat perl python-base python-modules xorg-inputproto-devel xorg-kbproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xextproto-devel xorg-xproto-devel zlib-devel
BuildPreReq: firebird-devel gcc-c++ libGLU-devel libXcursor-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXrandr-devel libcups-devel libmng-devel libmysqlclient-devel
BuildPreReq: libunixODBC-devel libuuid-devel postgresql-devel

BuildPreReq: zlib-devel libjpeg-devel libmng-devel libgif-devel  libfreetype-devel fontconfig-devel libcups-devel libuuid-devel libaudio-devel  libXrender-devel libXcursor-devel  libXinerama-devel
BuildPreReq: libXft-devel libXext-devel libX11-devel libSM-devel libICE-devel libXt-devel  libXmu-devel  libXi-devel xorg-proto-devel libGL-devel libGLU-devel
BuildPreReq: libmysql++-devel libunixODBC-devel libsqlite-devel libsqlite3-devel postgresql postgresql-devel firebird-devel

# BEGIN SourceDeps(oneline):
BuildRequires: liblcms-devel libuuid-devel libpnglite-devel
BuildRequires: libpng++-devel libpng-devel
# END SourceDeps(oneline)

# GCC visibility stuff
%define EXTRA_CFLAGS -fvisibility=hidden -fvisibility-inlines-hidden

%description
This is the Trolltech TQt library, version 3. It's necessary for
applications that link against the libtqt-mt.so.3, e.g. all Trinity
applications.

##########

Summary: TQt GUI Library (Threaded runtime version), Version 3
Group: System/Libraries
Provides: qt3-mt = %version-%release
Provides: tqt3 = %version-%release
Provides: libtqt3 = %version-%release

%description
This is the Trolltech TQt library, version 3. It's necessary for
applications that link against the libtqt-mt.so.3, e.g. all Trinity
applications.

###########

%package -n libtqt3-devel
Summary: TQt development files (Threaded)
Group: Development/KDE and QT
Provides: trinity-tqt3-devel = %version-%release
Provides: tqt3-devel = %version-%release
Requires: %name = %version-%release

%description -n libtqt3-devel
TQt is a C++ class library optimized for graphical user interface
development. This package contains the libtqt-mt.so symlink, necessary
for building threaded TQt applications as well as the libtqui.so symlink
and the necessary header files for libtqui.so. (See README.Debian and
the TQt Documentation for instructions on libtqui.so)

WARNING: If you plan to build some older TQt3 applications, you will
most probably have to install the tqt3-compat-headers package. It
contains all the headers which are not part of the official TQt3 API
anymore but which are still used by some programs. So if you encounter
problems with missing header files, please install this package first
before you send a bugreport.

##########

%package -n libtqt3-mt-mysql
Summary: MySQL database driver for TQt3 (Threaded)
Group: System/Libraries
Provides: tqt3-mt-mysql = %version-%release
Requires: %name = %version-%release

%description -n libtqt3-mt-mysql
This package contains the threaded MySQL plugin for TQt3. Install it if
you intend to use or write TQt programs that are to access a MySQL DB.

##########

%package -n libtqt3-mt-odbc
Summary: ODBC database driver for TQt3 (Threaded)
Group: System/Libraries
Provides: tqt3-mt-odbc = %version-%release
Requires: %name = %version-%release

%description -n libtqt3-mt-odbc
This package contains the threaded ODBC plugin for TQt3. Install it if
you intend to use or write TQt programs that are to access an ODBC DB.

##########

%package -n libtqt3-mt-psql
Summary: PostgreSQL database driver for TQt3 (Threaded)
Group: System/Libraries
Provides: tqt3-mt-psql = %version-%release
Requires: %name = %version-%release

%description -n libtqt3-mt-psql
This package contains the threaded PostgreSQL plugin for TQt3.
Install it if you intend to use or write TQt programs that are
to access a PostgreSQL DB.

##########

%if %with_ibase
%package -n libtqt3-mt-ibase
Summary:	InterBase/FireBird database driver for TQt3 (Threaded)
Group:		System/Libraries
Provides:	tqt3-mt-ibase = %version-%release
Requires:	%name = %version-%release

%description -n libtqt3-mt-ibase
This package contains the threaded InterBase/FireBird plugin
for TQt3. Install it if you intend to use or write TQt programs
that are to access an InterBase/FireBird DB.
%endif


##########

%package -n libtqt3-mt-sqlite3
Summary: SQLite3 database driver for TQt3 (Threaded)
Group:   System/Libraries
Provides: tqt3-mt-sqlite3 = %version-%release
Requires: libtqt3-devel = %version-%release

%description -n libtqt3-mt-sqlite3
This package contains the threaded SQLite3 plugin for TQt3. Install
it if you intend to use or write TQt programs that are to access an
SQLite3 DB.

##########

%package -n libtqt3-mt-sqlite
Summary: SQLite database driver for TQt3 (Threaded)
Group:   System/Libraries
Provides: tqt3-mt-sqlite = %version-%release
Requires: libtqt3-devel = %version-%release

%description -n libtqt3-mt-sqlite
This package contains the threaded SQLite plugin for TQt3. Install
it if you intend to use or write TQt programs that are to access an
SQLite DB.



%package -n libtqt3-compat-headers
Summary: TQt 1.x and 2.x compatibility includes
Group: Development/KDE and QT
Provides: tqt3-compat-headers
Requires: %name = %version-%release
BuildArch: noarch

%description -n libtqt3-compat-headers
This package contains header files that are intended for build
compatibility for applications that build with TQt3 but still use
deprecated includes. It is meant as an intermediate solution and
these header files are not part of the official TQt3 API.
All sourcecode that is still using the headers of this package is
subject to be changed to use the new header files which are in
qt3headers.

###########

%package -n libtqt3-dev-tools
Summary: TQt3 development tools
Group: Development/KDE and QT
Provides: tqt3-dev-tools
Requires: tqt3-devel = %version-%release
Requires: libtqt3-dev-tools-devel = %version-%release

%description -n libtqt3-dev-tools
This package contains all tools that are necessary to build programs
that are written using TQt3. These are: qmake, uic and moc.
For TQt3 development, you most likely want to install this package.

##########

%package -n libtqt3-dev-tools-devel
Summary: TQt3 development tools
Group: Development/KDE and QT
Provides: tqt3-dev-tools-devel

%description -n libtqt3-dev-tools-devel
This package contains all tools that are necessary to build programs
that are written using TQt3.

##########

%package -n tqt3-designer
Summary: TQt3 Designer
Group: Development/KDE and QT
Requires: %name = %version-%release
Requires: tqt3-doc-html = %version-%release

%description -n tqt3-designer
The TQt Designer is a GUI design program that interactively lets you
construct user interfaces for the TQt library. Additionally it lets you
create whole project and works together with the database drivers
provided by TQt to create applications with easy database access through
TQt. The resulting user interface files can then be converted to
C++ classes using the uic commandline utility which is usually done
automatically for the developer with a project management with qmake
or automake.

###########

%package -n tqt3-apps-devel
Summary: TQt3 Developer applications development files
Group: Development/KDE and QT
Requires: tqt3-devel = %version-%release

%description -n tqt3-apps-devel
This package is intended for developers who want to develop applications
using the additional static libraries that ship with the applications
included with TQt; the TQt Designer and the TQt Assistant.
It allows integrating additional enhancements into the TQt Designer
respectively faciliate the TQt Assistant from within your TQt application
to interactively call the Assistant for displaying online help that the
developer includes with his application.

%package -n tqt3-linguist
Summary: The TQt3 Linguist
Group: Development/KDE and QT
Requires: %name = %version-%release
Requires: tqt3-doc-html = %version-%release

%description -n tqt3-linguist
This package contains the TQt3 Linguist which provides translators a
tool perfect for translating any TQt-based application into other
languages and can be used and installed independently of any TQt
development files by the translator.

##########

%package -n tqt3-assistant
Summary: The TQt3 assistant application
Group: Text tools
Requires: %name = %version-%release
Requires: tqt3-doc-html = %version-%release

%description -n tqt3-assistant
This package contains the TQt3 Assistant, an easy to use frontend for
the complete TQt3 documentation and serves as an online help viewer for
any TQt program that wants to give the usesr access to online help.
Within the TQt tools it is used as the help viewer for the online help
for the TQt3 Designer and Linguist as well as qmake and the TQt 3 API
documentation.

Developers of TQt Application who want to faciliate the TQt Assistant for online
help display should refer to the README.Debian file for tqt3-devel and
the package tqt3-apps-devel.

##########

%package -n tqt3-qtconfig
Summary: The TQt3 Configuration Application
Group:   Development/KDE and QT
Requires: %name = %version-%release
Requires: tqt3-doc-html = %version-%release

%description -n tqt3-qtconfig
The TQt Configuration program allows endusers to configure the look
and behavior of any TQt3 application. It is mostly only necessary
on systems which don't run TDE because the Trinity control center already
covers this configuration automatically for the users TQt3 applications
according to his desktop settings in TDE. However, if you need to run
CJK-fonts or other non-latin scripts, you will most likely want to
install this package.

###########

%package -n libtqt3-dev-tools-embedded
Summary: Tools to develop embedded TQt applications
Group: Development/KDE and QT
Provides: tqt3-dev-tools-embedded
Requires: tqt3-devel = %version-%release

%description -n libtqt3-dev-tools-embedded
This package contains applications only suitable for developing
applications with TQt Embedded and/or Qtopia. It provides the QVFB
program for simulating an embedded device desktop as well as maketqpf
for converting fonts to embedded fonts suitable for being utilized
by TQt Embedded applications.

###########

%package -n libtqt3-dev-tools-compat
Summary: Conversion utilities for TQt3 development
Group:   Development/KDE and QT
Requires: tqt3-devel = %version-%release
Provides: tqt3-dev-tools-compat

%description -n libtqt3-dev-tools-compat
This package contains some older TQt tools (namely tqt20fix tqtrename140,
tqm2ts, tqtmergetr, tqtfindtr and msg2tqm). These tools are needed only by
application developers who need to migrate any TQt application written
for TQt 1.x or 2.x over to TQt 3.x. The purpose of the tools are to
help fixing the changes with include file renaming as well as migrating
the message file format of TQt 2 translation files or any gettext-based
translation system to the TQt 3 system.

##########

%package -n tqt3-i18n
Summary: Translation (i18n) files for TQt3 library
Group:   Development/KDE and QT
Requires: %name = %version-%release
BuildArch: noarch

%description -n tqt3-i18n
This package contains the internationalization files for the TQt library.
TQt applications that are internationalized will need to depend on this package
for full internationalization support of the application towards the end user.

##########

%package -n tqt3-doc-html
Summary: TQt3 API documentation
Group:   Development/KDE and QT
BuildArch: noarch

%description -n tqt3-doc-html
This package contains the complete API documentation for TQt3.
Examples to coding are in tqt3-examples. The documentation is provided
in HTML and manpage format; the HTML version can be viewed in conjunction
with the TQt Assistant.

##########

%package -n tqt3-examples
Summary: Examples for TQt3
Group:   Development/KDE and QT
BuildArch: noarch

%description -n tqt3-examples
These are examples provided with TQt3. They may be especially useful for
you if you are learning to program in TQt as they cover tquite a lot of
things that are possible with TQt3.

%prep
%setup -n %name-%tde_version%{?preversion:~%preversion}

%patch4 -p1
%patch6 -p1
%patch12 -p1
%patch13 -p1
%patch17 -p1
%patch19 -p1

%patch22 -p1

%patch30 -p0
%patch34 -p0
%patch107 -p1
%patch109 -p1

%patch400 -p1

# Add missing sqlite3 header
ln -s ../src/sql/drivers/sqlite3/qsql_sqlite3.h include/qsql_sqlite3.h

%__subst  "s|#ifdef ENABLE_T*QSTYLECONTROLELEMENTDATA_SLOW_COPY|#if 1|"  src/kernel/ntqstyle.h

%__sed mkspecs/*/qmake.conf \
  -e "s|^QMAKE_INCDIR_QT.*|QMAKE_INCDIR_QT		= %_includedir/tqt3|" \
  -e "s|\$(QTDIR)|/usr|g" \
  -e "s|-lqt|-ltqt|g" \
  -e "s|^QMAKE_CFLAGS		=.*|QMAKE_CFLAGS		= %{?optflags}|" \
  -e "s|^QMAKE_INCDIR		=.*|QMAKE_INCDIR		= %_includedir|" \
  -e "s|^QMAKE_LIBDIR		=.*|QMAKE_LIBDIR		= %_libdir|" \
  -e "s|^QMAKE_RPATH		= .*|QMAKE_RPATH		=|" \
  -e "s|^QMAKE_STRIP             =.*|QMAKE_STRIP             =|" \
  -e "s|^QMAKE_STRIPFLAGS_LIB 	+=.*|QMAKE_STRIPFLAGS_LIB 	+=|" \
  -e "s|^QMAKE_MOC		=.*|QMAKE_MOC		= %_bindir/tqmoc|" \
  -e "s|^QMAKE_UIC		=.*|QMAKE_UIC		= %_bindir/tquic|" \
  -e "s|^QMAKE_INCDIR_QT		=.*|QMAKE_INCDIR_QT		= %_includedir/tqt3|" \
  -e "s|^QMAKE_LIBDIR_QT         =.*|QMAKE_LIBDIR_QT         = %_libdir|" \

%if %build_qsa
rm -rf qsa-x11*
tar xf %SOURCE1000 > /dev/null
mv qsa-x11* qsa-x11
pushd qsa-x11/src/qsa
%__subst "s|^VERSION\s*=.*|VERSION = 0.%qsa_ver|" qsa.pro
popd
%endif

# pushd translations
# rm -f ./*.qm
# tar xf %SOURCE11 > /dev/null
# popd
# 


%__subst "s,-O2,%optflags -DGLX_GLXEXT_LEGACY,g" mkspecs/*/qmake.conf
%__subst "s|-Wl,-rpath,| |" mkspecs/*/qmake.conf

find . -type d -name CVS| xargs rm -rf > /dev/null
find . -type f -name .cvsignore | xargs rm -f > /dev/null


# Create a qmake target for linking without libstdc++ - avoid bloat if
# possible...
# pushd mkspecs
# for i in *-g++ qws/*-g++; do
#    [ -d $i ] || continue
#    TARGET=`echo $i |sed -e 's,g++$,gcc,'`
#    cp -aR $i $TARGET
#    %__subst "s,g\+\+,gcc,g;s,^(QMAKE_LIBS[[:space:]]*=.*),\1 -lsupc++,g" $TARGET/*
#   done
# popd
# #%__subst 's,^(.*linux.*)-g\+\+(.*),\1-gcc\2,' configure
# #%__subst 's,^(.*CXX.*LFLAGS.*),\1 -lsupc++,' qmake/GNUmakefile.in

[ -f Makefile.cvs ] && make -f Makefile.cvs

%build
unset QTDIR QTINC QTLIB
export QTDIR=$(pwd)
export PATH=${QTDIR}/bin:${PATH}
export MANPATH=${QTDIR}/doc/man:${MANPATH}
export LD_LIBRARY_PATH="${QTDIR}/lib"

# Checks for supplementary include dir
INCDIRS=""
for d in \
	%_includedir/fontconfig \
	%_includedir/pgsql \
	%_includedir/pgsql/server \
	%_includedir/postgresql/server \
	%_includedir/Xft2 \
	%_includedir/Xft2/X11/Xft \
	%_includedir/mysql \
	%_includedir/libpng15 \
	%_includedir/libpng16 \
; do
	if [ -d "${d}" ]; then
		INCDIRS="${INCDIRS} -I${d}"
	fi
done

# Checks for supplementary library dirs
LIBDIRS=""
for d in \
	%_libdir/mysql \
	%_libdir/pgsql \
; do
	if [ -d "${d}" ]; then
		LIBDIRS="${LIBDIRS} -L${d}"
	fi
done

# build shared, threaded (default) libraries
echo yes | ./configure \
		${INCDIRS} \
		${LIBDIRS} \
		-L%_libdir \
		-prefix		"%prefix" \
		-libdir		"%_libdir" \
		-sysconfdir	"%_sysconfdir/tqt3" \
		-datadir	"%_datadir/tqt3" \
		-headerdir	"%_includedir/tqt3" \
		-docdir		"%tqdoc" \
		-plugindir	"%tqtdir/plugins" \
		-translationdir	"%_datadir/tqt3/translations" \
		\
		-thread \
		-shared \
		-fast \
		-no-exceptions \
%ifarch x86_64
		-platform linux-g++-64 \
%else
		-platform linux-g++ \
%endif
		\
		-nis				\
		-no-pch				\
		-cups				\
		-stl				\
		-ipv6				\
		\
		-sm				\
		-xshape				\
		-xinerama			\
		-xcursor			\
		-xrandr				\
		-xrender			\
		-xft				\
		-tablet				\
		-xkb				\
		\
		-system-zlib			\
		-system-libpng			\
		-system-libmng			\
		-system-libjpeg			\
		%{?with_nas:-system-nas-sound} %{?!with_nas:-no-nas-sound}		\
		\
		-enable-opengl			\
		-dlopen-opengl			\
		\
		-qt-gif				\
		-qt-imgfmt-mng \
		-qt-imgfmt-png			\
		-qt-imgfmt-jpeg			\
		-plugin-imgfmt-mng		\
		\
		-plugin-sql-odbc		\
		-plugin-sql-psql		\
		-plugin-sql-mysql		\
		%{?with_ibase:-plugin-sql-ibase}		\
		-plugin-sql-sqlite		\
		-plugin-sql-sqlite3		\
		\
		-lfontconfig			\
		-inputmethod			\
		%{?with_glibmainloop:-glibmainloop} \
		-v

# proceed
%make_build sub-src sub-plugins sub-tools

# build tqtconv2ui
%make_build -C tools/designer/tools/tqtconv2ui

# build tqvfb
%make_build -C tools/tqvfb 

LD_LIBRARY_PATH=./lib ./bin/tqlrelease ./translations/*.ts

# fix .prl files
%__sed -i lib/*.prl -e "s|${QTDIR}|%{_datadir}/tqt3|g"

%install
export QTDIR=$(pwd)
export PATH="${QTDIR}/bin:${PATH}"
export LD_LIBRARY_PATH=${QTDIR}/lib

%if %debug
%set_strip_method none
%endif
export tqtdir=%tqtdir
export PATH=%tqtdir/bin:%buildroot/%tqtdir/bin:$PATH
export LD_LIBRARY_PATH=%buildroot/%tqtdir/lib:$LD_LIBRARY_PATH
export KDEDIR=%kdedir

# Installs all the remaining
%make INSTALL_ROOT=%buildroot install > /dev/null
%make INSTALL_ROOT=%buildroot install  plugins-install > /dev/null


# Work around for a broken make install
install -d -m 0755 %buildroot/%_bindir

# Work around for a broken make install
%make INSTALL_ROOT=%buildroot install -C plugins/src  > /dev/null

# Installs 'libtqt-mt.so.3' library
%make INSTALL_ROOT=%buildroot  install  -C src  > /dev/null


install -m755 "bin/tqtrename140" "%buildroot%_bindir"
install -m755 "bin/tqt20fix" "%buildroot%_bindir"
install -m755 "bin/tqtfindtr" "%buildroot%_bindir" 

# install tqtconv2ui
install -m755 "bin/tqtconv2ui" "%buildroot%_bindir/tqtconv2ui"

# install tqvfb
install -m755 -D "tools/tqvfb/tqvfb" "%buildroot%_bindir/tqvfb"
install -m644 -D "tools/tqvfb/pda.skin" "%buildroot%_sysconfdir/tqt3/tqvfb/pda.skin"
install -m644 -D "tools/tqvfb/pda_down.png" "%buildroot%_datadir/tqvfb/pda_down.png"
install -m644 -D "tools/tqvfb/pda_up.png" "%buildroot%_datadir/tqvfb/pda_up.png"

## create tqt3-apps-dev-package
cp tools/designer/interfaces/*.h "%buildroot%_includedir/tqt3/" > /dev/null
cp tools/designer/editor/*.h "%buildroot%_includedir/tqt3/" > /dev/null

# language file for linguist
install -D -m644 "translations/qt_untranslated.ts" "%buildroot%_docdir/tqt3-linguist/qt_untranslated.ts"


## i18n files for designer, linguist and assistant
for i in designer/designer assistant linguist/linguist; do
  pushd "tools/${i}"
  tqlrelease "${i##*/}.pro"
  for j in ${i##*/}_*.qm; do
    install -m644 "${j}" "%buildroot%_datadir/tqt3/translations/"  > /dev/null
  done
  popd
done

cd %buildroot%_datadir/tqt3/translations
rename *.qm tq*.qm *.qm
cd -


install -m644 translations/*.qm  %buildroot%_datadir/tqt3/translations/  > /dev/null


# desktop lnk files
install -m644 -D "%SOURCE111" "%buildroot%_desktopdir/tqassistant.desktop"
install -m644 -D "%SOURCE112" "%buildroot%_desktopdir/tqdesigner.desktop"
install -m644 -D "%SOURCE113" "%buildroot%_desktopdir/tqlinguist.desktop"
install -m644 -D "%SOURCE114" "%buildroot%_desktopdir/tqtconfig.desktop"


# Install applications icons
install -m644 -D "tools/assistant/images/appicon.png" "%buildroot%_niconsdir/tqassistant.png"
install -m644 -D "tools/designer/designer/images/designer_appicon.png" "%buildroot%_niconsdir/tqdesigner.png"
install -m644 -D "tools/linguist/linguist/images/appicon.png" "%buildroot%_niconsdir/tqlinguist.png"
install -m644 -D "tools/qtconfig/images/appicon.png" "%buildroot%_niconsdir/tqtconfig.png"

# build attic package and copy it to tqt3-compat-headers
pushd src
tar cvvfz "attic.tar.gz" attic/ > /dev/null
install -D -m644 "attic.tar.gz" "%buildroot%tqdoc//tqt3-compat-headers/attic.tar.gz"
popd

# install the man pages
# install -D -m644 "doc/man/man1/moc.1" "%buildroot%_man1dir/moc-tqt3.1"
# install -D -m644 "doc/man/man1/uic.1" "%buildroot%_man1dir/uic-tqt3.1"
# install -D -m644 "doc/man/man1/lrelease.1" "%buildroot%_man1dir/lrelease-tqt3.1"
# install -D -m644 "doc/man/man1/lupdate.1" "%buildroot%_man1dir/lupdate-tqt3.1"

# Install man pages
install -d -m 0755 %buildroot/%_man1dir/
cd doc/man/man1/
#for i in %_builddir/%{?buildsubdir}/doc/man/man1/* ; do
for i in * ; do
    %__subst 's|3qt|tqt3|g' $i
   ib=$(basename $i .1)
   install -m 0644 $i %buildroot/%_man1dir/tq$ib.1 > /dev/null
done
cd -
#


# install the man3 pages
#
install -d -m 0755 %buildroot/%_man3dir/
cd doc/man/man3
for i in * ; do
   install -m 0644 $i %buildroot/%_man3dir/  > /dev/null
done
cd -
#

pushd %buildroot/%_mandir/
    for i in $(find . -name *Q\* > /dev/null);do
	%__subst 's|3qt|tqt|g' $i
    done
    for i in $(find . -name \*.3qt > /dev/null);do > /dev/null
	ib=$(basename $i .3qt)
	mv -f $i man3/$ib.tqt.3 > /dev/null
    done
popd



# Install source for the designer tools, such as tqtcreatecw.
install -d -m755 %buildroot/%tqtdir/
cp -ra tools/designer/tools %buildroot%tqtdir/tools > /dev/null
rm -f %buildroot%_datadir/%tdir/tools/tqtcreatecw/*

# create examples package
install -d %tdir-examples
cp -ax examples %tdir-examples/ > /dev/null
cp -ax tutorial %tdir-examples/ > /dev/null
mkdir -p %tdir-examples/tools/designer
cp -ax tools/designer/examples %tdir-examples/tools/designer/ > /dev/null
mkdir -p %tdir-examples/tools/linguist
cp -ax tools/linguist/tutorial %tdir-examples/tools/linguist/ > /dev/null
find %tdir-examples -name "tt1" -print | xargs rm -rf > /dev/null
find %tdir-examples -name "tt2" -print | xargs rm -rf > /dev/null
find %tdir-examples -name "tt3" -print | xargs rm -rf > /dev/null
find %tdir-examples -name ".moc" | xargs rm -rf > /dev/null
find %tdir-examples -name ".obj" | xargs rm -rf > /dev/null
find %tdir-examples -name "Makefile" | xargs rm -rf > /dev/null
install -D -m 755 %SOURCE1 %buildroot%_docdir/%tdir-examples/build-examples
tar cvvfz %tdir-examples.tar.gz %tdir-examples/ > /dev/null
install -D -m644 "%tdir-examples.tar.gz" "%buildroot%_docdir/%tdir-examples/%tdir-examples.tar.gz"


install -m644  {FAQ,LICENSE*,README*,changes*}  %buildroot/%tqdoc/

mv -f %buildroot%_man1dir/tqmaketqpf.1 %buildroot%_man1dir/maketqpf.1
rm -fdr %buildroot/%tqtdir/tools/tqtcreatecw/{.moc,.obj}
rm -fdr %buildroot/%tqtdir/tools/tqtconv2ui/{.moc,.obj}

rm -fdr %buildroot/%tqtdir/tools/tqtconv2ui/Makefile
rm -fdr %buildroot/%tqtdir/tools/tqtcreatecw/{Makefile,tqtcreatecw}


#rm -fd %buildroot/%tqtdir/tools/tqtconv2ui/.*

ln -s tqassistant %buildroot/%_bindir/assistant-tqt3
ln -s tqdesigner %buildroot/%_bindir/designer-tqt3
ln -s tqlinguist %buildroot/%_bindir/linguist-tqt3
ln -s tqmake %buildroot/%_bindir/qmake-tqt3
ln -s tquic %buildroot/%_bindir/uic-tqt3
ln -s tqmoc %buildroot/%_bindir/moc-tqt3
ln -s tqlrelease %buildroot/%_bindir/lrelease-tqt3
ln -s tqlupdate %buildroot/%_bindir/lupdate-tqt3


%files
%docdir %tqdoc
%exclude %tqdoc/tqt3-compat-headers/*
%exclude %tqdoc/html
%exclude %tqdoc/html/*

%tqdoc/*
%dir %_niconsdir/*
%exclude %_niconsdir/tqdesigner.png
%exclude %_niconsdir/tqlinguist.png
%exclude %_niconsdir/tqassistant.png
%exclude %_niconsdir/tqtconfig.png

%dir %tqtdir/
%dir %tqdoc/
%dir %tqtdir/plugins/
%dir %tqtdir/plugins/designer/
%dir %tqtdir/plugins/imageformats/
%dir %tqtdir/plugins/inputmethods/
%dir %tqtdir/plugins/sqldrivers/
%dir %_sysconfdir/tqt3
%_libdir/libtqt-mt.so.3
%_libdir/libtqt-mt.so.3.5
%_libdir/libtqt-mt.so.3.5.0
%_libdir/libtqui.so.1
%_libdir/libtqui.so.1.0
%_libdir/libtqui.so.1.0.0
%tqtdir/plugins/imageformats/libqmng.so
%tqtdir/plugins/inputmethods/libqimsw-multi.so
%tqtdir/plugins/inputmethods/libqimsw-none.so
%tqtdir/plugins/inputmethods/libqsimple.so
%tqtdir/plugins/inputmethods/libqxim.so

%dir %tqinclude/private/
%tqinclude/private/*.h


%files -n libtqt3-devel
%_libdir/libtqt-mt.la
%_libdir/libtqt-mt.so
%_libdir/libtqt-mt.prl
%_libdir/libtqui.so
%_libdir/libtqui.prl
%_pkgconfigdir/tqt-mt.pc
%dir %tqinclude
%tqinclude/ntqgl.h
%tqinclude/ntqglcolormap.h
%tqinclude/ntqwidgetfactory.h
%tqinclude/actioninterface.h
%tqinclude/arghintwidget.h
%tqinclude/browser.h
%tqinclude/cindent.h
%tqinclude/classbrowserinterface.h
%tqinclude/completion.h
%tqinclude/conf.h
%tqinclude/designerinterface.h
%tqinclude/editor.h
%tqinclude/editorinterface.h
%tqinclude/filterinterface.h
%tqinclude/interpreterinterface.h
%tqinclude/languageinterface.h
%tqinclude/markerwidget.h
%tqinclude/ntqabstractlayout.h
%tqinclude/ntqaccel.h
%tqinclude/ntqaccessible.h
%tqinclude/ntqaction.h
%tqinclude/ntqapplication.h
%tqinclude/ntqasciicache.h
%tqinclude/ntqasciidict.h
%tqinclude/ntqasyncimageio.h
%tqinclude/ntqasyncio.h
%tqinclude/ntqbig5codec.h
%tqinclude/ntqbitarray.h
%tqinclude/ntqbitmap.h
%tqinclude/ntqbrush.h
%tqinclude/ntqbuffer.h
%tqinclude/ntqbutton.h
%tqinclude/ntqbuttongroup.h
%tqinclude/ntqcache.h
%tqinclude/ntqcanvas.h
%tqinclude/ntqcdestyle.h
%tqinclude/ntqcheckbox.h
%tqinclude/ntqcleanuphandler.h
%tqinclude/ntqclipboard.h
%tqinclude/ntqcolor.h
%tqinclude/ntqcolordialog.h
%tqinclude/ntqcombobox.h
%tqinclude/ntqcommonstyle.h
%tqinclude/ntqcompactstyle.h
%tqinclude/ntqconfig.h
%tqinclude/ntqconnection.h
%tqinclude/ntqcstring.h
%tqinclude/ntqcursor.h
%tqinclude/ntqdatabrowser.h
%tqinclude/ntqdatastream.h
%tqinclude/ntqdatatable.h
%tqinclude/ntqdataview.h
%tqinclude/ntqdatetime.h
%tqinclude/ntqdatetimeedit.h
%tqinclude/ntqdeepcopy.h
%tqinclude/ntqdesktopwidget.h
%tqinclude/ntqdial.h
%tqinclude/ntqdialog.h
%tqinclude/ntqdict.h
%tqinclude/ntqdir.h
%tqinclude/ntqdns.h
%tqinclude/ntqdockarea.h
%tqinclude/ntqdockwindow.h
%tqinclude/ntqdom.h
%tqinclude/ntqdragobject.h
%tqinclude/ntqdrawutil.h
%tqinclude/ntqdropsite.h
%tqinclude/ntqeditorfactory.h
%tqinclude/ntqerrormessage.h
%tqinclude/ntqeucjpcodec.h
%tqinclude/ntqeuckrcodec.h
%tqinclude/ntqevent.h
%tqinclude/ntqeventloop.h
%tqinclude/ntqfeatures.h
%tqinclude/ntqfile.h
%tqinclude/ntqfiledialog.h
%tqinclude/ntqfileinfo.h
%tqinclude/ntqfocusdata.h
%tqinclude/ntqfont.h
%tqinclude/ntqfontdatabase.h
%tqinclude/ntqfontdialog.h
%tqinclude/ntqfontinfo.h
%tqinclude/ntqfontmetrics.h
%tqinclude/ntqframe.h
%tqinclude/ntqftp.h
%tqinclude/ntqgarray.h
%tqinclude/ntqgb18030codec.h
%tqinclude/ntqgbkcodec.h
%tqinclude/ntqgcache.h
%tqinclude/ntqgdict.h
%tqinclude/ntqgeneric.h
%tqinclude/ntqgif.h
%tqinclude/ntqglist.h
%tqinclude/ntqglobal.h
%tqinclude/ntqgplugin.h
%tqinclude/ntqgrid.h
%tqinclude/ntqgridview.h
%tqinclude/ntqgroupbox.h
%tqinclude/ntqguardedptr.h
%tqinclude/ntqgvector.h
%tqinclude/ntqhbox.h
%tqinclude/ntqhbuttongroup.h
%tqinclude/ntqheader.h
%tqinclude/ntqhgroupbox.h
%tqinclude/ntqhostaddress.h
%tqinclude/ntqhttp.h
%tqinclude/ntqiconset.h
%tqinclude/ntqiconview.h
%tqinclude/ntqimage.h
%tqinclude/ntqimageformatplugin.h
%tqinclude/ntqinputcontext.h
%tqinclude/ntqinputcontextfactory.h
%tqinclude/ntqinputcontextplugin.h
%tqinclude/ntqinputdialog.h
%tqinclude/ntqintcache.h
%tqinclude/ntqintdict.h
%tqinclude/ntqinterlacestyle.h
%tqinclude/ntqiodevice.h
%tqinclude/ntqjiscodec.h
%tqinclude/ntqjpegio.h
%tqinclude/ntqjpunicode.h
%tqinclude/ntqkeycode.h
%tqinclude/ntqkeysequence.h
%tqinclude/ntqlabel.h
%tqinclude/ntqlayout.h
%tqinclude/ntqlcdnumber.h
%tqinclude/ntqlibrary.h
%tqinclude/ntqlineedit.h
%tqinclude/ntqlistbox.h
%tqinclude/ntqlistview.h
%tqinclude/ntqlocale.h
%tqinclude/ntqlocalfs.h
%tqinclude/ntqmainwindow.h
%tqinclude/ntqmap.h
%tqinclude/ntqmemarray.h
%tqinclude/ntqmenubar.h
%tqinclude/ntqmenudata.h
%tqinclude/ntqmessagebox.h
%tqinclude/ntqmetaobject.h
%tqinclude/ntqmime.h
%tqinclude/ntqmngio.h
%tqinclude/ntqmodules.h
%tqinclude/ntqmotifplusstyle.h
%tqinclude/ntqmotifstyle.h
%tqinclude/ntqmovie.h
%tqinclude/ntqmultilineedit.h
%tqinclude/ntqmutex.h
%tqinclude/ntqnamespace.h
%tqinclude/ntqnetwork.h
%tqinclude/ntqnetworkprotocol.h
%tqinclude/ntqnp.h
%tqinclude/ntqobject.h
%tqinclude/ntqobjectcleanuphandler.h
%tqinclude/ntqobjectdefs.h
%tqinclude/ntqobjectdict.h
%tqinclude/ntqobjectlist.h
%tqinclude/ntqpaintdevice.h
%tqinclude/ntqpaintdevicedefs.h
%tqinclude/ntqpaintdevicemetrics.h
%tqinclude/ntqpainter.h
%tqinclude/ntqpair.h
%tqinclude/ntqpalette.h
%tqinclude/ntqpen.h
%tqinclude/ntqpicture.h
%tqinclude/ntqpixmap.h
%tqinclude/ntqpixmapcache.h
%tqinclude/ntqplatinumstyle.h
%tqinclude/ntqpngio.h
%tqinclude/ntqpoint.h
%tqinclude/ntqpointarray.h
%tqinclude/ntqpolygonscanner.h
%tqinclude/ntqpopupmenu.h
%tqinclude/ntqprintdialog.h
%tqinclude/ntqprinter.h
%tqinclude/ntqprocess.h
%tqinclude/ntqprogressbar.h
%tqinclude/ntqprogressdialog.h
%tqinclude/ntqptrcollection.h
%tqinclude/ntqptrdict.h
%tqinclude/ntqptrlist.h
%tqinclude/ntqptrqueue.h
%tqinclude/ntqptrstack.h
%tqinclude/ntqptrvector.h
%tqinclude/ntqpushbutton.h
%tqinclude/ntqradiobutton.h
%tqinclude/ntqrangecontrol.h
%tqinclude/ntqrect.h
%tqinclude/ntqregexp.h
%tqinclude/ntqregion.h
%tqinclude/ntqrtlcodec.h
%tqinclude/ntqscrollbar.h
%tqinclude/ntqscrollview.h
%tqinclude/ntqsemaphore.h
%tqinclude/ntqsemimodal.h
%tqinclude/ntqserversocket.h
%tqinclude/ntqsession.h
%tqinclude/ntqsessionmanager.h
%tqinclude/ntqsettings.h
%tqinclude/ntqsgistyle.h
%tqinclude/ntqshared.h
%tqinclude/ntqsignal.h
%tqinclude/ntqsignalmapper.h
%tqinclude/ntqsignalslotimp.h
%tqinclude/ntqsimplerichtext.h
%tqinclude/ntqsize.h
%tqinclude/ntqsizegrip.h
%tqinclude/ntqsizepolicy.h
%tqinclude/ntqsjiscodec.h
%tqinclude/ntqslider.h
%tqinclude/ntqsocket.h
%tqinclude/ntqsocketdevice.h
%tqinclude/ntqsocketnotifier.h
%tqinclude/ntqsortedlist.h
%tqinclude/ntqsound.h
%tqinclude/ntqspinbox.h
%tqinclude/ntqsplashscreen.h
%tqinclude/ntqsplitter.h
%tqinclude/ntqsql.h
%tqinclude/ntqsqlcursor.h
%tqinclude/ntqsqldatabase.h
%tqinclude/ntqsqldriver.h
%tqinclude/ntqsqldriverplugin.h
%tqinclude/ntqsqleditorfactory.h
%tqinclude/ntqsqlerror.h
%tqinclude/ntqsqlfield.h
%tqinclude/ntqsqlform.h
%tqinclude/ntqsqlindex.h
%tqinclude/ntqsqlpropertymap.h
%tqinclude/ntqsqlquery.h
%tqinclude/ntqsqlrecord.h
%tqinclude/ntqsqlresult.h
%tqinclude/ntqsqlselectcursor.h
%tqinclude/ntqstatusbar.h
%tqinclude/ntqstring.h
%tqinclude/ntqstringlist.h
%tqinclude/ntqstrlist.h
%tqinclude/ntqstrvec.h
%tqinclude/ntqstyle.h
%tqinclude/ntqstylefactory.h
%tqinclude/ntqstyleplugin.h
%tqinclude/ntqstylesheet.h
%tqinclude/ntqsyntaxhighlighter.h
%tqinclude/ntqt.h
%tqinclude/ntqtabbar.h
%tqinclude/ntqtabdialog.h
%tqinclude/ntqtable.h
%tqinclude/ntqtabwidget.h
%tqinclude/ntqtextbrowser.h
%tqinclude/ntqtextcodec.h
%tqinclude/ntqtextcodecfactory.h
%tqinclude/ntqtextcodecplugin.h
%tqinclude/ntqtextedit.h
%tqinclude/ntqtextstream.h
%tqinclude/ntqtextview.h
%tqinclude/ntqthread.h
%tqinclude/ntqthreadstorage.h
%tqinclude/ntqtimer.h
%tqinclude/ntqtl.h
%tqinclude/ntqtoolbar.h
%tqinclude/ntqtoolbox.h
%tqinclude/ntqtoolbutton.h
%tqinclude/ntqtooltip.h
%tqinclude/ntqtranslator.h
%tqinclude/ntqtsciicodec.h
%tqinclude/ntqurl.h
%tqinclude/ntqurlinfo.h
%tqinclude/ntqurloperator.h
%tqinclude/ntqutfcodec.h
%tqinclude/ntquuid.h
%tqinclude/ntqvalidator.h
%tqinclude/ntqvaluelist.h
%tqinclude/ntqvaluestack.h
%tqinclude/ntqvaluevector.h
%tqinclude/ntqvariant.h
%tqinclude/ntqvbox.h
%tqinclude/ntqvbuttongroup.h
%tqinclude/ntqvfbhdr.h
%tqinclude/ntqvgroupbox.h
%tqinclude/ntqwaitcondition.h
%tqinclude/ntqwhatsthis.h
%tqinclude/ntqwidget.h
%tqinclude/ntqwidgetintdict.h
%tqinclude/ntqwidgetlist.h
%tqinclude/ntqwidgetplugin.h
%tqinclude/ntqwidgetstack.h
%tqinclude/ntqwindowdefs.h
%tqinclude/ntqwindowsstyle.h
%tqinclude/ntqwinexport.h
%tqinclude/ntqwizard.h
%tqinclude/ntqwmatrix.h
%tqinclude/ntqworkspace.h
%tqinclude/ntqxml.h
%tqinclude/paragdata.h
%tqinclude/parenmatcher.h
%tqinclude/preferenceinterface.h
%tqinclude/preferences.h
%tqinclude/preferences.ui.h
%tqinclude/projectsettingsiface.h
%tqinclude/qconfig-dist.h
%tqinclude/qconfig-large.h
%tqinclude/qconfig-medium.h
%tqinclude/qconfig-minimal.h
%tqinclude/qconfig-small.h
%tqinclude/qsql_ibase.h
%tqinclude/qsql_odbc.h
%tqinclude/qsql_psql.h
%tqinclude/qsqlcachedresult.h
%tqinclude/qt_pch.h
%tqinclude/qtmultilineedit.h
%tqinclude/qttableview.h
%tqinclude/qwindow.h
%tqinclude/sourcetemplateiface.h
%tqinclude/templatewizardiface.h
%tqinclude/viewmanager.h
%tqinclude/widgetinterface.h
%_man3dir/*


%files -n libtqt3-mt-mysql

%tqinclude/qsql_mysql.h

%files -n libtqt3-mt-odbc
%tqtdir/plugins/sqldrivers/libqsqlodbc.so

%files -n libtqt3-mt-psql
%tqtdir/plugins/sqldrivers/libqsqlpsql.so

%if %with_ibase
%files -n libtqt3-mt-ibase
%tqtdir/plugins/sqldrivers/libqsqlibase.so
%endif

%files -n libtqt3-mt-sqlite3
%tqtdir/plugins/sqldrivers/libqsqlite3.so

%files -n libtqt3-mt-sqlite
%exclude %tqtdir/plugins/sqldrivers/libqsqlmysql.so
%exclude %tqtdir/plugins/sqldrivers/libqsqlodbc.so
%exclude %tqtdir/plugins/sqldrivers/libqsqlpsql.so
%exclude %tqtdir/plugins/sqldrivers/libqsqlite3.so
%exclude %tqtdir/plugins/sqldrivers/libqsqlibase.so
%tqtdir/plugins/sqldrivers/*.so

%tqinclude/qsql_sqlite.h
%tqinclude/qsql_sqlite3.h


%files -n libtqt3-compat-headers
%tqinclude/ntq1xcompatibility.h
%tqinclude/ntqapp.h
%tqinclude/ntqarray.h
%tqinclude/ntqbitarry.h
%tqinclude/ntqbttngrp.h
%tqinclude/ntqchkbox.h
%tqinclude/ntqclipbrd.h
%tqinclude/ntqcollect.h
%tqinclude/ntqcollection.h
%tqinclude/ntqcombo.h
%tqinclude/ntqconnect.h
%tqinclude/ntqdatetm.h
%tqinclude/ntqdrawutl.h
%tqinclude/ntqdstream.h
%tqinclude/ntqfiledef.h
%tqinclude/ntqfiledlg.h
%tqinclude/ntqfileinf.h
%tqinclude/ntqfontinf.h
%tqinclude/ntqfontmet.h
%tqinclude/ntqgrpbox.h
%tqinclude/ntqintcach.h
%tqinclude/ntqiodev.h
%tqinclude/ntqlcdnum.h
%tqinclude/ntqlined.h
%tqinclude/ntqlist.h
%tqinclude/ntqmenudta.h
%tqinclude/ntqmetaobj.h
%tqinclude/ntqmlined.h
%tqinclude/ntqmsgbox.h
%tqinclude/ntqmultilinedit.h
%tqinclude/ntqobjcoll.h
%tqinclude/ntqobjdefs.h
%tqinclude/ntqpaintd.h
%tqinclude/ntqpaintdc.h
%tqinclude/ntqpdevmet.h
%tqinclude/ntqpmcache.h
%tqinclude/ntqpntarry.h
%tqinclude/ntqpopmenu.h
%tqinclude/ntqprndlg.h
%tqinclude/ntqprogbar.h
%tqinclude/ntqprogdlg.h
%tqinclude/ntqpsprn.h
%tqinclude/ntqpushbt.h
%tqinclude/ntqqueue.h
%tqinclude/ntqradiobt.h
%tqinclude/ntqrangect.h
%tqinclude/ntqscrbar.h
%tqinclude/ntqsocknot.h
%tqinclude/ntqstack.h
%tqinclude/ntqtabdlg.h
%tqinclude/ntqtstream.h
%tqinclude/ntqvector.h
%tqinclude/ntqwidcoll.h
%tqinclude/ntqwindefs.h

%dir %tqdoc/tqt3-compat-headers
%tqdoc/tqt3-compat-headers/attic.tar.gz


%files -n libtqt3-dev-tools
%tqdoc/html/qmake*html
%tqdoc/html/qmake*dcf

%_bindir/qmake-tqt3
%_bindir/lrelease-tqt3
%_bindir/lupdate-tqt3
%_bindir/uic-tqt3
%_bindir/moc-tqt3

%_bindir/tqmake
%_bindir/tqlupdate
%_bindir/tqlrelease
%_bindir/tquic
%_bindir/tqmoc
%_bindir/tqembed
%_man1dir/tqlupdate.1*
%_man1dir/tqlrelease.1*
%_man1dir/tqmoc.1*
%_man1dir/tquic.1*

%files -n libtqt3-dev-tools-devel
%dir %_datadir/tqt3/mkspecs/
%_datadir/tqt3/mkspecs/*

%files -n tqt3-designer
%_bindir/tqdesigner
%_bindir/tqtcreatecw
%_bindir/tqtconv2ui
%_bindir/designer-tqt3


%tqdoc/html/designer*html
%tqdoc/html/designer*dcf
%tqdoc/html/designer*jpg
%dir %_datadir/tqt3/templates/
%_datadir/tqt3/templates/*
%tqtdir/plugins/designer/libcppeditor.so
%tqtdir/plugins/designer/libdlgplugin.so
%tqtdir/plugins/designer/libgladeplugin.so
%tqtdir/plugins/designer/libkdevdlgplugin.so
%tqtdir/plugins/designer/librcplugin.so
%tqtdir/plugins/designer/libwizards.so
%dir %tqtdir/tools/tqtconv2ui
%tqtdir/tools/tqtconv2ui/main.cpp
%tqtdir/tools/tqtconv2ui/tqtconv2ui.pro
%dir %tqtdir/tools/tqtcreatecw
%tqtdir/tools/tqtcreatecw/README
%tqtdir/tools/tqtcreatecw/main.cpp
%tqtdir/tools/tqtcreatecw/tqtcreatecw.pro
%_desktopdir/tqdesigner.desktop
%_niconsdir/tqdesigner.png
%_man1dir/tqdesigner.1.*
%_man1dir/tqtqtcreatecw.1.*


%files -n tqt3-apps-devel
%_libdir/libtqtdesignercore.prl
%_libdir/libtqtdesignercore.so
%_libdir/libtqtdesignercore.so.1
%_libdir/libtqtdesignercore.so.1.0
%_libdir/libtqtdesignercore.so.1.0.0
%_libdir/libtqteditor.prl
%_libdir/libtqteditor.so
%_libdir/libtqteditor.so.1
%_libdir/libtqteditor.so.1.0
%_libdir/libtqteditor.so.1.0.0
%_libdir/libtqassistantclient.prl
%_libdir/libtqassistantclient.so
%_libdir/libtqassistantclient.so.1
%_libdir/libtqassistantclient.so.1.0
%_libdir/libtqassistantclient.so.1.0.0
%tqinclude//ntqassistantclient.h

%files -n tqt3-linguist
%_bindir/tqlinguist
%_bindir/linguist-tqt3

%dir %_datadir/tqt3/phrasebooks/
%_datadir/tqt3/phrasebooks/*
%tqdoc/html/linguist*html
%tqdoc/html/linguist*dcf
%dir %_docdir/tqt3-linguist
%_docdir/tqt3-linguist/qt_untranslated.ts
%_desktopdir/tqlinguist.desktop
%_niconsdir/tqlinguist.png
%_man1dir/tqlinguist.1.*

%files -n tqt3-assistant
%_bindir/tqassistant
%_bindir/assistant-tqt3
%tqdoc/html/assistant*html
%tqdoc/html/assistant*dcf
%_desktopdir/tqassistant.desktop
%_niconsdir/tqassistant.png


%files -n tqt3-qtconfig
%_bindir/tqtconfig
%_desktopdir/tqtconfig.desktop
%_niconsdir/tqtconfig.png
%_man1dir/tqqtconfig.1.*

%files -n libtqt3-dev-tools-embedded
%_bindir/maketqpf
%_bindir/tqvfb
%dir %_sysconfdir/tqt3/tqvfb
%config /etc/tqt3/tqvfb/pda.skin
%dir /usr/share/tqvfb
%_datadir/tqvfb/pda_down.png
%_datadir/tqvfb/pda_up.png
%_man1dir/tqtqvfb.1.*
%_man1dir/tqqembed.1.*
%_man1dir/maketqpf.1.*

%files -n libtqt3-dev-tools-compat
%_bindir/tqt20fix
%_bindir/tqtrename140
%_bindir/tqm2ts
%_bindir/tqtmergetr
%_bindir/tqtfindtr
%_bindir/msg2tqm

%_man1dir/tqtqt20fix.1.*
%_man1dir/tqmsg2tqm.1.*
%_man1dir/tqtqtmergetr.1.*
%_man1dir/tqtqtfindtr.1.*


%files -n tqt3-i18n
%defattr(-,root,root,-)
%dir %_datadir/tqt3/translations/
%_datadir/tqt3/translations/*.qm

%files -n tqt3-doc-html
%exclude %tqdoc/html/qmake*html
%exclude %tqdoc/html/qmake*dcf
%exclude %tqdoc/html/designer*html
%exclude %tqdoc/html/designer*dcf
%exclude %tqdoc/html/designer*jpg
%exclude %tqdoc/html/linguist*html
%exclude %tqdoc/html/linguist*dcf
%exclude %tqdoc/html/assistant*html
%exclude %tqdoc/html/assistant*dcf
%tqdoc/html/*


%files -n tqt3-examples
%dir %_docdir/%tdir-examples/
%_docdir/%tdir-examples/build-examples
%_docdir/%tdir-examples/%tdir-examples.tar.gz

%changelog
* Sat Jul 23 2016 Hihin Ruslan <ruslandh@altlinux.ru> 3.5.0-alt1
- initial build for ALT Linux Sisyphus

* Tue Jan 12 2016 Hihin Ruslan <ruslandh@altlinux.ru> 14.0.2-alt1
- Rename Packge to trinity-tqt3
- New version

* Thu Nov 05 2015 Michael Shigorin <mike@altlinux.org> 3.3.8d-alt9
- Hardwire "CXX3" for any gcc not just 4.x (thx glebfm@ for suggestion).

* Sat Oct 03 2015 Michael Shigorin <mike@altlinux.org> 3.3.8d-alt8
- Some doc subpackages made noarch.
- Minor spec cleanup.

* Sat Oct 03 2015 Michael Shigorin <mike@altlinux.org> 3.3.8d-alt7
- Rebuilt for gcc5 C++11 ABI.

* Fri Nov 01 2013 Roman Savochenko <rom_as@altlinux.ru> 3.3.8d-alt6
- Icons hide fix.
