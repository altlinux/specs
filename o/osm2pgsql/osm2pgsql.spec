%define _unpackaged_files_terminate_build 1
%def_enable proj

Name: osm2pgsql
Summary: Imports map data from www.OpenStreetMap.org to a PostgresSQL database
Group: Databases
Version: 1.7.1
Release: alt1

License: GPLv2+
Url: https://github.com/openstreetmap/osm2pgsql

Source: %name-%version.tar
Patch1: fix-install-osm2pgsql-replication.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake >= 3.5.0
BuildRequires: rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: boost-devel boost-filesystem-devel boost-geometry-devel
BuildRequires: libexpat-devel
BuildRequires: libgeos-devel
BuildRequires: liblua5.3-devel
BuildRequires: libxml2-devel
BuildRequires: postgresql-devel >= 9.5
BuildRequires: bzlib-devel zlib-devel liblz4-devel
%{?_enable_proj:BuildRequires: libproj-devel}
BuildRequires: libprotobuf-c-devel
# TODO: external system libs
#BuildRequires: libfmt-devel libosmium-devel libprotozero-devel rapidjson-devel

%description
Processes the planet file from the communtiy mapping project at
http://www.openstreetmap.org. The map data is converted from XML to a
database stored in PostgreSQL with PostGIS geospatial extentions. This
database may then be used to render maps with Mapnik or for other
geospatial analysis.

%prep
%setup
%patch1 -p1

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc docs README.md AUTHORS COPYING
%_bindir/%name
%_bindir/%name-replication
%_datadir/%name
%_man1dir/%name.*
%_man1dir/%name-replication.*

%changelog
* Fri Oct 28 2022 Alexey Shabalin <shaba@altlinux.org> 1.7.1-alt1
- new version 1.7.1

* Sun Oct 06 2019 Vladislav Zavjalov <slazav@altlinux.org> 0.96.0-alt3
- Rebuild with libproj 6.2.0 (use ACCEPT_USE_OF_DEPRECATED_PROJ_API_H)

* Sat Feb 16 2019 Vladislav Zavjalov <slazav@altlinux.org> 0.96.0-alt2
- Rebuild with libproj 5.2.0.

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
