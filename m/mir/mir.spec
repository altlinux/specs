%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%def_with check

%define commonlib_sover         12
%define mircore_sover            2
%define mirplatform_sover       34
%define lomiri_sover             9
%define miral_sover              7
%define mirserver_sover         67
%define mirwayland_sover         6
%define mirserverplatform_sover 23
%define mirevdev_sover          10

Name: mir
Version: 2.28.0
Release: alt1

Summary: The Mir compositor
License: (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
Group: Graphical desktop/Other
Url: https://github.com/canonical/mir

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: boost-program_options-devel
BuildRequires: pkgconfig(wayland-eglstream)
BuildRequires: libglm-devel
BuildRequires: pkgconfig(libapparmor)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(lttng-ust)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(libxml++-2.6)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(yaml-cpp)
BuildRequires: python3(PIL)
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(libevdev)
BuildRequires: pkgconfig(umockdev-1.0)
BuildRequires: pkgconfig(wlcs)
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: doxygen
BuildRequires: /usr/bin/Xwayland
BuildRequires: pkgconfig(libdisplay-info)
BuildRequires: /usr/bin/dot

%if_with check
BuildRequires: ctest
BuildRequires: python3(dbusmock)
BuildRequires: /proc
BuildRequires: /dev/pts
%endif

%description
Mir is a Wayland display server toolkit for Linux systems, with a focus
on efficiency, robust operation, and a well-defined driver model.

%package devel
Summary: Development files for Mir
Group: Development/Other
Requires: %{name}-test-libs-static = %{version}-%{release}
Requires: libmircommon%{commonlib_sover} = %{version}-%{release}
Requires: libmirevdev%{mirevdev_sover} = %{version}-%{release}
Requires: libmiroil%{lomiri_sover} = %{version}-%{release}
Requires: libmirserver%{mirserver_sover} = %{version}-%{release}
Requires: libmirserverplatform%{mirserverplatform_sover} = %{version}-%{release}

%description devel
This package provides the development files to create compositors built
on Mir

%package private-devel
Summary: Development files for Mir exposing private internals
Group: Development/Other
Requires: %{name}-devel = %{version}-%{release}

%description private-devel
This package provides extra development files to create compositors
built on Mir that need acces to private internal interfaces

%package -n libmircommon%{commonlib_sover}
Summary: Mir server library
Group: System/Libraries
License: LGPL-2.1-only OR LGPL-3.0-only

%description -n libmircommon%{commonlib_sover}
Component library of the Mir compositing stack

%package -n libmircore%{mircore_sover}
Summary: Mir core library
Group: System/Libraries
License: LGPL-2.1-only OR LGPL-3.0-only

%description -n libmircore%{mircore_sover}
Component library of the Mir compositing stack

%package -n libmirplatform%{mirplatform_sover}
Summary: Mir platform library
Group: System/Libraries
License: LGPL-2.1-only OR LGPL-3.0-only

%description -n libmirplatform%{mirplatform_sover}
Component library of the Mir compositing stack

%package -n libmiroil%{lomiri_sover}
Summary: Lomiri compatibility libraries for Mir
Group: System/Libraries
License: LGPL-2.1-only OR LGPL-3.0-only

%description -n libmiroil%{lomiri_sover}
This package provides the libraries for Lomiri to use Mir as a Wayland
compositor

%package -n libmiral%{miral_sover}
Summary: Mir Abstraction Layer library
Group: System/Libraries
License: LGPL-2.1-only OR LGPL-3.0-only

%description -n libmiral%{miral_sover}
Component library of the Mir compositing stack

%package -n libmirserver%{mirserver_sover}
Summary: Mir server library
Group: System/Libraries
License: GPL-2.0-only OR GPL-3.0-only
Requires: libmirevdev%{mirevdev_sover} = %{version}-%{release}
Requires: libmirserverplatform%{mirserverplatform_sover} = %{version}-%{release}

%description -n libmirserver%{mirserver_sover}
Component library of the Mir compositing stack

%package -n libmirwayland%{mirwayland_sover}
Summary: Mir Wayland library
Group: System/Libraries
License: LGPL-2.1-only OR LGPL-3.0-only

%description -n libmirwayland%{mirwayland_sover}
Component library of the Mir compositing stack

%package -n libmirserverplatform%{mirserverplatform_sover}
Summary: Mir Server Platform Library
Group: System/Libraries
License: LGPL-2.1-only OR LGPL-3.0-only

%description -n libmirserverplatform%{mirserverplatform_sover}
Component library of the Mir server platform

%package -n libmirevdev%{mirevdev_sover}
Summary: Evdev support for Mir
Group: System/Libraries
License: LGPL-2.1-only OR LGPL-3.0-only

%description -n libmirevdev%{mirevdev_sover}
evdev support library for the Mir server platform

%package test-tools
Summary: Testing tools for Mir
Group: Development/Other
License: GPL-2.0-only OR GPL-3.0-only
Requires: libmirserver%{mirserver_sover} = %{version}-%{release}
Requires: wlcs

%description test-tools
This package provides tools for testing Mir

%package demos
Summary: Demonstration applications using Mir
Group: Documentation
License: GPL-2.0-only OR GPL-3.0-only
Requires: inotify-tools
Requires: libmirserver%{mirserver_sover} = %{version}-%{release}

%description demos
This package provides applications for demonstrating the capabilities of
the Mir display server

%package test-libs-static
Summary: Testing framework library for Mir
License: GPL-2.0-only OR GPL-3.0-only
Group: Development/Other
Requires: %{name}-devel = %{version}-%{release}

%description test-libs-static
This package provides the static library for building Mir unit and
integration tests

%prep
%setup

%build
%cmake \
       -W no-dev \
       -DMIR_PLATFORM='atomic-kms;gbm-kms;x11;wayland;eglstream-kms' \
       -DMIR_FATAL_COMPILE_WARNINGS=OFF \
       -DCMAKE_INSTALL_LIBEXECDIR="%_libdir/%name" \
       -DMIR_USE_PRECOMPILED_HEADERS=OFF \
       -DMIR_BUILD_INTERPROCESS_TESTS=OFF \
       -DMIR_RUN_WLCS_TESTS=OFF \
%ifarch riscv64
       -DMIR_RUN_MIRAL_TESTS=OFF \
       -DMIR_RUN_WINDOW_MANAGEMENT_TESTS=OFF \
%endif
%ifnarch aarch64
       -DMIR_RUN_ACCEPTANCE_TESTS=OFF \
%endif
       -DMIR_ENABLE_RUST=OFF

%cmake_build

%install
%cmake_install

%check
export XDG_RUNTIME_DIR="%buildroot"
%ctest

%files devel
%doc COPYING.*
%_bindir/mir_wayland_generator
%_libdir/libmir*.so
%_libdir/pkgconfig/mir*.pc
%exclude %_libdir/pkgconfig/mir*internal.pc
%_includedir/mir*/
%exclude %_includedir/mir*internal/

%files private-devel
%doc COPYING.*
%_libdir/pkgconfig/mir*internal.pc
%_includedir/mir*internal/

%files -n libmircommon%{commonlib_sover}
%doc COPYING.LGPL* README.md
%dir %_libdir/mir
%_libdir/libmircommon.so.%{commonlib_sover}

%files -n libmircore%{mircore_sover}
%_libdir/libmircore.so.%{mircore_sover}

%files -n libmirplatform%{mirplatform_sover}
%_libdir/libmirplatform.so.%{mirplatform_sover}

%files -n libmiroil%{lomiri_sover}
%_libdir/libmiroil.so.%{lomiri_sover}

%files -n libmiral%{miral_sover}
%_libdir/libmiral.so.%{miral_sover}

%files -n libmirserver%{mirserver_sover}
%doc COPYING.GPL* README.md
%_libdir/libmirserver.so.%{mirserver_sover}

%files -n libmirwayland%{mirwayland_sover}
%_libdir/libmirwayland.so.%{mirwayland_sover}

%files -n libmirserverplatform%{mirserverplatform_sover}
%doc COPYING.GPL* README.md
%dir %_libdir/mir/server-platform
%_libdir/mir/server-platform/graphics-eglstream-kms.so.%{mirserverplatform_sover}
%_libdir/mir/server-platform/graphics-gbm-kms.so.%{mirserverplatform_sover}
%_libdir/mir/server-platform/graphics-wayland.so.%{mirserverplatform_sover}
%_libdir/mir/server-platform/renderer-egl-generic.so.%{mirserverplatform_sover}
%_libdir/mir/server-platform/server-virtual.so.%{mirserverplatform_sover}
%_libdir/mir/server-platform/server-x11.so.%{mirserverplatform_sover}
%_libdir/mir/server-platform/graphics-atomic-kms.so.%{mirserverplatform_sover}

%files -n libmirevdev%{mirevdev_sover}
%doc COPYING.GPL*
%doc README.md
%_libdir/mir/server-platform/input-evdev.so.%{mirevdev_sover}

%files test-tools
%doc COPYING.GPL*
%dir %_libdir/mir
%dir %_libdir/mir/tools
%dir %_libdir/mir/server-platform
%_bindir/mir-*test*
%_bindir/mir_*test*
%_libdir/mir/tools/libmirserverlttng.so
%_libdir/mir/miral_wlcs_integration.so
%_libdir/mir/server-platform/graphics-dummy.so.%{mirserverplatform_sover}
%_libdir/mir/server-platform/input-stub.so.%{mirevdev_sover}
%dir %_datadir/mir
%_datadir/mir/expected_wlcs_failures.list

%files test-libs-static
%doc COPYING.GPL*
%_libdir/libmir-test-assist.a
%_libdir/libmir-test-assist-internal.a

%files demos
%doc COPYING.GPL* README.md
%_bindir/mir_demo_*
%_bindir/mir-x11-kiosk*
%_bindir/miral-*
%_datadir/applications/miral-shell.desktop
%_datadir/icons/hicolor/scalable/apps/spiral-logo.svg

%changelog
* Sun Jun 28 2026 Nikolay Strelkov <snk@altlinux.org> 2.28.0-alt1
- New version 2.28.0.
- Enabled tests.

* Mon Jul 14 2025 Nikolay Strelkov <snk@altlinux.org> 2.21.1-alt1
- Initial build for Sisyphus
