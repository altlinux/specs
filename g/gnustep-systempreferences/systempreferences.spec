Name: gnustep-systempreferences
Version: 1.1.0
Release: alt2.git20120323
Summary: Implementation of the PreferencePanes framework (NSPreferencePane)
License: GPLv2+
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-systempreferences.git
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel gnustep-gui-devel /proc

Requires: lib%name = %version-%release

%description
This is the implementation of the PreferencePanes framework
(NSPreferencePane) as described in the Apple Documentation.

Inspiration for some of the panels comes from Jeff Teunissen's original
Preferences application (Backbone project:
http://www.nongnu.org/backbone/ ).

%package -n lib%name
Summary: Shared libraries of %name
Group: System/Libraries

%description -n lib%name
This is the implementation of the PreferencePanes framework
(NSPreferencePane) as described in the Apple Documentation.

This package contains shared libraries of %name.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
This is the implementation of the PreferencePanes framework
(NSPreferencePane) as described in the Apple Documentation.

This package contains development files of %name.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2' \
	CONFIG_SYSTEM_LIBS='-lgnustep-base -lobjc2'
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
for i in *.so*; do
	rm -f $i
	mv GNUstep/Frameworks/PreferencePanes.framework/Versions/Current/$i ./
	ln -s %_libdir/$i \
		GNUstep/Frameworks/PreferencePanes.framework/Versions/Current/
done
popd

%files
%doc ChangeLog README TODO
%_bindir/*
%_libdir/GNUstep

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2.git20120323
- Rebuilt with libobjc2 instead of libobjc

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20120323
- Initial build for Sisyphus

