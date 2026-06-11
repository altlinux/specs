Name: treeland-protocols
Version: 0.5.8
Release: alt1

Summary: Wayland protocol extensions for treeland

License: MIT
Group: System/Configuration/Other
Url: https://github.com/linuxdeepin/treeland-protocols
Vcs: https://github.com/linuxdeepin/treeland-protocols

# Source-url: https://github.com/linuxdeepin/treeland-protocols/archive/%version/%name-%version.tar.xz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ cmake

%description
%summary.

%prep
%setup
%patch -p1
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
%doc LICENSES/ README*.md debian/changelog
%dir %_datadir/%name/
%_datadir/%name/treeland*.xml
%dir %_libdir/cmake/TreelandProtocols/
%_libdir/cmake/TreelandProtocols/TreelandProtocolsConfig*.cmake
%_pkgconfigdir/%name.pc

%changelog
* Thu Jun 11 2026 Leontiy Volodin <lvol@altlinux.org> 0.5.8-alt1
- New version 0.5.8.

* Tue May 12 2026 Leontiy Volodin <lvol@altlinux.org> 0.5.6-alt1
- New version 0.5.6.

* Wed Mar 04 2026 Leontiy Volodin <lvol@altlinux.org> 0.5.5-alt1
- New version 0.5.5.

* Fri Feb 27 2026 Leontiy Volodin <lvol@altlinux.org> 0.5.4-alt1
- New version 0.5.4.

* Fri Dec 19 2025 Leontiy Volodin <lvol@altlinux.org> 0.5.2-alt1
- New version 0.5.2.

* Tue Nov 18 2025 Leontiy Volodin <lvol@altlinux.org> 0.5.1-alt1
- New version 0.5.1.

* Tue Sep 02 2025 Leontiy Volodin <lvol@altlinux.org> 0.5.0-alt1
- New version 0.5.0.
- Updated license tag.

* Mon Dec 30 2024 Leontiy Volodin <lvol@altlinux.org> 0.4.5-alt1
- Initial build for ALT Sisyphus.
