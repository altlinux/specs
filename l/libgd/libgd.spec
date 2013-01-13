Name: libgd
Version: 2.1.0
Release: alt1.hg20110617
Summary: Library for the dynamic creation of images by programmers
License: Public domain
Group: System/Libraries
Url: http://www.boutell.com/gd/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/pierrejoye/gd-libgd
Source: %name-%version.tar

BuildPreReq: cmake gcc-c++ libpng-devel libjpeg-devel libtiff-devel
BuildPreReq: libfreetype-devel fontconfig-devel libXpm-devel

%description
GD is an open source code library for the dynamic creation of images by
programmers. GD is written in C, and "wrappers" are available for Perl,
PHP and other languages. GD creates PNG, JPEG and GIF images, among
other formats. GD is commonly used to generate charts, graphics,
thumbnails, and most anything else, on the fly. While not restricted to
use on the web, the most common applications of GD involve website
development.

%package devel
Summary: Development files of GD (library for the dynamic creation of image)
Group: Development/C
Requires: %name = %version-%release

%description devel
GD is an open source code library for the dynamic creation of images by
programmers. GD is written in C, and "wrappers" are available for Perl,
PHP and other languages. GD creates PNG, JPEG and GIF images, among
other formats. GD is commonly used to generate charts, graphics,
thumbnails, and most anything else, on the fly. While not restricted to
use on the web, the most common applications of GD involve website
development.

This package contains development files of GD.

%package tools
Summary: Tools provided by GD (library for the dynamic creation of image)
Group: File tools
Requires: %name = %version-%release

%description tools
GD is an open source code library for the dynamic creation of images by
programmers. GD is written in C, and "wrappers" are available for Perl,
PHP and other languages. GD creates PNG, JPEG and GIF images, among
other formats. GD is commonly used to generate charts, graphics,
thumbnails, and most anything else, on the fly. While not restricted to
use on the web, the most common applications of GD involve website
development.

This package contains tools provided by GD.

%prep
%setup

%build
cmake \
%ifarch x86_64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
	-DCMAKE_STRIP:FILEPATH='/bin/echo' \
	.

%make_build VERBOSE=1

%install
%makeinstall_std

%files
%doc ChangeLog NEWS
%_libdir/*.so

%files devel
%_includedir/*

%files tools
%_bindir/*

%changelog
* Sun Jan 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.hg20110617
- Initial build for Sisyphus

