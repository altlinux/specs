# BEGIN SourceDeps(oneline):
BuildRequires: cmake gcc-c++ libdbus-devel libtqt4-devel perl(DB_File.pm) perl(Fcntl.pm) perl(Shell.pm)
# END SourceDeps(oneline)
BuildRequires(pre):	rpm-macros-suse-compat
BuildRequires(pre):	rpm-macros-cmake
BuildRequires(pre): rpm-macros-trinity
#
# spec file for package dbus-1-tqt (version R14)
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

Name: trinity-dbus-1-tqt
Epoch: %tde_epoch
Version: 0.9
Release: alt1_14.0.4_1
Summary: Dbus bindings for the Trinity Qt [TQt] interface
Group: System/Libraries
Url: http://www.trinitydesktop.org/

License: GPL-2.0+

#Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name-%tde_version%{?preversion:~%preversion}.tar.gz
Source44: import.info

# BuildRequires:	libtqt3-mt-devel >= 3.5.0
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

This package provides bindings for the Trinity Qt TQt interface.

See the dbus description for more information about D-BUS in general.

###########

%package -n %libdbus-1-tqt0
Summary: Dbus bindings for the Trinity Qt [TQt] interface
Group: System/Libraries
Provides: libdbus-1-tqt0 = %{?epoch:%epoch:}%version-%release

Obsoletes: trinity-dbus-1-tqt < %{?epoch:%epoch:}%version-%release
Provides: trinity-dbus-1-tqt = %{?epoch:%epoch:}%version-%release

%description -n %libdbus-1-tqt0
D-BUS is a message bus, used for sending messages between applications.
Conceptually, it fits somewhere in between raw sockets and CORBA in
terms of complexity.

This package provides bindings for the Trinity Qt TQt interface.

See the dbus description for more information about D-BUS in general.

%files -n %libdbus-1-tqt0
%_libdir/libdbus-1-tqt.so.0
%_libdir/libdbus-1-tqt.so.0.0.0

##########

%package -n %libdbus-1-tqt-devel
Summary: Dbus bindings for the Trinity Qt [TQt] interface (Development Files)
Group: Development/C
Provides: libdbus-1-tqt-devel = %{?epoch:%epoch:}%version-%release
# Requires:		%libdbus-1-tqt0 = %{?epoch:%epoch:}%version-%release

Obsoletes: trinity-dbus-1-tqt-devel < %{?epoch:%epoch:}%version-%release
Provides: trinity-dbus-1-tqt-devel = %{?epoch:%epoch:}%version-%release

# Requires:	dbus-1-devel

%description -n %libdbus-1-tqt-devel
D-BUS is a message bus, used for sending messages between applications.
Conceptually, it fits somewhere in between raw sockets and CORBA in
terms of complexity.

This package provides bindings for the Trinity Qt TQt interface.

See the dbus description for more information about D-BUS in general.

%files -n %libdbus-1-tqt-devel
%_bindir/dbusxml2qt3
%_includedir/*.h
%_libdir/libdbus-1-tqt.so
%_pkgconfigdir/*.pc

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
  -DBIN_INSTALL_DIR=%_bindir \
  -DINCLUDE_INSTALL_DIR=%_includedir \
  -DLIB_INSTALL_DIR=%_libdir \
  ..

%make_build || %__make

%install
rm -rf %{?buildroot}
%make_install install DESTDIR=%{?buildroot} -C build

%changelog
* Tue Dec 06 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:0.9-alt1_14.0.4_1
- converted for ALT Linux by srpmconvert tools

* Tue Aug 09 2016 Hihin Ruslan <ruslandh@altlinux.ru> 0.9-alt1
- initial build for ALT Linux Sisyphus

* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 2:0.9-1
- Initial release for TDE R14.0.0
