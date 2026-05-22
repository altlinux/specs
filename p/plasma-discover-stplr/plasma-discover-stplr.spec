%define _unpackaged_files_terminate_build 1

Name: plasma-discover-stplr
Version: 0.1.1
Release: alt1

Summary: Plasma Discover stplr support
License: GPL-2.0-only
Group: System/Configuration/Packaging
Url: https://altlinux.space/stapler/plasma-discover-stplr
Vcs: https://altlinux.space/stapler/plasma-discover-stplr.git

Source: %name-%version.tar

Requires: plasma-discover-core
Requires: stplr >= 0.1.0

BuildRequires(pre): rpm-macros-cmake rpm-build-kf6
BuildRequires: cmake extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: qt6-declarative-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kcmutils-devel
BuildRequires: kf6-kconfigwidgets-devel
BuildRequires: kf6-kcolorscheme-devel
BuildRequires: libappstream-qt6-devel

BuildRequires: libdiscovercommon6

%description
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md LICENSE
%_K6plug/discover/stplr-backend.so
%_prefix/libexec/%name
%_datadir/polkit-1/actions/dev.stplr.%name.policy
%_datadir/metainfo/org.kde.discover.stplr.appdata.xml

%changelog
* Fri May 22 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.1.1-alt1
- New version 0.1.1 (closes: #58903).

* Fri Apr 10 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.1.0-alt1
- Initial build.

