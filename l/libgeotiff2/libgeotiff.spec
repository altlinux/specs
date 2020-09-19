%define oldname libgeotiff
Name: libgeotiff2
Version: 1.3.0
Release: alt3

Summary: Library for reading and writing GeoTIFF information tags.
License: Public domain
Group: System/Legacy libraries
Url: http://trac.osgeo.org/geotiff/
Packager: Dmitry Derjavin <dd@altlinux.org>

Source: %oldname-%version.tar

%def_disable static
%def_enable data

# Automatically added by buildreq on Tue Jul 06 2010
BuildRequires: gcc-c++ libtiff-devel libjpeg-devel zlib-devel

%package -n %oldname
Group: System/Legacy libraries
Summary: Compat geotiff library

%description
Libgeotiff is an open source library normally hosted on top of libtiff
for reading and writing GeoTIFF information tags. The libgeotiff
library is a sub-project of the MetaCRS project.
http://wiki.osgeo.org/wiki/MetaCRS

%description -n %oldname
This package contains compat %oldname library.

%prep
%setup -q -n %oldname-%version

%build
%autoreconf
%configure --with-zlib --with-jpeg
%make_build

%install
%makeinstall_std

%files -n %oldname
%_libdir/%oldname.so.?*
%doc README
%doc LICENSE

%changelog
* Sat Sep 19 2020 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt3
- compat legacy library

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2.1
- Rebuilt with libtiff5

* Mon Dec 26 2011 Dmitry Derjavin <dd@altlinux.org> 1.3.0-alt2
- RPATH issue fixed on x86_64 (closes: 26704)
- data package with EPSG csv files is now enabled by default (closes: 24405)

* Fri Jul 30 2010 Dmitry Derjavin <dd@altlinux.org> 1.3.0-alt1
- Initial ALTLinux build.
