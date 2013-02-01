Name: spatialite-tools
Version: 4.0.0
Release: alt1
Summary: A set of useful CLI tools for SpatiaLite

Group: Development/Other
License: GPLv3+
Source0: http://www.gaia-gis.it/gaia-sins/%name-%version.tar.gz
Url: https://www.gaia-gis.it/fossil/spatialite-tools
Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildRequires: libexpat-devel
BuildRequires: freexl-devel
BuildRequires: libgeos-devel
BuildRequires: libspatialite-devel
BuildRequires: libproj-devel
BuildRequires: libreadline-devel
BuildRequires: readosm-devel
BuildRequires: libsqlite-devel
BuildRequires: zlib-devel

%description
Spatialite-Tools is a set of useful CLI tools for SpatiaLite.

%prep
%setup

# Remove unused Makefiles
rm -f Makefile-static*

%build
%configure

make %{?_smp_mflags}

%install
make install DESTDIR=%buildroot

%files
%doc AUTHORS COPYING
%_bindir/exif_loader
%_bindir/shp_doctor
%_bindir/spatialite
%_bindir/spatialite_convert
%_bindir/spatialite_gml
%_bindir/spatialite_network
%_bindir/spatialite_osm*
%_bindir/spatialite_tool

%changelog
* Sat Feb 02 2013 Ilya Mashkin <oddity@altlinux.ru> 4.0.0-alt1
- Build for Sisyphus

* Sun Dec  2 2012 Volker Frohlich <volker27@gmx.at> - 4.0.0-1
- New upstream release
- Remove PPC restrictions

* Sat Aug 18 2012 Volker Frohlich <volker27@gmx.at> - 3.1.0b-1
- Update for new release
- Update URL and source URL
- Drop LDFLAG -lm
- Exclude ppc as well

* Sun Jul 17 2011 Volker Frohlich <volker27@gmx.at> - 2.4.0-0.4.RC4
- Support readline
- Drop EPEL5 specific statements and definitions
- Drop unnecessary defattr
- Slightly improved description
- More explicit files section

* Fri Feb 25 2011 Volker Frohlich <volker27@gmx.at> - 2.4.0-0.3.RC4
- Exclude ppc64

* Fri Jan 14 2011 Volker Frohlich <volker27@gmx.at> - 2.4.0-0.2.RC4
- Dropped prefix from configure macro
- Corrected license
- Use macros in source URL

* Mon Dec 20 2010 Volker Frohlich <volker27@gmx.at> - 2.4.0-0.1.RC4
- Inital packaging
