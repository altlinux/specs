# FIXME: grass is poorly packaged /usr/lib/grass62/lib/
# http://www.cmake.org/Wiki/CMake_RPATH_handling
#set_verify_elf_method unresolved=relaxed

Name: qgis
Version: 1.7.4
Release: alt1
Summary: A user friendly Open Source Geographic Information System

Group: Sciences/Geosciences
License: GPLv2+
Url: http://qgis.org/

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: http://qgis.org/downloads/%name-%version.tar.bz2

Source1: %name.desktop

Patch0: python-site-packages-dir-0.9.1.patch
Patch1: %name-0.9.1.patch
Patch2: qgis-1.5.0-grass.patch
Patch3: %name-1.6.0-sip.patch
Patch4: %name-alt-external-qwtpolar.patch

# http://osgeo-org.1560.n6.nabble.com/Problems-building-qgis-td4125345.html#a4125347
Patch5: %name-alt-sip.patch

# http://hub.qgis.org/issues/3562
Patch6: %name-libqwt6.patch

BuildRequires: ccmake flex gcc-c++ grass libexpat-devel libgdal-devel
BuildRequires: libgeos-devel libgsl-devel libnss-mysql libpth-devel libqt3-devel
BuildRequires: libqt4-devel libsqlite3-devel postgresql-devel python-module-PyQt4-devel
BuildRequires: perl-Net-FastCGI perl-FCGI libfcgi-devel
BuildRequires: grass-devel libproj-devel python-module-sip-devel subversion chrpath
BuildRequires: libqwtpolar-devel libqwtplot3d-devel libplotmm-devel libqwt6-devel
BuildRequires: desktop-file-utils

%description
Quantum GIS (QGIS) is a user friendly Open Source Geographic Information
System (GIS) that runs on Linux, Unix, Mac OSX, and Windows. QGIS supports
vector, raster, and database formats. QGIS is licensed under the GNU
General Public License. QGIS lets you browse and create map data on your
computer. It supports many common spatial data formats (e.g. ESRI ShapeFile,
geotiff). QGIS supports plugins to do things like display tracks from your GPS.

#%package devel
#Summary: Headers and libraries for building against qgis
#Group: Development/Libraries
#Requires: %name = %version-%release
#
#%description devel
#Headers and libraries for building against qgis

#package grass
#Summary: GRASS plugins for qgis
#Group: Sciences/Geosciences
#Requires: %name = %version-%release
#Requires: grass

#description grass
#GRASS plugins for qgis

#%package python
#Summary: python integration and plugins
#Group: Applications/Engineering
#Requires: %name = %version-%release
#
#%description python
#python integration and plugins

#package theme-nkids
#Summary: Addtional theme for qgis - nkids
#Group: Sciences/Geosciences
#Requires: %name = %version-%release

#%description theme-nkids
#Addtional theme for qgis - nkids

%prep
%setup -q -n %{name}-%version

%patch2 -p1 -b .grass
##patch3 -p0
%patch4 -p2
#patch5 -p2
%patch6 -p2

%build
# FIXIT in grass package
#for dir in %_libdir/grass*/ ; do
#	GRASS_PREFIX=$dir
#done
GRASS_PREFIX=%_libdir

cmake \
	-D QGIS_MANUAL_SUBDIR=share/man \
	-D QGIS_LIB_SUBDIR=%_lib \
	-D QGIS_PLUGIN_SUBDIR=%_lib/qgis \
	-D WITH_BINDINGS:BOOL=TRUE \
	-D BINDINGS_GLOBAL_INSTALL:BOOL=TRUE \
	-D GRASS_PREFIX=$GRASS_PREFIX \
	-D GDAL_INCLUDE_DIR=%_includedir/gdal \
	-D GDAL_LIBRARY=%_libdir/libgdal.so \
	-D GEOS_LIBRARY=%_libdir/libgeos_c.so \
	-D CMAKE_INSTALL_PREFIX=%_prefix \
	-D CMAKE_SKIP_RPATH:BOOL=TRUE \
	-D QWTPOLAR_INCLUDE_DIR:PATH=%_includedir/qwt \
	.
#	-D CMAKE_SKIP_RPATH:BOOL=ON
#make_build

make VERBOSE=1

%install
# check sipconfig from python-module-sip for LFLAGS's RPATH
# hack before fix https://bugzilla.altlinux.org/show_bug.cgi?id=14655
#chrpath -d python/core/core.so python/gui/gui.so
#makeinstall_std

make install DESTDIR=%buildroot

# remove headers and so files
rm -rf %buildroot%_includedir/%name
rm -f %buildroot%_libdir/*.so

# install desktop file
install -d %buildroot/{%_pixmapsdir,%_desktopdir}
install -m0644 \
	%buildroot/%_datadir/%name/images/icons/qgis-icon.png \
	%buildroot/%_pixmapsdir/%name.png
install -m0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop


%ifarch x86_64
mv %buildroot/usr/lib/%name/qgis_help  %buildroot%_libdir/%name/qgis_help
%endif

%find_lang %name --with-kde
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Engineering \
	%buildroot%_desktopdir/qgis.desktop


%files
%doc BUGS COPYING CHANGELOG README
%_bindir/%name
#_bindir/%{name}_help
#%_bindir/msexport
%_libdir/lib%{name}*.so.*
%_libdir/libqgispython.so.*
%dir %_libdir/%name/
#_libdir/%name/libcopyrightlabelplugin.so
#_libdir/%name/libdelimitedtextplugin.so
#_libdir/%name/libdelimitedtextprovider.so
#_libdir/%name/libgeorefplugin.so
#_libdir/%name/libgpsimporterplugin.so
#_libdir/%name/libgpxprovider.so
%_libdir/%name/*.so
%_libdir/%name/qgis_help
#_libdir/%name/libnortharrowplugin.so
#_libdir/%name/libogrprovider.so
#_libdir/%name/libpggeoprocessingplugin.so
#_libdir/%name/libpostgresprovider.so
#_libdir/%name/libscalebarplugin.so
###_libdir/%name/libquickprintplugin.so
#_libdir/%name/libspitplugin.so
#_libdir/%name/libwfsplugin.so
#_libdir/%name/libmemoryprovider.so
#_libdir/%name/libwfsprovider.so
#_libdir/%name/libwmsprovider.so
#_libdir/%name/libcoordinatecaptureplugin.so
#_libdir/%name/libdiagramoverlay.so
#libdir/%name/libdisplacementplugin.so
#_libdir/%name/libdxf2shpconverterplugin.so
#_libdir/%name/libevis.so
#_libdir/%name/libinterpolationplugin.so
#_libdir/%name/libofflineeditingplugin.so
###_libdir/%name/libogrconverterplugin.so
#_libdir/%name/liboracleplugin.so
#_libdir/%name/libosmprovider.so
#_libdir/%name/librasterterrainplugin.so
#_libdir/%name/libspatialiteprovider.so
#_libdir/%name/libspatialqueryplugin.so
%_datadir/%name/doc/
%_pixmapsdir/%name.png
%_desktopdir/%name.desktop
%dir %_datadir/%name/
%_datadir/%name/i18n/
%_datadir/%name/images/
%_datadir/%name/python/
%_datadir/%name/resources/
%_datadir/%name/svg/
#dir %_datadir/%name/themes/
#dir %_datadir/%name/themes/default/
#_datadir/%name/themes/default/*.png
%python_sitelibdir/%name/
%python_sitelibdir/pyspatialite/
%_man1dir/*

#%files devel
#%_includedir/%name

#files grass
#%_libdir/libqgisgrass.so.*
###_libdir/libqgisgrass.so
#_libdir/%name/libgrass*.so
#_datadir/%name/grass/
#%_datadir/%name/themes/default/grass

#%files python
#%_datadir/%name/python

#files theme-nkids
#_datadir/%name/themes/nkids

%changelog
* Thu Feb 23 2012 Ilya Mashkin <oddity@altlinux.ru> 1.7.4-alt1
- 1.7.4

* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.3-alt1.1
- Rebuilt with libqwt6 instead of libqwt

* Sun Dec 18 2011 Ilya Mashkin <oddity@altlinux.ru> 1.7.3-alt1
- 1.7.3

* Tue Dec 06 2011 Ilya Mashkin <oddity@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Fri Oct 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.7.1-alt1.1
- Rebuild with Python-2.7

* Thu Oct 06 2011 Ilya Mashkin <oddity@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Wed Jun 22 2011 Ilya Mashkin <oddity@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.6.0-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for qgis

* Thu May 12 2011 Ilya Mashkin <oddity@altlinux.ru> 1.6.0-alt2
- fix build (Patch3)

* Wed Dec 22 2010 Ilya Mashkin <oddity@altlinux.ru> 1.6.0-alt1
- 1.6.0
- without grass

* Sun Dec 28 2008 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt2
- fix build on x86_64
- cleanup spec, move libqgisgrass to qgis-grass package

* Sat Nov 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt1
- new version 0.11.0 (with rpmrb script)

* Sun Feb 03 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- initial build for ALT Linux Sisyphus

* Mon Jan 28 2008 Douglas E. Warner <silfreed@silfreed.net> 0.9.1-2
- defining lib path in build
- installing python bindings globally
- adding patch to determine python site packages dir correctly

* Mon Dec 17 2007 Douglas E. Warner <silfreed@silfreed.net> 0.9.1-1
- update to 0.9.1
- removing lib64 and man instal path patches (included upstream)
- enabling python integration

* Fri Oct 05 2007 Douglas E. Warner <silfreed@silfreed.net> 0.9.0-2
- enabling build for PPC64 (bug#247152)

* Wed Sep 26 2007 Douglas E. Warner <silfreed@silfreed.net> 0.9.0-1
- update to 0.9.0
- remove settings-include-workdir.patch
- updated man-install-share.patch to man-install-share-0.9.0.patch
- updated lib64-suffix.patch to lib64-suffix-0.9.0.patch
- enabled python to support msexport tool
- added Requires: grass to grass subpackage

* Tue Aug 28 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-13
- bump for expat 2.0 rebuild bug#195888

* Thu Aug 02 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-12
- updated License from GPL to GPLv2+

* Tue Jul 10 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-11
- allowing docs to be installed by qgis so they can be referenced by internal
  help system (bug#241403)
- updated lib64 patch (bug#247549) to try to get plugins found on x86_64

* Thu Jul 05 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-10
- updated lib64 patch for core and grass libraries

* Thu Jul 05 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-9
- updated lib64 patch

* Thu Jul 05 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-8
- adding ExcludeArch: ppc64 for bug#247152 (lrelease segfault)

* Thu Jul 05 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-7
- adding patch for lib64 support through lib_suffix

* Thu Jun 28 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-6
- fixed date of changelog entry for 0.8.1-5 from Wed Jun 27 2007 to
  Thu Jun 28 2007
- linking icon to included png instead of packaging it again

* Thu Jun 28 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-5
- adding comment on why grass is required in addition to grass-devel for BR
- fixing typo

* Wed Jun 27 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-4
- adding contributors to doc
- adding desktop file and icon

* Mon Jun 25 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-3
- updating detection of grass libraries to not use RPM call
- disabling building of -devel package due to shared libraries not being
  versioned and having no other packages that compile against qgis
  (see bug #241403)
- removing chmod of test_export.py due to lack of python requirement
- removing msexport and share/python directory due to removal of python

* Fri Jun 22 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-2
- added BuildRequires: cmake
- updated build to use cmake macro and make verbose

* Mon Jun 19 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-1
- updating version
- removed BuildRequires: python-devel due to lack of PyQt4 bindings
- updated build for use of cmake instead of autotools
- added patch for setting WORKDIR in settings.pro file
- added patch for fixing install path of man pages
- updated library names

* Tue May 29 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.0-6
- adding BuildRequires bison, flex

* Tue May 29 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.0-5
- fixing more directory owernship (themes, themes-default)
- fixing qt4 hardcoded lib path
- removing Requires ldconfig
- adding BuildRequires sqlite-devel
- adding patch for supporting python 2.5 in configure script

* Sat May 26 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.0-4
- moving all BuildRequires to main section
- dropping use of makeinstall macro
- making sure directories are owned by this package
- removing *.a and *.la files
- disabled stripping of libraries and binaries to allow debuginfo package
  to be built
- fixing macros in changelog
- removing executable bits on source files

* Wed May 16 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.0-3
- fixing Requires statements for sub-packages

* Tue May 15 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.0-2
- added devel dependancy on qgis
- moved qgis-config to devel package
- moving doc directory
- removed zero-length NEWS doc
- added postin/postun ldconfig calls
- split packages up to reduce package size and split out dependancies
  grass, theme-nkids

* Mon May 14 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.0-1
- Initial RPM release.

