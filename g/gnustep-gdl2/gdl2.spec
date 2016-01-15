%set_verify_elf_method unresolved=strict

Name: gnustep-gdl2
Version: 0.12.0
Release: alt5.svn20130819.1
Summary: The GNUstep Database Library 2 (GDL2)
License: LGPLv3
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/GDL
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/libs/gdl2/trunk/
Source: %name-%version.tar
Source1: RCS_ID.h

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel
BuildPreReq: postgresql-devel libsqlite3-devel
BuildPreReq: texinfo texi2html texlive-latex-base
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: lib%name = %version-%release
Requires: gnustep-back

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

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

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
	shared=yes
 
%make_build -C Documentation \
	messages=yes

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%makeinstall_std -C Documentation \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

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

install -d %buildroot%_includedir
cp -fR EOInterface %buildroot%_includedir/

gzip ChangeLog

%files
%doc ANNOUNCE AUTHORS ChangeLog* NEWS README TODO 
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
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.12.0-alt5.svn20130819.1
- NMU: Rebuild with libgnutls30.

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt5.svn20130819
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt4.svn20130819
- New snapshot from SVN

* Tue Jan 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt4.git20130819
- Added EOInterface headers

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt3.git20130819
- Rebuilt with new gnustep-gui

* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt1.git20130819
- New snapshot

* Tue Mar 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt1.git20130302
- New snapshot

* Sat Jan 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt1.git20120811
- Initial build for Sisyphus

