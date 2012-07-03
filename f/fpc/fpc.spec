Name: fpc
Epoch: 2
Version: 2.6.0
Release: alt2.qa1

Summary: Free Pascal Compiler -- Meta Package
License: GPL
Group: Development/Other
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Url: http://www.freepascal.org
Source: fpcbuild-%version.tar
Source1: fp.desktop
Source2: fp.sh
Source3: fp.cfg
Source4: fp16x16.xpm
Source5: fp48x48.xpm
Source6: ppc386_bootstrap
Source7: ppcx64_bootstrap

Patch: %name-%version-alt-changes.patch

%define makedoc 0
%define makesrc 1
%define maketests 1
%define makewin32 1

ExclusiveOS: Linux
ExclusiveArch: %ix86 amd64 x86_64
Requires: fpc-units-rtl fpc-compiler fpc-units-base fpc-ide fpc-units-fcl fpc-units-fv fpc-units-gtk fpc-units-gtk2 fpc-units-gnome1 fpc-units-db fpc-units-gfx fpc-units-net fpc-units-math fpc-units-misc fpc-units-multimedia

# Automatically added by buildreq on Thu Oct 01 2009
BuildRequires: fpc-compiler fpc-utils libexpat-devel libgdb-devel libncurses-devel libreadline-devel-static rpm-build-fpc python-devel zlib-devel
%if %makedoc
BuildRequires: tex4ht texlive-generic-recommended texlive-latex-recommended fpc-units-fcl
%endif

%ifarch %ix86
%define ppctarget i386-linux
%else
%define ppctarget x86_64-linux
%define makewin32 0
%endif
%define ppcname %(basename `fpc -PB`)

%description
The Free Pascal Compiler is an object pascal compiler supporting both Delphi
and Turbo Pascal 7.0 dialects as well as Mac pascal dialects.
It provides a completely portable RunTime Library (RTL) available on many
platforms and compatible with Turbo Pascal, but also a platfrom independent
class based Free Component Library (FCL) adding many Delphi extensions and
interfacing many popular open source libraries.

Some extensions are added to the language, like function overloading. Shared
libraries can be linked and created. Delphi language extentions like classes,
exceptions, ansi strings and open arrays are also supported.

This package contains dependency on all FPC packages provided on your
architecture. Experienced users may want to install only packages they need,
and can skip installing this metapackage.

%prep
%setup -q -n fpcbuild-%version
%patch -p1

%__subst "s|/usr/local/lib|%_libdir|g" fpcsrc/packages/gdbint/src/gdbint.pp
sed -i "/LINKLIB/s/python/python2.7/" fpcsrc/packages/gdbint/src/gdbint.pp
sed -i "/LINKLIB ncurses/a {\$LINKLIB z}" fpcsrc/packages/gdbint/src/gdbint.pp

sed -i '/fp/s/\/bin/\/usr\/bin/g' fpcsrc/compiler/utils/samplecfg

