#
# spec file for package libdecor
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.altlinux.org/
#

Name: libdecor
Version: 0.1.1
Release: alt1

Summary: Wayland client side decoration library
License: MIT
Group: System/Libraries

Url: https://gitlab.gnome.org/jadahl/libdecor
Source: %name-%version.tar

BuildRequires: meson
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(xkbcommon)

%description
A library that can help Wayland clients draw window decorations for them.
It aims to provide multiple backends that implements the decoration drawing.

%package -n libdecor-0
Summary: Library for client-side Wayland decorations
Group: System/Libraries

%description -n libdecor-0
A client-side decorations library for Wayland client.

%package devel
Summary: Development files for libdecor
Group: Development/C

%description devel
Libraries and header files for developing applications that target libdecor.

%prep
%setup

%build
%meson -Ddemo=false
%meson_build

%install
%meson_install

%files -n libdecor-0
%doc LICENSE README.md
%_libdir/libdecor/
%_libdir/libdecor-0.so.0*

%files devel
%_includedir/libdecor-0/
%_libdir/libdecor-0.so
%_libdir/pkgconfig/libdecor-0.pc

%changelog
* Mon May 08 2023 Michael Shigorin <mike@altlinux.org> 0.1.1-alt1
- built for ALT Linux (based on openSUSE spec)
