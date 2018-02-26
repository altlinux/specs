
%define svn 28333

Summary: Imports map data from www.OpenStreetMap.org to a PostgresSQL database
Name: osm2pgsql
Group: Databases
Version: 0.80.0
Release: alt1.svn%svn

License: GPLv2+
Url: http://svn.openstreetmap.org/applications/utils/export/osm2pgsql

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++
BuildRequires: libgeos-devel
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
%setup -n %name-%version
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--with-zlib=yes \
	--with-zlib-inc=%_includedir \
	--with-zlib-lib=%_libdir \
	--with-bzip2=yes \
	--with-bzip2-inc=%_includedir \
	--with-bzip2-lib=%_libdir \
	--with-proj=yes \
	--with-proj-inc=%_includedir \
	--with-proj-lib=%_libdir \
	--with-protobuf_c=yes \
	--with-protobuf_c-inc=%_includedir \
	--with-protobuf_c-lib=%_libdir


%make_build

%install
%make_install install DESTDIR=%buildroot

%files
%doc README ChangeLog AUTHORS COPYING NEWS TODO install-postgis-osm-db.sh install-postgis-osm-user.sh mapnik-osm-updater.sh
%_bindir/%name
%_datadir/%name
%_man1dir/%name.*

%changelog
* Thu Apr 26 2012 Alexey Shabalin <shaba@altlinux.ru> 0.80.0-alt1.svn28333
- initial build for ALT Linux Sisyphus
