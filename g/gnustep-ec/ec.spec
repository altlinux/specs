%set_verify_elf_method unresolved=strict

Name: gnustep-ec
Version: 1.0.2
Release: alt4.svn20140228
Summary: Enterprise Control Configuration and Logging framework
License: GPLv3 / LGPLv3
Group: Graphical desktop/GNUstep
Url: https://github.com/gnustep/gnustep-ec
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/libs/ec/trunk/
Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: libreadline-devel libncurses-devel

Requires: lib%name = %EVR
Requires: gnustep-back

%description
Enterprise Control Configuration and Logging framework.

%package -n lib%name
Summary: Shared libraries of Enterprise Control Configuration and Logging framework
Group: System/Libraries

%description -n lib%name
Enterprise Control Configuration and Logging framework.

This package contains shared libraries of Enterprise Control
Configuration and Logging framework.

%package -n lib%name-devel
Summary: Development files of Enterprise Control Configuration and Logging framework
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
Enterprise Control Configuration and Logging framework.

This package contains development files of Enterprise Control
Configuration and Logging framework.

%package docs
Summary: Documentation for Enterprise Control Configuration and Logging framework
Group: Documentation
BuildArch: noarch

%description docs
Enterprise Control Configuration and Logging framework.

This package contains documentation for Enterprise Control
Configuration and Logging framework.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%autoreconf
%configure \
	--with-readline \
	--disable-net-snmp

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS='-lgnustep-base -lobjc2'
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog README*
%_bindir/*
%_menudir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files docs
%_docdir/GNUstep

%changelog
* Mon Mar 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt4.svn20140228
- New snapshot

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt4.svn20140116
- Built with clang

* Mon Feb 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt3.svn20140116
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt2.svn20140116
- New snapshot

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt2.git20131212
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20131212
- Initial build for Sisyphus

