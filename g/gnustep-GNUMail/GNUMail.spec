%set_verify_elf_method unresolved=strict

Name: gnustep-GNUMail
Version: 1.2.0
Release: alt5
Summary: Official GNUstep mail application and a clone of NeXT's Mail.app
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Pantomime-devel
BuildPreReq: gnustep-AddressManager-devel

Requires: lib%name = %EVR
Requires: gnustep-AddressManager gnustep-Pantomime

%description
GNUMail is the official GNUstep mail application and a clone of NeXT's
Mail.app.

The current version of GNUMail.app is already quite stable and rich in
functionalities and will work well for a day-to-day MUA use.

%package -n lib%name
Summary: Shared libraries of GNUstep GNUMail
Group: System/Libraries

%description -n lib%name
GNUMail is the official GNUstep mail application and a clone of NeXT's
Mail.app.

The current version of GNUMail.app is already quite stable and rich in
functionalities and will work well for a day-to-day MUA use.

This package contains shared libraries of GNUstep GNUMail.

%package -n lib%name-devel
Summary: Development files of GNUstep GNUMail
Group: Development/Objective-C
Requires: lib%name = %EVR
Requires: %name = %EVR
Provides: %name-devel = %EVR

%description -n lib%name-devel
GNUMail is the official GNUstep mail application and a clone of NeXT's
Mail.app.

The current version of GNUMail.app is already quite stable and rich in
functionalities and will work well for a day-to-day MUA use.

This package contains development files of GNUstep GNUMail.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	CONFIG_SYSTEM_LIBS='-lPantomime -lAddressView -lAddresses -lgnustep-gui -lgnustep-base -lobjc2' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

pushd %buildroot%_libdir
for i in GNUMail; do
	lib=$(ls lib$i.so.*.*.*)
	for j in lib$i.so*; do
		rm -f $j
		mv GNUstep/Frameworks/$i.framework/Versions/1/$j ./
		ln -s %_libdir/$lib GNUstep/Frameworks/$i.framework/Versions/1/$j
	done
	rm -f GNUstep/Frameworks/$i.framework/Versions/1/$i
	ln -s %_libdir/$lib GNUstep/Frameworks/$i.framework/Versions/1/$i
done
popd

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog* README Documentation
%_bindir/*
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/*.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/*.framework/Versions/1/Headers
%_menudir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/*.framework/Headers
%_libdir/GNUstep/Frameworks/*.framework/Versions/1/Headers

%changelog
* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt5
- Rebuilt with new gnustep-gui

* Sat Mar 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt4
- Fixed menu file by kostyalamer@

* Thu Feb 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt3
- Added menu file (thnx kostyalamer@)

* Wed Feb 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2
- Added Requires: gnustep-AddressManager gnustep-Pantomime

* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus

