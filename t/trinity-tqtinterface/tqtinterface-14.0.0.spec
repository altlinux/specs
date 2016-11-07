# BEGIN SourceDeps(oneline):
BuildRequires: libtqt3-devel perl(DB_File.pm) perl(Fcntl.pm) perl(Shell.pm) libtqt3-apps-devel
# END SourceDeps(oneline)
BuildRequires(pre): rpm-macros-trinity
%define suse_version 1320
BuildRequires(pre):	rpm-macros-suse-compat
BuildRequires(pre):	rpm-macros-cmake
#
# spec file for package tqtinterface (version R14)
#
# Copyright (c) 2014 Trinity Desktop Environment
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.0.3
%endif
%define tde_pkg tqtinterface
%define cmake_modules_dir %_datadir/cmake/Modules

%define libtqt4 libtqt4

Name: trinity-tqtinterface
Epoch: %tde_epoch
Version: 4.2.0
Release: alt3_14.0.3_2
Summary: The Trinity Qt Interface Libraries
Group: Graphical desktop/Other
Url: http://www.trinitydesktop.org/

License: GPL-2.0+

#Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name-%tde_version%{?preversion:~%preversion}.tar

# BuildRequires:	libtqt3-mt-devel >= 3.5.0
# BuildRequires:	tqt3-dev-tools >= 3.5.0

# BuildRequires:	trinity-cmake-macros

# BuildRequires:	cmake >= 2.8
# BuildRequires:	gcc-c++
# BuildRequires:	pkgconfig

# UUID support
%define uuid_devel libuuid-devel
%if 0%{?rhel} == 5
%define uuid_devel e2fsprogs-devel
%endif
%{?uuid_devel:BuildRequires: %uuid_devel}

# PTHREAD support
# BuildRequires:	pth-devel

# MESA support
# BuildRequires: Mesa-libGL-devel
# BuildRequires: Mesa-libGLU-devel

# X11 libraries
%if 0%{?rhel} == 4
# BuildRequires:	xorg-x11-devel
%endif
# BuildRequires:	libXi-devel
%if 0%{?suse_version} == 1140
# BuildRequires:	libXi6-devel
%endif
Source44: import.info
BuildRequires: cmake gcc-c++ libtqt3-devel tqt3-dev-tools

%description
The Trinity Qt Interface is a library that abstracts Qt from Trinity.
This allows the Trinity code to rapidly port from one version of Qt to another.
This is primarily accomplished by defining old functions in terms of new functions,
although some code has been added for useful functions that are no longer part of Qt.

##########

%package -n %libtqt4
Group: Graphical desktop/Other
Summary: The Trinity Qt Interface Libraries
Provides: libtqt4 = %{?epoch:%epoch:}%version-%release

# Requires:	libtqt3-mt >= 3.5.0

# Requires:		trinity-cmake-macros

Obsoletes: trinity-tqtinterface < %{?epoch:%epoch:}%version-%release
Provides: trinity-tqtinterface = %{?epoch:%epoch:}%version-%release

%description -n %libtqt4
The Trinity Qt Interface is a library that abstracts Qt from Trinity.
This allows the Trinity code to rapidly port from one version of Qt to another.
This is primarily accomplished by defining old functions in terms of new functions,
although some code has been added for useful functions that are no longer part of Qt.

%files -n %libtqt4
%_libdir/libtqt.so.4
%_libdir/libtqt.so.4.2.0

%package -n %libtqt4-devel
Group: Development/C
Summary: The Trinity Qt Interface Libraries (Development Files)
Provides: libtqt4-devel = %{?epoch:%epoch:}%version-%release

# Requires:	%libtqt4 = %{?epoch:%epoch:}%version-%release
# Requires:	libtqt3-mt-devel >= 3.5.0
# Requires:	tqt3-dev-tools >= 3.5.0

# Requires:		trinity-cmake-macros

Obsoletes: trinity-tqtinterface-devel < %{?epoch:%epoch:}%version-%release
Provides: trinity-tqtinterface-devel = %{?epoch:%epoch:}%version-%release

%description -n %libtqt4-devel
The Trinity Qt Interface is a library that abstracts Qt from Trinity.
This allows the Trinity code to rapidly port from one version of Qt to another.
This is primarily accomplished by defining old functions in terms of new functions,
although some code has been added for useful functions that are no longer part of Qt.

%files -n %libtqt4-devel
%_bindir/convert_qt_tqt1
%_bindir/convert_qt_tqt2
%_bindir/convert_qt_tqt3
%_bindir/dcopidl-tqt
%_bindir/dcopidl2cpp-tqt
%_bindir/dcopidlng-tqt
%_bindir/mcopidl-tqt
%_bindir/moc-tqt
%_bindir/tmoc
%_bindir/tqt-replace
%_bindir/tqt-replace-stream
%_bindir/uic-tqt
%_includedir/tqt/
%_libdir/libtqt.so
%_pkgconfigdir/tqt.pc
%_pkgconfigdir/tqtqui.pc
%cmake_modules_dir/*.cmake

##########

%prep
%setup -n %name-%tde_version%{?preversion:~%preversion}

%build
unset QTDIR QTINC QTLIB

%suse_cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_SKIP_RPATH=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DQTDIR="%_datadir/tqt3" \
  -DQT_INCLUDE_DIR="%_includedir/tqt3" \
  -DQT_LIBRARY_DIR="%_libdir" \
  \
  -DCMAKE_INSTALL_PREFIX="%prefix" \
  -DPKGCONFIG_INSTALL_DIR="%_pkgconfigdir" \
  -DINCLUDE_INSTALL_DIR=%_includedir/tqt \
  -DLIB_INSTALL_DIR=%_libdir \
  -DBIN_INSTALL_DIR=%_bindir \
  \
  -DCMAKE_LIBRARY_PATH="%_libdir" \
  -DCMAKE_INCLUDE_PATH="%_includedir" \
  \
  -DWITH_QT3="ON" \
  -DBUILD_ALL="ON" \
  -DUSE_QT3="ON" \
  ..

%make_build || %__make

%install
rm -rf "%{?buildroot}"
%make_install install DESTDIR="%{?buildroot}" -C build

# Install 'cmake' modules for development use
mkdir -p "%{?buildroot}%cmake_modules_dir"
for i in cmake/modules/*.cmake; do
  install -m 644 "$i" "%{?buildroot}%cmake_modules_dir"
done

%changelog
* Mon Nov 07 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:4.2.0-alt3_14.0.3_2
- Rebuild with new macros

* Sun Nov 06 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:4.2.0-alt3_14.0.3_1
- converted for ALT Linux by srpmconvert tools
- convert from rpmcs

* Sun Nov 06 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:4.2.0-alt2.1_14.0.3_1
- converted for ALT Linux by srpmconvert tools

* Fri Nov 04 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:4.2.0-alt2.1
- Etalon test Version

* Fri Nov 04 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:4.2.0-alt2
- Developer Version

* Fri Nov 04 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:4.2.0-alt1_14.0.3_1
- converted for ALT Linux by srpmconvert tools

* Sun Aug 07 2016 Hihin Ruslan <ruslandh@altlinux.ru> 4.2.0-alt1
- initial build for ALT Linux Sisyphus

* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 4.2.0-1
- Initial release for TDE 14.0.0

