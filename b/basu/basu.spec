Name: basu
Version: 0.2.0
Release: alt1
License: LGPL-2.1
Summary: The sd-bus library, extracted from systemd
URL: https://github.com/emersion/basu
Group: System/Libraries

Source: %name-%version.tar

Patch0: basu-disable-test-bus-creds.patch

%define soversion 0
%define soname %name%soversion

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

BuildRequires: cmake meson
BuildRequires: gperf
BuildRequires: pkgconfig(audit)
BuildRequires: pkgconfig(libcap)

# for tests
BuildRequires: dbus

%description
Some projects rely on the sd-bus library for DBus support. However not all
systems have systemd or elogind installed. This library provides just sd-bus
(and the busctl utility).

%package -n lib%soname
Summary: %summary
Group: System/Libraries
Provides: lib%name = %version-%release

%description -n lib%soname
Some projects rely on the sd-bus library for DBus support. However not all
systems have systemd or elogind installed. This library provides just sd-bus
(and the busctl utility).

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%soname = %version-%release

%description -n lib%name-devel
This package provides development files for lib%name library.

%prep
%setup
%autopatch -p1

if ! grep -qs '^soversion[[:space:]]*=[[:space:]]*%soversion[[:space:]]*$' meson.build; then
	echo >&2 "Outdated %%soversion value in spec"
	exit 1
fi

%build
%meson
%meson_build

%install
%meson_install

%check
dbus-run-session -- %meson_test

%files
%_bindir/basuctl

%files -n lib%soname
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/basu
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%changelog
* Tue Apr 27 2021 Alexey Gladkov <legion@altlinux.ru> 0.2.0-alt1
- Initial build.
