%define _name hal-flash

Name: lib%_name
Version: 0.2.0rc1
Release: alt1

Summary: HAL library for Flash plugin
Group: System/Libraries
License: GPLv2
Url: https://github.com/cshorler/hal-flash

# git://github.com/cshorler/hal-flash.git
Source: %_name-%version.tar

Conflicts: libhal
Requires: dbus
BuildRequires: libdbus-devel

%description
HAL is a hardware abstraction layer. HAL is no longer used on modern
Linux systems - with the advent of tools such as UDev and UDisks the
same and improved functionality is provided by other means.

The flash plugin currently requires libhal for playback of drm content.

This library provides a compatibility layer and minimal libhal
implementation for that purpose.

This library does NOT provide a full HAL interface or daemon.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/libhal.so.*
%exclude %_libdir/*.so
%doc README

%changelog
* Fri Jan 31 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.0rc1-alt1
- first build for sisyphus

