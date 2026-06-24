%define _unpackaged_files_terminate_build 1
%define qt_ver 6.5.0
%define ecm_ver 5.240.0
# Shared library ABI version (== CALAMARES_SOVERSION, i.e. major.minor).
# Bump when the soname of libcalamares/libcalamaresui changes.
%define sover 3.4

Name: calamares
Version: 3.4.2
Release: alt1

Summary: Distribution-independent installer framework
License: GPL-3.0-or-later
Group: System/Base
Url:  https://calamares.io
VCS:  https://codeberg.org/Calamares/calamares

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

%K6init no_altplace appdata man

# libcalamares is an in-process pybind11 module exported by the
# calamares binary itself, not a separate Python package.
%filter_from_requires /^python3(libcalamares.*)/d
# initramfs-tools is a Debian/Ubuntu package; in ALT we use make-initrd.
# The initramfscfg module's hook scripts source this file but we don't
# need the module on ALT installs.
%filter_from_requires /\/usr\/share\/initramfs-tools\/hook-functions/d

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: qt6-base-devel
BuildRequires: qt6-tools-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-declarative-devel
BuildRequires: libpolkitqt6-qt6-devel
BuildRequires: libyaml-cpp-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kwidgetsaddons-devel
BuildRequires: kf6-kservice-devel
BuildRequires: kf6-kparts-devel
BuildRequires: kf6-kpackage-devel
BuildRequires: kf6-kcrash-devel
BuildRequires: libappstream-qt6-devel
BuildRequires: libkpmcore-devel
BuildRequires: libpwquality-devel
BuildRequires: libparted-devel
BuildRequires: python3-devel
BuildRequires: pybind11-devel

%description
Calamares is a distribution-independent system installer with an
advanced partitioning feature, supporting both manual and automated
partitioning operations. It is designed to be customizable by
distribution maintainers without patching, via third-party branding
and external modules support.

%package -n libcalamares%sover
Summary: Calamares core library
Group: System/Libraries

%description -n libcalamares%sover
The non-UI core library of Calamares: job and queue infrastructure,
GlobalStorage, the module system and partitioning, locale, network
and package helpers.

%package -n libcalamaresui%sover
Summary: Calamares UI library
Group: System/Libraries

%description -n libcalamaresui%sover
The UI library of Calamares: Branding, ViewManager, view pages and
widgets used by the installer shell and view modules.

%package -n libcalamares-devel
Summary: Development files for Calamares
Group: Development/C++
Requires: libcalamares%sover = %EVR
Requires: libcalamaresui%sover = %EVR

%description -n libcalamares-devel
Development headers and CMake config files for building Calamares
modules and embedding libcalamares and libcalamaresui.

%prep
%setup
%autopatch -p1

%build
%K6build \
    -DWITH_QT6:BOOL=ON \
    -DWITH_PYBIND11:BOOL=ON \
    -DBUILD_APPSTREAM:BOOL=ON \
    -DBUILD_CRASH_REPORTING:BOOL=ON \
    #

%install
%K6install
install -Dm0644 io.calamares.calamares.appdata.xml \
    %buildroot%_datadir/metainfo/io.calamares.calamares.appdata.xml
%find_lang %name --all-name

%files -f %name.lang
%doc README.md CONTRIBUTING.md CHANGES-3.4
%_K6bin/calamares
%_K6lib/calamares/
%_datadir/calamares/
%_K6xdgapp/calamares.desktop
%_iconsdir/hicolor/scalable/apps/calamares.svg
%_datadir/metainfo/io.calamares.calamares.appdata.xml
%_datadir/polkit-1/actions/io.calamares.calamares.policy
%_man8dir/calamares.8*

%files -n libcalamares%sover
%_K6lib/libcalamares.so.%{sover}*

%files -n libcalamaresui%sover
%_K6lib/libcalamaresui.so.%{sover}*

%files -n libcalamares-devel
%_includedir/libcalamares/
%_K6link/libcalamares.so
%_K6link/libcalamaresui.so
%_K6lib/cmake/Calamares/

%changelog
* Wed Jun 24 2026 Ajrat Makhmutov <rauty@altlinux.org> 3.4.2-alt1
- Initial build for Sisyphus.
