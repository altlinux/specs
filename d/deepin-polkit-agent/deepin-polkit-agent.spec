%define repo dde-polkit-agent

%def_disable clang

Name: deepin-polkit-agent
Version: 6.0.20
Release: alt1

Summary: Deepin Polkit Agent

License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-polkit-agent
Vcs: https://github.com/linuxdeepin/dde-polkit-agent

# Source-url: %url/archive/%version/%repo-%version.tar.gz
Source: %repo-%version.tar
Patch: %name-%version-%release.patch

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6
BuildRequires: cmake libdtk6widget-devel dtk6-common-devel dqt6-tools-devel dqt6-declarative-devel libdde-shell-devel deepin-shell libpolkitqt6-dqt6-devel libcups-devel libwayland-client-devel
BuildRequires: vulkan-headers libdqt6-concurrent

%description
DDE Polkit Agent is the polkit agent used in Deepin Desktop Environment.

%package devel
Summary: Development package for %name
Group: Graphical desktop/Other
BuildArch: noarch

%description devel
Header files and libraries for %name.

%prep
%setup -n %repo-%version
%autopatch -p1
# find special polkitqt6
sed \
  -e '/Polkit-qt6_LIBRARIES/i \
  %_dqt6_libdir/libpolkit-qt6-agent-1.so.1 \
  %_dqt6_libdir/libpolkit-qt6-core-1.so.1 \
  %_dqt6_libdir/libpolkit-qt6-gui-1.so.1' \
  -e '/Polkit-qt6_LIBRARIES/d' \
  -i CMakeLists.txt

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
%DQ6build \
  -DCMAKE_INCLUDE_PATH=%_dqt6_headerdir \
#

%install
%DQ6install
%find_lang --with-qt %repo

%files -f %repo.lang
%doc README.md
%doc LICENSE
%doc debian/changelog
%dir %_libexecdir/polkit-1-dde
%_libexecdir/polkit-1-dde/%repo
# package outside find_lang
%dir %_datadir/%repo/
%dir %_datadir/%repo/translations/
%_datadir/%repo/translations/%repo.qm

%files devel
%dir %_includedir/dpa/
%_includedir/dpa/agent-extension-proxy.h
%_includedir/dpa/agent-extension.h

%changelog
* Tue Apr 14 2026 Leontiy Volodin <lvol@altlinux.org> 6.0.20-alt1
- New version 6.0.20.

* Tue Mar 03 2026 Leontiy Volodin <lvol@altlinux.org> 6.0.19-alt1
- New version 6.0.19.
- Fixed build on shrinked dqt6.

* Tue Jan 27 2026 Leontiy Volodin <lvol@altlinux.org> 6.0.17-alt1
- New version 6.0.17.
- Fixed build on dtk 6.7.31.

* Mon Oct 06 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.16-alt1
- New version 6.0.16.
- Applied FindLang Policy.

* Thu Sep 25 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.15-alt1
- New version 6.0.15.

* Tue Sep 09 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.14-alt1
- New version 6.0.14.
- Built with polkitqt6-dqt6 instead polkitqt6-qt6.

* Thu Jun 05 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.13-alt1
- New version 6.0.13.
- Added vcs tag.
- Switched to dqt6.

* Thu May 23 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.7-alt1
- New version 6.0.7.
- Built via separate qt5 instead system (ALT #48138).

* Mon Feb 27 2023 Leontiy Volodin <lvol@altlinux.org> 5.5.22-alt1
- New version (5.5.22).

* Tue Nov 29 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.21-alt1
- New version (5.5.21).

* Fri Aug 20 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.12-alt1
- New version (5.4.12).

* Thu Jul 01 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.7-alt1
- New version (5.4.7).

* Tue Apr 27 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.0.3-alt2
- Changed location of the libraries.

* Wed Nov 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.3-alt1
- New version (5.3.0.3) with rpmgs script.

* Wed Oct 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.2-alt1
- New version (5.3.0.2) with rpmgs script.

* Mon Aug 03 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.7-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

