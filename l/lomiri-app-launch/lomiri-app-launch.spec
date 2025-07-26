%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define _libexecdir %_prefix/libexec

%def_with check

Name: lomiri-app-launch
Version: 0.1.12
Release: alt1

Summary: User space daemon for launching applications
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri-app-launch

Source: %name-%version.tar

# sync with version 0.1.12-1 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-systemd

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: /usr/bin/gdbus-codegen
BuildRequires: /usr/bin/lttng-gen-tp
BuildRequires: /usr/bin/g-ir-scanner
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(zeitgeist-2.0)
BuildRequires: pkgconfig(click-0.4)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(dbustest-1)
BuildRequires: pkgconfig(liblomiri-api)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(properties-cpp)

%if_with check
BuildRequires: ctest
BuildRequires: dbus
BuildRequires: /usr/bin/dbus-test-runner
BuildRequires: ayatana-cmake-modules
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(gmock)
BuildRequires: python3(dbusmock)
%endif

Requires: zeitgeist

%description
Application launching system and associated utilities that is used to
launch applications in a standard and confined way.

This package provides the Lomiri App Launch user space daemon.

%package -n lomiri-app-launch-tools
Summary: Tools for working wtih launched applications
Group: Graphical desktop/Other
Requires: lomiri-app-launch = %{version}-%{release}

%description -n lomiri-app-launch-tools
Application launching system and associated utilities that is used to
launch applications in a standard and confined way.

This package provides tools for working with Lomiri App Launch.

%package -n liblomiri-app-launch0
Summary: library for sending requests to Lomiri App Launch
Group: System/Libraries

%description -n liblomiri-app-launch0
Application launching system and associated utilities that is used to
launch applications in a standard and confined way.

This package contains shared libraries to be used by applications.

%package -n liblomiri-app-launch-devel
Summary: library for sending requests to the Lomiri App Launch
Group: Development/Other
Requires: liblomiri-app-launch0 = %{version}-%{release}

%description -n liblomiri-app-launch-devel
Application launching system and associated utilities that is used to
launch applications in a standard and confined way.

This package contains files that are needed to build applications.

%package -n lomiri-app-launch-gir
Summary: typelib file for liblomiri-app-launch
Group: System/Libraries
Requires: liblomiri-app-launch0 = %{version}-%{release}

%description -n lomiri-app-launch-gir
Application launching system and associated utilities that is used to
launch applications in a standard and confined way.

Interface for starting apps and getting info on them.

This package can be used by other packages using the GIRepository format
to generate dynamic bindings for liblomiri-app-launch0.

%prep
%setup
%patch -p1

%build
%cmake \
       -DLOMIRI_APP_LAUNCH_ARCH=%_arch \
       -DENABLE_COVERAGE=OFF \
%if_without check
       -DENABLE_TESTS=OFF \
%endif
       -DENABLE_MIRCLIENT=OFF
%cmake_build

%install
%cmake_install

%post
%systemd_user_post lal-application-end.target

%preun
%systemd_user_preun lal-application-end.target

%postun
%systemd_user_postun lal-application-end.target

%check
%ctest -j1 -VV

%files
%doc AUTHORS ChangeLog COPYING NEWS
%_userunitdir/lal-application-end.target
%dir %_libexecdir/%name
%_libexecdir/%name/*

%files -n lomiri-app-launch-tools
%_bindir/lomiri-*

%files -n liblomiri-app-launch0
%_libdir/liblomiri-app-launch.so.0
%_libdir/liblomiri-app-launch.so.0.0.0

%files -n liblomiri-app-launch-devel
%_libdir/liblomiri-app-launch.so
%dir %_includedir/liblomiri-app-launch-0
%_includedir/liblomiri-app-launch-0/*
%_pkgconfigdir/lomiri-app-launch-0.pc
%_girdir/LomiriAppLaunch-0.gir

%files -n lomiri-app-launch-gir
%_typelibdir/LomiriAppLaunch-0.typelib

%changelog
* Sat Jul 12 2025 Nikolay Strelkov <snk@altlinux.org> 0.1.12-alt1
- Initial build for Sisyphus
