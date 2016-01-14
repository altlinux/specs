%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-SystemConfig
Version: 0.2
Release: alt1.git20140217.1
Summary: Provides various a common way to set system specific preferences
License: LGPLv2.1 / BSD
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/etoile/SystemConfig.git
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator libacpi-devel libX11-devel

Requires: lib%name = %EVR
Requires: gnustep-back

%description
SystemConfig is a framework which provides various a common way to set
system specific preferences by interfacing with the host system. Host
system means the following combo:

* operating sytem
* additional abstraction support (sound, network etc.)
* display/window server

%package -n lib%name
Summary: Shared libraries of SystemConfig
Group: System/Libraries

%description -n lib%name
SystemConfig is a framework which provides various a common way to set
system specific preferences by interfacing with the host system. Host
system means the following combo:

* operating sytem
* additional abstraction support (sound, network etc.)
* display/window server

This package contains shared libraries of SystemConfig.

%package -n lib%name-devel
Summary: Development files of SystemConfig
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
SystemConfig is a framework which provides various a common way to set
system specific preferences by interfacing with the host system. Host
system means the following combo:

* operating sytem
* additional abstraction support (sound, network etc.)
* display/window server

This package contains development files of SystemConfig.

%prep
%setup

cp %_libdir/GNUstep/Etoile/* ~/RPM/
prepare_docgen

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%make \
	messages=yes \
	debug=yes \
	strip=no \
	documentation=yes \
	PROJECT_NAME=SystemConfig \
	LIBACPI=yes

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=SystemConfig \
	LIBACPI=yes

rm -f \
	%buildroot%_libdir/GNUstep/Frameworks/*.framework/*.framework

pushd %buildroot%_libdir
for j in SystemConfig; do
	for i in lib$j.so*; do
		rm -f $i
		mv GNUstep/Frameworks/$j.framework/Versions/Current/$i ./
		for k in lib$j.so.*.*; do
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/Current/$i
			rm GNUstep/Frameworks/$j.framework/Versions/Current/$j
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/Current/$j
		done
	done
done
popd

#install -d %buildroot%_docdir/GNUstep/UnitKit
#cp -fRP Documentation/* %buildroot%_docdir/GNUstep/UnitKit/

%files
%doc ChangeLog NEWS README TODO
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/SystemConfig.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/SystemConfig.framework/Versions/0/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/SystemConfig.framework/Headers
%_libdir/GNUstep/Frameworks/SystemConfig.framework/Versions/0/Headers

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.2-alt1.git20140217.1
- NMU: Rebuild with libgnutls30.

* Thu Mar 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20140217
- Initial build for Sisyphus

