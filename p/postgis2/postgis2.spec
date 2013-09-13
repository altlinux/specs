%define pg_ver 9.1
%define ver_major 2.1

Name: postgis2
Version: %ver_major.0
Release: alt1

Summary: Geographic Information Systems Extensions to PostgreSQL
Summary(ru_RU.UTF-8): Геоинформационные расширения для PostgreSQL
License: GPLv2+
Group: Development/Databases
Url: http://postgis.org

Source: %name-%version.tar
# Patch: %name-%version-%release.patch

BuildPreReq: postgresql%pg_ver-devel

BuildRequires: ImageMagick-tools docbook-dtds docbook-style-xsl flex libgeos-devel libgtk+2-devel libproj-devel libxml2-devel postgresql-devel xsltproc
BuildRequires: libgdal-devel libjson-devel

%description
PostGIS adds support for geographic objects to the PostgreSQL
object-relational database. In effect, PostGIS "spatially enables" the
PostgreSQL server, allowing it to be used as a backend spatial
database for geographic information systems (GIS).

%description -l ru_RU.UTF-8
PostGIS добавляет поддержку географических объектов в PostgreSQL. В
сущности PostGIS является расширением PostgreSQL сервера,
позволяющим использовать его для хранения и обработки геоданных в
геоинформационных системах (ГИС).

%package -n postgresql%pg_ver-%name
Summary: The PostGIS extension for PostgreSQL
Group: Databases
Requires: postgresql%pg_ver-server

%description -n postgresql%pg_ver-%name
This package contains shared library for PostgreSQL server

%description -n postgresql%pg_ver-%name -l ru_RU.UTF-8
Подгружаемая postgis библиотека для PostgreSQL сервера

%package -n liblwgeom
Summary: LWGEOM geometry library
Group: System/Libraries

%description -n liblwgeom
This library is the generic geometry handling section of PostGIS. The geometry
objects, constructors, destructors, and a set of spatial processing functions,
are implemented here.

%package -n liblwgeom-devel
Summary: LWGEOM geometry library
Group: Development/C

%description -n liblwgeom-devel
This library is the generic geometry handling section of PostGIS. The geometry
objects, constructors, destructors, and a set of spatial processing functions,
are implemented here.

%prep
%setup
# %patch -p1
%__subst "s|PGSQL_DOCDIR|DOCDIR|g" doc/Makefile.in

# fix build postgis_tiger_geocoder.sql
mkdir -p extensions/postgis_tiger_geocoder/sql/

%build
./autogen.sh
%configure \
	--with-gui \
	--with-xsldir=%_datadir/xml/docbook/xsl-stylesheets

%make all docs comments


%install
install -d %buildroot%_libdir/pgsql/
install -d %buildroot%_bindir/
install -d %buildroot%_includedir/

%make_install \
	DESTDIR=%buildroot \
	DOCDIR=%_docdir/%name-%version \
	install docs-install comments-install

%files
%_bindir/*
#%_man1dir/*
#%doc %_docdir/%name-%version

%files -n postgresql%pg_ver-%name
%_libdir/pgsql/*.so
%_datadir/pgsql/contrib/postgis-%ver_major
%_datadir/pgsql/extension

%files -n liblwgeom
%_libdir/liblwgeom-*.so

%files -n liblwgeom-devel
%_libdir/liblwgeom.so
%_includedir/*

%changelog
* Fri Sep 13 2013 Alexey Shabalin <shaba@altlinux.ru> 2.1.0-alt1
- 2.1.0 as postgis2 package

* Tue Nov 27 2012 Alexey Shabalin <shaba@altlinux.ru> 1.5.8-alt1
- 1.5.8

* Mon Jul 30 2012 Alexey Shabalin <shaba@altlinux.ru> 1.5.5-alt1
- 1.5.5

* Thu Apr 19 2012 Alexey Shabalin <shaba@altlinux.ru> 1.5.3-alt1
- 1.5.3

* Sat May 22 2010 Denis Klimov <zver@altlinux.org> 1.5.1-alt5
- change proj-devel to libproj-devel in BuildRequires

* Mon Mar 29 2010 Denis Klimov <zver@altlinux.org> 1.5.1-alt4
- add subpackage with postgresql shared lib
- remove wildchars from create_template_postgis
- add patch for install dirs
- Closes #23248

* Sun Mar 28 2010 Denis Klimov <zver@altlinux.org> 1.5.1-alt3
- fix install create_template_postgis

* Sun Mar 28 2010 Denis Klimov <zver@altlinux.org> 1.5.1-alt2
- add create_template_postgis script

* Wed Mar 17 2010 Denis Klimov <zver@altlinux.org> 1.5.1-alt1
- Initial build for ALT Linux

