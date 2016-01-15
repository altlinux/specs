%set_verify_elf_method unresolved=strict

Name: gnustep-corebase
Version: 0.2
Release: alt2.svn20140220.1
Summary: Open implementation of CoreFoundation
License: LGPLv2+, GPLv3+
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-corebase.git
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel libicu-devel /proc
BuildPreReq: doxygen graphviz
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel zlib-devel

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

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%autoreconf
%configure \
	--libexecdir=%_libdir \
	--with-zoneinfo-dir=%_datadir/zoneinfo \
	--with-installation-domain=SYSTEM

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files -n lib%name
%doc ANNOUNCE ChangeLog README
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.2-alt2.svn20140220.1
- NMU: Rebuild with libgnutls30.

* Mon Mar 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2.svn20140220
- New snapshot

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2.svn20140203
- Built with clang

* Tue Feb 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.svn20140203
- New snapshot

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20130921
- New snapshot

* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20130814
- New snapshot

* Wed Jan 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20130121
- New snapshot

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20121221
- New snapshot

* Thu Dec 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20121206
- Initial build for Sisyphus

