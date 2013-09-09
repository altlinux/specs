Name: dbus-test-runner
Version: 12.10.2daily13.02.26
Release: alt2

Summary: Run tests under a new DBus session
Group: Development/Tools
License: GPLv3
URL: https://launchpad.net/dbus-test-runner

Source0: https://launchpad.net/ubuntu/+archive/primary/+files/dbus-test-runner_%{version}.orig.tar.gz

Patch0: dbus-test-runner-12.10.2daily13.02.26-alt-bustle.patch

Packager: Igor Zubkov <icesik@altlinux.org>

BuildRequires: glib2-devel intltool libdbus-glib-devel
BuildRequires: libgio-devel

# for tests
BuildRequires: dbus

Requires: bustle

Requires: libdbustest = %version-%release

%description
A simple little executable for running a couple of programs under a new DBus
session.

%package -n libdbustest
Summary: Shared library for running programs under a new DBus session
Group: System/Libraries

%description -n libdbustest
This package contains a shared library for running programs under a new DBus
session.

%package -n libdbustest-devel
Summary: Development files for libdbustest
Group: Development/C

Requires: libdbustest = %{version}-%{release}

%description -n libdbustest-devel
This package contains the development files for the dbustest library.

%prep
%setup -q
%patch0 -p1
autoreconf -fisv

%build
%configure \
  --disable-static
%make_build

%check
make check || exit 1

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/dbus-test-runner
%dir %_libexecdir/dbus-test-runner/
%_libexecdir/dbus-test-runner/dbus-test-watchdog
%dir %_datadir/dbus-test-runner/
%_datadir/dbus-test-runner/dbus-test-bustle-handler
%_datadir/dbus-test-runner/session.conf

%files -n libdbustest
%_libdir/libdbustest.so.*

%files -n libdbustest-devel
%_includedir/libdbustest-1/
%_libdir/libdbustest.so
%_pkgconfigdir/dbustest-1.pc

%changelog
* Mon Sep 09 2013 Igor Zubkov <icesik@altlinux.org> 12.10.2daily13.02.26-alt2
- Fix for new bustle

* Tue Sep 03 2013 Igor Zubkov <icesik@altlinux.org> 12.10.2daily13.02.26-alt1
- build for Sisyphus

* Fri May 03 2013 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 12.10.2daily13.02.26-1
- Initial release
- Version 12.10.2daily13.02.26
