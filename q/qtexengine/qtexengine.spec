%define sover 0

Name: qtexengine
Version: 0.3
Release: alt2
Summary: QTeXEngine - TeX support for Qt
License: GPL v3
Group: Graphics
Url: http://soft.proindependent.com/qtexengine/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://download.berlios.de/qtiplot/QTeXEngine-0.3-opensource.zip

BuildPreReq: unzip qt4-devel gcc-c++

Requires: texmf-pgf

%description
QTeXEngine enables Qt based applications to easily export graphics
created using the QPainter class to TeX.

%package -n lib%name
Summary: Shared library of QTeXEngine
Group: System/Libraries

%description -n lib%name
QTeXEngine enables Qt based applications to easily export graphics
created using the QPainter class to TeX.

This package contains shared library of QTeXEngine.

%package -n lib%name-devel
Summary: Development files of QTeXEngine
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
QTeXEngine enables Qt based applications to easily export graphics
created using the QPainter class to TeX.

This package contains development files of QTeXEngine.

%package -n lib%name-devel-doc
Summary: Documentation for QTeXEngine
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
QTeXEngine enables Qt based applications to easily export graphics
created using the QPainter class to TeX.

This package contains development documentation for QTeXEngine.

%prep
%setup

for i in $(find ./ -type f); do
	touch $i
done

%build
export PATH=$PATH:%_qt4dir/bin
qmake QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags" QTeXEngine.pro
%make

%install
install -d %buildroot%_includedir
install -m644 src/*.h %buildroot%_includedir

install -d %buildroot%_libdir
LIB=libQTeXEngine
g++ -shared -Wl,--whole-archive $LIB.a -Wl,--no-whole-archive \
	-o %buildroot%_libdir/$LIB.so.%sover -Wl,-soname,$LIB.so.%sover \
	$(pkg-config --libs Qt3Support) -Wl,-z,defs
ln -s $LIB.so.%sover %buildroot%_libdir/$LIB.so

%files -n lib%name
%doc *.txt
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-doc
%doc doc/html

%changelog
* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Rebuilt for debuginfo

* Sat Nov 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

