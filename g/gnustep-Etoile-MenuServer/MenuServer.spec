%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-MenuServer
Version: 0.4
Release: alt1.svn20130610
Summary: The server app which provides the menubar's background
License: GPLv2+
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn://svn.gna.org/svn/etoile/trunk/Etoile/Services/Private/MenuServer/
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator
BuildPreReq: gnustep-Etoile-XWindowServerKit-devel
BuildPreReq: gnustep-Etoile-SystemConfig-devel

Requires: gnustep-back gnustep-Etoile-XWindowServerKit
Requires: gnustep-Etoile-SystemConfig

%description
EtoileMenuServer communicates with System the Etoile daemonizer to
handle requests such as sleep, reboot and shut down. System plays the
role of a session manager in Etoile environment. You can specifiy
another session manager than System by setting assigning another name to
ETSessionManager default and registering an object in some other process
for this name by the mean of Distributed Objects. Then EtoileMenuServer
will retrieve a proxy for this object and forward those requests to it.
This remote object must implement a simple protocol that consists of the
following messages:

- (oneway void) logOut;
- (oneway void) powerOff: (BOOL)reboot;
- (oneway void) suspend;

System implements theses messages in SCSystem class.

%prep
%setup

cp %_libdir/GNUstep/Etoile/* ~/
prepare_docgen

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%make \
	messages=yes \
	debug=yes \
	strip=no \
	documentation=yes \
	PROJECT_NAME=MenuServer

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=MenuServer

#install -d %buildroot%_docdir/GNUstep/UnitKit
#cp -fRP Documentation/* %buildroot%_docdir/GNUstep/UnitKit/

%files
%doc ChangeLog README
%_bindir/*
%_libdir/GNUstep

%changelog
* Fri Mar 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.svn20130610
- Initial build for Sisyphus

