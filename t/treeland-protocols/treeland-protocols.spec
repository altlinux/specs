Name: treeland-protocols
Version: 0.4.5
Release: alt1

Summary: Wayland protocol extensions for treeland

License: Apache-2.0 or LGPL-3.0-only or GPL-3.0-only
Group: System/Configuration/Other
Url: https://github.com/linuxdeepin/treeland-protocols
Vcs: git://github.com/linuxdeepin/treeland-protocols.git

Source: %url/archive/%version/%name-%version.tar.xz
BuildRequires: gcc-c++ cmake

%description
%summary.

%prep
%setup
# cmake and pc files installed in libdir only
sed -i 's|CMAKE_INSTALL_DATADIR|CMAKE_INSTALL_LIBDIR|g' \
  cmake/CMakeLists.txt
sed -i 's|${pc_sysrootdir}||' \
  cmake/treeland-protocols.pc.in

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc LICENSES/ README*.md
%dir %_datadir/%name/
%_datadir/%name/treeland*.xml
%dir %_libdir/cmake/TreelandProtocols/
%_libdir/cmake/TreelandProtocols/TreelandProtocolsConfig.cmake
%_pkgconfigdir/%name.pc

%changelog
* Mon Dec 30 2024 Leontiy Volodin <lvol@altlinux.org> 0.4.5-alt1
- Initial build for ALT Sisyphus.
