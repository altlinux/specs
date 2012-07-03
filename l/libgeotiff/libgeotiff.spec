Name: libgeotiff
Version: 1.3.0
Release: alt2

Summary: Library for reading and writing GeoTIFF information tags.
License: Public domain
Group: System/Libraries
Url: http://trac.osgeo.org/geotiff/
Packager: Dmitry Derjavin <dd@altlinux.org>

Source: %name-%version.tar

%def_disable static
%def_enable data

# Automatically added by buildreq on Tue Jul 06 2010
BuildRequires: gcc-c++ libtiff-devel libjpeg-devel zlib-devel

%package utils
Summary: Programs for manipulating GeoTIFF information tags
Group: Graphics
Requires: %name = %version-%release

%package devel
Summary: Development tools for programs which will use geotiff library
Group: Development/C
Requires: %name = %version-%release
Requires: %name-data = %version-%release

%package devel-static
Summary: Static geotiff library
Group: Development/C
Requires: %name-devel = %version-%release

%package data
Summary: CSV data files derived from the EPSG Tables
Group: Graphics
Requires: %name-utils = %version-%release

%description
Libgeotiff is an open source library normally hosted on top of libtiff
for reading and writing GeoTIFF information tags. The libgeotiff
library is a sub-project of the MetaCRS project.
http://wiki.osgeo.org/wiki/MetaCRS

%description utils
This package contains client programs for accessing libgeotiff
functions.

%description devel
This package contains header files for developing programs which
will manipulate GeoTIFF information data using geotiff library.

%description devel-static
This package contains static %name library.

%description data
This package contains CSV data files derived from the EPSG Tables.

%prep
%setup -q

%build
%autoreconf
%configure --with-zlib --with-jpeg
%make_build

%install
%makeinstall_std

%files
%_libdir/%name.so.?*
%doc README
%doc LICENSE

%files utils
%_bindir/*

%files devel
%_libdir/%name.so
%_includedir/*.h*
# EPSG data files. Check license!
%_includedir/*.inc*

%if_enabled static
%files devel-static
%_libdir/%name.a
%endif

%if_enabled data
%files data
%_datadir/epsg_csv
%endif

%changelog
* Mon Dec 26 2011 Dmitry Derjavin <dd@altlinux.org> 1.3.0-alt2
- RPATH issue fixed on x86_64 (closes: 26704)
- data package with EPSG csv files is now enabled by default (closes: 24405)

* Fri Jul 30 2010 Dmitry Derjavin <dd@altlinux.org> 1.3.0-alt1
- Initial ALTLinux build.
