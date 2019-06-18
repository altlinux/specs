Name: qbs
Version: 1.13.1
Release: alt1

Summary: Qt Build Suite
License: LGPLv2.1 with exceptions
Group: Development/Tools

Url: http://qt-project.org/wiki/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: %name-%version.tar

BuildRequires: qt5-script-devel

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
%setup

%build
export LD_LIBRARY_PATH=`pwd`/lib
%qmake_qt5 -r %name.pro \
	QBS_INSTALL_PREFIX=%_prefix \
	QBS_LIB_INSTALL_DIR=%_libdir \
	QBS_PLUGINS_INSTALL_DIR=%_libdir \
	CONFIG+=disable_rpath \
	CONFIG+=nostrip \
	QMAKE_LFLAGS="-Wl,--as-needed"

%make_build

%install
make INSTALL_ROOT=%buildroot install
rm -f %buildroot%_libdir/libqbscore.prl
rm -rf %buildroot%_datadir/qbs/python/dmgbuild

%files
%doc LGPL_EXCEPTION.txt LICENSE.LGPLv3 LICENSE.LGPLv21 README
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
%_prefix/libexec/qbs
%_man1dir/%name.1*

%files devel
%_includedir/%name
%_libdir/lib%{name}core.so

%files examples
%_datadir/%name/examples

%changelog
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
