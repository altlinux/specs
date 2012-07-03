%global __strip %_mingw32_strip
%global __objdump %_mingw32_objdump

Name: mingw32-dbus
Version: 1.4.6
Release: alt1
Summary: MinGW Windows port of D-Bus

License: GPLv2+ or AFL
Group: Development/Other
Url: http://www.freedesktop.org/wiki/Software/dbus

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dbus.freedesktop.org/releases/dbus/dbus-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-mingw32

BuildRequires: mingw32-filesystem >= 33
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw32-glib2
BuildRequires: mingw32-expat
BuildRequires: libtool, automake, autoconf

Requires: pkgconfig

# Upstream patch: sysdeps-win needs _dbus_path_is_absolute
Patch: dbus-1.4.6-path-is-absolute.patch

%description
D-BUS is a system for sending messages between applications. It is
used both for the system wide message bus service, and as a
per-user-login-session messaging facility.

%package static
Summary: Static version of MinGW Windows port of DBus library
Requires: %name = %version-%release
Group: Development/Other

%description static
D-BUS is a system for sending messages between applications. It is
used both for the system wide message bus service, and as a
per-user-login-session messaging facility.

Static version of MinGW Windows port of DBus library

%prep
%setup -n dbus-%version
%patch0 -p1

%build
%_mingw32_configure --disable-static
%make_build

%install
%makeinstall_std

# Remove manpages because they duplicate what's in the
# Fedora native package already.
rm -r %buildroot%_mingw32_mandir/man1

# The init.d script is unneeded for Win32 environments so it can be dropped
rm -r %buildroot%_mingw32_sysconfdir/rc.d/init.d/messagebus

%files
%doc COPYING
%_mingw32_bindir/dbus-daemon.exe
%_mingw32_bindir/dbus-launch.exe
%_mingw32_bindir/dbus-monitor.exe
%_mingw32_bindir/dbus-send.exe
%_mingw32_bindir/libdbus-1-3.dll
%_mingw32_libdir/libdbus-1.dll.a
%_mingw32_libdir/libdbus-1.la
%_mingw32_libdir/pkgconfig/dbus-1.pc
%_mingw32_sysconfdir/dbus-1/
%_mingw32_includedir/dbus-1.0/
%_mingw32_libdir/dbus-1.0/

%if 0
%files static
%_mingw32_libdir/libdbus-1.a
%endif

%changelog
* Fri Jun 17 2011 Vitaly Lipatov <lav@altlinux.ru> 1.4.6-alt1
- initial build for ALT Linux Sisyphus

* Mon Mar 28 2011 Ivan Romanov <drizt@land.ru> - 1.4.6-1
- New upstream version
- Removed clean stage
- Added dbus-1.4.6-path-is-absolute.patch patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-0.2.20101008git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 8 2010 Ivan Romanov <drizt@land.ru> - 1.4.1-0.1.20101008git
- Updated to 1.4.1 version from git
- windbus is now part of freedesktop dbus
- Removed mingw32-dbus-c++ package (c++ bindings it's not part of dbus)
- Removed mingw32-dbus-1.2.4-20081031-mingw32.patch
- Removed unusual dependencies
- Removed init.d script
- Changed define tags on the top to global tags
- Added static subpackage with static library
- Added debuginfo

* Fri Feb 6 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.4-0.3.20081031svn
- Include license.

* Tue Jan 13 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.4-0.2.20081031svn
- Requires pkgconfig.

* Mon Nov 3 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.4-0.1.20081031svn
- Initial RPM release.
