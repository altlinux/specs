%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: scidavis
Version: 2.9.2
Release: alt1

Summary: Application for Scientific Data Analysis and Visualization
License: GPL-2.0-only
Group: Sciences/Mathematics
Url: https://scidavis.sourceforge.net/
Vcs: https://github.com/SciDAVis/scidavis

Source: %name-%version.tar
Source1: submodules-%name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): cmake

BuildRequires: gcc-c++
BuildRequires: qt5-tools-devel
BuildRequires: python3-devel
BuildRequires: python3-module-PyQt5-sip
BuildRequires: python3-module-sip6
BuildRequires: python3-module-PyQt-builder
BuildRequires: python3-module-PyQt5
BuildRequires: python3-module-PyQt5-devel
BuildRequires: /usr/bin/lrelease-qt5

BuildRequires: pkgconfig(Qt5)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(gsl)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(muparser)
BuildRequires: pkgconfig(glu)

%if_with check
BuildRequires: ctest
BuildRequires: pkgconfig(gtest)
BuildRequires: /usr/bin/xvfb-run
BuildRequires: python3-module-numpy
%endif

%description
SciDAVis stands for Scientific Data Analysis and Visualization.
It is a free cross-platform program for two- and three-dimensional
graphical presentation of data sets and for data analysis.

The plots can be produced from data sets stored in tables, in matrix or
from analytical functions.

The documentation is available at
https://highperformancecoder.github.io/scidavis-handbook/ .

%prep
%setup -a1
%patch -p1

sed -i 's|VERSION 2.3.0|VERSION %{version}|' CMakeLists.txt

sed -i 's|pythonconfig.path = "$$INSTALLBASE/../etc"|pythonconfig.path = "$$INSTALLBASE/..%{python3_sitelibdir}/scidavis"|g' config.pri
sed -i 's|pythonutils.path = "$$INSTALLBASE/share/scidavis"|pythonutils.path = "$$INSTALLBASE/..%{python3_sitelibdir}/scidavis"|g' config.pri
sed -i 's|set(PYTHON_SCRIPTDIR etc|set(PYTHON_SCRIPTDIR %{python3_sitelibdir}/scidavis|g' scidavis/CMakeLists.txt
sed -i 's|FILES scidavisrc.py ${CMAKE_CURRENT_BINARY_DIR}/$<CONFIG>/scidavisrc.pyc DESTINATION|FILES scidavisrc.py DESTINATION|g' scidavis/CMakeLists.txt
sed -i 's|FILES scidavisrc.py ${CMAKE_CURRENT_BINARY_DIR}/scidavisrc.pyc DESTINATION|FILES scidavisrc.py DESTINATION|g' scidavis/CMakeLists.txt
sed -i 's|FILES scidavisUtil.py DESTINATION share/scidavis|FILES scidavisUtil.py DESTINATION ${PYTHON_SCRIPTDIR}|g' scidavis/CMakeLists.txt
sed -i 's|PYTHON_CONFIG_PATH="${CMAKE_INSTALL_PREFIX}/etc"|PYTHON_CONFIG_PATH="%{python3_sitelibdir}/scidavis"|g' libscidavis/CMakeLists.txt
sed -i 's|PYTHON_UTIL_PATH="${CMAKE_INSTALL_PREFIX}/share/scidavis"|PYTHON_UTIL_PATH="%{python3_sitelibdir}/scidavis"|g' libscidavis/CMakeLists.txt

%build
lrelease-qt5 scidavis.pro
%cmake \
       -DPython3_EXECUTABLE=%__python3 \
       -DSEARCH_FOR_UPDATES=off \
       -DDOWNLOAD_LINKS=off \
       -DSCRIPTING_MUPARSER=on \
       -DORIGIN_IMPORT=on \
       -DSCRIPTING_PYTHON=on \
%if_with check
       -DBUILD_TESTS=on
%else
       -DBUILD_TESTS=off
%endif

%cmake_build

%install
%cmake_install

%find_lang %name --with-qt

%check
export PYTHONPATH=%buildroot%python3_sitelibdir/scidavis
xvfb-run -a %ctest -j1 -VV -E '^(python_Establishing_contact|python_integration_with_python-crash|python_linear_and_polynomial_fits)'

%files -f %{name}.lang
%doc ChangeLog.md gpl.txt LICENSE license.rtf README.md
%_bindir/scidavis
%dir %_libdir/scidavis
%dir %_libdir/scidavis/plugins
%_libdir/scidavis/plugins/libexp_saturation.so
%_libdir/scidavis/plugins/libexplin.so
%_libdir/scidavis/plugins/libfitRational0.so
%_libdir/scidavis/plugins/libfitRational1.so
%_libdir/scidavis/plugins/libplanck_wavelength.so
%_desktopdir/scidavis.desktop
%exclude %_datadir/doc/scidavis/ChangeLog.md
%exclude %_datadir/doc/scidavis/README.md
%exclude %_datadir/doc/scidavis/gpl.txt
%exclude %_datadir/doc/scidavis/license.rtf
%_iconsdir/hicolor/*/apps/scidavis.png
%_iconsdir/locolor/*/apps/scidavis.png
%_iconsdir/hicolor/scalable/apps/scidavis.svg
%_man1dir/scidavis.1.*
%_datadir/metainfo/scidavis.appdata.xml
%_datadir/mime/packages/scidavis.xml
%exclude %_datadir/mimelnk/application/x-sciprj.desktop
%dir %python3_sitelibdir/scidavis
%python3_sitelibdir/scidavis/*

%changelog
* Wed Mar 04 2026 Nikolay Strelkov <snk@altlinux.org> 2.9.2-alt1
- Initial build for Sisyphus
