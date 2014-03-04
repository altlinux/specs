%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-EtoileFoundation
Version: 0.5
Release: alt1.git20140227
Summary: The core framework for all Etoile projects
License: BSD
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/etoile/EtoileFoundation.git
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: libssl-devel

Requires: lib%name = %EVR
Requires: gnustep-back

%description
EtoileFoundation is the core framework for all Etoile projects,
providing numerous convenience methods on top of the OpenStep foundation
and significantly better support for reflection. Here is a summary of
some the interesting features:

- mirror-based reflection
- mixins and traits
- prototypes
- double-dispatch
- collection class protocol and additions
- UUID
- convenient macros such as FOREACH
- dynamic C array
- metamodel
- UTI
- generic history model
- socket
- stack trace recording

%package -n lib%name
Summary: Shared libraries of EtoileFoundation
Group: System/Libraries

%description -n lib%name
EtoileFoundation is the core framework for all Etoile projects,
providing numerous convenience methods on top of the OpenStep foundation
and significantly better support for reflection.

This package contains shared libraries of EtoileFoundation.

%package -n lib%name-devel
Summary: Development files of EtoileFoundation
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
EtoileFoundation is the core framework for all Etoile projects,
providing numerous convenience methods on top of the OpenStep foundation
and significantly better support for reflection.

This package contains development files of EtoileFoundation.

%prep
%setup

cp %_libdir/GNUstep/Etoile/* ~/RPM/

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

%make \
	messages=yes \
	debug=yes \
	strip=no \
	documentation=no \
	PROJECT_NAME=EtoileFoundation

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=no \
	PROJECT_NAME=EtoileFoundation

rm -f \
	%buildroot%_libdir/GNUstep/Frameworks/*.framework/*.framework

pushd %buildroot%_libdir
for j in EtoileFoundation EtoileXML EtoileThread; do
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

%files
%doc NEWS README.md TODO
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/*.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/EtoileFoundation.framework/Versions/0/Headers
%exclude %_libdir/GNUstep/Frameworks/EtoileThread.framework/Versions/0/Headers
%exclude %_libdir/GNUstep/Frameworks/EtoileXML.framework/Versions/0/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/*.framework/Headers
%_libdir/GNUstep/Frameworks/EtoileFoundation.framework/Versions/0/Headers
%_libdir/GNUstep/Frameworks/EtoileThread.framework/Versions/0/Headers
%_libdir/GNUstep/Frameworks/EtoileXML.framework/Versions/0/Headers

%changelog
* Tue Mar 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20140227
- Initial build for Sisyphus

