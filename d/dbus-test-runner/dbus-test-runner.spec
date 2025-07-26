%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: dbus-test-runner
Version: 19.04.0
Release: alt1

Summary: Runs tests under a new DBus session
License: GPL-3.0
Group: Development/Tools
Url: https://salsa.debian.org/debian/dbus-test-runner

Source: %name-%version.tar

# sync with version 19.04.0-1.1 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires: intltool
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: /usr/bin/dbus-daemon

%filter_from_requires /^.usr.bin.bustle-dbus-monitor/d
%filter_from_requires /^.usr.bin.bustle-pcap/d

%description
A simple little executable for running a couple of programs under a
new DBus session.

Use this DBus tool for unit testing of code that accesses DBus at
runtime.

%package -n libdbustest1
Summary: Runs tests under a new DBus session (shared library)
Group: System/Libraries

%description -n libdbustest1
A simple little executable for running a couple of programs under a
new DBus session.

This package contains the shared libraries.

%package -n libdbustest1-devel
Summary: Runs tests under a new DBus session (development files)
Group: Development/C
Requires: libdbustest1 = %{version}-%{release}

%description -n libdbustest1-devel
A simple little executable for running a couple of programs under a
new DBus session.

This package contains files that are needed for development.

%prep
%setup
%patch -p1
%autoreconf

%build
%configure \
           --enable-static=no
%make_build

%install
%makeinstall_std

install -D -m 0644 debian/man/dbus-test-runner.1 -t "%{buildroot}%{_man1dir}/"

%check
%make_build check

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%_bindir/%name
%_man1dir/%{name}.1*

%files -n libdbustest1
%_libdir/libdbustest.so.1
%_libdir/libdbustest.so.1.0.0
%dir %_libexecdir/%name
%_libexecdir/%name/*
%dir %_datadir/%name
%_datadir/%name/*

%files -n libdbustest1-devel
%dir %_includedir/libdbustest-1/
%_includedir/libdbustest-1/*
%_libdir/libdbustest.so
%_libdir/pkgconfig/dbustest-1.pc

%changelog
* Sat Jul 12 2025 Nikolay Strelkov <snk@altlinux.org> 19.04.0-alt1
- Initial build for Sisyphus
