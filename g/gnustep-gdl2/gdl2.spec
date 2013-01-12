%set_verify_elf_method unresolved=strict

Name: gnustep-gdl2
Version: 0.12.0
Release: alt1.git20120811
Summary: The GNUstep Database Library 2 (GDL2)
License: LGPLv3
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-gdl2.git
Source: %name-%version.tar
Source1: RCS_ID.h

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel
BuildPreReq: postgresql-devel libsqlite3-devel
BuildPreReq: texinfo texi2html texlive-latex-base

Requires: lib%name = %version-%release

%description
The GNUstep Database Library 2 (GDL2) is a set of libraries to map
Objective-C objects to rows of relational database management systems
(RDBMS).  It aims to be compatible with Enterprise Objects Framework
(EOF) as released with WebObjects 4.5 from Apple Inc.

%package -n lib%name
Summary: Shared libraries of the GNUstep Database Library 2
Group: System/Libraries

%description -n lib%name
The GNUstep Database Library 2 (GDL2) is a set of libraries to map
Objective-C objects to rows of relational database management systems
(RDBMS).  It aims to be compatible with Enterprise Objects Framework
(EOF) as released with WebObjects 4.5 from Apple Inc.

This package contains shared libraries of GDL2.

%package -n lib%name-devel
Summary: Development files of the GNUstep Database Library 2
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: %name = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
The GNUstep Database Library 2 (GDL2) is a set of libraries to map
Objective-C objects to rows of relational database management systems
(RDBMS).  It aims to be compatible with Enterprise Objects Framework
(EOF) as released with WebObjects 4.5 from Apple Inc.

This package contains development files of GDL2.

%package doc
Summary: Documentation for the GNUstep Database Library 2
Group: Documentation
BuildArch: noarch

%description doc
The GNUstep Database Library 2 (GDL2) is a set of libraries to map
Objective-C objects to rows of relational database management systems
(RDBMS).  It aims to be compatible with Enterprise Objects Framework
(EOF) as released with WebObjects 4.5 from Apple Inc.

This package contains documentation for GDL2.

%prep
%setup
install -m644 %SOURCE1 ./

for i in $(find ./ -type f); do
	sed -i 's|objc/|objc2/|g' $i
done

%build
%autoreconf
%configure \
	--libexecdir=%_libdir \
	--with-installation-domain=SYSTEM \
	--with-pgsql-include=%_includedir/pgsql \
	--with-sqlite3-include=-I%_includedir

sed -i 'r RCS_ID.h' config.h

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNU_RUNTIME -DGNUSTEP'
 
%make_build -C Documentation \
	messages=yes \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%makeinstall_std -C Documentation \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

pushd %buildroot%_libdir
for i in PostgreSQLEOAdaptor SQLite3EOAdaptor; do
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

# bad info
rm -fR %buildroot%_infodir

%files
%doc ANNOUNCE AUTHORS ChangeLog NEWS README TODO 
%_bindir/*
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/*.framework/Versions/0/Headers
%exclude %_libdir/GNUstep/Frameworks/*.framework//Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/*.framework/Versions/0/Headers
%_libdir/GNUstep/Frameworks/*.framework//Headers
%_datadir/GNUstep

%files doc
%_docdir/GNUstep

%changelog
* Sat Jan 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt1.git20120811
- Initial build for Sisyphus

