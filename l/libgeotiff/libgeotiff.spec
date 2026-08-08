%define soversion 5
Name: libgeotiff
Version: 1.7.4
Release: alt1

Summary: Library for reading and writing GeoTIFF information tags.
License: ALT-Public-Domain and X11
Group: System/Libraries
Url: https://github.com/OSGeo/libgeotiff

Source: %name-%version.tar
# upstream fix: testlistgeo robust to PROJ 9.8 changes
Patch0: %name-1.7.4-testlistgeo-proj9.8.patch

%def_disable static
%def_disable data

# Automatically added by buildreq on Tue Jul 06 2010
BuildRequires: gcc-c++ libtiff-devel libjpeg-devel zlib-devel libproj-devel

%package -n %name%soversion
Summary: Library for reading and writing GeoTIFF information tags.
Group: System/Libraries

%package utils
Summary: Programs for manipulating GeoTIFF information tags
Group: Graphics
Requires: %name%soversion = %EVR

%package devel
Summary: Development tools for programs which will use geotiff library
Group: Development/C
Requires: %name%soversion =  %EVR
%if_enabled data
Requires: %name-data =  %EVR
%endif

%package devel-static
Summary: Static geotiff library
Group: Development/C
Requires: %name-devel =  %EVR

%package data
Summary: CSV data files derived from the EPSG Tables
Group: Graphics
Requires: %name-utils = %EVR

%description
Libgeotiff is an open source library normally hosted on top of libtiff
for reading and writing GeoTIFF information tags. The libgeotiff
library is a sub-project of the MetaCRS project.
http://wiki.osgeo.org/wiki/MetaCRS

%description -n %name%soversion
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
%patch0 -p1

%build
pushd libgeotiff
%autoreconf
%configure \
	--prefix=%{_prefix}	\
	--includedir=%{_includedir}/%{name}/	\
	--with-zlib		\
	--with-jpeg		\
	--with-proj		\
	%{subst_enable static}

%make_build

%check
pushd libgeotiff
%make check
popd

%install
pushd libgeotiff
%makeinstall_std

# install manualy some file
install -p -m 755 bin/makegeo %{buildroot}%{_bindir}

# install pkgconfig file
cat > geotiff.pc <<EOF
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}/%{name}

Name: geotiff
Description: GeoTIFF file format library
Version: %{version}
Libs: -L\${libdir} -lgeotiff
Cflags: -I\${includedir}
EOF

mkdir -p %buildroot%_pkgconfigdir/
install -p -m 644 geotiff.pc %buildroot%_pkgconfigdir/


%files -n %name%soversion
%doc libgeotiff/LICENSE
%_libdir/%name.so.%{soversion}
%_libdir/%name.so.%{soversion}.*

%files utils
%_bindir/*
%_man1dir/*

%files devel
%_libdir/%name.so
%_pkgconfigdir/geotiff.pc
%_pkgconfigdir/libgeotiff.pc
%_includedir/%name

%if_enabled static
%files devel-static
%_libdir/%name.a
%endif

%if_enabled data
%files data
%_datadir/epsg_csv
%endif

%changelog
* Mon Jul 06 2026 Anton Farygin <rider@altlinux.org> 1.7.4-alt1
- 1.6.0 -> 1.7.4

* Wed Jun 30 2021 Igor Vlasenko <viy@altlinux.org> 1.6.0-alt2
- install makegeo
- pkgconfig should be geotiff.pc

* Sat Sep 19 2020 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1
- updated to 1.6.0 (closes: #38967)
- switched to shared libs policy (%%name%%soversion lib package)

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2.1
- Rebuilt with libtiff5

* Mon Dec 26 2011 Dmitry Derjavin <dd@altlinux.org> 1.3.0-alt2
- RPATH issue fixed on x86_64 (closes: 26704)
- data package with EPSG csv files is now enabled by default (closes: 24405)

* Fri Jul 30 2010 Dmitry Derjavin <dd@altlinux.org> 1.3.0-alt1
- Initial ALTLinux build.
