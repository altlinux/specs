Name: entt-devel
Version: 3.13.2
Release: alt1
License: MIT

Summary: A header-only, tiny and easy to use entity-component system

Group: Development/C++

Url: https://github.com/skypjack/entt

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: gcc-c++ cmake

%description
EnTT is a header-only, tiny and easy to use library for game
programmingand much more written in modern C++.
Among others, it's used in Minecraft by Mojang,
the ArcGIS Runtime SDKs by Esri and the amazing Ragdoll.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_includedir/entt/
%_libdir/EnTT/cmake/
%_pkgconfigdir/entt.pc

%changelog
* Sun Aug 05 2024 Kirill Unitsaev <fiersik@altlinux.org> 3.13.2-alt1
- Initial build
