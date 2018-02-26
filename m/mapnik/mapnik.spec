Name: mapnik
Version: 2.0.1
Release: alt3
Summary: Free Toolkit for developing mapping applications
Group: Engineering
License: LGPLv2+
Url: http://mapnik.org/

Source: %name-%version.tar
Source2: paths.py
Patch: %name-%version-%release.patch

BuildRequires: postgresql-devel
BuildRequires: libgdal-devel libproj-devel libagg-devel
BuildRequires: scons desktop-file-utils gcc-c++
BuildRequires: libltdl-devel qt4-devel
BuildRequires: libxml2-devel libicu-devel
BuildRequires: boost-devel  boost-filesystem-devel boost-program_options-devel boost-python-devel boost-interprocess-devel
BuildRequires: libsqlite3-devel
BuildRequires: libtiff-devel libjpeg-devel libpng-devel
BuildRequires: libcairomm-devel python-module-pycairo-devel libfreetype-devel

%description
Mapnik is a Free Toolkit for developing mapping applications.
It's written in C++ and there are Python bindings to
facilitate fast-paced agile development. It can comfortably
be used for both desktop and web development, which was something
I wanted from the beginning.

Mapnik is about making beautiful maps. It uses the AGG library
and offers world class anti-aliasing rendering with subpixel
accuracy for geographic data. It is written from scratch in
modern C++ and doesn't suffer from design decisions made a decade
ago. When it comes to handling common software tasks such as memory
management, filesystem access, regular expressions, parsing and so
on, Mapnik doesn't re-invent the wheel, but utilises best of breed
industry standard libraries from boost.org

%package -n lib%name
Summary: Mapnik is a Free toolkit for developing mapping applications
Group: Engineering
Requires: fonts-ttf-dejavu fonts-ttf-dejavu-lgc

%description -n lib%name
Mapnik is a Free Toolkit for developing mapping applications.
It's written in C++ and there are Python bindings to
facilitate fast-paced agile development. It can comfortably
be used for both desktop and web development, which was something
I wanted from the beginning.

Mapnik is about making beautiful maps. It uses the AGG library
and offers world class anti-aliasing rendering with subpixel
accuracy for geographic data. It is written from scratch in
modern C++ and doesn't suffer from design decisions made a decade
ago. When it comes to handling common software tasks such as memory
management, filesystem access, regular expressions, parsing and so
on, Mapnik doesn't re-invent the wheel, but utilises best of breed
industry standard libraries from boost.org

%package -n lib%name-devel
Summary: Mapnik is a Free toolkit for developing mapping applications
Group: Development/Tools
Requires: lib%name = %version-%release

%description -n lib%name-devel
Mapnik is a Free Toolkit for developing mapping applications.
It's written in C++ and there are Python bindings to
facilitate fast-paced agile development. It can comfortably
be used for both desktop and web development, which was something
I wanted from the beginning.

Mapnik is about making beautiful maps. It uses the AGG library
and offers world class anti-aliasing rendering with subpixel
accuracy for geographic data. It is written from scratch in
modern C++ and doesn't suffer from design decisions made a decade
ago. When it comes to handling common software tasks such as memory
management, filesystem access, regular expressions, parsing and so
on, Mapnik doesn't re-invent the wheel, but utilises best of breed
industry standard libraries from boost.org

%package -n python-module-%name
Summary: Python bindings for the Mapnik spatial visualization library
License: GPLv2+
Group: Development/Python
Requires: lib%name = %version-%release

%description -n python-module-%name
Language bindings to enable the Mapnik library to be used from python

%package utils
License: GPLv2+
Summary: Utilities distributed with the Mapnik spatial visualization library
Group: Development/Other
Requires: lib%name = %version-%release

%description utils
Miscellaneous utilities distributed with the Mapnik spatial visualization
library

%package demo
Summary: Demo utility and some sample data distributed with mapnik
License: GPLv2+ GeoGratis
Group: Development/Other
Requires: lib%name-devel = %version-%release
Requires: python-module-%name = %version-%release

%description demo
Demo application and sample vector datas distributed with the Mapnik
spatial visualization library

%prep
%setup -n %name-%version

%patch -p1

%build
scons \
	PREFIX=%prefix \
	LIB_DIR_NAME=%name \
	MAPNIK_LIB_BASE=%_libdir \
	MAPNIK_LIB_DIR=%_libdir/%name \
	MAPNIK_INPUT_PLUGINS=%_libdir/%name/input \
	THREADING=multi \
	XMLPARSER=libxml2 \
	GDAL_INCLUDES=%_includedir/gdal \
	INTERNAL_LIBAGG=False \
	SYSTEM_FONTS=%_datadir/ttf/dejavu \
	BOOST_SYSTEM_REQUIRED=True

# build mapnik viewer app
pushd demo/viewer
qmake-qt4 viewer.pro
# WARNING smp may break build
# %{?_smp_mflags}
make
popd

%install
scons install \
	DESTDIR=%buildroot \
	PREFIX=%prefix \
	LIB_DIR_NAME=%name \
	MAPNIK_LIB_BASE=%_libdir \
	MAPNIK_LIB_DIR=%_libdir/%name \
	MAPNIK_INPUT_PLUGINS=%_libdir/%name/input \
	THREADING=multi \
	XMLPARSER=libxml2 \
	GDAL_INCLUDES=%_includedir/gdal \
	INTERNAL_LIBAGG=False \
	SYSTEM_FONTS=%_datadir/ttf/dejavu \
	BOOST_SYSTEM_REQUIRED=True

# replace paths.py
install -p -m 644 %SOURCE2 %buildroot%python_sitelibdir/%name/paths.py

# get rid of fonts use external instead
rm -rf %buildroot%_libdir/%name/fonts

# install pkgconfig file
cat > %name.pc <<EOF
prefix=%prefix
exec_prefix=%prefix
includedir=%_includedir

Name: mapnik
Description: Free Toolkit for developing mapping applications
Version: 2.0.1
Requires: libagg
Libs: -lmapnik
Cflags: -I\${includedir}/%name
EOF

mkdir -p %buildroot%_pkgconfigdir
install -p -m 644 %name.pc %buildroot%_pkgconfigdir/%name.pc

%files -n lib%name
%doc AUTHORS.md COPYING README.md INSTALL.md CHANGELOG
%dir %_libdir/%name
%dir %_libdir/%name/input
%_bindir/mapnik-config
%_libdir/%name/input/*.input
%_libdir/lib%name.so.*

%files -n lib%name-devel
%doc docs/
%dir %_includedir/%name
%_includedir/%name/*
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%files -n python-module-%name
%python_sitelibdir/*

%files utils
%_bindir/shapeindex
%_bindir/mapnik-speed-check
%_bindir/upgrade_map_xml.py

%files demo
%doc demo/c++
%doc demo/data
%doc demo/python demo/test

%changelog
* Fri Apr 27 2012 Alexey Shabalin <shaba@altlinux.ru> 2.0.1-alt3
- really fix plugin path in python bindings

* Thu Apr 26 2012 Alexey Shabalin <shaba@altlinux.ru> 2.0.1-alt2
- fix plugins path in python module
- fix requires to fonts

* Thu Apr 19 2012 Alexey Shabalin <shaba@altlinux.ru> 2.0.1-alt1
- initial build for ALT Linux Sisyphus
