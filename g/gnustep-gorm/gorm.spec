%set_verify_elf_method unresolved=strict

Name: gnustep-gorm
Version: 1.2.18
Release: alt2.git20120726
Summary: The GNUstep Interface Builder
License: GPLv3+
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-gorm.git
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel gnustep-gui-devel /proc
BuildPreReq: texinfo texi2html texlive-latex-base

Requires: lib%name = %version-%release

%description
Gorm is an acronym for Graphic Object Relationship modeler (or perhaps
GNUstep Object Relationship Modeler).

Gorm is a clone of the Cocoa (OpenStep/NeXTSTEP) `Interface Builder'
application for GNUstep.

%package -n lib%name
Summary: Shared libraries of the GNUstep Interface Builder
Group: System/Libraries

%description -n lib%name
Gorm is an acronym for Graphic Object Relationship modeler (or perhaps
GNUstep Object Relationship Modeler).

This package contains shared libraries of Gorm.

%package -n lib%name-devel
Summary: Development files of the GNUstep Interface Builder
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release
Requires: %name = %version-%release

%description -n lib%name-devel
Gorm is an acronym for Graphic Object Relationship modeler (or perhaps
GNUstep Object Relationship Modeler).

This package contains development files of Gorm.

%package doc
Summary: Documentation for the GNUstep Interface Builder
Group: Documentation
BuildArch: noarch

%description doc
Gorm is an acronym for Graphic Object Relationship modeler (or perhaps
GNUstep Object Relationship Modeler).

This package contains documentation for Gorm.

%prep
%setup

%build
export GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

buildIt() {
	%make_build \
		messages=yes \
		debug=yes \
		strip=no \
		shared=yes \
		AUXILIARY_CPPFLAGS='-O2' \
		CONFIG_SYSTEM_LIBS="-lgnustep-gui -lgnustep-base -lobjc2 -lm $1 $2 $3"
}

libGorm=$PWD/GormLib/obj/libGorm.so
libGormCore=$PWD/GormCore/obj/libGormCore.so
libGormPrefs=$PWD/GormPrefs/obj/libGormPrefs.so

buildIt
pushd GormCore
%make clean
buildIt $libGorm
popd
pushd GormPrefs
%make clean
buildIt $libGormCore $libGorm
popd

for i in 0Menus 1Windows 2Controls 3Containers 4Data Gorm Nib GModel Xib
do
	rm -f $(find ./ -name $i -type f)
done
buildIt $libGormPrefs $libGormCore $libGorm
 
%make_build -C Documentation \
	messages=yes

%install
%makeinstall_std \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%makeinstall_std -C Documentation \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

gzip ChangeLog

%files
%doc ANNOUNCE ChangeLog* NEWS NOTICE README TODO
%_bindir/*
%_libdir/GNUstep

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files doc
%_docdir/GNUstep
%_infodir/*

%changelog
* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.18-alt2.git20120726
- Rebuilt with libobjc2 instead of libobjc

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.18-alt1.git20120726
- Initial build for Sisyphus

