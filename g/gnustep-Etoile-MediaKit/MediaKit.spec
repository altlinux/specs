%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-MediaKit
Version: 0.1
Release: alt1.svn20140217
Summary: Work-in-progress replacement for MultimediaKit
License: BSD
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn://svn.gna.org/svn/etoile/trunk/Etoile/Frameworks/MediaKit/
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator libavcodec-devel
BuildPreReq: libavformat-devel gnustep-Etoile-EtoileFoundation-devel
BuildPreReq: gnustep-Etoile-SystemConfig-devel libtag-devel
BuildPreReq: libmpeg4ip-devel

Requires: lib%name = %EVR
Requires: gnustep-back ossp gnustep-Etoile-EtoileFoundation
Requires: gnustep-Etoile-SystemConfig

%description
This is a work-in-progress replacement for MultimediaKit. It currently
only plays music files. It uses OSS for sound output and libavcodec /
libavformat for file parsing.

%package -n lib%name
Summary: Shared libraries of MediaKit
Group: System/Libraries

%description -n lib%name
This is a work-in-progress replacement for MultimediaKit. It currently
only plays music files. It uses OSS for sound output and libavcodec /
libavformat for file parsing.

This package contains shared libraries of MediaKit.

%package -n lib%name-devel
Summary: Development files of MediaKit
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
This is a work-in-progress replacement for MultimediaKit. It currently
only plays music files. It uses OSS for sound output and libavcodec /
libavformat for file parsing.

This package contains development files of MediaKit.

%package docs
Summary: Documentation for MediaKit
Group: Development/Documentation
BuildArch: noarch

%description docs
This is a work-in-progress replacement for MultimediaKit. It currently
only plays music files. It uses OSS for sound output and libavcodec /
libavformat for file parsing.

This package contains documentation for MediaKit.

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
	PROJECT_NAME=MediaKit

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=MediaKit

rm -f \
	%buildroot%_libdir/GNUstep/Frameworks/*.framework/*.framework

pushd %buildroot%_libdir
for j in MediaKit; do
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

install -d %buildroot%_docdir/GNUstep/MediaKit
cp -fRP Documentation/* %buildroot%_docdir/GNUstep/MediaKit/

%files
%doc NEWS README
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/MediaKit.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/MediaKit.framework/Versions/0/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/MediaKit.framework/Headers
%_libdir/GNUstep/Frameworks/MediaKit.framework/Versions/0/Headers

%files docs
%_docdir/GNUstep

%changelog
* Thu Mar 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.svn20140217
- Initial build for Sisyphus

