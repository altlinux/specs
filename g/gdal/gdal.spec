%def_with docs
%def_without check

# TODO: enable system libtiff when it will support BigTiff (from 4.0?)
%def_without libtiff
%def_without geotiff

Summary: The Geospatial Data Abstraction Library (GDAL)
Name: gdal
Version: 3.6.2
Release: alt1
Group: Sciences/Geosciences

License: MIT
URL: http://www.gdal.org
Packager: ALT QA Team <qa@packages.altlinux.org>
# ftp://ftp.remotesensing.org/%name/%version/%name-%version.tar.xz
Source: %name-%version.tar

Patch: %name-2.2.3-alt-mysql8-transition.patch

%define libname lib%name

BuildRequires: doxygen gcc-c++ libMySQL-devel libcfitsio-devel libcurl-devel
BuildRequires: libexpat-devel libgeos-devel libgif-devel libhdf5-devel
BuildRequires: libjpeg-devel libpng-devel libsqlite3-devel
BuildRequires: libunixODBC-devel postgresql-devel swig zlib-devel

BuildRequires: chrpath libnetcdf-devel
BuildRequires: libproj-devel
BuildRequires: libxerces-c-devel
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: libnumpy-py3-devel
BuildRequires: libtiff-devel libgeotiff-devel libxml2-devel libzstd-devel
BuildRequires: libqhull-devel libpcre2-devel libspatialite-devel
BuildRequires: librasterlite2-devel libwebp-devel freexl-devel
BuildRequires: libblas-devel liblapack-devel libhdf5-devel libkea-devel
BuildRequires: pkgconfig(OpenCL) liblzma-devel libheif-devel
BuildRequires: libopenjpeg2.0-devel libpoppler-devel
%ifarch %ix86 x86_64
BuildRequires: libarmadillo-devel
%endif
%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx_rtd_theme
BuildRequires: python3-module-breathe
BuildRequires: python3-module-sphinx-bootstrap-theme
BuildRequires: python3-module-sphinxcontrib-spelling
BuildRequires: python3-module-recommonmark
%endif
%if_with check
BuildRequires: ctest
BuildRequires: python3-module-pytest
BuildRequires: python3-module-numpy-testing
BuildRequires: /proc
%endif

%description
The Geospatial Data Abstraction Library (GDAL) is a unifying
C/C++ API for accessing raster geospatial data, and currently
includes formats like GeoTIFF, Erdas Imagine, Arc/Info
Binary, CEOS, DTED, GXF, and SDTS. It is intended to provide
efficient access, suitable for use in viewer applications,
and also attempts to preserve coordinate systems and metadata.
Python, C, and C++ interfaces are available.

%if_with docs
%package doc
Summary: Documentation for GDAL/OGR
Group: Documentation
BuildArch: noarch

%description doc
This package contains documentation for the GDAL/OGR library
and utilities.
%endif

%package scripts
Summary: Scripts for GDAL
Group: Sciences/Geosciences
BuildArch: noarch

%description scripts
This package contains various scripts for GDAL (written in python)

%package -n %libname
Summary: Libraries required for the GDAL library
Group: Sciences/Geosciences

%description -n %libname
Libraries required for the GDAL library

%package -n %libname-devel
Summary: Development files for using the GDAL library
Group: Development/C
Requires: %libname = %version-%release

%description -n lib%name-devel
Development files for using the GDAL library

%package -n python3-module-%name
Summary: The Python bindings for the GDAL library
Group: Development/Python3
Requires: %libname = %version
Requires: %name
Provides: python3-module-osgeo = %version

%description -n python3-module-%name
Python module for %name.

%prep
%setup
%patch -p0

