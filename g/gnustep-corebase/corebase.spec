Name: gnustep-corebase
Version: 0.2
Release: alt1.git20121206
Summary: Open implementation of CoreFoundation
License: LGPLv2+, GPLv3+
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-corebase.git
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel libicu-devel /proc
BuildPreReq: doxygen graphviz

%description
The GNUstep CoreBase Library is a library of general-purpose,
non-graphical C objects.  For example, it includes types for strings,
collections, byte streams, typed coders, invocations, notifications,
notification dispatchers, moments in time, network ports, and event
loops.

It provides functionality that aims to implement the non-graphical
portion of Apple's CoreFoundation framework.

%package -n lib%name
Summary: Open implementation of CoreFoundation
Group: System/Libraries

%description -n lib%name
The GNUstep CoreBase Library is a library of general-purpose,
non-graphical C objects.  For example, it includes types for strings,
collections, byte streams, typed coders, invocations, notifications,
notification dispatchers, moments in time, network ports, and event
loops.

It provides functionality that aims to implement the non-graphical
portion of Apple's CoreFoundation framework.

This package contains shared libraries of the GNUstep CoreBase Library.

%package -n lib%name-devel
Summary: Development files of open implementation of CoreFoundation
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
The GNUstep CoreBase Library is a library of general-purpose,
non-graphical C objects.  For example, it includes types for strings,
collections, byte streams, typed coders, invocations, notifications,
notification dispatchers, moments in time, network ports, and event
loops.

It provides functionality that aims to implement the non-graphical
portion of Apple's CoreFoundation framework.

This package contains development files of the GNUstep CoreBase Library.

%prep
%setup

for i in $(find ./ -type f); do
	sed -i 's|objc/|objc2/|g' $i
done

%build
%autoreconf
%configure \
	--libexecdir=%_libdir \
	--with-zoneinfo-dir=%_datadir/zoneinfo \
	--with-installation-domain=SYSTEM

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2'
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files -n lib%name
%doc ANNOUNCE ChangeLog README
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Thu Dec 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20121206
- Initial build for Sisyphus

