Name: readosm
Version: 1.0.0b
Release: alt1
Summary: Library to extract data from Open Streetmap input files

Group: System/Libraries
License: MPLv1.1 or GPLv2+ or LGPLv2+
Source0: http://www.gaia-gis.it/gaia-sins/%name-%version.tar.gz
Url: https://www.gaia-gis.it/fossil/readosm
Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildRequires: libexpat-devel
BuildRequires: zlib-devel

%description
ReadOSM is a simple library intended for extracting the contents from
Open Street Map files: both input formats (.osm XML based and .osm.pbf based
on Google's Protocol Buffer serialization) are indifferently supported.

%package devel
Summary: Development libraries and headers for %name
Group: System/Libraries
Requires: %name%{?_isa} = %version-%release
Requires: pkgconfig

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%configure --disable-static

make %{?_smp_mflags}

%install
make install DESTDIR=%buildroot

# Delete undesired libtool archives
rm -f %buildroot%_libdir/lib%name.la

%check
make check

%files
%doc AUTHORS COPYING
%_libdir/lib%name.so.*

%files devel
%_libdir/pkgconfig/%name.pc
%_libdir/lib%name.so
%_includedir/%name.h

%changelog
* Thu Jan 31 2013 Ilya Mashkin <oddity@altlinux.ru> 1.0.0b-alt1
- Build for Sisyphus

* Sun Dec  2 2012 Volker Frohlich <volker27@gmx.at> - 1.0.0b-1
- New upstream release

* Sun Aug 12 2012 Volker Frohlich <volker27@gmx.at> - 1.0.0a-2
- Disable coverage profiling

* Sun Aug 12 2012 Volker Frohlich <volker27@gmx.at> - 1.0.0a-1
- Inital package for Fedora
