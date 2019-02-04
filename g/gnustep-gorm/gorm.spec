%set_verify_elf_method unresolved=strict

Name: gnustep-gorm
Version: 1.2.20
Release: alt4.svn20140119
Summary: The GNUstep Interface Builder
License: GPLv3+
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
ExcludeArch: aarch64

# http://svn.gna.org/svn/gnustep/apps/gorm/trunk/
Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel gnustep-gui-devel /proc
BuildPreReq: texinfo texi2html texlive-latex-base

Requires: lib%name = %version-%release
Requires: gnustep-back

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
sed -i 's/@subsection/@section/g' Documentation/*.texi

%build
export GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

buildIt() {
	%make_build \
		messages=yes \
		debug=yes \
		strip=no \
		shared=yes \
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
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%makeinstall_std -C Documentation \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

gzip ChangeLog

%files
%doc ANNOUNCE ChangeLog* NEWS NOTICE README TODO
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files doc
%_docdir/GNUstep
%_infodir/*

%changelog
* Mon Feb 04 2019 Ivan A. Melnikov <iv@altlinux.org> 1.2.20-alt4.svn20140119
- Fix build with recent texinfo

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.20-alt3.svn20140119
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.20-alt2.svn20140119
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.20-alt1.svn20140119
- New snapshot

* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.20-alt1.svn20130703
- Version 1.2.20

* Tue Mar 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.18-alt3.git20130225
- New snapshot

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.18-alt3.git20130130
- New snapshot

* Sun Jan 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.18-alt3.git20130127
- New snapshot
- Added menu file (thnx kostyalamer@)

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.18-alt2.git20120726
- Rebuilt with libobjc2 instead of libobjc

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.18-alt1.git20120726
- Initial build for Sisyphus

