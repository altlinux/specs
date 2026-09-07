%define _unpackaged_files_terminate_build 1
%define soversion 8
Name: libspatialite
Version: 5.1.0
Release: alt1

Summary: Spatial extension turning SQLite into a Spatial DBMS
# Upstream is tri-licensed MPL-1.1/GPL-2.0-or-later/LGPL-2.1-or-later, but the
# rttopo and gcp modules enabled below are GPL-2.0-or-later only, which the
# whole build then inherits.
License: GPL-2.0-or-later
Group: System/Libraries
Url: https://www.gaia-gis.it/fossil/libspatialite
VCS: https://www.gaia-gis.it/fossil/libspatialite

Source: http://www.gaia-gis.it/gaia-sins/%name-sources/%name-%version.tar.gz
Patch0: libspatialite-5.1.0-alt-pkgconfig.patch
Patch1: libspatialite-5.1.0-debian-libxml2-nanohttp.patch

BuildRequires: gcc-c++
BuildRequires: freexl-devel
BuildRequires: libgeos-devel
BuildRequires: libminizip-devel
BuildRequires: libproj-devel
BuildRequires: librttopo-devel
BuildRequires: libsqlite3-devel
BuildRequires: libxml2-devel
BuildRequires: zlib-devel

%description
SpatiaLite extends the SQLite core into a full fledged Spatial DBMS,
lightweight and mostly OGC-SFS compliant.

%package -n %name%soversion
Summary: %summary
Group: System/Libraries
Provides: %name = %EVR
Obsoletes: %name < %EVR

%description -n %name%soversion
SpatiaLite extends the SQLite core into a full fledged Spatial DBMS,
lightweight and mostly OGC-SFS compliant.

%package module%soversion
Summary: SpatiaLite loadable extension for SQLite
Group: System/Libraries

%description module%soversion
mod_spatialite, the SpatiaLite extension in the form SQLite loads at runtime
through load_extension(). Needed by everything that reaches SpatiaLite over a
plain SQLite connection instead of linking the library: the sqlite3 shell,
GDAL, QGIS, GeoDjango.

%package devel
Summary: Development files for SpatiaLite
Group: Development/C
Requires: %name%soversion = %EVR
Requires: %name-module%soversion = %EVR

%description devel
Headers and link-time files for building applications against SpatiaLite.

%prep
%setup
%autopatch -p1
%autoreconf

%build
%configure \
    --disable-static \
    --disable-geosadvanced \
    --enable-rttopo \
    --enable-gcp

%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/*.la
# autoheader templates, installed by upstream along with the real headers
rm -f %buildroot%_includedir/spatialite/*.h.in

%files -n %name%soversion
%doc AUTHORS COPYING
%_libdir/libspatialite.so.%soversion
%_libdir/libspatialite.so.%soversion.*

%files module%soversion
%doc AUTHORS COPYING
%_libdir/mod_spatialite.so.%soversion
%_libdir/mod_spatialite.so.%soversion.*

%files devel
%doc examples/*.c
%_includedir/spatialite.h
%_includedir/spatialite
%_libdir/libspatialite.so
%_libdir/mod_spatialite.so
%_pkgconfigdir/spatialite.pc

%changelog
* Sun Sep 06 2026 Ajrat Makhmutov <rauty@altlinux.org> 5.1.0-alt1
- New version.
- Fix FTBFS with libxml2 built without HTTP support: libxml2 disables
  nanoHTTP by default since 2.14 and drops it in 2.15 (patch from
  Debian, proposed upstream).
- Rename the library package to libspatialite8, following the soname
  bump; it provides and obsoletes the old libspatialite name.
- Move mod_spatialite into the new libspatialite-module8 package. It
  shares no code at runtime with the library, so neither pulls the
  other in; libspatialite-devel keeps both unversioned symlinks and
  requires both packages.
- Change the license to GPL-2.0-or-later: --enable-rttopo and
  --enable-gcp bring in GPL-only code, which overrides the upstream
  MPL/GPL/LGPL tri-license for the binaries we ship.
- Spec cleanup.

* Sat Dec 25 2021 Ilya Mashkin <oddity@altlinux.ru> 5.0.1-alt1
- 5.0.1

* Fri Oct 04 2019 Vladislav Zavjalov <slazav@altlinux.org> 4.3.0a-alt3
- Rebuild with libproj 6.2.0 (use DACCEPT_USE_OF_DEPRECATED_PROJ_API_H)

* Sat Feb 16 2019 Vladislav Zavjalov <slazav@altlinux.org> 4.3.0a-alt2
- Rebuild with libproj 5.2.0

* Wed Feb 28 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0a-alt1
- New version. (ALT #34590)

* Thu Feb 04 2016 Andrey Cherepanov <cas@altlinux.org> 4.1.1-alt1.1
- Rebuild with new geos

* Thu Feb 27 2014 Ilya Mashkin <oddity@altlinux.ru> 4.1.1-alt1
- 4.1.1

* Tue Jan 29 2013 Ilya Mashkin <oddity@altlinux.ru> 4.0.0-alt1
- Build for Sisyphus

* Sun Dec  1 2012 Volker Frohlich <volker27@gmx.at> - 4.0.0-1
- New upstream release
- Remove arch restrictions, solving BZ 663938 and 846301
- Update conditional for geosadvanced

* Sat Aug 18 2012 Volker Frohlich <volker27@gmx.at> - 3.1.0-0.3.RC2
- Add ppc to excluded archs (BZ #846301)
- Don't build with profiling

* Fri Jan 27 2012 Volker Frohlich <volker27@gmx.at> - 3.1.0-0.1.RC2
- Add pkconfig as Requirement to the devel sub-package
- Drop freexl patch (solved), build with Freexl
- Update descriptions and summaries
- Re-design conditionals for build flags
- Don't run checks if built without advancedgeos
- Include examples as documentation

* Wed Jan 14 2012 Volker Frohlich <volker27@gmx.at> - 3.0.1-1
- New upstream release
- Drop defattr
- Run tests
- Own spatialite include-dir
- Add GPLv2+ and LGPLv2+ as alternative licenses
- Update URL and source URL
- Reduce build conditions to EPEL or not
- Use isa macro in base package Requires

* Tue Dec 7 2010 Volker Frohlich <volker27@gmx.at> 2.4.0-0.5.RC4
- Corrected wrong Fedora version number in if-statement

* Sun Dec 5 2010 Volker Frohlich <volker27@gmx.at> 2.4.0-0.4.RC4
- Refined configure condition to support RHEL

* Fri Dec 3 2010 Volker Frohlich <volker27@gmx.at> 2.4.0-0.3.RC4
- Added buildroot
- Added doc files

* Wed Dec 1 2010 Volker Frohlich <volker27@gmx.at> 2.4.0-0.2.RC4
- Added description of devel package
- Switched to disable-static flag

* Sun Nov 28 2010 Volker Frohlich <volker27@gmx.at> 2.4.0-0.1.RC4
- Initial packaging for Fedora
