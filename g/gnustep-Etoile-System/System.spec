%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-System
Version: 0.1
Release: alt1.git20121130
Summary: Etoile main system process
License: LGPLv2.1
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/etoile/System.git
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator libdbus-devel
BuildPreReq: gnustep-Etoile-EtoileFoundation-devel

Requires: lib%name = %EVR
Requires: gnustep-back gnustep-Etoile-EtoileFoundation

%description
Etoile main system process, which plays the role of an init process
and a main server process (taking care of starting/stopping
and monitor Etoile core processes, possibly restarting them if they
die).

%package -n lib%name
Summary: Shared libraries of Etoile main system process
Group: System/Libraries

%description -n lib%name
Etoile main system process, which plays the role of an init process
and a main server process (taking care of starting/stopping
and monitor Etoile core processes, possibly restarting them if they
die).

This package contains shared libraries of Etoile main system process.

%package -n lib%name-devel
Summary: Development files of Etoile main system process
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
Etoile main system process, which plays the role of an init process
and a main server process (taking care of starting/stopping
and monitor Etoile core processes, possibly restarting them if they
die).

This package contains development files of Etoile main system process.

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
	PROJECT_NAME=System

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=System

#install -d %buildroot%_docdir/GNUstep/UnitKit
#cp -fRP Documentation/* %buildroot%_docdir/GNUstep/UnitKit/

%files
%doc ChangeLog README
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Thu Mar 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20121130
- Initial build for Sisyphus

