Summary: Imports map data from www.OpenStreetMap.org to a PostgresSQL database
Name: osm2pgsql
Group: Databases
Version: 0.96.0
Release: alt1

License: GPLv2+
Url: https://github.com/openstreetmap/osm2pgsql

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: libexpat-devel
BuildRequires: libgeos-devel
BuildRequires: liblua5.3-devel
BuildRequires: libxml2-devel
BuildRequires: postgresql-devel
BuildRequires: bzlib-devel zlib-devel
BuildRequires: libproj-devel
BuildRequires: libprotobuf-c-devel

%description
Processes the planet file from the communtiy mapping project at
http://www.openstreetmap.org. The map data is converted from XML to a
database stored in PostgreSQL with PostGIS geospatial extentions. This
database may then be used to render maps with Mapnik or for other
geospatial analysis.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc docs README.md ChangeLog AUTHORS COPYING install-postgis-osm-db.sh install-postgis-osm-user.sh
%_bindir/%name
%_datadir/%name
%_man1dir/%name.*

%changelog
* Thu May 03 2018 Andrey Cherepanov <cas@altlinux.org> 0.96.0-alt1
- New version.

* Sat Oct 07 2017 Andrey Cherepanov <cas@altlinux.org> 0.94.0-alt1
- New version

* Fri Aug 18 2017 Andrey Cherepanov <cas@altlinux.org> 0.92.1-alt1
- New version
- Build by cmake
- Fix build with geos > 3.6 (see https://github.com/openstreetmap/osm2pgsql/pull/684)

* Wed Aug 16 2017 Andrey Cherepanov <cas@altlinux.org> 0.86.0-alt1.2
- Rebuild with geos 3.6.2

* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.86.0-alt1.1
- Rebuilt with new geos

* Thu Dec 04 2014 Dmitry Derjavin <dd@altlinux.org> 0.86.0-alt1
- 0.86.0;
- gazetteer patch does not seem to be needed any more;
- diff removed from gear rules;
- documentation files updated.

* Thu Jul 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.80.0-alt1.svn28333.3
- Rebuilt with updated geos

* Wed Nov 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.80.0-alt1.svn28333.2
- Rebuilt with updated geos

* Wed Sep 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.80.0-alt1.svn28333.1
- Rebuilt with updated geos

* Thu Apr 26 2012 Alexey Shabalin <shaba@altlinux.ru> 0.80.0-alt1.svn28333
- initial build for ALT Linux Sisyphus
