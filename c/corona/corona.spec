Name: corona
Version: 1.0.2
Release: alt1.svn20120929
Summary: Image input/output library that can read, write, and manipulate image files
License: zlib
Group: File tools
Url: http://corona.sourceforge.net/home.php
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn://svn.code.sf.net/p/corona/code/trunk/corona
Source: %name-%version.tar

BuildPreReq: libpng-devel zlib-devel libjpeg-devel libungif-devel
BuildPreReq: gcc-c++ scons doxygen graphviz

Requires: lib%name = %EVR

%description
Corona is an image input/output library that can read, write, and
manipulate image files in just a few lines of code. It can write PNG and
TGA files, and read PNG, JPEG, PCX, BMP, TGA, and GIF. Corona was
designed to be easy to use, and exports a straightforward C++ API. With
just a few lines of C++, you can add image loading to your application.

%package -n lib%name
Summary: Shared library of %name
Group: System/Libraries

%description -n lib%name
Corona is an image input/output library that can read, write, and
manipulate image files in just a few lines of code. It can write PNG and
TGA files, and read PNG, JPEG, PCX, BMP, TGA, and GIF. Corona was
designed to be easy to use, and exports a straightforward C++ API. With
just a few lines of C++, you can add image loading to your application.

This package contains shared library of %name.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
Corona is an image input/output library that can read, write, and
manipulate image files in just a few lines of code. It can write PNG and
TGA files, and read PNG, JPEG, PCX, BMP, TGA, and GIF. Corona was
designed to be easy to use, and exports a straightforward C++ API. With
just a few lines of C++, you can add image loading to your application.

This package contains development files of %name.

%package -n lib%name-devel-docs
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-docs
Corona is an image input/output library that can read, write, and
manipulate image files in just a few lines of code. It can write PNG and
TGA files, and read PNG, JPEG, PCX, BMP, TGA, and GIF. Corona was
designed to be easy to use, and exports a straightforward C++ API. With
just a few lines of C++, you can add image loading to your application.

This package contains development documentation for %name.

%prep
%setup

for i in jpeg libpng libungif zlib; do
	rm -fR src/${i}*
done

touch NEWS README AUTHORS ChangeLog

%build
%autoreconf
%configure \
	--enable-debug \
	--enable-static=no
%make_build

pushd doc/doxygen
doxygen %name.doxy
popd

%install
%makeinstall_std

%files
%doc doc/*.txt
%_bindir/corconvert

%files -n lib%name
%_libdir/lib%name-*.so

%files -n lib%name-devel
%_bindir/%name-config
%_includedir/*
%_libdir/lib%name.so

%files -n lib%name-devel-docs
%doc doc/doxygen/html/*

%changelog
* Wed Sep 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.svn20120929
- Initial build for Sisyphus

