Name: gnustep-renaissance
Version: 0.9.0
Release: alt2.git20121208
Summary: The GNUstep development framework
License: LGPLv2.1+
Group: Development/Tools
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-renaissance.git
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel gnustep-gui-devel /proc
BuildPreReq: texlive-latex-base

Requires: lib%name = %version-%release

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
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='%optflags -DGNUSTEP' \
	CONFIG_SYSTEM_LIBS='-lgnustep-gui -lgnustep-base -lobjc' \

%make_build -C Documentation \
	messages=yes \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%makeinstall_std -C Documentation \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

gzip ChangeLog

%files
%doc AUTHORS ChangeLog* NEWS README TODO
%_bindir/*
%_libdir/GNUstep

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files doc
%_docdir/GNUstep

%changelog
* Thu Dec 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt2.git20121208
- Added synonym: lib%name-devel -> %name-devel

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20121208
- Initial build for Sisyphus

