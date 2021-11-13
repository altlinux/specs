Name: qbs
Version: 1.20.1
Release: alt1

Summary: Qt Build Suite
License: LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later) AND (LGPL-2.1-only OR LGPL-3.0-only WITH Qt-LGPL-exception-1.1) AND GPL-3.0-only WITH Qt-GPL-exception-1.0
Group: Development/Tools

Url: http://qt-project.org/wiki/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://download.qt.io/official_releases/%name/%version/%name-src-%version.tar.gz
Source: %name-src-%version.tar

BuildRequires: qt5-script-devel
BuildRequires: rpm-build-python3

%add_python3_path %_datadir/%name/python/biplist
%add_python3_path %_datadir/%name/python/ds_store
%add_python3_path %_datadir/%name/python/mac_alias

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

%package examples
Summary: Examples for the usage of %name
Group: Development/Tools
BuildArch: noarch

%description examples
Provides examples for using the %name

%prep
%setup -n %name-src-%version

%build
export LD_LIBRARY_PATH=`pwd`/lib
%qmake_qt5 -r %name.pro \
	QBS_INSTALL_PREFIX=%_prefix \
	QBS_LIB_INSTALL_DIR=%_libdir \
	QBS_LIBEXEC_INSTALL_DIR=%_libexecdir/%name \
	QBS_PLUGINS_INSTALL_DIR=%_libdir \
	CONFIG+=disable_rpath \
	CONFIG+=nostrip \
	QMAKE_LFLAGS="-Wl,--as-needed"

%make_build

%install
%install_qt5_base
%__rm %buildroot%_libdir/libqbscore.prl
%__rm %buildroot%_libexecdir/%name/dmgbuild

%files
%doc README.md
%_bindir/%name
%_bindir/%name-config
%_bindir/%name-config-ui
%_bindir/%name-create-project
%_bindir/%name-setup-android
%_bindir/%name-setup-qt
%_bindir/%name-setup-toolchains
%_datadir/%name
%exclude %_datadir/%name/examples
%_libdir/%name/plugins/*.so
%_libdir/lib%{name}core.so.*
%_libexecdir/%name
%_man1dir/%name.1*

%files devel
%_includedir/%name
%_libdir/lib%{name}core.so

%files examples
%_datadir/%name/examples

%changelog
* Sat Nov 13 2021 Nazarov Denis <nenderus@altlinux.org> 1.20.1-alt1
- Version 1.20.1

* Tue Jun 18 2019 Andrey Cherepanov <cas@altlinux.org> 1.13.1-alt1
- New version.

* Tue Jul 12 2016 Nazarov Denis <nenderus@altlinux.org> 1.5.2-alt1
- Version 1.5.2

* Sat Jan 16 2016 Nazarov Denis <nenderus@altlinux.org> 1.4.4-alt1
- Version 1.4.4

* Mon Nov 09 2015 Nazarov Denis <nenderus@altlinux.org> 1.4.3-alt1
- Version 1.4.3

* Wed Jul 29 2015 Nazarov Denis <nenderus@altlinux.org> 1.4.1-alt1
- Version 1.4.1

* Tue Jun 23 2015 Nazarov Denis <nenderus@altlinux.org> 1.4.0-alt1
- Version 1.4.0

* Wed Oct 15 2014 Nazarov Denis <nenderus@altlinux.org> 1.3.2-alt1
- Version 1.3.2

* Thu Sep 18 2014 Nazarov Denis <nenderus@altlinux.org> 1.3.1-alt1
- Version 1.3.1

* Sun Jun 01 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt0.M70T.1
- Build for branch t7

* Fri May 30 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt1
- Version 1.2.1

* Thu May 08 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.0-alt0.M70T.1
- Build for branch t7

* Wed May 07 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.0-alt1
- Version 1.2.0

* Sun Feb 16 2014 Nazarov Denis <nenderus@altlinux.org> 1.1.2-alt0.M70T.1
- Build for branch t7

* Fri Feb 14 2014 Nazarov Denis <nenderus@altlinux.org> 1.1.2-alt1
- Version 1.1.2

* Thu Jan 16 2014 Nazarov Denis <nenderus@altlinux.org> 1.1.1-alt1.M70T.1
- Build for branch t7

* Thu Jan 16 2014 Nazarov Denis <nenderus@altlinux.org> 1.1.1-alt2
- Fix arch for examples subpackage

* Thu Jan 16 2014 Nazarov Denis <nenderus@altlinux.org> 1.1.1-alt1
- Initial release for ALT Linux
