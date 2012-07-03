%define pg_ver 9.1

Name: postgis
Version: 1.5.3
Release: alt1

Summary: Geographic Information Systems Extensions to PostgreSQL
Summary(ru_RU.UTF-8): Геоинформационные расширения для PostgreSQL
License: GPLv2
Group: Development/Databases
Url: http://postgis.refractions.net

Source: %name-%version.tar
Source1: create_template_postgis
Patch: %name-%version-install-dirs.patch

BuildPreReq: postgresql%pg_ver-devel

# Automatically added by buildreq on Wed Jan 20 2010
BuildRequires: ImageMagick-tools docbook-dtds docbook-style-xsl flex libgeos-devel libgtk+2-devel libproj-devel libxml2-devel postgresql-devel xsltproc

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

%prep
%setup
%patch -p1

%build
AUTOHEADER=true autoreconf -fisv -I macros
%configure \
	--with-gui \
	--with-xsldir=%_datadir/xml/docbook/xsl-stylesheets

%make_build all docs comments


%install
install -pD -m0755 %SOURCE1 %buildroot%_bindir/create_template_postgis
install -d %buildroot%_libdir/pgsql/

%make_install \
	DESTDIR=%buildroot \
	DOCDIR=%_docdir/%name-%version \
	MAN1DIR=%_man1dir \
	install docs-install comments-install

%files
%_bindir/pgsql2shp
%_bindir/shp2pgsql*
%_man1dir/*
%doc %_docdir/%name-%version

%files -n postgresql%pg_ver-%name
%_bindir/create_template_postgis
%_libdir/pgsql/%{name}*.so
%_datadir/pgsql/contrib/postgis-*/*.sql


%changelog
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

