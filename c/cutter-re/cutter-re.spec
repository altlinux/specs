%define _unpackaged_files_terminate_build 1
%global gitname cutter

Name: cutter-re
Version: 2.3.4
Release: alt1

Summary: GUI for Rizin reverse engineering framework
License: GPL-3.0-only
Group: Development/Tools
Url: https://cutter.re
VCS: https://github.com/rizinorg/cutter

# Source-url: https://github.com/rizinorg/%gitname/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %gitname-postsubmodules-%version.tar

BuildRequires(pre): rpm-macros-qt5-webengine
BuildRequires: cmake
BuildRequires: rizin-devel >= 0.6.1
BuildRequires: kf5-syntax-highlighting-devel
BuildRequires: libgraphviz-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-tools-devel
%ifarch %qt5_qtwebengine_arches
BuildRequires: qt5-webengine-devel
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
mkdir -p src/translations
%__cp -rf dependencies/%gitname-translations/* src/translations

%build
%cmake -DCUTTER_USE_BUNDLED_RIZIN=OFF
%cmake_build

%install
%cmake_install
mv %buildroot%_bindir/cutter %buildroot%_bindir/%name

# rename cutter to cutter-re in the desktop file
sed -i 's/%gitname/%name/g' %buildroot%_desktopdir/re.rizin.cutter.desktop

# rename cutter svg icon to cutter-re
mv %buildroot%_datadir/icons/hicolor/scalable/apps/{%gitname,%name}.svg
sed -i 's/bin\/%gitname/bin\/%name/g' %buildroot%_libdir/cmake/Cutter/CutterTargets-*.cmake

%files
%doc COPYING README.md src/img/icons/Iconic-LICENSE
%_bindir/%name
%_desktopdir/*.desktop
%_datadir/rizin/%gitname/translations/*.qm
%_iconsdir/hicolor/scalable/apps/*.svg

%files devel
%_includedir/cutter
%_libdir/cmake/Cutter/*.cmake
%dir %_libdir/cmake/Cutter

%changelog
* Mon Apr 01 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 2.3.4-alt1
- Initial build for ALT Linux
