%define soversion 1

Name:           sdbusplus
Version:        1.0.0
Release:        alt2.gitfe1ebd4

Summary:        C++ bindings for systemd dbus APIs

License:        Apache-2.0
Group:          Development/Other
URL:            https://www.openbmc.org
Vcs:            https://github.com/openbmc/sdbusplus.git

Source:         %name-%version.tar
Patch: 0001-boost-version-1.86-support.patch

BuildRequires(pre): meson
BuildRequires: gcc-c++ cmake
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(nlohmann_json)
BuildRequires: python3(inflection)
BuildRequires: python3(jsonschema)
BuildRequires: python3(mako)
BuildRequires: python3(setuptools)
BuildRequires: python3(yaml)
BuildRequires: boost-asio-devel

%description
%name contains two parts:
   1. A C++ library (lib%name) for interacting with D-Bus, built on top of the sd-bus library from systemd.
   2. A tool (sdbus++) to generate C++ bindings to simplify the development of D-Bus-based applications.

%package -n lib%name%soversion
Summary: C++ library bindings for systemd dbus APIs
Group: Development/C++

%description -n lib%name%soversion
A C++ library (lib%name) for interacting with D-Bus,
built on top of the sd-bus library from systemd.

%package -n lib%name-devel
Summary: lib%name C++ headers for systemd dbus APIs bindings
Group: Development/C++

%description -n lib%name-devel
A C++ headers (lib%name) for interacting with D-Bus,
built on top of the sd-bus library from systemd.

%package tools
Summary: Python3 tool for %name
Group: Development/Python3
BuildArch: noarch
Provides: sdbus++

%description tools
A Python3 tools for interacting with D-Bus,
built on top of the sd-bus library from systemd.

%prep
%setup
%autopatch -p1

%build
%meson -Dtests=disabled -Dexamples=disabled
%meson_build
pushd tools
%pyproject_build
popd

%install
%meson_install
pushd tools
%pyproject_install
popd

%files -n lib%name%soversion
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_libdir/lib%name.so
%_includedir/%name
%_pkgconfigdir/%name.pc

%files tools
%_bindir/sdbus++
%_bindir/sdbus++-gen-meson
%python3_sitelibdir_noarch/%name
%python3_sitelibdir_noarch/%name-1.0.dist-info

%changelog
* Tue Aug 26 2025 Ulysses Apokin <ulysses@altlinux.org> 1.0.0-alt2.gitfe1ebd4
- NMU: Downgraded to commit from revision list.

* Thu Apr 24 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus(thx alton@).
