%define _libexecdir %_prefix/libexec

%def_disable clang

Name: deepin-desktop-theme
Version: 1.1.31
Release: alt1

Summary: Deepin desktop themes

License: CC-BY-4.0 and CC0-1.0 and GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-desktop-theme
VCS: https://github.com/linuxdeepin/deepin-desktop-theme

# Source-url: %url/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-dqt6
BuildRequires: cmake dqt6-base-devel dqt6-tools-devel libcups-devel dtk6-common-devel libdtk6core-devel libdtk6gui-devel libdtk6widget-devel libwayland-client-devel
%if_enabled clang
BuildRequires: clang-devel lld-devel libstdc++-devel
%else
BuildRequires: gcc-c++
%endif

%description
%summary.

%package -n deepin-desktop-themes
Summary: Deepin desktop themes
Group: Graphical desktop/Other
BuildArch: noarch
Provides: desktop-theme-deepin
Obsoletes:  desktop-theme-deepin
Provides: %name

%description -n deepin-desktop-themes
This package provides desktop themes for DDE.

%package -n xdgicon2dci
Summary: Tools for %name
Group: Graphical desktop/Other
Requires: libdqt6-gui = %_dqt6_version
Requires: dtk6gui

%description -n xdgicon2dci
This package provides xdgicon2dci tool for %name.

%package -n deepin-xdgicon-convert
Summary: Tools for %name
Group: Graphical desktop/Other

%description -n deepin-xdgicon-convert
This package provides deepin-xdgicon-convert tool
for %name.

%prep
%setup
%autopatch -p1

%build
%if_enabled clang
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif

%DQ6build

%install
%DQ6install
# remove broken icon symlinks
find %buildroot%_datadir/dsg/icons/{bloom-classic,bloom-classic-dark} -name "*symbolic.dci" -delete
# package language files
%find_lang --with-qt deepin-xdgicon-convert

%files -n deepin-desktop-themes
%doc README.md README.zh_CN.md debian/changelog
%dir %_datadir/deepin-themes/
%_datadir/deepin-themes/bloom/
%_datadir/deepin-themes/vintage/
%_datadir/deepin-themes/flow/
%_datadir/deepin-themes/hazy-color/
%_datadir/deepin-themes/organic-glass/
%_datadir/deepin-themes/macaron/
%_datadir/deepin-themes/square/
%_datadir/deepin-themes/nirvana/
%_datadir/deepin-themes/origin/
%dir %_iconsdir/flow/
%_iconsdir/flow/*
%dir %_iconsdir/hazy-color/
%_iconsdir/hazy-color/*
%dir %_iconsdir/organic-glass/
%_iconsdir/organic-glass/*
%dir %_iconsdir/macaron/
%_iconsdir/macaron/*
%dir %_iconsdir/square/
%_iconsdir/square/*
%dir %_iconsdir/nirvana/
%_iconsdir/nirvana/*
%dir %_iconsdir/origin/
%_iconsdir/origin/*
%dir %_datadir/dsg/
%dir %_datadir/dsg/icons/
%_datadir/dsg/icons/*.dci
%_datadir/dsg/icons/flow/
%_datadir/dsg/icons/hazy-color/
%_datadir/dsg/icons/organic-glass/
%_datadir/dsg/icons/macaron/
%_datadir/dsg/icons/square/
%_datadir/dsg/icons/bloom-classic/
%_datadir/dsg/icons/bloom-classic-dark/
%_datadir/dsg/icons/bloom-dark/
%_datadir/dsg/icons/bloom/
%_datadir/dsg/icons/vintage/
%_datadir/dsg/icons/nirvana/
%_datadir/dsg/icons/origin/

%files -n xdgicon2dci
%dir %_libexecdir/deepin-desktop-theme/
%_libexecdir/deepin-desktop-theme/xdgicon2dci

%files -n deepin-xdgicon-convert -f deepin-xdgicon-convert.lang
%_bindir/deepin-xdgicon-convert
%_desktopdir/deepin-xdgicon-convert.desktop
%_iconsdir/hicolor/scalable/apps/deepin-xdgicon-convert.svg
%dir %_datadir/deepin-xdgicon-convert/
%dir %_datadir/deepin-xdgicon-convert/translations/

%changelog
* Thu Jun 25 2026 Leontiy Volodin <lvol@altlinux.org> 1.1.31-alt1
- New version 1.1.31.

* Fri Apr 10 2026 Leontiy Volodin <lvol@altlinux.org> 1.1.30-alt1
- New version 1.1.30.

* Tue Mar 10 2026 Leontiy Volodin <lvol@altlinux.org> 1.1.29-alt1
- New version 1.1.29.

* Thu Mar 05 2026 Leontiy Volodin <lvol@altlinux.org> 1.1.28-alt1
- New version 1.1.28.

* Mon Jan 26 2026 Leontiy Volodin <lvol@altlinux.org> 1.1.27-alt2
- Fixed build on dtk 6.7.31.

* Tue Jan 13 2026 Leontiy Volodin <lvol@altlinux.org> 1.1.27-alt1
- New version 1.1.27.
- Fixed xdgicon2dci startup.

* Fri Dec 26 2025 Leontiy Volodin <lvol@altlinux.org> 1.1.26-alt1
- New version 1.1.26.

* Thu Dec 25 2025 Leontiy Volodin <lvol@altlinux.org> 1.1.25-alt1
- New version 1.1.25.

* Mon Dec 08 2025 Leontiy Volodin <lvol@altlinux.org> 1.1.24-alt1
- New version 1.1.24.

* Tue Nov 18 2025 Leontiy Volodin <lvol@altlinux.org> 1.1.23-alt1
- New version 1.1.23.

* Mon Nov 10 2025 Leontiy Volodin <lvol@altlinux.org> 1.1.22-alt1
- New version 1.1.22.

* Sat Nov 01 2025 Leontiy Volodin <lvol@altlinux.org> 1.1.21-alt1
- New version 1.1.21.

* Thu Oct 23 2025 Leontiy Volodin <lvol@altlinux.org> 1.1.18-alt1
- New version 1.1.18.
- New subpackage: deepin-xdgicon-convert.

* Fri Oct 03 2025 Leontiy Volodin <lvol@altlinux.org> 1.1.17-alt1
- New version 1.1.17.

* Mon Sep 22 2025 Leontiy Volodin <lvol@altlinux.org> 1.1.16-alt1
- New version 1.1.16.

* Fri Sep 05 2025 Leontiy Volodin <lvol@altlinux.org> 1.1.14-alt1
- New version 1.1.14.

* Thu Aug 28 2025 Leontiy Volodin <lvol@altlinux.org> 1.1.13-alt1
- New version 1.1.13.
- Renamed: desktop-theme-deepin -> deepin-desktop-themes.
- New subpackage: xdgicon2dci.
- Removed broken icon symlinks.
- Updated license tag.

* Mon Jul 28 2025 Leontiy Volodin <lvol@altlinux.org> 1.1.9-alt1
- New version 1.1.9.
- Added VCS tag.

* Wed May 29 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.13-alt1
- New version 1.0.13.

* Fri Nov 24 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.9-alt1
- Initial build for ALT Sisyphus.