%build
# install src
%__rm -rf ../fpcsrc
%__mkdir_p ../fpcsrc
%__cp -fR  fpcsrc/* ../fpcsrc/
%__rm -rf ../fpcsrc/{ide,installer,tests,utils}

export OPT="-vwn "
export GDBLIBDIR=%_libdir
export LIBGDBFILE=%_libdir/libgdb.a

# bootstrap fpc
%ifarch %ix86
%__cp %SOURCE6 .
make -C fpcsrc/compiler cycle RELEASE=1 FPC=$PWD/ppc386_bootstrap
%else
%__cp %SOURCE7 .
make -C fpcsrc/compiler cycle RELEASE=1 FPC=$PWD/ppcx64_bootstrap
%endif
cp -pv fpcsrc/compiler/%ppcname %ppcname

# bootstrap fpcmake
%fpc_build FPC=$PWD/%ppcname FPCDIR=$PWD -C fpcsrc/rtl
%fpc_build FPC=$PWD/%ppcname FPCDIR=$PWD -C fpcsrc/compiler
%fpc_build FPC=$PWD/%ppcname FPCDIR=$PWD -C fpcsrc/packages fcl_smart
%fpc_build FPC=$PWD/%ppcname FPCDIR=$PWD -C fpcsrc/utils
cp -pv fpcsrc/utils/fpcm/fpcmake fpcmake

#Fix path
%ifarch x86_64
%__subst "s|/lib/fpc/lexyacc|/lib64/fpc/lexyacc|g" fpcsrc/utils/tply/Makefile.fpc
%endif

# Begin make all use new fpcmake
./fpcmake -r -Tall

%fpc_build FPC=$PWD/%ppcname FPCMAKE=$PWD/fpcmake FPCDIR=$PWD -C fpcsrc/rtl
%fpc_build FPC=$PWD/%ppcname FPCMAKE=$PWD/fpcmake FPCDIR=$PWD -C fpcsrc/compiler
%fpc_build FPC=$PWD/%ppcname FPCMAKE=$PWD/fpcmake FPCDIR=$PWD -C fpcsrc/packages fcl_smart
%fpc_build FPC=$PWD/%ppcname FPCMAKE=$PWD/fpcmake FPCDIR=$PWD -C fpcsrc/ide gdb
%fpc_build FPC=$PWD/%ppcname FPCMAKE=$PWD/fpcmake FPCDIR=$PWD -C fpcsrc/utils


%ifnarch %ix86
%fpc_make  FPC=$PWD/%ppcname FPCMAKE=$PWD/fpcmake FPCDIR=$PWD CROSSINSTALL=1 PPC_TARGET=i386 -C fpcsrc/compiler
cp -pv fpcsrc/compiler/ppc386 ppc386
%endif

%ifarch %makewin32
#Build for win32
%fpc_build_win32 FPC=$PWD/ppc386 FPCMAKE=$PWD/fpcmake FPCDIR=$PWD -C fpcsrc/rtl
%endif

%if %makedoc
make -C fpcdocs html pdf
%endif

%if %maketests
%__make TEST_FPC=$PWD/%ppcname FPCDIR=$PWD QUICKTEST=YES -C fpcsrc/tests digest
%endif

%install
%fpc_install FPC=$PWD/%ppcname FPCMAKE=$PWD/fpcmake FPCDIR=$PWD INSTALL_DOCDIR=%buildroot%_docdir/%name-%version -C fpcsrc/compiler
%fpc_install FPC=$PWD/%ppcname FPCMAKE=$PWD/fpcmake FPCDIR=$PWD INSTALL_DOCDIR=%buildroot%_docdir/%name-%version -C fpcsrc/rtl
%fpc_install FPC=$PWD/%ppcname FPCMAKE=$PWD/fpcmake FPCDIR=$PWD INSTALL_DOCDIR=%buildroot%_docdir/%name-%version INSTALL_PREFIX=%buildroot%_usr -C fpcsrc/packages
%fpc_install FPC=$PWD/%ppcname FPCMAKE=$PWD/fpcmake FPCDIR=$PWD INSTALL_DOCDIR=%buildroot%_docdir/%name-%version -C fpcsrc/ide
%fpc_install FPC=$PWD/%ppcname FPCMAKE=$PWD/fpcmake FPCDIR=$PWD INSTALL_DOCDIR=%buildroot%_docdir/%name-%version INSTALL_PREFIX=%buildroot%_usr -C fpcsrc/utils


%if %makedoc
make INSTALL_DOCDIR=%buildroot%_docdir/%name-%version DESTDIR=%buildroot -C fpcdocs htmlinstall pdfinstall
%endif

# this symbolic link must be absolute (so that fpcmake can detect FPCDIR)
ln -s %fpc_dir/%ppcname %buildroot%_bindir/%ppcname

#Install src
%if %makesrc
%__mkdir_p %buildroot%_datadir/fpcsrc
%__cp -fR ../fpcsrc %buildroot%_datadir/
%add_verify_elf_skiplist */fpcsrc/*
%add_findreq_skiplist */fpcsrc/*
%endif

%ifnarch %ix86
install -pD -m755 ppc386 %buildroot%fpc_dir/ppc386
ln -s %fpc_dir/ppc386 %buildroot%_bindir/ppc386
%endif

%if %makewin32
#Install for win32
%fpc_install_win32 FPC=$PWD/ppc386 FPCMAKE=$PWD/fpcmake -C fpcsrc/rtl
%endif

#Install man
%__make INSTALL_PREFIX=%buildroot%_datadir -C install/man installman

#Instal docs
%__mkdir_p %buildroot%_defaultdocdir/%name-%version
%__install -p -m 644 install/doc/copying* install/doc/whatsnew.txt install/doc/readme.txt install/doc/faq.txt %buildroot%_defaultdocdir/%name-%version

# Create fpc.cfg
chmod 755 fpcsrc/compiler/utils/samplecfg
fpcsrc/compiler/utils/samplecfg "%fpc_dir" %buildroot%_sysconfdir
iconv -f CP866 -t UTF8 %buildroot%fpc_dir/msg/errorr.msg > %buildroot%fpc_dir/msg/errorru.msg
%__subst "s|errorn.msg|errorn.msg\n-Fr%fpc_dir/msg/errorru.msg|g" %buildroot%_sysconfdir/%name.cfg

%__mkdir_p %buildroot%_datadir/pixmaps
%__mkdir_p %buildroot%_miconsdir
%__mkdir_p %buildroot%_liconsdir
%__mkdir_p %buildroot%_niconsdir
%__mkdir_p %buildroot%_datadir/applications
%__install -p -m 644 %SOURCE1 %buildroot%_datadir/applications
%__mv %buildroot%_bindir/fp %buildroot%_bindir/fp-bin
%__install -p -m 755 %SOURCE2 %buildroot%_bindir/fp
%__install -p -m 644 %SOURCE3 %buildroot%_sysconfdir/fp.cfg
%__install -p -m 644 install/unix/fp32x32.xpm %buildroot%_datadir/pixmaps/fp.xpm
%__install -p -m 644 install/unix/fp32x32.xpm %buildroot%_niconsdir/fp.xpm
%__install -p -m 644 %SOURCE4 %buildroot%_miconsdir/fp.xpm
%__install -p -m 644 %SOURCE5 %buildroot%_liconsdir/fp.xpm

#Fix for depend
%ifarch x86_64
%__install -p -m 644 fpcsrc/utils/fppkg/units/x86_64-linux/*.{o,ppu} %buildroot%fpc_dir/units/x86_64-linux/fppkg/
%__subst "s|\$fpctarget|x86_64-linux|g" %buildroot%_sysconfdir/%name.cfg
%__subst "s|\$fpctarget|x86_64-linux|g" %buildroot%_sysconfdir/fp.cfg
%__subst "s|/usr/lib|%_libdir|g" %buildroot%_sysconfdir/fp.cfg
%else
%__install -p -m 644 fpcsrc/utils/fppkg/units/i386-linux/*.{o,ppu} %buildroot%fpc_dir/units/i386-linux/fppkg/
%__subst "s|\$fpctarget|i386-linux|g" %buildroot%_sysconfdir/%name.cfg
%__subst "s|\$fpctarget|i386-linux|g" %buildroot%_sysconfdir/fp.cfg
%endif
%__subst "s|\$fpcversion|fpc|g" %buildroot%_sysconfdir/%name.cfg

%files

%package common
Summary: Free Pascal -- Common files and dirs
Group: Development/Other

%description common
The Free Pascal Compiler is a Turbo Pascal 7.0 and Delphi compatible 32/64-bit
Pascal Compiler. It comes with a fully compatible TP 7.0 runtime library.
Some extensions are added to the language, like function overloading. Shared
libraries can be linked and created. Basic Delphi support is already
implemented (classes, exceptions, ansistrings). This package contains the
common files and dirs.

%files common
%dir %fpc_dir
%dir %_defaultdocdir/%name-%version

%package compiler
Summary: Free Pascal -- Compiler
Group: Development/Other
Requires: %name-common = %version-%release
Requires: binutils
Obsoletes: fpc <= 2.1-alt3

%description compiler
The Free Pascal Compiler is an object pascal compiler supporting both Delphi
and Turbo Pascal 7.0 dialects as well as Mac pascal dialects.
It provides a completely portable RunTime Library (RTL) available on many
platforms and compatible with Turbo Pascal, but also a platfrom independent
class based Free Component Library (FCL) adding many Delphi extensions and
interfacing many popular open source libraries.

Some extensions are added to the language, like function overloading. Shared
libraries can be linked and created. Delphi language extentions like classes,
exceptions, ansi strings and open arrays are also supported.

This package contains the command line compiler.

%files compiler
%config(noreplace) %_sysconfdir/%name.cfg
%_defaultdocdir/%name-%version/copying*
%_defaultdocdir/%name-%version/whatsnew.txt
%_defaultdocdir/%name-%version/readme.txt
%_defaultdocdir/%name-%version/faq.txt
%_bindir/fpc
%_bindir/ppc*
%_bindir/fpcsubst
%_bindir/fpcmkcfg
%_bindir/fppkg
%_bindir/grab_vcsa
%fpc_dir/samplecfg
%fpc_dir/ppc*
%fpc_dir/msg

#%doc /usr/share/doc/fp-compiler
%_man1dir/fpc.*
%_man1dir/fpcmkcfg.*
%_man1dir/fpcsubst.*
%_man1dir/ppc*.*
%_man1dir/grab_vcsa.*
%_man5dir/fpc.cfg.*

# utils
%package utils
Summary: Free Pascal -- Utils
Group: Development/Other
#Requires: %name = %version-%release
Obsoletes: fpcmake data2inc

%description utils
The Free Pascal Compiler is an object pascal compiler supporting both Delphi
and Turbo Pascal 7.0 dialects as well as Mac pascal dialects.
It provides a completely portable RunTime Library (RTL) available on many
platforms and compatible with Turbo Pascal, but also a platfrom independent
class based Free Component Library (FCL) adding many Delphi extensions and
interfacing many popular open source libraries.

This package contains some handy utils for usage with the Free Pascal
Compiler:
  - ppumove     Place multiple units in a shared library
  - ppufiles    Show needed files for units
  - ppudump     Dump the information stored in a .ppu (unit) file
  - fpcmake     Create Makefile from Makefile.fpc
  - h2pas       Convert .h files to pascal units
  - ppdep       Create a dependency file which can be used with Makefiles
  - ptop        Source beautifier
  - data2inc    Convert binary/text data to include files
  - plex/pyacc  Pascal Lex/Yacc implementation

%files utils
%_bindir/ppufiles
%_bindir/ppudump
%_bindir/ppumove
%_bindir/ppdep
%_bindir/ptop
%_bindir/rstconv
%_bindir/data2inc
%_bindir/bin2obj
%_bindir/delp
%_bindir/plex
%_bindir/pyacc
%_bindir/h2pas
%_bindir/h2paspp
%_bindir/postw32
%_bindir/fpcmake
%_bindir/fpcres
%_bindir/fprcp
%_bindir/fpdoc
%_bindir/makeskel
%_bindir/unitdiff
#%_bindir/mkxmlrpc
%_bindir/rmcvsdir
%_bindir/fpclasschart
%_bindir/chmcmd
%_bindir/chmls
%_bindir/mkarmins
%_bindir/mkx86ins
%_bindir/instantfpc
%doc fpcsrc/utils/fpcm/fpcmake.ini
%fpc_dir/units/%ppctarget/lexyacc
%fpc_dir/lexyacc
%_man1dir/bin2obj.1*
%_man1dir/data2inc.1*
%_man1dir/fprcp.1*
%_man1dir/h2paspp.1*
%_man1dir/makeskel.1*
%_man1dir/postw32.1*
%_man1dir/unitdiff.1*
%_man1dir/delp.1*
%_man1dir/fpcmake.1*
%_man1dir/h2pas.1*
%_man1dir/plex.1*
%_man1dir/ppdep.1*
%_man1dir/ppudump.1*
%_man1dir/ppufiles.1*
%_man1dir/ppumove.1*
%_man1dir/ptop.1*
%_man1dir/pyacc.1*
%_man1dir/rstconv.1*
%_man1dir/fpdoc.1*
%_man1dir/fpcres.1*
%_man1dir/fppkg.1*
%_man1dir/mkxmlrpc.1*
%_man1dir/rmcvsdir.1*
%_man1dir/chmcmd.1*
%_man1dir/chmls.1*
%_man1dir/fpclasschart.1*
%_man5dir/fpcmake.5*
%_man5dir/ptop.cfg.5*

# packages/rtl
%package units-rtl
Summary: Free Pascal -- Runtime Library
Group: Development/Other
Requires: %name-compiler = %version-%release

%description units-rtl
The Free Pascal Compiler is an object pascal compiler supporting both Delphi
and Turbo Pascal 7.0 dialects as well as Mac pascal dialects.
It provides a completely portable RunTime Library (RTL) available on many
platforms and compatible with Turbo Pascal, but also a platfrom independent
class based Free Component Library (FCL) adding many Delphi extensions and
interfacing many popular open source libraries.

This package contains the Runtime Libraries for the Free Pascal Compiler.

%files units-rtl
%dir %fpc_dir/units
%dir %fpc_dir/units/%ppctarget
%fpc_dir/units/%ppctarget/rtl

# packages/base
%package units-base
Summary: Free Pascal -- base units
Group: Development/Other
#Requires: %name = %version-%release

%description units-base
The Free Pascal Compiler is an object pascal compiler supporting both Delphi
and Turbo Pascal 7.0 dialects as well as Mac pascal dialects.
It provides a completely portable RunTime Library (RTL) available on many
platforms and compatible with Turbo Pascal, but also a platfrom independent
class based Free Component Library (FCL) adding many Delphi extensions and
interfacing many popular open source libraries.

This package contains Free Pascal units for common libraries.  Some of these
units are also required by the Free Component Library:
 - X11 (Xlib, Xutil)
 - NCurses
 - ZLib

%files units-base
#%doc /usr/share/doc/fp-units-base

%fpc_dir/units/%ppctarget/paszlib
%fpc_dir/units/%ppctarget/pasjpeg
%fpc_dir/units/%ppctarget/ncurses
%fpc_dir/units/%ppctarget/x11
%fpc_dir/units/%ppctarget/regexpr
%fpc_dir/units/%ppctarget/hash
%fpc_dir/units/%ppctarget/uuid
%fpc_dir/units/%ppctarget/fppkg
%fpc_dir/units/%ppctarget/iconvenc

# packages/fcl
%package units-fcl
Summary: Free Pascal -- Free Component Library
Group: Development/Other
#Requires: %name = %version-%release

%description units-fcl
The Free Pascal Compiler is an object pascal compiler supporting both Delphi
and Turbo Pascal 7.0 dialects as well as Mac pascal dialects.
It provides a completely portable RunTime Library (RTL) available on many
platforms and compatible with Turbo Pascal, but also a platfrom independent
class based Free Component Library (FCL) adding many Delphi extensions and
interfacing many popular open source libraries.

This package contains the Free Component Library for the Free Pascal Compiler.

%files units-fcl
#%doc /usr/share/doc/fp-units-fcl
%fpc_dir/units/%ppctarget/fcl-base
%fpc_dir/units/%ppctarget/fcl-db
%fpc_dir/units/%ppctarget/fcl-fpcunit
%fpc_dir/units/%ppctarget/fcl-image
%fpc_dir/units/%ppctarget/fcl-net
%fpc_dir/units/%ppctarget/fcl-passrc
%fpc_dir/units/%ppctarget/fcl-registry
%fpc_dir/units/%ppctarget/fcl-web
%fpc_dir/units/%ppctarget/fcl-xml
%fpc_dir/units/%ppctarget/fcl-process
%fpc_dir/units/%ppctarget/fcl-json
%fpc_dir/units/%ppctarget/fcl-async
%fpc_dir/units/%ppctarget/fcl-res
%fpc_dir/units/%ppctarget/fcl-extra
%fpc_dir/units/%ppctarget/fcl-js
#fpc_dir/units/%ppctarget/fcl-stl

# packages/fv
%package units-fv
Summary: Free Pascal -- Free Vision units
Group: Development/Other
#Requires: %name = %version-%release

%description units-fv
The Free Pascal Compiler is an object pascal compiler supporting both Delphi
and Turbo Pascal 7.0 dialects as well as Mac pascal dialects.
It provides a completely portable RunTime Library (RTL) available on many
platforms and compatible with Turbo Pascal, but also a platfrom independent
class based Free Component Library (FCL) adding many Delphi extensions and
interfacing many popular open source libraries.

This package contains the Free Vision units for the Free Pascal Compiler.

%files units-fv
#%doc /usr/share/doc/fp-units-fv
%fpc_dir/units/%ppctarget/fv

# packages/gtk
%package units-gtk
Summary: Free Pascal -- GTK+ 1.2 units
Group: Development/Other
#Requires: %name = %version-%release

%description units-gtk
The Free Pascal Compiler is an object pascal compiler supporting both Delphi
and Turbo Pascal 7.0 dialects as well as Mac pascal dialects.
It provides a completely portable RunTime Library (RTL) available on many
platforms and compatible with Turbo Pascal, but also a platfrom independent
class based Free Component Library (FCL) adding many Delphi extensions and
interfacing many popular open source libraries.

This package contains Free Pascal units and examples to create
programs with GTK+ 1.2.

%files units-gtk
#%doc /usr/share/doc/fp-units-gtk
%fpc_dir/units/%ppctarget/gtk1
%fpc_dir/units/%ppctarget/fpgtk

# packages/gtk2
%package units-gtk2
Summary: Free Pascal -- GTK+ 2.x units
Group: Development/Other
#Requires: %name = %version-%release

%description units-gtk2
The Free Pascal Compiler is an object pascal compiler supporting both Delphi
and Turbo Pascal 7.0 dialects as well as Mac pascal dialects.
It provides a completely portable RunTime Library (RTL) available on many
platforms and compatible with Turbo Pascal, but also a platfrom independent
class based Free Component Library (FCL) adding many Delphi extensions and
interfacing many popular open source libraries.

This package contains Free Pascal units and examples to create
programs with GTK+ 2.x.

%files units-gtk2
#%doc /usr/share/doc/fp-units-gtk2
%fpc_dir/units/%ppctarget/gtk2

# packages/gnome1
%package units-gnome1
Summary: Free Pascal -- GNOME 1 units
Group: Development/Other
#Requires: %name = %version-%release

%description units-gnome1
The Free Pascal Compiler is an object pascal compiler supporting both Delphi
and Turbo Pascal 7.0 dialects as well as Mac pascal dialects.
It provides a completely portable RunTime Library (RTL) available on many
platforms and compatible with Turbo Pascal, but also a platfrom independent
class based Free Component Library (FCL) adding many Delphi extensions and
interfacing many popular open source libraries.

This package contains Free Pascal units and examples to create
programs for GNOME 1.

%files units-gnome1
#%doc /usr/share/doc/fp-units-gnome1
%fpc_dir/units/%ppctarget/imlib
%fpc_dir/units/%ppctarget/gnome1

# packages/db
%package units-db
Summary: Free Pascal -- database libraries units
Group: Development/Other
#Requires: %name = %version-%release

%description units-db
The Free Pascal Compiler is an object pascal compiler supporting both Delphi
and Turbo Pascal 7.0 dialects as well as Mac pascal dialects.
It provides a completely portable RunTime Library (RTL) available on many
platforms and compatible with Turbo Pascal, but also a platfrom independent
class based Free Component Library (FCL) adding many Delphi extensions and
interfacing many popular open source libraries.

This package contains Free Pascal units with bindings for:
 - MySQL
 - Interbase
 - PostgreSQL
 - Oracle
 - ODBC
 - GDBM
 - SQLite

%files units-db
#%doc /usr/share/doc/fp-units-db
%fpc_dir/units/%ppctarget/mysql
%fpc_dir/units/%ppctarget/ibase
%fpc_dir/units/%ppctarget/postgres
%fpc_dir/units/%ppctarget/oracle
%fpc_dir/units/%ppctarget/odbc
%fpc_dir/units/%ppctarget/gdbm
%fpc_dir/units/%ppctarget/sqlite
%fpc_dir/units/%ppctarget/ldap
%fpc_dir/units/%ppctarget/pxlib

# packages/gfx
%package units-gfx
Summary: Free Pascal -- graphics libraries units
Group: Development/Other
#Requires: %name = %version-%release

%description units-gfx
The Free Pascal Compiler is an object pascal compiler supporting both Delphi
and Turbo Pascal 7.0 dialects as well as Mac pascal dialects.
It provides a completely portable RunTime Library (RTL) available on many
platforms and compatible with Turbo Pascal, but also a platfrom independent
class based Free Component Library (FCL) adding many Delphi extensions and
interfacing many popular open source libraries.

This package contains Free Pascal units with bindings for:
 - opengl :OpenGL
 - forms : Forms 0.88
 - svgalib : Svgalib
 - ggi : General Graphical Interface
 - libgd
 - libpng
 - graph
 - openal
 - cairo

%files units-gfx
#%doc /usr/share/doc/fp-units-gfx
%fpc_dir/units/%ppctarget/opengl
%fpc_dir/units/%ppctarget/xforms
%fpc_dir/units/%ppctarget/svgalib
%fpc_dir/units/%ppctarget/ggi
%fpc_dir/units/%ppctarget/libgd
%fpc_dir/units/%ppctarget/libpng
%fpc_dir/units/%ppctarget/graph
%fpc_dir/units/%ppctarget/openal
%fpc_dir/units/%ppctarget/cairo
%fpc_dir/units/%ppctarget/imagemagick
%fpc_dir/units/%ppctarget/rsvg
%fpc_dir/units/%ppctarget/hermes
%fpc_dir/units/%ppctarget/opencl
%fpc_dir/units/%ppctarget/ptc
#%fpc_dir/units/%ppctarget/fpvectorial
%_bindir/fd2pascal
%_man1dir/fd2pascal.1*


# packages/net
%package units-net
Summary: Free Pascal -- networking units
Group: Development/Other
#Requires: %name = %version-%release

%description units-net
The Free Pascal Compiler is an object pascal compiler supporting both Delphi
and Turbo Pascal 7.0 dialects as well as Mac pascal dialects.
It provides a completely portable RunTime Library (RTL) available on many
platforms and compatible with Turbo Pascal, but also a platfrom independent
class based Free Component Library (FCL) adding many Delphi extensions and
interfacing many popular open source libraries.

This package contains Free Pascal units for creating network tools:
 - netdb : NetDB unit for TCP/IP handling
 - libasync : LibAsync unit for easy Asynchronous IO
 - libcurl
 - dbus: D-Bus
 - httpd-1.3
 - httpd-2.0
 - httpd-2.2
 - ldap
 - openssl : Open SSL
 - pcap

%files units-net
#%doc /usr/share/doc/fp-units-net
%fpc_dir/units/%ppctarget/libcurl
%fpc_dir/units/%ppctarget/dbus
%fpc_dir/units/%ppctarget/httpd*
%fpc_dir/units/%ppctarget/openssl
%fpc_dir/units/%ppctarget/pcap
%fpc_dir/units/%ppctarget/fastcgi

# packages/math
%package units-math
Summary: Free Pascal - math units
Group: Development/Other
#Requires: %name = %version-%release

%description units-math
The Free Pascal Compiler is an object pascal compiler supporting both Delphi
and Turbo Pascal 7.0 dialects as well as Mac pascal dialects.
It provides a completely portable RunTime Library (RTL) available on many
platforms and compatible with Turbo Pascal, but also a platfrom independent
class based Free Component Library (FCL) adding many Delphi extensions and
interfacing many popular open source libraries.

This package contains Free Pascal math interfacing units for:
 - gmp : Interface for the GNU Multiple Precision Arithmetic Library
 - proj4 : Compute projections
 - numlib : numerical computing
 - symbolic : symbolic computing

%files units-math
#%doc /usr/share/doc/fp-units-math
%fpc_dir/units/%ppctarget/gmp
%fpc_dir/units/%ppctarget/proj4
%fpc_dir/units/%ppctarget/numlib
%fpc_dir/units/%ppctarget/symbolic

# packages/misc
%package units-misc
Summary: Free Pascal -- miscellaneous units
Group: Development/Other
#Requires: %name = %version-%release

%description units-misc
The Free Pascal Compiler is an object pascal compiler supporting both Delphi
and Turbo Pascal 7.0 dialects as well as Mac pascal dialects.
It provides a completely portable RunTime Library (RTL) available on many
platforms and compatible with Turbo Pascal, but also a platfrom independent
class based Free Component Library (FCL) adding many Delphi extensions and
interfacing many popular open source libraries.

This package contains Free Pascal miscellaneous units for:
 - fppkg : support of FPC packaging system
 - Utmp
 - PasZLib (Pascal-only zlib implementation)

%files units-misc
#%doc /usr/share/doc/fp-units-misc
%ifarch %ix86
%fpc_dir/units/%ppctarget/libc
%fpc_dir/units/%ppctarget/unixutil
%endif

%fpc_dir/units/%ppctarget/utmp
%fpc_dir/units/%ppctarget/pthreads
%fpc_dir/units/%ppctarget/zlib
%fpc_dir/units/%ppctarget/tcl
%fpc_dir/units/%ppctarget/cdrom
%fpc_dir/units/%ppctarget/bfd
%fpc_dir/units/%ppctarget/syslog
%fpc_dir/units/%ppctarget/gdbint
%fpc_dir/units/%ppctarget/unzip
%fpc_dir/units/%ppctarget/newt
%fpc_dir/units/%ppctarget/fftw
%fpc_dir/units/%ppctarget/fpmkunit
%fpc_dir/units/%ppctarget/users
%fpc_dir/units/%ppctarget/aspell
%fpc_dir/units/%ppctarget/chm
%fpc_dir/units/%ppctarget/libxml2
%fpc_dir/units/%ppctarget/lua
%fpc_dir/units/%ppctarget/bzip2
%fpc_dir/units/%ppctarget/zorba
%fpc_dir/units/%ppctarget/libsee

# packages/media
%package units-multimedia
Summary: Free Pascal -- graphics libraries units
Group: Development/Other
Obsoletes: fpc-units-media <= 2.2.0
Provides: fpc-units-media
#Requires: %name = %version-%release

%description units-multimedia
The Free Pascal Compiler is an object pascal compiler supporting both Delphi
and Turbo Pascal 7.0 dialects as well as Mac pascal dialects.
It provides a completely portable RunTime Library (RTL) available on many
platforms and compatible with Turbo Pascal, but also a platfrom independent
class based Free Component Library (FCL) adding many Delphi extensions and
interfacing many popular open source libraries.

This package contains Free Pascal multimedia interfacing units for:
 - oggvorbis
 - a52
 - dts (http://www.videolan.org/developers/libdca.html)
 - mad
 - modplug

%files units-multimedia
%fpc_dir/units/%ppctarget/a52
%fpc_dir/units/%ppctarget/dts
%fpc_dir/units/%ppctarget/oggvorbis
%fpc_dir/units/%ppctarget/mad
%fpc_dir/units/%ppctarget/modplug
%fpc_dir/units/%ppctarget/sdl

# ide
%package ide
Summary: Free Pascal -- IDE
Group: Development/Other
Requires: %name-common = %version-%release

%description ide
The Free Pascal Compiler is an object pascal compiler supporting both Delphi
and Turbo Pascal 7.0 dialects as well as Mac pascal dialects.
It provides a completely portable RunTime Library (RTL) available on many
platforms and compatible with Turbo Pascal, but also a platfrom independent
class based Free Component Library (FCL) adding many Delphi extensions and
interfacing many popular open source libraries.

Some extensions are added to the language, like function overloading. Shared
libraries can be linked and created. Delphi language extentions like classes,
exceptions, ansi strings and open arrays are also supported.

This package contains the Integrated Development Environment (IDE). The IDE
has an internal compiler.

%files ide
#%doc /usr/share/doc/fp-ide
%config(noreplace) %_sysconfdir/fp.cfg
%_bindir/fp
%_bindir/fp-bin
%fpc_dir/ide
%_man1dir/fp.1*
%_datadir/doc/%name-%version/readme.ide
%_datadir/pixmaps/*
%_miconsdir/*
%_liconsdir/*
%_niconsdir/*
%_datadir/applications/*

# src
%if %makesrc
%package src
Summary: Source of Free Pascal
Group: Development/Other
BuildArch: noarch
#Requires: %name = %version-%release

%description src
The Free Pascal Compiler is an object pascal compiler supporting both Delphi
and Turbo Pascal 7.0 dialects as well as Mac pascal dialects.
It provides a completely portable RunTime Library (RTL) available on many
platforms and compatible with Turbo Pascal, but also a platfrom independent
class based Free Component Library (FCL) adding many Delphi extensions and
interfacing many popular open source libraries.

This package contains Free Pascal's own source code. It is meant to be used by
the Lazarus IDE.

%files src
%_datadir/fpcsrc
%endif

%if %makedoc
%package docs
Group: Documentation
Summary: Free Pascal Compiler - Documentation
BuildArch: noarch
Requires: %name-common = %version-%release

%description docs
The Free Pascal Compiler is an object pascal compiler supporting both Delphi
and Turbo Pascal 7.0 dialects as well as Mac pascal dialects.
It provides a completely portable RunTime Library (RTL) available on many
platforms and compatible with Turbo Pascal, but also a platfrom independent
class based Free Component Library (FCL) adding many Delphi extensions and
interfacing many popular open source libraries.

This package provides documentation for the Free Pascal Compiler in HTML and 
PDF format.

%files docs
%_datadir/doc/%name-%version/*
%exclude %_datadir/doc/%name-%version/readme.ide
%exclude %_defaultdocdir/%name-%version/copying*
%exclude %_defaultdocdir/%name-%version/whatsnew.txt
%exclude %_defaultdocdir/%name-%version/readme.txt
%exclude %_defaultdocdir/%name-%version/faq.txt

%endif

%if %makewin32
# win32
%package win32
Summary: Free Pascal runtime library units cross-compiled for win32
Group: Development/Other
Requires: %name = %version-%release
#Requires: i386-mingw32msvc-binutils

%description win32
The Free Pascal Compiler is an object pascal compiler supporting both Delphi
and Turbo Pascal 7.0 dialects as well as Mac pascal dialects.
It provides a completely portable RunTime Library (RTL) available on many
platforms and compatible with Turbo Pascal, but also a platfrom independent
class based Free Component Library (FCL) adding many Delphi extensions and
interfacing many popular open source libraries.

%files win32
%ifnarch %ix86
%_bindir/ppc386
%fpc_dir/ppc386
%endif
%fpc_files *-win32 rtl

%endif

%changelog
* Fri May 11 2012 Andrey Cherepanov <cas@altlinux.org> 2:2.6.0-alt2.qa1
- Increase epoch to rollback version in p6 branch

* Sun Jan 01 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1:2.6.0-alt2
- New version 
- Fix (ALT #26509)

* Sat Dec 10 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1:2.6.0-alt1rc1
- RC1

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:2.5.20110826-alt2.1
- Rebuild with Python-2.7

* Sat Aug 27 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1:2.5.20110826-alt2
- Add Epoch for downgrade fpc in t6

* Fri Aug 26 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.5.20110826-alt1
- New development snapshot
- Fix build for x86_64 with bootstrap
- Update spec

* Sat Apr 30 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.5.20110430-alt1
- New development snapshot
- Use bootstrap for build
- Update spec

* Sun Feb 27 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.5.20110227-alt1
- New development snapshot

* Sun Feb 20 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.5.20101117-alt1
- New development snapshot
- Update spec

* Thu Sep 09 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 2.5.20100406-alt3
- Fix (ALT #24050)

* Thu May 06 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 2.5.20100406-alt2
- Fix encoding of errorru.msg

* Tue Apr 06 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 2.5.20100406-alt1
- New development version

* Fri Jan 01 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 2.4.0-alt1
- New version
- Update descriptions
- Add new subpackage %name-units-math
- Disable build documentation

* Wed Dec 02 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2.4-alt4
- Fix fp.desktop

* Thu Oct 01 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2.4-alt3
- Add new subpackage %name-common for provide common dirs
- Build docs
- Set BuildArch: noarch in %name-src %name-docs packages

* Wed Sep 30 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2.4-alt2
- Update spec for remove workaround for #11921
- Add fpcmake.ini to /usr/share/doc/%name-utils/ (ALT #20638)

* Sun Apr 19 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 2.2.4-alt1
- 2.2.4
- Switch to git
- Update spec (Thanks ender@)
- Add options for switch off win32 subpackage
- Cross-compiling from non-i386 to i386 is not yet supported at this time. Comment it.

* Sat Aug 16 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 2.2.2-alt1
- New version
- Update spec
- Rename subpackage fpc-units-media to fpc-units-multimedia

* Wed Dec 12 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2.0-alt3
- Cleanup fpc-src package for use minimal space. Removed %_datadir/fpcsrc/{ide,installer,tests,utils}
- Rename fp -> fp-bin and fp.sh -> fp (#13701)
- Add BuildRequires: fpc-utils

* Mon Nov 19 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2.0-alt2
- Fix #13442 (Thanks sbolshakov@)

* Tue Sep 11 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2.0-alt1
- New version
- Fix #12904 , #12758
- Add ru_utf8 message file and make default
- Add fp.sh: wrapper for copy /etc/fp.cfg -> $HOME/fpc/fp.cfg and start fp

* Wed Aug 01 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 2.1.4-alt2
- rebuilt with new fpc

* Tue May 22 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 2.1.4-alt1
- New version
- subpackages: fpc-units-rtl, fpc-compiler, fpc-units-base, fpc-ide, fpc-units-fcl, fpc-units-fv,
  fpc-units-gtk, fpc-units-gtk2, fpc-units-gnome1, fpc-units-db, fpc-units-gfx, fpc-units-net,
  fpc-units-misc, fpc-units-media, fpc-src

* Thu Feb 01 2007 Alexey Tourbin <at@altlinux.ru> 2.1-alt3
- updated to svn revision 6276

* Sun Jan 21 2007 Alexey Tourbin <at@altlinux.ru> 2.1-alt2
- updated to svn revision 6095 (fixes x86_64 build)
- packaged %_bindir/msg2inc

* Thu Jan 18 2007 Alexey Tourbin <at@altlinux.ru> 2.1-alt1
- this release is based on 2.1 development branch
- imported compiler/ and rtl/ from svn trunk; adapted for gear
- packaged internal compiler units into fpc-compunits package
- rtl/inc/videoh.inc: changed max screen width from 132 to 240
- fpc-win32: removed mingw32 binutils dependency (internal linker on)

* Sat Sep 16 2006 Alexey Tourbin <at@altlinux.ru> 2.0.4-alt2.1
- removed fpcmake from build requires; this should now build
  on x86_64, but will fail on i586, which is ok

* Sat Sep 16 2006 Alexey Tourbin <at@altlinux.ru> 2.0.4-alt2
- don't strip static libraries

* Sun Sep 10 2006 Alexey Tourbin <at@altlinux.ru> 2.0.4-alt1
- 2.0.2 -> 2.0.4+ (svn revision 4597)
- only fpc and rtl packaged now from here; buncha funky wild-ass
  units to be packaged separately
- fpc-win32 now works on x86_84 (as well as x86)

* Tue May 02 2006 Alexey Tourbin <at@altlinux.ru> 2.0.2-alt1
- 2.0.0 -> 2.0.2, Sisyphus release
- x86_64 build ok
- subpackages: fpc, fpc-utils, fpc-packages, fpc-ide, etc.;
  fpc-win32: cross-compile for win32 (i586 only)
- docs will be packaged separately
- TODO: examples unpackaged

* Fri Oct 21 2005 Alexey Tourbin <at@altlinux.ru> 2.0.0-alt1
- 1.0.10 -> 2.0.0
- fpcdir:='%_libdir/fpc2'; fpcdocdir:='%_docdir/fpc2'
- forward release for Daedalus

* Tue Feb 11 2004 Sergey P. Kondratyev <seirge@altlinux.ru> 1.0.10-alt1
- new version + docs and examples

* Mon Oct 07 2002 Michael Shigorin <mike@altlinux.ru> 1.0.6-alt1.1
- spec cleanup

* Sat Sep 19 2002 Sergey <skrivulja@erec.ru>
- adopted for Master

