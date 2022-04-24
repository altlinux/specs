# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: PrusaSlicer
Summary: G-code generator for 3D printers (RepRap, Makerbot, Ultimaker etc.)
Version: 2.4.1
Release: alt1
License: AGPL-3.0-only
Group: Engineering
Url: https://www.prusa3d.com/prusaslicer/

# Source-url: https://github.com/prusa3d/PrusaSlicer/archive/refs/tags/version_%version.tar.gz
Source: %name-%version.tar

ExcludeArch: %arm %ix86 ppc64le

Provides: prusa-slicer

BuildRequires: libblosc-devel
BuildRequires: cereal-devel
BuildRequires: cgal-devel >= 4.13.2
BuildRequires: cmake
BuildRequires: eigen3 >= 3

BuildRequires: gcc-c++
BuildRequires: libgtest >= 1.7
BuildRequires: ctest
BuildRequires: boost-devel
BuildRequires: boost-asio-devel
BuildRequires: boost-atomic-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-geometry-devel
BuildRequires: boost-iostreams-devel
BuildRequires: boost-locale-devel
BuildRequires: boost-log-devel
BuildRequires: boost-polygon-devel
BuildRequires: boost-regex-devel
BuildRequires: boost-system-devel
BuildRequires: boost-thread-devel
BuildRequires: libcurl-devel
BuildRequires: libexpat-devel
BuildRequires: libnlopt-devel
BuildRequires: openexr-devel
BuildRequires: openvdb-devel >= 5
BuildRequires: tbb-devel
BuildRequires: libwxGTK3.0-devel
BuildRequires: pkgconfig(libudev)
BuildRequires: libdbus-devel
BuildRequires: zlib-devel
BuildRequires: libpng-devel
BuildRequires: libgtk+3-devel
BuildRequires: libgmpxx-devel
BuildRequires: libglew-devel
#Requires:      noto-sans-fonts

%description
PrusaSlicer takes 3D models (STL, OBJ, AMF) and converts them into G-code
instructions for FFF printers or PNG layers for mSLA 3D printers. It's
compatible with any modern printer based on the RepRap toolchain, including
all those based on the Marlin, Prusa, Sprinter and Repetier firmware.
It also works with Mach3, LinuxCNC and Machinekit controllers.

%prep
%setup -n %name-%version
%autopatch -p1

# Fix the "UNKNOWN" in the displayed version string
sed -i 's/UNKNOWN/ALT/' version.inc

# Unbundle libraries
unbundle () {
    rm -rf src/$1
    sed -i "/add_subdirectory($1)/d" src/CMakeLists.txt
}

unbundle eigen
unbundle expat
unbundle glew

%build
# sse2 flags for 32-bit: see gh#prusa3d/PrusaSlicer#3781
%ifarch %ix86
  export CFLAGS="%optflags -mfpmath=sse -msse2"
  export CXXFLAGS="$CFLAGS"
%endif

# -DSLIC3R_FHS=1 - Enable FHS layout instead of installing things into the resources directory
# -DSLIC3R_WX_STABLE=1 - Allow use of wxGTK version 3.0 instead of 3.1.
%cmake \
  -DSLIC3R_FHS=1 \
  -DSLIC3R_GTK=3 \
  -DSLIC3R_WX_STABLE=1 \
  -DSLIC3R_BUILD_TESTS=1 \
  -DCMAKE_BUILD_TYPE=Release \
  -DOPENVDB_FIND_MODULE_PATH=%_libdir/cmake/OpenVDB \
  -DWITH_WERROR=OFF
%cmake_build

%install
%cmake_install

# remove stray font file
#rm -rf %buildroot%_datadir/%name/fonts

# fix path udev rules
mkdir -p %buildroot/lib
mv %buildroot/{usr/,}lib/udev

# install locales
rm -r resources/localization/wx_locale
rm -r resources/localization/ko_KR
for i in $(ls resources/localization/*/*.mo); do
	locale=$(echo "$i"| cut -f 3 -d /)
	mkdir -p %buildroot/%_datadir/locale/$locale/LC_MESSAGES
	install -m644 "$i" %buildroot/%_datadir/locale/$locale/LC_MESSAGES
done
rm -r %buildroot/%_datadir/%name/localization
%find_lang %name

%check
pushd %_cmake__builddir
ctest
popd

%files -f %name.lang
%_bindir/prusa-slicer
%_bindir/prusa-gcodeviewer
%_datadir/%name/
/lib/udev/rules.d/90-3dconnexion.rules
%_iconsdir/hicolor/*/apps/*.png
%_desktopdir/PrusaSlicer.desktop
%_desktopdir/PrusaGcodeviewer.desktop
%doc README.md doc/

%changelog
* Sun Apr 24 2022 Anton Midyukov <antohami@altlinux.org> 2.4.1-alt1
- initial build for ALT Sisyphus (Closes: 42501)
