Name:           libdtkwm
Version:        2.0.12
Release:        alt1

Summary:        Deepin graphical user interface library

License:        GPLv3
Group:          System/Libraries
Url:            https://github.com/linuxdeepin/dtkwm

# Source0-url:   https://github.com/martyr-deepin/dtkwm/archive/refs/tags/%{version}.tar.gz
Source0:        %name-%version.tar

BuildRequires:  qt5-base-devel qt5-tools
BuildRequires:  libxcbutil-devel
BuildRequires:  dtk5-core-devel dtk5-common
BuildRequires:  qt5-x11extras-devel

%description
DtkWm is used to handle double screen for deepin desktop development.
This package contains the shared libraries.

%package devel
Summary:        Development package for %{name}
Group:          System/Libraries
Requires:       %name = %EVR

%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %name-%version

%build
%qmake_qt5 PREFIX=%_prefix LIB_INSTALL_DIR=%_libdir DTK_MODULE_NAME=dtkwm
%make_build

%install
%install_qt5_base

%files
%doc README.md
%_libdir/libdtkwm.so.5*

%files devel
%_includedir/libdtk-*/
%_qt5_archdatadir/mkspecs/modules/*.pri
%dir %_libdir/cmake/DtkWm/
%_libdir/cmake/DtkWm/DtkWmConfig.cmake
%_libdir/pkgconfig/dtkwm.pc
%_libdir/libdtkwm.so

%changelog
* Sun Aug 21 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 2.0.12-alt1
- Initial build in Sisyphus
