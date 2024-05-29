%define repo deepin-desktop-theme

%def_disable clang

Name: desktop-theme-deepin
Version: 1.0.13
Release: alt1

Summary: Deepin desktop theme.

License: CC-BY-4.0 and CC0-1.0
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/%repo

Source: %url/archive/%version/%repo-%version.tar.gz

BuildArch: noarch

Provides: %repo = %EVR

BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake
%if_enabled clang
BuildRequires: clang-devel lld-devel libstdc++-devel
%else
BuildRequires: gcc-c++
%endif

%description
%summary.

%prep
%setup -n %repo-%version

%build
%if_enabled clang
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif

%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
#
%cmake_build

%install
%cmake_install

%files
%doc README.md README.zh_CN.md
%dir %_datadir/deepin-themes/
%_datadir/deepin-themes/bloom/
%_datadir/deepin-themes/vintage/
%_datadir/deepin-themes/flow/
%_datadir/deepin-themes/hazy-color/
%_datadir/deepin-themes/organic-glass/
%_datadir/deepin-themes/macaron/
%_datadir/deepin-themes/square/
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
%dir %_datadir/dsg/
%dir %_datadir/dsg/icons/
%_datadir/dsg/icons/flow/
%_datadir/dsg/icons/hazy-color/
%_datadir/dsg/icons/organic-glass/
%_datadir/dsg/icons/macaron/
%_datadir/dsg/icons/square/
%_datadir/dsg/icons/bloom-classic/
%_datadir/dsg/icons/bloom-dark/
%_datadir/dsg/icons/bloom/
%_datadir/dsg/icons/vintage/

%changelog
* Wed May 29 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.13-alt1
- New version 1.0.13.

* Fri Nov 24 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.9-alt1
- Initial build for ALT Sisyphus.
