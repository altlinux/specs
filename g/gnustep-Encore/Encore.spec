%set_verify_elf_method unresolved=strict

Name: gnustep-Encore
Version: 0.3.1
Release: alt3
Summary: A set of utility classes
License: LGPLv2.1
Group: Graphical desktop/GNUstep
Url: http://fortytwo.sourceforge.net/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: lib%name = %EVR
Requires: gnustep-back

%description
Encore is a set of utility classes written in Objective-C for GNUstep
and Mac OS X.  The motivation of writting these classes was driven by
implementing the projects BDB and FT. The classes may be useful for
other projects as well.

The classes include
  - logging:  A flexible logging mechanism similiar to log4j. Supports
    logging levels, logging contexts, different output channels per
    context, configuration per xml, ...
  - XML-based reflection: a configuration mechanism which is based on
    XML and uses inversion of control (see tests for an example)
  - a simple testing framework
  - StringUtils class
  - an iterator interface

%package -n lib%name
Summary: Shared libraries of Encore
Group: System/Libraries

%description -n lib%name
Encore is a set of utility classes written in Objective-C for GNUstep
and Mac OS X.  The motivation of writting these classes was driven by
implementing the projects BDB and FT. The classes may be useful for
other projects as well.

This package contains shared libraries of Encore.

%package -n lib%name-devel
Summary: Development files of Encore
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
Encore is a set of utility classes written in Objective-C for GNUstep
and Mac OS X.  The motivation of writting these classes was driven by
implementing the projects BDB and FT. The classes may be useful for
other projects as well.

This package contains development files of Encore.

%prep
%setup

for i in $(find ./ -type f); do
	sed -i 's|Encore/||g' $i
done

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	CONFIG_SYSTEM_LIBS='-lgnustep-base -lobjc2' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

pushd %buildroot%_libdir
for j in Encore; do
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
%doc ANNOUNCEMENT ChangeLog README TODO documentation/encore.html
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/Encore.framework/Versions/0/Headers
%exclude %_libdir/GNUstep/Frameworks/Encore.framework/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/Encore.framework/Versions/0/Headers
%_libdir/GNUstep/Frameworks/Encore.framework/Headers

%changelog
* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt3
- Added Requires: gnustep-back

* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt2
- Added %_includedir/Encore/ECLoggingConfigurationFactory.h

* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus

