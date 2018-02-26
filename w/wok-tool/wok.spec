Name: wok-tool
Version: 6.5.2
Release: alt1
Summary: Open CASCADE Technology WOK tool
License: BSD-like
Group: Development/Tools
Url: http://www.opencascade.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: wok.pdf

BuildPreReq: libopencascade-devel libX11-devel libftgl-devel
BuildPreReq: libqt4-devel libfreetype-devel libtbb-devel gcc-c++
BuildPreReq: libXmu-devel java-devel-default tk-devel

Requires: lib%name = %version-%release

%description
Open CASCADE Technology WOK tool.

%package -n lib%name
Summary: Shared libraries of WOK tool
Group: System/Libraries

%description -n lib%name
Open CASCADE Technology WOK tool.

This package contains shared libraries of WOK tool.

%package -n lib%name-devel
Summary: Development files of WOK tool
Group: Development/C++
Requires: lib%name = %version-%release
Conflicts: libbobpp-devel openquicktime-devel

%description -n lib%name-devel
Open CASCADE Technology WOK tool.

This package contains development files of WOK tool.

%package doc
Summary: Documentation for Open CASCADE Technology WOK tool
Group: Documentation
BuildArch: noarch

%description doc
Open CASCADE Technology WOK tool.

This package contains documentation for WOK tool.

%prep
%setup

%build
DEFS="-DHAVE_IOSTREAM -DHAVE_IOMANIP -DHAVE_FSTREAM -DHAVE_SYS_IPC_H"
DEFS="$DEFS -DHAVE_IOS -UHAVE_SYS_SEM_H -UUSE_OLD_STREAMS"
DEFS="$DEFS -DSEMOP_NO_REFERENCE=1 -UDECOSF1"
%add_optflags $DEFS -I%_includedir/freetype2
%autoreconf
sed -i '2a\ac_cv_header_X11_extensions_multibuf_h=yes' configure
%configure \
	--with-x \
	--with-freetype \
	--with-ftgl \
	--with-tbb-include=%_includedir/tbb \
	--with-tbb-library=%_libdir \
	--with-tcl=%_libdir \
	--with-tk=%_libdir \
	--with-qt=%_qt4dir \
	--with-java-include=%java_home/include
%make_build

%install
%makeinstall

install -d %buildroot%_includedir/wok
mv %buildroot%prefix/inc/* %buildroot%_includedir/wok/
rm -f %buildroot%_includedir/wok/config.h
sed -i 's|config\.h|wok/config.h|' \
	%buildroot%_includedir/wok/*
mv %buildroot%prefix/config.h %buildroot%_includedir/wok/
ln -s wok/config.h %buildroot%_includedir/

install -d %buildroot%_docdir/%name
install -p -m644 %SOURCE1 %buildroot%_docdir/%name

%files
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files doc
%_docdir/%name

%changelog
* Wed Feb 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.2-alt1
- Version 6.5.2

* Thu Dec 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.1-alt1
- Version 6.5.1

* Sat May 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.0-alt2
- Fixed requirements

* Thu May 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.0-alt1
- Initial build for Sisyphus