%build
%add_optflags -fno-strict-aliasing -I%_includedir/netcdf
%ifarch %e2k
# lcc 1.23 can't do those __builtin_functions (mcst#3588)
%add_optflags -D__INTEL_COMPILER
%endif
%cmake \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DCMAKE_INSTALL_INCLUDEDIR:PATH=%_includedir/%name \
    -DGDAL_USE_EXTERNAL_LIBS=ON \
    -DGDAL_USE_CFITSIO=OFF \
    -DGDAL_USE_CURL=ON \
    -DGDAL_USE_EXPAT=ON \
    -DGDAL_USE_FREEXL=ON \
    -DGDAL_USE_GEOS=ON \
    -DGDAL_USE_GIF=ON \
    -DGDAL_USE_HDF5=ON \
    -DGDAL_USE_HEIF=ON \
    -DGDAL_USE_JPEG=ON \
    -DGDAL_USE_JSONC_INTERNAL=ON \
    -DGDAL_USE_LIBLZMA=ON \
    -DGDAL_USE_LIBXML2=ON \
    -DGDAL_USE_MYSQL=ON \
    -DGDAL_USE_NETCDF=ON \
    -DGDAL_USE_ODBC=ON \
    -DGDAL_USE_OGDI=OFF \
    -DGDAL_USE_OPENCL=ON \
    -DGDAL_USE_OPENJPEG=ON \
    -DGDAL_USE_PCRE=ON \
    -DGDAL_USE_PCRE2=ON \
    -DGDAL_USE_PNG=ON \
    -DGDAL_USE_POPPLER=ON \
    -DGDAL_USE_POSTGRESQL=ON \
    -DGDAL_USE_QHULL=ON \
    -DGDAL_USE_SHAPELIB=OFF \
    -DGDAL_USE_SPATIALITE=ON \
    -DGDAL_USE_TIFF=ON \
    -DGDAL_USE_WEBP=ON \
    -DGDAL_USE_XERCESC=ON \
    -DGDAL_USE_ZLIB=ON \
    -DGDAL_USE_ZSTD=ON \
    -DOGR_BUILD_OPTIONAL_DRIVERS=ON

%cmake_build
%if_with docs
export LD_LIBRARY_PATH="$PWD/%_cmake__builddir"
export PYTHONPATH="$PWD/%_cmake__builddir/swig/python"
# latexmk isn't available to make gdal.pdf
sed -i \
    "s|ln -sf ../latex/gdal.pdf build/html|#ln -sf ../latex/gdal.pdf build/html|" \
    doc/Makefile
make SPHINXBUILD="sphinx-build-3" -C doc html
make SPHINXBUILD="sphinx-build-3" -C doc man
%endif

