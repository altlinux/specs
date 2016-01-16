Name: qbs
Version: 1.4.4
Release: alt1

Summary: Qt Build Suite
License: LGPLv2.1 with exceptions
Group: Development/Tools

Url: http://qt-project.org/wiki/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: http://download.qt-project.org/official_releases/%name/%version/%name-src-%version.tar.gz

BuildRequires: gcc-c++
BuildRequires: glibc-devel-static
BuildRequires: qt5-script-devel
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

%package examples
Summary: Examples for the usage of %name
Group: Development/Tools
BuildArch: noarch

%description examples
Provides examples for using the %name

%prep
%setup -n %name-src-%version

%build
%qmake_qt5 -r %name.pro \
	QBS_INSTALL_PREFIX=%_prefix \
	QBS_LIB_INSTALL_DIR=%_libdir \
	QBS_PLUGINS_INSTALL_DIR=%_libdir \
	CONFIG+=disable_rpath \
	CONFIG+=nostrip \
	QMAKE_LFLAGS="-Wl,--as-needed"

%make_build

%install
%__make INSTALL_ROOT=%buildroot install

%files
%doc LGPL_EXCEPTION.txt LICENSE.LGPLv3 LICENSE.LGPLv21 README
%_bindir/%name
%_bindir/%name-config
%_bindir/%name-config-ui
%_bindir/%name-qmltypes
%_bindir/%name-setup-android
%_bindir/%name-setup-qt
%_bindir/%name-setup-toolchains
%dir %_datadir/%name
%_datadir/%name/imports
%dir %_datadir/%name/modules
%_datadir/%name/modules
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/lib%{name}_cpp_scanner.so
%_libdir/%name/plugins/lib%{name}_qt_scanner.so
%_libdir/lib%{name}core.so.*
%_libdir/lib%{name}qtprofilesetup.so.*

%files devel
%_includedir/%name
%_libdir/lib%{name}core.so
%_libdir/lib%{name}qtprofilesetup.so

%files examples
%dir %_datadir/%name
%_datadir/%name/examples

%changelog
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
