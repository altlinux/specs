%define _unpackaged_files_terminate_build 1

%def_with check

Name: engauge-digitizer
Version: 12.9.1
Release: alt1

Summary: Extracts data points from images of graphs
License: GPL-2.0-or-later
Group: Sciences/Mathematics
Url: https://github.com/akhuettel/engauge-digitizer

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-qt6

BuildRequires: qt6-tools-devel
BuildRequires: pkgconfig(libopenjp2)
BuildRequires: pkgconfig(poppler-qt6)
BuildRequires: pkgconfig(fftw3)

%if_with check
BuildRequires: /usr/bin/xvfb-run
%endif

%description
The Engauge Digitizer tool assists in interactively extracting numbers
from images of graphs. Conceptually, it is thus the opposite of a
graphing tool that converts data points to graphs. It provides assistance
in enhancing the image quality and matching the data points. Engauge
Digitizer is used by individuals such as grad students and researchers as
well as engineers and employees in large government and commercial
organizations for processing single files but also managing databases of
thousands of image files.

Features of Engauge Digitizer include:

* Automatic grid line removal;
* Automatic point and axis matching;
* Automatic curve tracing;
* Image processing for separating important details from background information;
* A wizard providing an interactive tutorial to explain the basic steps;
* Multiple coordinate systems in the same image can be digitized in advanced mode;
* Cubic spline interpolation between points gives more accurate curves with fewer points;
* Handling of cartesian, polar, linear and logarithmic graphs;
* Support for drag-and-drop and copy-and-paste;
* Context-sensitive help, user manual and tutorials explaining every feature;
* Preview windows to give immediate feedback while modifying settings;
* Automated line and point extraction to rapidly digitize data.

%prep
%setup
sed -i "/QMAKE_CXXFLAGS_WARN_ON/s/-O1//" engauge.pro
sed -i "s|qmake6|qmake-qt6|" help/build.bash
sed -i 's|^qhelpgenerator engauge.qhp|%_libdir/qt6/libexec/qhelpgenerator engauge.qhp engauge.qhcp|' help/build.bash
sed -i 's|"/translations"|"/../share/engauge-digitizer/translations"|' src/Translator/TranslatorContainer.cpp
sed -i "s/Categories=.*/Categories=Science;Math;DataVisualization;/" dev/engauge-digitizer.desktop

%build
export QT_SELECT=qt6
export ENGAUGE_RELEASE=1
export LC_ALL=C.UTF-8

lrelease-qt6 engauge.pro

export OPENJPEG_INCLUDE=$(pkg-config --variable includedir libopenjp2) export OPENJPEG_LIB=%_libdir
export POPPLER_INCLUDE=$(pkg-config --cflags-only-I poppler-qt6 | cut -d ' ' -f 1 | sed 's/^-I//')
export POPPLER_LIB=%_libdir

%qmake_qt6 engauge.pro \
           CONFIG+="jpeg2000 pdf log4cpp_null" \
           DEFINES+=HELPDIR=%_datadir/doc/%name-%version/help
%make_build

pushd help
bash ./build.bash
rm -vf build build.*
rm -vf .gitignore
popd
cp -v bin/documentation/engauge.qch help/
cp -v bin/documentation/engauge.qhc help/

%install
install -pDm755 bin/Engauge %buildroot%_bindir/engauge
install -pDm644 dev/engauge-digitizer.desktop %buildroot%_desktopdir/engauge-digitizer.desktop
install -pDm644 dev/gnome/engauge-digitizer.appdata.xml %buildroot%_datadir/metainfo/engauge-digitizer.appdata.xml
install -pDm644 src/img/engauge-digitizer.svg %buildroot%_iconsdir/hicolor/scalable/apps/engauge-digitizer.svg

mkdir -pv %buildroot%_datadir/%name-%version/img/
install -pm 644 src/img/* %buildroot%_datadir/%name-%version/img/

mkdir -pv %buildroot%_datadir/%name/translations/
install -p -m 0644 translations/*.qm %buildroot%_datadir/%name/translations/

%find_lang %name --all-name --with-qt

%check
pushd src
xvfb-run -a ./build_and_run_all_gui_tests
# popd

%files -f %{name}.lang
%doc README.md help samples
%_bindir/engauge
%_desktopdir/engauge-digitizer.desktop
%_datadir/metainfo/engauge-digitizer.appdata.xml
%_iconsdir/hicolor/scalable/apps/engauge-digitizer.svg
%dir %_datadir/%name-%version/
%dir %_datadir/%name-%version/img/
%_datadir/%name-%version/img/*

%changelog
* Sun Jul 05 2026 Nikolay Strelkov <snk@altlinux.org> 12.9.1-alt1
- Initial build for Sisyphus