%install
%cmake_install
%if_with docs
mkdir -p %buildroot%_man1dir
install -m 644 doc/build/man/*.1 %buildroot%_man1dir
%endif

%check
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%buildroot%_libdir
export GDAL_DATA=%buildroot%_datadir/%name
export PYTHONPATH=%buildroot%python3_sitelibdir
export GDAL_DOWNLOAD_TEST_DATA=0
pushd %_cmake__builddir/autotest
py.test-3 -v
popd

%files
%_datadir/%name
%_bindir/ogr*
%_bindir/gdal*
%_bindir/nearblack
%_bindir/gnmanalyse
%_bindir/gnmmanage
%exclude %_bindir/gdal-config
%exclude %_bindir/*.py
%_datadir/bash-completion/completions/gdal*
%_datadir/bash-completion/completions/ogr*
%_libdir/cmake/%name/*.cmake
%if_with docs
%_man1dir/*

%files doc
%doc *.md *.txt doc/build/html
%endif

%files scripts
%_bindir/*.py

%files -n %libname-devel
%_bindir/gdal-config
%_libdir/*.so
%_includedir/%name
%_pkgconfigdir/gdal.pc

%files -n %libname
%_libdir/*.so.*
%_libdir/gdalplugins/drivers.ini

%files -n python3-module-%name
%python3_sitelibdir/*

%changelog
* Sat Feb 11 2023 Alexander Stepchenko <geochip@altlinux.org> 3.6.2-alt1
- Update to 3.6.2

* Fri Oct 15 2021 Ivan A. Melnikov <iv@altlinux.org> 3.0.4-alt1.7
- build with setuptools again to fix the package update

* Thu Oct 14 2021 Ivan A. Melnikov <iv@altlinux.org> 3.0.4-alt1.6
- fix FTBFS:
  + fix build with gcc11
  + avoid using python3-module-setuptools: it breaks build
    since setuptools 58+ dropped use_2to3 support.

* Tue Aug 17 2021 Vitaly Lipatov <lav@altlinux.ru> 3.0.4-alt1.5
- NMU: drop libnumpy-devel (it is unused python2 only package)

* Thu Jul 01 2021 Andrey Cherepanov <cas@altlinux.org> 3.0.4-alt1.4
- FTBFS: build with libxerces-c-devel (ALT #40327)

* Fri May 14 2021 Michael Shigorin <mike@altlinux.org> 3.0.4-alt1.3
- fixed ftbfs with archlinux patch, dropped -fpermissive quick hack

* Sat Sep 19 2020 Igor Vlasenko <viy@altlinux.ru> 3.0.4-alt1.2
- NMU: fixed build (build w/o python2) (closes: #38911)
- TODO: remove -fpermissive quick hack
- TODO: build --with-netcdf

* Thu Apr 16 2020 Michael Shigorin <mike@altlinux.org> 3.0.4-alt1.1
- E2K: fix build with lcc 1.23

* Thu Feb 27 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 3.0.4-alt1
- update to 3.0.4
- unconditional python3
- stop 2to3 usage

* Thu Apr 25 2019 Vitaly Lipatov <lav@altlinux.ru> 2.2.3-alt3.1
- drop unneeded python3-module-BeautifulSoup req

* Thu Feb 07 2019 Nikolai Kostrigin <nickel@altlinux.org> 2.2.3-alt3
- fix FTBFS against libmysqlclient21

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 2.2.3-alt2.1
- rebuild with new perl 5.28.1

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.3-alt2
- (NMU) Rebuilt with python-3.6.4.

* Sat Feb 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.3-alt1
- New version.

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt5.1
- rebuild with new perl 5.26.1

* Mon Aug 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.2-alt5
- Rebuilt with libnetcdf11.

* Wed Aug 16 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt4.1
- Rebuild with geos 3.6.2

* Sun Feb 12 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt4
- NMU: enabled perl after perl5.24.1 upgrade

* Sun Feb 05 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt3
- NMU: disabled perl for perl5.24.1 upgrade

* Sat May 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt2
- NMU: rebuild with python3-module-xlwt

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.2-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Tue Mar 08 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.0.2-alt1
- NMU: 2.0.0 -> 2.0.2 (fixes FTBFS).

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2.1
- rebuild with new perl 5.22.0

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2
- Rebuilt with new geos

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1
- Version 2.0.0

* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.2-alt1
- Version 1.11.2
- Added module for Python 3

* Wed Jan 21 2015 Dmitry Derjavin <dd@altlinux.org> 1.11.1-alt1
- 1.11.1;
- Perl module build Error 255 workaround.

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.10.1-alt3.1.1
- rebuild with new perl 5.20.1

* Wed Mar 26 2014 Sergey V Turchin <zerg@altlinux.org> 1.10.1-alt3.1
- NMU: rebuilt with new cfitsio

* Fri Jan 31 2014 Dmitry Derjavin <dd@altlinux.org> 1.10.1-alt3
- libproj: fixed hardcoded library path and dependency added

* Mon Jan 20 2014 Dmitry Derjavin <dd@altlinux.org> 1.10.1-alt2
- Static build disabled;
- accidentally disabled apps-install patch got back.

* Thu Jan 16 2014 Dmitry Derjavin <dd@altlinux.org> 1.10.1-alt1
- 1.10.1

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 1.8.0-alt4
- built for perl 5.18

* Tue Jul 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt3.1
- Rebuilt with new libhdf5

* Sun Jan 27 2013 Fr. Br. George <george@altlinux.ru> 1.8.0-alt3
- Move python module out of .egg directory (Closes: #26462)

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt2.1
- Rebuilt with libpng15

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 1.8.0-alt2
- rebuilt for perl-5.16

* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1.4
- Rebuilt with libhdf5-7-seq 1.8.8-alt2

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.0-alt1.3.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1.3
- Removed bad RPATH

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.0-alt1.2.1
- Rebuild with Python-2.7

* Sun Oct 16 2011 Alexey Tourbin <at@altlinux.ru> 1.8.0-alt1.2
- rebuilt for perl-5.14

* Thu Sep 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1.1
- Rebuilt with libhdf5-7

* Fri Apr 15 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.0-alt1
- 1.8.0
- build fixed

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.7.1-alt3.1
- rebuilt with perl 5.12

* Thu Aug 12 2010 Egor Vyscrebentsov <evyscr@altlinux.org> 1.7.1-alt3
- packaged python scripts into subpackage (break circular dependencies)

* Mon Jun 07 2010 Egor Vyscrebentsov <evyscr@altlinux.org> 1.7.1-alt2
- packaged utils binaries, not wrappers (#23397)
- packaged docs and mans

* Thu Apr 22 2010 Egor Vyscrebentsov <evyscr@altlinux.org> 1.7.1-alt1
- new version: 1.7.1
- enabled perl bindings
- fixed python bindings

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt2.1
- Rebuilt with python 2.6

* Tue Jul 28 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.6.1-alt2
- use %%python_sitelibdir instead of hardcoded path

* Tue Jul 14 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.1-alt1
- new version

* Mon Oct 27 2008 Andriy Stepanov <stanv@altlinux.ru> 1.5.3-alt0.M41.1
- M41

* Mon Oct 27 2008 Andriy Stepanov <stanv@altlinux.ru> 1.5.3-alt1
- New version

* Tue Aug 28 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1.1
- changes from Sir Raorn <raorn@altlinux.ru> 1.4.0-alt1.1:
-- Major spec cleanup
-- Packaged headers
-- Disabled perl/python/ruby in configure (not packaged by default)
-- Fixed Group

* Thu Jan 18 2007 Dmitri Kuzishchin <dim@altlinux.ru> 1.4.0-alt1
- Initial package.
