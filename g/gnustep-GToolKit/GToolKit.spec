%set_verify_elf_method unresolved=strict

Name: gnustep-GToolKit
Version: 0.9.5
Release: alt1
Summary: Implements a simple and easy to use ObjC interface to the GTK+ widget set
License: GPLv2 / LGPLv2.1
Group: Graphical desktop/GNUstep
Url: http://gnu.ethz.ch/linuks.mine.nu/aclock/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gtk+-devel

%description
GToolKit is a (relatively) small library that implements a simple and
easy to use Objective-C interface to the GTK+ widget set. GTK+, which
stands for The Gimp Toolkit, is a library for creating graphical user
interfaces for the X Window System and MS Win32 (and maybe BeOS in the
future).

There are already a number of different Objective-C interface libraries
around and each one has its own features, so you have to decide for
yourself which one to try and use.

%package -n lib%name
Summary: Implements a simple and easy to use ObjC interface to the GTK+ widget set
Group: System/Libraries

%description -n lib%name
GToolKit is a (relatively) small library that implements a simple and
easy to use Objective-C interface to the GTK+ widget set. GTK+, which
stands for The Gimp Toolkit, is a library for creating graphical user
interfaces for the X Window System and MS Win32 (and maybe BeOS in the
future).

There are already a number of different Objective-C interface libraries
around and each one has its own features, so you have to decide for
yourself which one to try and use.

%package -n lib%name-devel
Summary: Development files of GToolKit
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
GToolKit is a (relatively) small library that implements a simple and
easy to use Objective-C interface to the GTK+ widget set. GTK+, which
stands for The Gimp Toolkit, is a library for creating graphical user
interfaces for the X Window System and MS Win32 (and maybe BeOS in the
future).

There are already a number of different Objective-C interface libraries
around and each one has its own features, so you have to decide for
yourself which one to try and use.

This package contains development files of GToolKit.

%package -n lib%name-devel-doc
Summary: Documentation for GToolKit
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
GToolKit is a (relatively) small library that implements a simple and
easy to use Objective-C interface to the GTK+ widget set. GTK+, which
stands for The Gimp Toolkit, is a library for creating graphical user
interfaces for the X Window System and MS Win32 (and maybe BeOS in the
future).

There are already a number of different Objective-C interface libraries
around and each one has its own features, so you have to decide for
yourself which one to try and use.

This package contains development documentation for GToolKit.

%prep
%setup

for i in $(find ./ -type f); do
	sed -i 's|objc/|objc2/|g' $i
done

%build
%autoreconf
%configure \
	--with-gnustep \
	--enable-static=no

%make_build -C GToolKit \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP -I%_includedir/gtk-1.2' \
	CONFIG_SYSTEM_LIBS='-lgtk -lgnustep-base -lobjc2' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles \
	GNUSTEP_SYSTEM_ROOT=%_datadir/GNUstep
 
%install
%makeinstall_std -C GToolKit GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles \
	GNUSTEP_SYSTEM_ROOT=%_datadir/GNUstep

%files -n lib%name
%doc NEWS README* TODO
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_datadir/GNUstep

%files -n lib%name-devel-doc
%doc html/*

%changelog
* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1
- Initial build for Sisyphus

