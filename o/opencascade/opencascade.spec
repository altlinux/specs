Name: opencascade
Version: 6.5.2
Release: alt3
Summary: Development platform for 3D modeling and numerical simulation
License: BSD-like
Group: Development/Tools
Url: http://www.opencascade.org
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: OpenCASCADE_src.tar
Source1: LICENSE
Source2: OSD_Common.hxx

Requires: lib%name = %version-%release
Requires: %name-common = %version-%release

BuildPreReq: gcc-c++ libX11-devel libGL-devel libGLU-devel
BuildPreReq: tcl-devel tcl-tix libfltk-devel tk-devel libXmu-devel
BuildPreReq: java-devel-default libcoin3d-devel libfreetype-devel
BuildPreReq: python-module-gist libtbb-devel libftgl-devel
BuildPreReq: libgl2ps-devel

%description
Open CASCADE Technology version 6.3., a minor release, which introduces quite a
number of new features and improved traditional functionality along with certain
changes over the previous public release and maintenance releases exclusively
available to the customers.

This release makes Open CASCADE Technology even a more powerful and stable
development platform for 3D modeling and numerical simulation applications. 

%package -n lib%name
Summary: Shared libraries of Open CASCADE
Group: System/Libraries

%description -n lib%name
Shared libraries of Open CASCADE, development platform for 3D modeling and
numerical simulation applications.

%package -n lib%name-devel
Summary: Development files for Open CASCADE Technology
Group: Development/C++
Requires: lib%name = %version-%release
Requires: %name-common = %version-%release
Conflicts: svgalib-devel

%description -n lib%name-devel
Development files for Open CASCADE Technology, development platform for 3D
modeling and numerical simulation applications.

%package common
Summary: Architecture independent files of Open CASCADE
Group: Development/C++
BuildArch: noarch

%description common
Architecture independent files of Open CASCADE, development platform for 3D
modeling and numerical simulation applications.

%prep
%setup
install -p -m644 %SOURCE1 .
install -p -m644 %SOURCE2 src/OSD

%build
export DISTRIBUTIVE_DIR=$PWD
export CASROOT=$PWD
DEFS="-DHAVE_IOSTREAM -DHAVE_IOMANIP -DHAVE_FSTREAM -DHAVE_SYS_IPC_H"
DEFS="$DEFS -DHAVE_IOS -UHAVE_SYS_SEM_H -UUSE_OLD_STREAMS"
DEFS="$DEFS -DSEMOP_NO_REFERENCE=1 -UDECOSF1"
%add_optflags $DEFS -fpermissive
%autoreconf
%configure \
	--with-gl-include=%_includedir \
	--with-gl-library=%_libdir \
	--with-xmu-include=%_includedir/X11/Xmu \
	--with-xmu-library=%_libdir \
	--with-tcl=%_libdir \
	--with-tk=%_libdir \
	--with-x \
	--with-tbb-include=%_includedir/tbb \
	--with-tbb-library==%_libdir \
	--with-freetype=%prefix \
	--with-ftgl=%prefix \
	--disable-debug \
	--disable-static \
	--enable-debug \
	--enable-production \
	--enable-wrappers=yes \
	--enable-wok=yes \
	--enable-draw=yes \
	--with-java-include=%_libexecdir/jvm/java/include \
	--with-gl2ps=%prefix

for i in $(find ./ -name Makefile) libtool; do
	sed -i 's|\-O2|-O1|g' $i
done
if [ "%__nprocs" = "1" -o "%__nprocs" = "" ]; then
	NPROCS=2
else
	NPROCS=%__nprocs
fi
#make -j$NPROCS
sed -i 's|define VERSION|define OCCVERSION|' config.h
%make

%install
%makeinstall
sed -i \
	-e '1s/ksh\ \-f/sh/' \
	-e '1a\export CASROOT=%_datadir/%name' \
	-e 's/\/\$OS_NAME//g' \
	%buildroot%prefix/env_DRAW.sh
sed -i 's|src|share/%name/src|g' %buildroot%prefix/env_DRAW.sh
%ifarch x86_64
sed -i 's|/lib|/lib64|g' %buildroot%prefix/env_DRAW.sh
%endif

install -d %buildroot%_datadir/%name
mv %buildroot%prefix/env_DRAW.sh %buildroot%_datadir/%name/
mv %buildroot%prefix/src %buildroot%_datadir/%name/
mv %buildroot%prefix/inc %buildroot%_includedir
#install -d %buildroot%_datadir/%name/src/jcas
#install -p -m644 src/jcas/* %buildroot%_datadir/%name/src/jcas

install -d %buildroot%_includedir/%name

install -p -m644 src/OSD/OSD_Common.hxx %buildroot%_includedir
pushd %buildroot%_includedir
rm -f config.h
mv ../config.h %name/
for i in Xw_Extension.h Standard_values.h Standard_Macro.hxx
do
	sed -i 's|<config.h>|<%name/config.h>|' $i
done
popd
#sed -i 's|^\(CONFIG_HEADER\).*|\1 = %_includedir/%name/config.h|' \
#	%buildroot%_datadir/%name/src/WOKTclLib/template.min*

mv %buildroot%_bindir/DRAWEXE  %buildroot%_bindir/DRAWEXE_
cat <<EOF >%buildroot%_bindir/DRAWEXE
#!/bin/bash

export TCLHOME=%prefix
source %_datadir/%name/env_DRAW.sh
DRAWEXE_ "\$@"
EOF
chmod +x %buildroot%_bindir/DRAWEXE

%files
%doc LICENSE
%_bindir/*
%_datadir/%name/env_DRAW.sh

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files common
%dir %_datadir/%name
%_datadir/%name/src

%changelog
* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.2-alt3
- Fixed build

* Sun Mar 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.2-alt2
- Fixed build with TBB 40_297

* Wed Feb 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.2-alt1
- Version 6.5.2

* Thu Sep 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.1-alt1
- Version 6.5.1

* Thu Apr 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.0-alt1
- Version 6.5.0

* Tue Mar 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt10
- Rebuilt for debuginfo

* Tue Nov 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt9
- Rebuilt for soname set-versions

* Sat Oct 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt8
- Fixed underlinking of libraries

* Tue Aug 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt7
- Fixed for checkbashisms

* Mon Mar 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt6
- Reduced optimization level: -O2 -> -O1
- Rebuilt with java

* Tue Dec 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt5
- Set opencascade-commom as noarch

* Tue Dec 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt4
- Rebuilt without java

* Tue Sep 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt3
- Changed owner of %_datadir/%name: %name -> %name-common
- Rebuild with gcc4.4

* Wed May 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt2
- Removed %name directory from /usr/lib
- Fixed channel permission

* Sat May 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt1
- Initial build for Sisyphus

