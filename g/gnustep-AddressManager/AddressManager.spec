%set_verify_elf_method unresolved=strict

Name: gnustep-AddressManager
Version: 0.4.8
Release: alt6
Summary: Versatile address book application for managing contact information
License: LGPL
Group: Networking/Mail
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel gnustep-gui-devel

Requires: lib%name = %EVR
Requires: gnustep-back

%description
AddressManager is a versatile address book application for managing
contact information.

It stores addresses, phone numbers, pictures, instant messaging
information, email, homepages and whatever.

%package -n lib%name
Summary: Shared libraries of GNUstep AddressManager
Group: System/Libraries

%description -n lib%name
AddressManager is a versatile address book application for managing
contact information.

It stores addresses, phone numbers, pictures, instant messaging
information, email, homepages and whatever.

This package contains shared libraries of GNUstep AddressManager.

%package -n lib%name-devel
Summary: Development files of GNUstep AddressManager
Group: Development/Objective-C
Requires: lib%name = %EVR
Requires: %name = %EVR
Provides: %name-devel = %EVR

%description -n lib%name-devel
AddressManager is a versatile address book application for managing
contact information.

It stores addresses, phone numbers, pictures, instant messaging
information, email, homepages and whatever.

This package contains development files of GNUstep AddressManager.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build -C Frameworks/Addresses \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	CONFIG_SYSTEM_LIBS='-lgnustep-gui -lgnustep-base -lobjc2'

%make_build $1 $2 \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	CONFIG_SYSTEM_LIBS="-lAddresses -lgnustep-gui -lgnustep-base -lobjc2"
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
for i in Addresses AddressView; do
	lib=$(ls lib$i.so.*.*.*)
	for j in lib$i.so*; do
		rm -f $j
		mv GNUstep/Frameworks/$i.framework/Versions/0/$j ./
		ln -s %_libdir/$lib GNUstep/Frameworks/$i.framework/Versions/0/$j
	done
	rm -f GNUstep/Frameworks/$i.framework/Versions/0/$i
	ln -s %_libdir/$lib GNUstep/Frameworks/$i.framework/Versions/0/$i
done
popd

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%_bindir/*
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/*.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/*.framework/Versions/0/Headers
%_menudir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/*.framework/Headers
%_libdir/GNUstep/Frameworks/*.framework/Versions/0/Headers

%changelog
* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt6
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt5
- Rebuilt with new gnustep-gui

* Thu Feb 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt4
- Added menu file (thnx kostyalamer@)

* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt3
- Added requirement on %name for lib%name-devel

* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt2
- Moved Headers into devel subpackage

* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt1
- Initial build for Sisyphus

