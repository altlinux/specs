%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%add_findreq_skiplist %_K6bin/kdevplatform_shell_environment.sh

Name: kdevelop
Epoch: 3
Version: 26.04.0
Release: alt1

Summary: Cross-platform IDE for C, C++, Python, QML/JavaScript and PHP
License: GPL-2.0-or-later
Group: Graphical desktop/KDE
Url: https://invent.kde.org/kdevelop/kdevelop

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-kf6

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules

BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Core5Compat)
BuildRequires: pkgconfig(Qt6Quick)
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kitemmodels-devel
BuildRequires: kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel
BuildRequires: kf6-kcmutils-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-knewstuff-devel
BuildRequires: kf6-knotifyconfig-devel
BuildRequires: kf6-kparts-devel
BuildRequires: kf6-kservice-devel
BuildRequires: kf6-ktexteditor-devel
BuildRequires: kf6-threadweaver-devel
BuildRequires: kf6-kxmlgui-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: kf6-kcrash-devel
BuildRequires: kf6-kguiaddons-devel
BuildRequires: kf6-karchive-devel
BuildRequires: kf6-knotifications-devel
BuildRequires: kf6-sonnet-devel
BuildRequires: kf6-ktexttemplate-devel
BuildRequires: kf6-ktextwidgets-devel
BuildRequires: kf6-kdoctools-devel
BuildRequires: kde6-libkomparediff2-devel
BuildRequires: kdevelop-pg-qt
BuildRequires: qt6-webengine-devel
BuildRequires: boost-devel
BuildRequires: pkgconfig(cups)
BuildRequires: pkgconfig(Qt6Help)
BuildRequires: libastyle-devel
BuildRequires: clang-devel
BuildRequires: llvm-devel

BuildRequires: pkgconfig(libffi)
BuildRequires: pkgconfig(libedit)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: kf6-purpose-devel
BuildRequires: plasma6-lib-devel
BuildRequires: plasma6-libksysguard-devel
BuildRequires: kf6-kpackage-devel
BuildRequires: kf6-krunner-devel
BuildRequires: pkgconfig(bash-completion)

Requires: clang-tools
Requires: cppcheck
Requires: meson
Requires: cmake
Requires: astyle
Requires: git

Requires: konsole
Requires: kf6-kio
Requires: qt6-tools-doc

Requires: plasma6-breeze
Requires: icon-theme-breeze

Requires: %{name}-libs = %{epoch}:%{version}-%{release}

ExcludeArch: %ix86 riscv64

%description
KDevelop is a fully-featured Integrated Development Environment, perfect
for C and C++ projects and other supported languages. It has great code
completion and project support, along with documentation integration
that keeps you close to where you're editing code.

%package devel
Summary: Development files for %{name}
Group: Development/Other
Requires: %{name}-libs = %{epoch}:%{version}-%{release}
Requires: kf6-ktexteditor-devel
Requires: kf6-threadweaver-devel
Requires: pkgconfig(Qt6Core5Compat)
Requires: pkgconfig(Qt6WebEngineWidgets)
Requires: pkgconfig(Qt6Test)
%description devel
%{summary}.

%package libs
Group: System/Libraries
Summary: %{name} runtime libraries
%description libs
%{summary}.

%prep
%setup
%patch -p1

%build
%K6build

%install
%K6install

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc README.md
%_K6bin/kdevelop
%_K6bin/kdevelop!
%_K6bin/kdev_includepathsconverter
%_K6bin/kdev_dbus_socket_transformer
%_K6bin/kdevplatform_shell_environment.sh
%_K6bin/kdev_format_source
%_K6data/kdev*/
%_K6xdgapp/org.kde.kdevelop.desktop
%_K6xdgapp/org.kde.kdevelop_ps.desktop
%_K6xdgapp/org.kde.kdevelop_bzr.desktop
%_K6xdgapp/org.kde.kdevelop_git.desktop
%_K6xdgapp/org.kde.kdevelop_kdev4.desktop
%_K6data/mime/packages/kdevelop.xml
%_K6data/mime/packages/kdevclang.xml
%_K6data/mime/packages/kdevgit.xml
%_K6data/plasma/plasmoids/org.kde.kdevelopsessions/*
%_K6data/knotifications6/kdevelop.notifyrc
%_K6data/icons/hicolor/*/*/*
%_K6data/qlogging-categories6/kdevelop.categories
%_K6data/qlogging-categories6/kdevplatform.categories
%_K6data/bash-completion/completions/kdevelop
%_K6data/knsrcfiles/kdev*.knsrc
%_K6data/metainfo/org.kde.kdevelop.appdata.xml
%_K6data/metainfo/org.kde.kdevelopsessions.appdata.xml
%_qt6_qmldir/org/kde/plasma/private/kdevelopsessions/libkdevelopsessionsplugin.so
%_qt6_qmldir/org/kde/plasma/private/kdevelopsessions/qmldir

%files libs
%_K6lib/libKDev*.so.65
%_K6lib/libKDev*.so.6.*
%_K6lib/libKDevelopSessionsWatch.so
%_K6plug/kdevplatform/
%_K6plug/kf6/krunner/kdevelopsessions.so
%_K6plug/kf6/ktexttemplate/kdev_filters.so

%files devel
%_K6lib/cmake/KDevelop/
%_K6lib/cmake/KDevPlatform
%_includedir/kdevelop/
%_includedir/kdevplatform/
%exclude %_K6lib/libKDevelopSessionsWatch.so
%_K6lib/libKDev*.so
%_K6lib/kf6/devel/libKDev*.so

%changelog
* Fri Apr 17 2026 Nikolay Strelkov <snk@altlinux.org> 3:26.04.0-alt1
- New version 26.04.0.

* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 3:25.12.3-alt1
- New version 25.12.3.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 3:25.12.2-alt1
- New version 25.12.2.

* Wed Feb 04 2026 Nikolay Strelkov <snk@altlinux.org> 3:25.12.1-alt1
- Initial build of kf6-based KDevelop for Sisyphus.
