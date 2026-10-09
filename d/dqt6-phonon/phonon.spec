%def_disable zeitgeist
%def_enable settings
%define _DK6link %_DK6lib

Name: dqt6-phonon
Version: 4.12.0
Release: alt0.dde.1
%DK6init altplace

Group: Graphical desktop/KDE
Summary: KDE Multimedia Framework
Url: http://phonon.kde.org/
License: LGPL-2.0-or-later

# Conflicts: dqt5-phonon-settings

#Source: ftp://ftp.kde.org/pub/kde/stable/%name/%version/%name-%version.tar.bz2
Source: %name-%version.tar

BuildRequires(pre): dqt6-base-devel rpm-build-dkf6
BuildRequires: dqt6-tools-devel dqt6-declarative-devel dqt6-5compat-devel
BuildRequires: libdqt6-designer vulkan-headers
BuildRequires: libEGL-devel libGL-devel
BuildRequires: cmake deepin-extra-cmake-modules
BuildRequires: glib2-devel libpulseaudio-devel
%if_enabled zeitgeist
BuildRequires: libqzeitgeist-devel
%endif

# find libraries
%add_findprov_lib_path %_DK6lib

%description
Phonon is the KDE Multimedia Framework

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: dqt6-base-common
%description common
%name common package

%package -n libphonon4dqt6experimental
Group: System/Libraries
Summary: Phonon library
Requires: %name-common
%description -n libphonon4dqt6experimental
Phonon library.

%package -n libphonon4dqt6
Group: System/Libraries
Summary: Phonon library
Requires: %name-common
%description -n libphonon4dqt6
Phonon library.

%package devel
Group: Development/KDE and QT
Summary: Header files and documentation for compiling Phonon applications
Requires: %name-common
%description devel
This package includes the header files you will need to compile applications
with Phonon.


%prep
%setup


%build
%add_optflags %optflags_shared
# -UPIE -U__PIE__
%DK6cmake \
    -DCMAKE_INSTALL_INCLUDEDIR:PATH=%_dqt6_headerdir \
    -DLOCALE_INSTALL_DIR:PATH=%_DK6i18n \
    -DPLUGIN_INSTALL_DIR:PATH=%_DK6archdata \
    -DPHONON_INSTALL_QT_COMPAT_HEADERS:BOOL=ON \
    -DPHONON_INSTALL_QT_EXTENSIONS_INTO_SYSTEM_QT:BOOL=ON \
    -DPHONON_BUILD_EXPERIMENTAL:BOOL=ON \
    -DPHONON_BUILD_QT5:BOOL=OFF \
    -DPHONON_BUILD_QT6:BOOL=ON \
    -DPHONON_BUILD_DESIGNER_PLUGIN:BOOL=ON \
    -DPHONON_BUILD_SETTINGS:BOOL=ON \
    -DPHONON_NO_CAPTURE:BOOL=OFF \
    #
%DK6make

%install
%DK6install
mkdir -p %buildroot/%_dqt6_plugindir/phonon4qt6_backend

%DK6find_qtlang --all-name libphonon_qt

%if_enabled settings
%files
%_DK6bin/phononsettings
%endif

%files common -f libphonon_qt.lang

%files -n libphonon4dqt6experimental
%_DK6lib/libphonon4qt6experimental.so.*

%files -n libphonon4dqt6
%dir %_DK6plug/phonon4qt6_backend/
%_DK6lib/libphonon4qt6.so.*

%files devel
%_dqt6_headerdir/phonon4qt6
%_DK6link/libphonon4qt6.so
%_DK6link/libphonon4qt6experimental.so
%_DK6lib/cmake/phonon4qt6/
%_DK6plug/designer/phonon4qt6widgets.so
%_DK6lib/pkgconfig/phonon4qt6.pc

%changelog
* Fri Oct 09 2026 Leontiy Volodin <lvol@altlinux.org> 4.12.0-alt0.dde.1
- fork for independent deepin buildings

* Thu May 02 2024 Sergey V Turchin <zerg@altlinux.org> 4.12.0-alt1
- initial build
