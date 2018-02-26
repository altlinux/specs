Name: simage
Version: 1.7.0
Release: alt4
Summary: Format loaders and front-ends to common import libraries
License: Public domain
Group: Video
Url: http://ftp.coin3d.org/coin/src/all
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://ftp.coin3d.org/coin/src/all/simage-1.7.0.tar.gz

BuildPreReq: gcc-c++ qt4-devel libquicktimehv-devel libX11-devel
BuildPreReq: libungif-devel libjpeg-devel zlib-devel libpng-devel
BuildPreReq: libtiff-devel ghostscript-utils libsndfile-devel
BuildPrereq: libvorbis-devel gcc-fortran guile18-devel
BuildPreReq: libquicktime-devel libqt4-uitools libqt4-opengl
BuildPreReq: libqt4-gui jasper libjasper-devel

%description
This is simage, a library with image format loaders and front-ends
to common import libraries. simage is meant for use with applications
which reads image files as textures.

%package -n lib%name
Summary: Shared libraries of Format loaders and front-ends to common import libraries
Group: System/Libraries

%description -n lib%name
This is simage, a library with image format loaders and front-ends
to common import libraries. simage is meant for use with applications
which reads image files as textures.

This package contains shared libraries of simage.

%package -n lib%name-devel
Summary: Development file of Format loaders and front-ends to common import libraries
Requires: lib%name = %version-%release
Group: Development/C++

%description -n lib%name-devel
This is simage, a library with image format loaders and front-ends
to common import libraries. simage is meant for use with applications
which reads image files as textures.

This package contains development files of simage.

%prep
%setup

%build
export QTDIR=%_qt4dir
%add_optflags -I%_includedir/qt4 -I%_includedir/q4/QtCore -I%_includedir/q4/QtGui
%configure \
	--disable-msvc \
	--enable-qimage \
	--enable-quicktime \
	--with-qt=true \
	--with-x \
	--with-ungif \
	--with-jpeg \
	--with-zlib \
	--with-png \
	--with-tiff \
	--with-rgb \
	--with-xwd \
	--with-eps \
	--with-mpeg2enc \
	--with-oggvorbis \
	--with-libsndfile \
	--with-avienc
%ifarch x86_64
	sed -i -e 's/^\(predep_objects\|postdep_objects\|compiler_lib_search_path\)=.*/\1=""/' \
		-e 's/^\(archive\(_expsym\)\?_cmds=\".*\) -nostdlib /\1 /' \
		libtool
	out="\$(\$CC -print-search-dirs |\$SED -e '/^libraries: *=/!d;s///;s!/:!:!g;s!/\$!!;s/:/ /g')"
	sed -i 's#^\(compiler_lib_search_dirs="\)/.*#\1'"$out"'"#' \
		libtool
%endif
%make_build

%install
%makeinstall_std

%files -n lib%name
%doc docs/* AUTHORS COPYING NEWS README ChangeLog
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_bindir/*
%_includedir/*
%_datadir/Coin/conf/*
%_datadir/aclocal/*
%_pkgconfigdir/*
%_datadir/guile/coin/*

%changelog
* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt4
- Rebuilt for debuginfo

* Thu Nov 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt3
- Fixed underlinking of libraries

* Wed Nov 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt2
- Rebuilt for soname set-versions

* Wed Mar 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1
- Version 1.7.0
- Added simage module for Guile

* Sat Jan 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1
- Initial build for Sisyphus

