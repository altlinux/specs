Name: qbs
Version: 1.1.1
Release: alt1

Summary: Qt Build Suite
License: LGPLv2.1 with exceptions
Group: Development/Tools

Url: http://qt-project.org/wiki/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: http://download.qt-project.org/official_releases/%name/%version/%name-%version.src.tar.gz
Patch0: %name-%version-alt-fix-lib-plugins.patch

BuildRequires: gcc-c++
BuildRequires: glibc-devel-static
BuildRequires: phonon-devel
BuildRequires: rpm-build-gir

%description
The Qt Build Suite (Qbs) is a tool that helps simplify the build process for
developing projects across multiple platforms. Qbs can be used for any software
project, whether it is written in Qt or not.

Qbs is an all-in-one tool that generates a build graph from a high-level
project description (like qmake or cmake) and additionally undertakes the task
of executing the commands in the low-level build graph (like make).

%package devel
Summary: Development files for %name
Group: Development/Tools
Requires: %name = %version-%release

%description devel
This package is required to build native/C++ extensions for %name

%package gui
Summary: UI support for configuring %name
Group: Development/Tools
Requires: %name = %version-%release

%description gui
Provides a UI based help program for configuring %name

%package cpp
Summary: C++ support for %name
Group: Development/Tools
Requires: %name = %version-%release

%description cpp
Provides C++ support for the %name

%package qt
Summary: Qt support for %name
Group: Development/Tools
Requires: %name = %version-%release
Requires: %name-cpp = %version-%release

%description qt
Provides Qt support for the %name

%package examples
Summary: Examples for the usage of %name
Group: Development/Tools

%description examples
Provides examples for using the %name

%prep
%setup -n %name-%version.src
%patch0 -p1

%build
%qmake_qt4 -r %name.pro \
	QBS_INSTALL_PREFIX=%_prefix \
	QBS_LIB_INSTALL_DIR=%_libdir \
	CONFIG+=disable_rpath \
	CONFIG+=nostrip \
	QMAKE_LFLAGS="-Wl,--as-needed"

%make_build

%install
%__make INSTALL_ROOT=%buildroot install

%__rm -rf %buildroot/%_datadir/%name/modules/ib

%files
%doc LICENSE.LGPL LGPL_EXCEPTION.txt README
%_bindir/%name
%_bindir/%name-config
%_bindir/%name-detect-toolchains
%_bindir/%name-qmltypes
%_datadir/%name/imports
%dir %_datadir/%name/modules
%_datadir/%name/modules/%name
%_datadir/%name/modules/utils.js
%dir %_libdir/%name/plugins
%_libdir/lib%{name}core.so.*

%files devel
%_includedir/%name
%_libdir/lib%{name}core.so

%files gui
%_bindir/%name-config-ui

%files cpp
%_datadir/%name/modules/cpp
%_libdir/%name/plugins/lib%{name}_cpp_scanner.so

%files qt
%_bindir/%name-setup-madde-platforms
%_bindir/%name-setup-qt
%_datadir/%name/modules/Qt/
%_libdir/%name/plugins/lib%{name}_qt_scanner.so

%files examples
%_datadir/%name/examples

%changelog
* Thu Jan 16 2014 Nazarov Denis <nenderus@altlinux.org> 1.1.1-alt1
- Initial release for ALT Linux
