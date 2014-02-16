Name: gnustep-renaissance
Version: 0.9.0
Release: alt7.svn20130529
Summary: The GNUstep development framework
License: LGPLv2.1+
Group: Development/Tools
Url: http://www.gnustep.it/Renaissance/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/libs/renaissance/trunk/
Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel gnustep-gui-devel /proc
BuildPreReq: texlive-latex-base

Requires: lib%name = %version-%release
Requires: gnustep-back

%description
Renaissance is an alternative way to make GUIs using which supports
automatic layout of widgets as well as for internationalization. GUIs
are specified in renaissance using a user-editable and readable XML
based format.

%package -n lib%name
Summary: Shared libraries of the GNUstep development framework
Group: System/Libraries

%description -n lib%name
Renaissance is an alternative way to make GUIs using which supports
automatic layout of widgets as well as for internationalization. GUIs
are specified in renaissance using a user-editable and readable XML
based format.

This package contains shared libraries of Renaissance.

%package -n lib%name-devel
Summary: Development files of the GNUstep development framework
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release
Requires: %name = %version-%release

%description -n lib%name-devel
Renaissance is an alternative way to make GUIs using which supports
automatic layout of widgets as well as for internationalization. GUIs
are specified in renaissance using a user-editable and readable XML
based format.

This package contains development files of Renaissance.

%package doc
Summary: Documentation for the GNUstep development framework
Group: Development/Documentation
BuildArch: noarch

%description doc
Renaissance is an alternative way to make GUIs using which supports
automatic layout of widgets as well as for internationalization. GUIs
are specified in renaissance using a user-editable and readable XML
based format.

This package contains documentation for Renaissance.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS='-lgnustep-gui -lgnustep-base -lobjc2'

%make_build -C Documentation \
	messages=yes
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%makeinstall_std -C Documentation \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

gzip ChangeLog

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc AUTHORS ChangeLog* NEWS README TODO
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files doc
%_docdir/GNUstep

%changelog
* Sun Feb 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt7.svn20130529
- Added menu file (thnx kostyalamer@)

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt6.svn20130529
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt5.svn20130529
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt4.svn20130529
- Rebuilt with new gnustep-gui

* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt3.svn20130529
- New snapshot

* Tue Mar 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt3.git20130131
- New snapshot

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt3.git20121208
- Rebuilt with libobjc2 instead of libobjc

* Thu Dec 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt2.git20121208
- Added synonym: lib%name-devel -> %name-devel

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20121208
- Initial build for Sisyphus

