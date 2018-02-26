Name: opendx
Version: 4.4.4
Release: alt4.1
Summary: Open Visualization Data Explorer
License: IBM Public License
Group: Graphics
Url: http://www.opendx.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://opendx.informatics.jax.org/source/dx-4.4.4.tar.gz

BuildPreReq: libhdf5-devel libtiff-devel flex
BuildPreReq: libnetcdf-devel libX11-devel libcdf-devel gcc-c++
BuildPreReq: libICE-devel libSM-devel libXt-devel libopenmotif-devel
BuildPreReq: libGL-devel libGLU-devel libXext-devel libXmu-devel
BuildPreReq: libXp-devel libXpm-devel librx-devel liblcms-devel
BuildPreReq: libfreetype-devel libjpeg-devel liblqr-devel glib2-devel
BuildPreReq: fontconfig-devel bzlib-devel libXinerama-devel
BuildPreReq: libImageMagick-devel

Requires: lib%name = %version-%release

%description
If you need visualization for anything from examining simple data sets
to analyzing complex, time-dependent data from disparate sources, OpenDX
has what you need: features and functions that let you easily gain
meaningful insight into your data.

And if you are looking to build visualization applications for your end
users, OpenDX has what you need: power to support their requirements and
versatility for customized application development.

OpenDX is a uniquely powerful, full-featured software package for the
visualization of scientific, engineering and analytical data: Its open
system design is built on familiar standard interface environments. And
its sophisticated data model provides users with great flexibility in
creating visualizations.

%package -n lib%name
Summary: Shared libraries of Open Visualization Data Explorer
Group: System/Libraries

%description -n lib%name
If you need visualization for anything from examining simple data sets
to analyzing complex, time-dependent data from disparate sources, OpenDX
has what you need: features and functions that let you easily gain
meaningful insight into your data.

This package contains shared libraries of OpenDX.

%package -n lib%name-devel
Summary: Development files of Open Visualization Data Explorer
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
If you need visualization for anything from examining simple data sets
to analyzing complex, time-dependent data from disparate sources, OpenDX
has what you need: features and functions that let you easily gain
meaningful insight into your data.

This package contains development files of OpenDX.

%package docs
Summary: Documentation for Open Visualization Data Explorer
Group: Documentation
BuildArch: noarch

%description docs
If you need visualization for anything from examining simple data sets
to analyzing complex, time-dependent data from disparate sources, OpenDX
has what you need: features and functions that let you easily gain
meaningful insight into your data.

This package contains documentation for OpenDX.

%prep
%setup
rm -f aclocal.m4

%build
%autoreconf
INCS="-I%_libexecdir/hdf5-seq/include -I%_libexecdir/hdf5-seq/include/netcdf-3"
INCS="$INCS -I%_includedir/ImageMagick"
%add_optflags $INCS -fno-strict-aliasing
%configure \
	--enable-shared \
	--enable-static=no \
	--with-hdf \
	--with-tiff \
	--with-netcdf \
	--with-magick \
	--with-large-arenas \
	--with-x \
	--enable-ddx
%make_build

%install
%makeinstall_std

install -d %buildroot%_mandir/manl

%files
%doc AUTHORS COPYING ChangeLog LICENSE NEWS README
%_bindir/*
%_libexecdir/dx
%exclude %_libexecdir/dx/doc
%exclude %_libexecdir/dx/help
%exclude %_libexecdir/dx/html
%exclude %_libexecdir/dx/lib
%_mandir/manl/*
%exclude %prefix/dx

%files -n lib%name
%_libdir/*.so.*
%_libexecdir/dx/lib

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/arch.mak

%files docs
%_libexecdir/dx/doc
%_libexecdir/dx/help
%_libexecdir/dx/html

%changelog
* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 4.4.4-alt4.1
- Rebuild with new libImageMagick

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.4-alt4
- Rebuilt with libnetcdf7

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.4-alt3
- Rebuilt for debuginfo
- Built with openmotif instead of lesstif

* Thu Nov 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.4-alt2
- Rebuilt for soname set-versions

* Wed Sep 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.4-alt1
- Initial build for Sisyphus

