# BEGIN SourceDeps(oneline):
BuildRequires: cmake gcc-c++ libdbus-devel libtqt4-devel perl(DB_File.pm) perl(Fcntl.pm) perl(Shell.pm)
# END SourceDeps(oneline)
BuildRequires(pre):	rpm-macros-suse-compat
BuildRequires(pre):	rpm-macros-cmake
BuildRequires(pre): rpm-macros-trinity
#
# spec file for package dbus-tqt (version R14)
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

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.0.4
%endif

%define libdbus libdbus

Name: trinity-dbus-tqt
Epoch: %tde_epoch
Version: 0.63
Release: alt1_14.0.4_1
Summary: Simple inter-process messaging system
Group: System/Libraries
Url: http://www.trinitydesktop.org/

License: GPL-2.0+

#Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name-%tde_version%{?preversion:~%preversion}.tar.gz
Source44: import.info

# BuildRequires:	libtqt4-devel >= %tde_epoch:4.2.0

# BuildRequires:	cmake >= 2.8
# BuildRequires:	gcc-c++
# BuildRequires:	pkgconfig

# DBUS support
# BuildRequires:	dbus-1-devel

%description
D-BUS is a message bus, used for sending messages between applications.
Conceptually, it fits somewhere in between raw sockets and CORBA in
terms of complexity.

This package provides the TQt-based shared library for applications using the
Qt interface to D-BUS.

See the dbus description for more information about D-BUS in general.

##########

%package -n %libdbus-tqt-1-0
Summary: Simple inter-process messaging system (TQt-based shared library)
Group: System/Libraries
Provides: libdbus-tqt-1-0 = %{?epoch:%epoch:}%version-%release

Obsoletes: trinity-dbus-tqt < %{?epoch:%epoch:}%version-%release
Provides: trinity-dbus-tqt = %{?epoch:%epoch:}%version-%release

%description -n %libdbus-tqt-1-0
D-BUS is a message bus, used for sending messages between applications.
Conceptually, it fits somewhere in between raw sockets and CORBA in
terms of complexity.

This package provides the TQt-based shared library for applications using the
Qt interface to D-BUS.

See the dbus description for more information about D-BUS in general.

%files -n %libdbus-tqt-1-0
%_libdir/libdbus-tqt-1.so.0
%_libdir/libdbus-tqt-1.so.0.0.0

##########

%package -n %libdbus-tqt-1-devel
Summary: Simple inter-process messaging system (TQt interface)
Group: Development/C
Provides: libdbus-tqt-1-devel = %{?epoch:%epoch:}%version-%release
# Requires:		%libdbus-tqt-1-0 = %{?epoch:%epoch:}%version-%release

Obsoletes: trinity-dbus-tqt-devel < %{?epoch:%epoch:}%version-%release
Provides: trinity-dbus-tqt-devel = %{?epoch:%epoch:}%version-%release

# Requires:	dbus-1-devel

%description -n %libdbus-tqt-1-devel
D-BUS is a message bus, used for sending messages between applications.
Conceptually, it fits somewhere in between raw sockets and CORBA in
terms of complexity.

This package provides the TQt-based shared library for applications using the
Qt interface to D-BUS.

See the dbus description for more information about D-BUS in general.

%files -n %libdbus-tqt-1-devel
%_includedir/dbus-1.0/*
%_libdir/libdbus-tqt-1.so
%_pkgconfigdir/dbus-tqt.pc

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
  -DINCLUDE_INSTALL_DIR=%_includedir \
  -DLIB_INSTALL_DIR=%_libdir \
  ..

%make_build

%install
rm -rf %{?buildroot}
%make_install install DESTDIR=%{?buildroot} -C build

%changelog
* Tue Dec 06 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:0.63-alt1_14.0.4_1
- converted for ALT Linux by srpmconvert tools

