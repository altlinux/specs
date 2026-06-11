%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: rkward
Version: 0.8.3
Release: alt2

Summary: Easily extensible and easy-to-use IDE/GUI for R
License: GPL-2.0-or-later
Group: Sciences/Mathematics
Url: https://invent.kde.org/education/rkward

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules

BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6WebEngineWidgets)
BuildRequires: pkgconfig(cups)

BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kdoctools-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kxmlgui-devel
BuildRequires: kf6-ktexteditor-devel
BuildRequires: kf6-kwidgetsaddons-devel
BuildRequires: kf6-kparts-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-knotifications-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: kf6-karchive-devel
BuildRequires: kf6-breeze-icons-devel
BuildRequires: kf6-kcrash-devel
BuildRequires: kf6-kio-devel
BuildRequires: libkdsingleapplication-qt6-devel
BuildRequires: R-base
BuildRequires: R-devel

%if_with check
BuildRequires: ctest
BuildRequires: icon-theme-breeze
BuildRequires: libqt6-svg
BuildRequires: xauth
BuildRequires: xvfb-run
%endif

Requires: R-base
Requires: R-devel
Requires: R-doc-html
Requires: gcc-c++
Requires: kf6-kio
Requires: kate
Requires: pandoc
Requires: kbibtex

Requires: plasma6-breeze
Requires: icon-theme-breeze

Requires: %{name}-data = %{version}-%{release}
Requires: lib%{name}libs = %{version}-%{release}

ExcludeArch: %ix86 riscv64

%description
RKWard aims to become an easy to use, transparent frontend to R,
a powerful system for statistical computation and graphics.
Besides a convenient GUI for the most important statistical functions,
future versions will also provide seamless integration with an
office-suite.

%package data
Summary: Data files for %name
Group: Sciences/Mathematics
BuildArch: noarch

%description data
RKWard aims to become an easy to use, transparent frontend to R,
a powerful system for statistical computation and graphics.
Besides a convenient GUI for the most important statistical functions,
future versions will also provide seamless integration with an
office-suite.

This package provides the architecture independent data files for %name.

%package -n lib%{name}libs
Group: System/Libraries
Summary: libraries for %name

%description -n lib%{name}libs
This package contains libraries for %name.

%prep
%setup
%patch -p1
rm -rfv 3rdparty/

%build
%cmake \
       -DCMAKE_INSTALL_PREFIX=%_prefix \
       -DCMAKE_INSTALL_LIBEXECDIR=%_lib \
       -DR_INCLUDEDIR=%_includedir/R \
%if_with check
       -DBUILD_TESTING=ON
%else
       -DBUILD_TESTING=OFF
%endif
%cmake_build

%install
%cmake_install

%find_lang %name --with-kde --all-name --with-man

%check
export LC_ALL=en_US.UTF-8
xvfb-run -a --server-args="-screen 0 1024x768x24+32" %ctest -j1 -VV -E "rkward-core_test"

%files -f %name.lang
%doc README
%_K6bin/rkward
%_man1dir/rkward.1.*
%_K6lib/rkward.rbackend

%files data
%_K6xdgapp/org.kde.rkward.desktop
%_K6icon/hicolor/*/apps/rkward.png
%_K6icon/hicolor/scalable/apps/rkward.svgz
%_K6data/kio/servicemenus/rkward.protocol
%_K6data/ktexteditor_snippets/data/*.xml
%_K6data/metainfo/org.kde.rkward.metainfo.xml
%_K6data/mime/packages/vnd.kde.rkward-output.xml
%_K6data/mime/packages/vnd.kde.rmarkdown.xml
%_K6data/mime/packages/vnd.rkward.r.xml
%dir %_K6data/rkward
%_K6data/rkward/*

%files -n lib%{name}libs
%_K6lib/librkward.rbackend.lib.so

%changelog
* Thu Jun 11 2026 Nikolay Strelkov <snk@altlinux.org> 0.8.3-alt2
- Moved libraries to librkwardlibs package.

* Fri May 01 2026 Nikolay Strelkov <snk@altlinux.org> 0.8.3-alt1
- New version 0.8.3 from upstream/releases/0.8.3 branch.

* Wed Feb 04 2026 Nikolay Strelkov <snk@altlinux.org> 0.8.2-alt1
- Initial build of kf6-based RKWard for Sisyphus

