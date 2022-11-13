%define _unpackaged_files_terminate_build 1

Name: chromiumos-platform
Version: 0.0.0.0.git847ed920
Release: alt1

Summary: CrOS platform daemons & projects

Group: Graphical desktop/Other
License: BSD
URL: https://chromium.googlesource.com/chromiumos/platform2

BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: wayland-devel
BuildRequires: pkgconfig(libevdev)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-composite)
BuildRequires: pkgconfig(xcb-shape)
BuildRequires: pkgconfig(xcb-xfixes)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(gmock)

Source: %name-%version.tar

%description
This package builds various CrOS platform subproject from the platform2
monorepo.
At the moment, the following subprojects are packaged:
* vm_tools/sommelier.

%prep
%setup

%build
%define __sourcedir vm_tools/sommelier
%meson
%meson_build

%install
%define __sourcedir vm_tools/sommelier
%meson_install
# FIXME: patch this executable()'s install argument?
rm %buildroot%_bindir/sommelier_test

%check
%meson_test

%package -n sommelier
Summary: a nested wayland compositor for CrOS
Group: Graphical desktop/Other

%description -n sommelier
Sommelier is an implementation of a Wayland compositor that delegates
compositing to a "host" compositor. Sommelier includes a set of features that
allows it to run inside a tight jail or virtual machine.

Sommelier can run as service or as a wrapper around the execution of a program.
As a service, called the parent sommelier, it spawns new processes as needed to
service clients.

%files -n sommelier
%_bindir/sommelier

%changelog
* Sun Nov 13 2022 Arseny Maslennikov <arseny@altlinux.org> 0.0.0.0.git847ed920-alt1
- Initial build for ALT Sisyphus.
