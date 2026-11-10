%define _unpackaged_files_terminate_build 1
%define optflags_lto -ffat-lto-objects
%global qt_module qtlanguageserver

Name:    qt6-languageserver
Version: 6.11.2
Release: alt1

Summary: Qt6 - Language Server module
License: GPL-3.0-only
Group:   System/Libraries

URL: https://www.qt.io

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6
BuildRequires: cmake ninja-build glibc-devel qt6-base-devel
BuildRequires(pre): qt6-tools

%description
The Qt Language Server component provides an implementation of the Language
Server protocol.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: qt6-base-devel
%description devel
%summary.

%prep
%setup -n %qt_module-everywhere-src-%version

%build
%Q6build \
    -DQT_GENERATE_SBOM:BOOL=OFF \
    #
 
%install
%Q6install_qt

# relax depends on plugins files
for f in %buildroot/%_libdir/cmake/Qt?*/Qt*Targets.cmake ; do
    sed -i '/message.*FATAL_ERROR.*target.* references the file/s|FATAL_ERROR|WARNING|' $f
done
 
%files devel
%_qt6_headerdir/Qt*/
%_qt6_libdir/libQt*.prl
%_qt6_libdatadir/libQt*.prl
%_qt6_libdir/lib*.a
%_qt6_libdatadir/lib*.a
%_qt6_libdir/cmake/Qt*/
%_qt6_libdir/qt6/metatypes/qt6*.json
%_qt6_libdir/qt6/modules/*.json
%_qt6_archdatadir/mkspecs/modules/*.pri

%changelog
* Mon Nov 09 2026 Andrey Alekseev <parovoz@altlinux.org> 6.11.2-alt1
- initial build for sisyphus
