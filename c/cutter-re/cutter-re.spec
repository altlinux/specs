%define _unpackaged_files_terminate_build 1
%global gitname cutter
%define plugindir %_libdir/%gitname/plugins

Name: cutter-re
Version: 2.5.0
Release: alt1

Summary: GUI for Rizin reverse engineering framework
License: LGPL-3.0-only and GPL-3.0-only
Group: Development/Tools
Url: https://cutter.re
VCS: https://github.com/rizinorg/cutter

# Source-url: https://github.com/rizinorg/%gitname/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %gitname-production-%version.tar
Patch1: alt-fix-namespace-conflict-with-openssl.patch

BuildRequires(pre): rpm-macros-qt6-webengine
BuildRequires: kf6-syntax-highlighting-devel
BuildRequires: qt6-5compat-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-tools-devel
BuildRequires: rizin-devel
%ifarch %qt6_qtwebengine_arches
BuildRequires: qt6-webengine-devel
%endif

%description
Cutter is a Qt and C++ GUI for Rizin. Its goal is making an advanced,
customizable and FOSS reverse-engineering platform while keeping the
user experience at mind. Cutter is created by reverse engineers for
reverse engineers.

%package devel
Summary: Development files for the cutter-re package
Group: Development/Tools
Requires: %name = %EVR

%description devel
Development files for the cutter-re package. See cutter-re package for
more information.

%prep
%setup
%setup -D -T -a1
%patch1 -p1

mkdir -p src/translations
%__cp -rf %gitname-translations/* src/translations/

%build
%cmake \
    -DCUTTER_USE_BUNDLED_RIZIN=OFF \
    -DCUTTER_ENABLE_GRAPHVIZ=OFF \
    -DCUTTER_EXTRA_PLUGIN_DIRS=%plugindir \
    #
%cmake_build

%install
%cmake_install
mv %buildroot%_bindir/cutter %buildroot%_bindir/%name

# rename cutter to cutter-re in the desktop file
sed -i -e 's/%gitname/%name/g' \
    -e 's/^\(Categories=.*\)$/\1Debugger;Viewer;DataVisualization;ComputerScience;/' \
    %buildroot%_desktopdir/re.rizin.cutter.desktop

# rename cutter svg icon to cutter-re
mv %buildroot%_datadir/icons/hicolor/scalable/apps/{%gitname,%name}.svg
sed -i 's/bin\/%gitname/bin\/%name/g' %buildroot%_libdir/cmake/Cutter/CutterTargets-*.cmake

%__install -d %buildroot%plugindir/native

%find_lang --with-qt --all-name %name

%files -f %name.lang
%doc README.md
%_bindir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/scalable/apps/*.svg
%_datadir/metainfo/*.xml
%dir %plugindir
%dir %plugindir/native

%files devel
%_includedir/cutter
%_libdir/cmake/Cutter/*.cmake
%dir %_libdir/cmake/Cutter

%changelog
* Wed Jun 24 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 2.5.0-alt1
- new version

* Wed Mar 04 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 2.4.1-alt2
- add additional categories to the desktop file

* Mon Jun 16 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 2.4.1-alt1
- new version

* Mon Apr 01 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 2.3.4-alt1
- Initial build for ALT Linux
