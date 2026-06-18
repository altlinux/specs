%global ini_name 39-mapserver.ini
%global project_owner MapServer
%global project_name MapServer

%def_without java
%def_without ruby
%def_without php
%def_with python

%define libname libmapserver2

Name: mapserver
Version: 8.6.4
Release: alt1

Summary: Environment for building spatially-enabled internet applications

License: MIT
Group: System/Servers
Url: http://www.mapserver.org

%define dashver %(echo %version | sed 's|\\.|-|g')
# Source-url: https://github.com/%project_owner/%project_name/archive/rel-%dashver/%project_name-%version.tar.gz
Source: %name-%version.tar

#Requires: httpd
Requires: font(dejavusans)

BuildRequires(pre): rpm-macros-cmake

BuildRequires: apache2-devel
BuildRequires: cmake

BuildRequires: gcc-c++
BuildRequires: libcairo-devel
BuildRequires: libcurl-devel
BuildRequires: libfcgi-devel
BuildRequires: libfreetype-devel
BuildRequires: libfribidi-devel
BuildRequires: libgd3-devel >= 2.0.16
BuildRequires: libgdal-devel
BuildRequires: libgeos-devel >= 3.7.1
BuildRequires: libgif-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: libxml2-devel
BuildRequires: libXpm-devel
BuildRequires: libxslt-devel
BuildRequires: libmysqlclient-devel
BuildRequires: libssl-devel
BuildRequires: libharfbuzz-devel
BuildRequires: libpam0-devel
#BuildRequires: perl-devel
#BuildRequires: perl-generators
#BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: libprotobuf-c-devel
BuildRequires: libpq-devel
BuildRequires: libproj-devel >= 5.2.0
BuildRequires: libreadline-devel
BuildRequires: swig
BuildRequires: zlib-devel
#Get
#%_datadir/fonts/dejavu-sans-fonts/DejaVuSans.ttf
#%_datadir/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf
# See %%prep below
#BuildRequires: font(dejavusans)

%description
Mapserver is an internet mapping program that converts GIS data to
map images in real time. With appropriate interface pages,
Mapserver can provide an interactive internet map based on
custom GIS data.

%package -n %libname
Summary: %summary
Group: System/Libraries

%description -n %libname
This package contains the libs for mapserver.

%package -n %libname-devel
Summary: Development files for mapserver
Requires: %name = %version
Group: Development/C

%description -n %libname-devel
This package contains development files for mapserver.

%if_with php
%package -n php-%name
Summary: PHP/Mapscript map making extensions to PHP
BuildRequires: php-devel
Requires: php-gd%{?_isa}
Requires: php(zend-abi) = %php_zend_api
Requires: php(api) = %php_core_api

%description -n php-%name
The PHP/Mapscript extension provides full map customization capabilities within
the PHP scripting language.
%endif

%package perl
Summary: Perl/Mapscript map making extensions to Perl
Requires: %name = %EVR
Group: Development/Perl

%description perl
The Perl/Mapscript extension provides full map customization capabilities
within the Perl programming language.

%if_with python
%package -n python3-module-mapserver
Summary: Python/Mapscript map making extensions to Python
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools
Requires: %name = %EVR
Requires: python3
Group: Development/Python3

%description -n python3-module-mapserver
The Python/Mapscript extension provides full map customization capabilities
within the Python programming language.
%endif

%if_with java
%package java
Summary: Java/Mapscript map making extensions to Java
BuildRequires: java-devel
Requires: %name = %EVR
Requires: java-headless
Group: Development/Java

%description java
The Java/Mapscript extension provides full map customization capabilities
within the Java programming language.
%endif

%if_with ruby
%package ruby
Summary: Ruby/Mapscript map making extensions to Ruby
BuildRequires: ruby-devel
Requires: %name = %EVR
Group: Development/Ruby

%description ruby
The Ruby/Mapscript extension provides full map customization capabilities within
the ruby programming language.
%endif

%prep
%setup

# replace fonts for tests with symlinks
#ln -sf %_datadir/fonts/dejavu-sans-fonts/DejaVuSans.ttf tests/vera/Vera.ttf
#ln -sf %_datadir/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf tests/vera/VeraBd.ttf

# Force swig to regenerate the wrapper
rm -rf mapscript/perl/mapscript_wrap.c

%build
export CFLAGS="${CFLAGS} -ldl -fPIC -fno-strict-aliasing"
export CXXFLAGS="%optflags -fno-strict-aliasing"

%cmake -DINSTALL_LIB_DIR=%_libdir \
      -DCMAKE_SKIP_RPATH=ON \
      -DCMAKE_SKIP_INSTALL_RPATH=ON \
      -DWITH_CAIRO=TRUE \
      -DWITH_CLIENT_WFS=TRUE \
      -DWITH_CLIENT_WMS=TRUE \
      -DWITH_CURL=TRUE \
      -DWITH_FCGI=TRUE \
      -DWITH_FRIBIDI=TRUE \
      -DWITH_GD=TRUE \
      -DWITH_GDAL=TRUE \
      -DWITH_GEOS=TRUE \
      -DWITH_GIF=TRUE \
      -DWITH_ICONV=TRUE \
%if_with java
      -DWITH_JAVA=TRUE \
%else
      -DWITH_JAVA=FALSE \
%endif
      -DWITH_KML=TRUE \
      -DWITH_LIBXML2=TRUE \
      -DWITH_OGR=TRUE \
      -DWITH_MYSQL=TRUE \
      -DWITH_PERL=TRUE \
      -DCUSTOM_PERL_SITE_ARCH_DIR="%perl_vendor_archlib" \
%if_with php
      -DWITH_PHPNG=TRUE \
%endif
      -DWITH_POSTGIS=TRUE \
      -DWITH_PROJ=TRUE \
      -DWITH_PROTOBUFC=FALSE \
%if_with python
      -DWITH_PYTHON=TRUE \
%endif
%if_with ruby
      -DWITH_RUBY=TRUE \
%endif
      -DWITH_V8=FALSE \
      -DWITH_SOS=TRUE \
      -DWITH_THREAD_SAFETY=TRUE \
      -DWITH_WCS=TRUE \
      -DWITH_WMS=TRUE \
      -DWITH_WFS=TRUE \
      -DWITH_XMLMAPFILE=TRUE \
      -DWITH_POINT_Z_M=TRUE \
      -DWITH_APACHE_MODULE=FALSE \
      -DWITH_SVGCAIRO=FALSE \
      -DWITH_CSHARP=FALSE \
      -DWITH_ORACLESPATIAL=FALSE \
      -DWITH_ORACLE_PLUGIN=FALSE \
      -DWITH_MSSQL2008=FALSE \
      -DWITH_SDE=FALSE \
      -DWITH_SDE_PLUGIN=FALSE \
      -DWITH_EXEMPI=FALSE \
      -Wno-dev

%cmake_build

%install
%cmake_install

%if_with python
# cmake tries to invoke pip and download things. we'll just use setuptools.
#mkdir -p %buildroot%python3_sitelibdir
pushd %_cmake__builddir/src/mapscript/python
%python3_install
popd
%endif

mkdir -p %buildroot%_datadir/%name
install -p -m 644 src/xmlmapfile/mapfile.xsd %buildroot%_datadir/%name
install -p -m 644 src/xmlmapfile/mapfile.xsl %buildroot%_datadir/%name

%if_with java
# install java
mkdir -p %buildroot%_javadir
install -p -m 644 %_vpath_builddir/src/mapscript/java/mapscript.jar %buildroot%_javadir/
%endif

%if_with php
# install php config file
mkdir -p %buildroot%php_inidir
cat > %buildroot%php_inidir/%ini_name <<EOF
; Enable %name extension module
extension=php_mapscriptng.so
EOF
%endif

# Install sample config file as %%doc
rm %buildroot%_usr/%_sysconfdir/mapserver-sample.conf

%files
%doc README.md
%doc etc/mapserver-sample.conf
%_bindir/coshp
%_bindir/legend
%_bindir/mapserv
%_bindir/map2img
%_bindir/msencrypt
%_bindir/scalebar
%_bindir/shptree
%_bindir/shptreetst
%_bindir/shptreevis
%_bindir/sortshp
%_bindir/tile4ms
%_datadir/%name/

%files -n %libname
%doc README.md
%_libdir/libmapserver.so.%version
%_libdir/libmapserver.so.2

%files -n %libname-devel
%doc README.md
%_libdir/libmapserver.so
%_includedir/%name/

%if_with php
%files -n php-%name
%doc src/mapscript/php/README.md
%config(noreplace) %php_inidir/%ini_name

# this is only installed when swig < 4.0.2 https://github.com/MapServer/MapServer/blob/25ef061bec310773511eb84ef03f4a91e0f5a081/src/mapscript/phpng/CMakeLists.txt#L86
%if ! 0%{?fedora} && 0%{?rhel} < 10
%php_extdir/mapscript.php
%endif

%php_extdir/php_mapscriptng.so
%endif
# end php-mapcache

%files perl
%doc README.md
%doc src/mapscript/perl/examples
%dir %perl_vendor_archlib/auto/mapscript
%perl_vendor_archlib/auto/mapscript/*
%perl_vendor_archlib/mapscript.pm

%if_with python
%files -n python3-module-mapserver
%doc src/mapscript/python/README.rst
%doc src/mapscript/python/examples
%python3_sitelibdir/mapscript*
%endif

%if_with java
%files java
%doc src/mapscript/java/README
%doc src/mapscript/java/examples
%doc src/mapscript/java/tests
%_javadir/*.jar
%_libdir/libjavamapscript.so
%endif

%if_with ruby
%files ruby
%doc src/mapscript/ruby/README
%doc src/mapscript/ruby/examples
%doc mapserver-ruby/README
%doc mapserver-ruby/examples
%ruby_sitearchdir/mapscript.so
%endif

%changelog
* Mon Jun 15 2026 Andrey Cherepanov <cas@altlinux.org> 8.6.4-alt1
- New version.

* Sun May 25 2025 Vitaly Lipatov <lav@altlinux.ru> 8.4.0-alt1
- initial build for ALT Sisyphus (thanks, Fedora!)
