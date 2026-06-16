%define _stripped_files_terminate_build 1

%add_findreq_skiplist %_K6bin/kdevplatform_shell_environment.sh

%define sover 65
%define libkdevcmakecommon libkdevcmakecommon%sover
%define libkdevclangprivate libkdevclangprivate%sover
%define libkdevplatformdebugger libkdevplatformdebugger%sover
%define libkdevplatformdocumentation libkdevplatformdocumentation%sover
%define libkdevplatforminterfaces libkdevplatforminterfaces%sover
%define libkdevplatformlanguage libkdevplatformlanguage%sover
%define libkdevplatformoutputview libkdevplatformoutputview%sover
%define libkdevplatformproject libkdevplatformproject%sover
%define libkdevplatformserialization libkdevplatformserialization%sover
%define libkdevplatformshell libkdevplatformshell%sover
%define libkdevplatformsublime libkdevplatformsublime%sover
%define libkdevplatformutil libkdevplatformutil%sover
%define libkdevplatformvcs libkdevplatformvcs%sover
%define libkdevelopsessionswatch libkdevelopsessionswatch%sover
%define libkdevcompileanalyzercommon libkdevcompileanalyzercommon%sover

%define rname kdevelop
Name: %rname
Version: 26.04.2
Release: alt2
Epoch: 3

Summary: Cross-platform IDE for C, C++, Python, QML/JavaScript and PHP
License: GPL-2.0-or-later
Group: Graphical desktop/KDE
Url: https://invent.kde.org/kdevelop/kdevelop

ExcludeArch: %ix86 riscv64

AutoReq: yes, nopython

Requires: kde6-runtime
Requires: konsole
Requires: clang-tools
Requires: cppcheck
Requires: meson
Requires: cmake
Requires: astyle
Requires: git
Requires: qt6-tools-doc
Requires: heaptrack-gui

Source: %rname-%version.tar
Patch1: alt-bashrc.patch
Patch2: alt-soname.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake extra-cmake-modules
BuildRequires: pkgconfig(Qt6) pkgconfig(Qt6Core5Compat) pkgconfig(Qt6Quick) pkgconfig(Qt6Help) qt6-webengine-devel
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
BuildRequires: kf6-purpose-devel
BuildRequires: kf6-kpackage-devel
BuildRequires: kf6-krunner-devel
BuildRequires: plasma6-lib-devel
BuildRequires: plasma6-libksysguard-devel
BuildRequires: kde6-libkomparediff2-devel
BuildRequires: kdevelop-pg-qt
BuildRequires: boost-devel
BuildRequires: pkgconfig(cups)
BuildRequires: libastyle-devel
BuildRequires: clang-devel
BuildRequires: llvm-devel
BuildRequires: pkgconfig(libffi)
BuildRequires: pkgconfig(libedit)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(bash-completion)

%description
KDevelop is a fully-featured Integrated Development Environment, perfect
for C and C++ projects and other supported languages. It has great code
completion and project support, along with documentation integration
that keeps you close to where you're editing code.

%package devel
Summary: Development files for %{name}
Group: Development/Other
Requires: kf6-ktexteditor-devel
Requires: kf6-threadweaver-devel
Requires: pkgconfig(Qt6Core5Compat)
Requires: pkgconfig(Qt6WebEngineWidgets)
Requires: pkgconfig(Qt6Test)
%description devel
%{summary}.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Conflicts: kdevelop-libs < 26.04.2-alt2
%description common
%name common package

%package -n %libkdevcmakecommon
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdevcmakecommon
%name library

%package -n %libkdevcompileanalyzercommon
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdevcompileanalyzercommon
%name library

%package -n %libkdevclangprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdevclangprivate
%name library

%package -n %libkdevplatformdebugger
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdevplatformdebugger
%name library

%package -n %libkdevplatformdocumentation
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdevplatformdocumentation
%name library

%package -n %libkdevplatforminterfaces
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdevplatforminterfaces
%name library

%package -n %libkdevplatformlanguage
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdevplatformlanguage
%name library

%package -n %libkdevplatformoutputview
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdevplatformoutputview
%name library

%package -n %libkdevplatformproject
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdevplatformproject
%name library

%package -n %libkdevplatformserialization
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdevplatformserialization
%name library

%package -n %libkdevplatformshell
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdevplatformshell
%name library

%package -n %libkdevplatformsublime
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdevplatformsublime
%name library

%package -n %libkdevplatformutil
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdevplatformutil
%name library

%package -n %libkdevplatformvcs
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdevplatformvcs
%name library

%package -n %libkdevelopsessionswatch
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdevelopsessionswatch
%name library

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

%build
%K6build

%install
%K6install

%find_lang %name --with-kde --all-name

%files common -f %name.lang

%files
%doc README.md
%_K6bin/kdevelop
%_K6bin/kdevelop!
%_K6bin/kdev_includepathsconverter
%_K6bin/kdev_dbus_socket_transformer
%_K6bin/kdevplatform_shell_environment.sh
%_K6bin/kdev_format_source
%_K6plug/kdevplatform/
%_K6plug/kf6/krunner/kdevelopsessions.so
%_K6plug/kf6/ktexttemplate/kdev_filters.so
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

%files devel
%_K6lib/cmake/KDevelop/
%_K6lib/cmake/KDevPlatform
%_includedir/kdevelop/
%_includedir/kdevplatform/
%_K6link/lib*.so

%files -n %libkdevcmakecommon
%_K6lib/libKDevCMakeCommon.so.%sover
%_K6lib/libKDevCMakeCommon.so.*
%files -n %libkdevclangprivate
%_K6lib/libKDevClangPrivate.so.%sover
%_K6lib/libKDevClangPrivate.so.*
%files -n %libkdevplatformdebugger
%_K6lib/libKDevPlatformDebugger.so.%sover
%_K6lib/libKDevPlatformDebugger.so.*
%files -n %libkdevplatformdocumentation
%_K6lib/libKDevPlatformDocumentation.so.%sover
%_K6lib/libKDevPlatformDocumentation.so.*
%files -n %libkdevplatforminterfaces
%_K6lib/libKDevPlatformInterfaces.so.%sover
%_K6lib/libKDevPlatformInterfaces.so.*
%files -n %libkdevplatformlanguage
%_K6lib/libKDevPlatformLanguage.so.%sover
%_K6lib/libKDevPlatformLanguage.so.*
%files -n %libkdevplatformoutputview
%_K6lib/libKDevPlatformOutputView.so.%sover
%_K6lib/libKDevPlatformOutputView.so.*
%files -n %libkdevplatformproject
%_K6lib/libKDevPlatformProject.so.%sover
%_K6lib/libKDevPlatformProject.so.*
%files -n %libkdevplatformserialization
%_K6lib/libKDevPlatformSerialization.so.%sover
%_K6lib/libKDevPlatformSerialization.so.*
%files -n %libkdevplatformshell
%_K6lib/libKDevPlatformShell.so.%sover
%_K6lib/libKDevPlatformShell.so.*
%files -n %libkdevplatformsublime
%_K6lib/libKDevPlatformSublime.so.%sover
%_K6lib/libKDevPlatformSublime.so.*
%files -n %libkdevplatformutil
%_K6lib/libKDevPlatformUtil.so.%sover
%_K6lib/libKDevPlatformUtil.so.*
%files -n %libkdevplatformvcs
%_K6lib/libKDevPlatformVcs.so.%sover
%_K6lib/libKDevPlatformVcs.so.*
%files -n %libkdevelopsessionswatch
%_K6lib/libKDevelopSessionsWatch.so.%sover
%_K6lib/libKDevelopSessionsWatch.so.*
%files -n %libkdevcompileanalyzercommon
%_K6lib/libKDevCompileAnalyzerCommon.so.%sover
%_K6lib/libKDevCompileAnalyzerCommon.so.*

%changelog
* Tue Jun 16 2026 Sergey V Turchin <zerg@altlinux.org> 3:26.04.2-alt2
- fix packaging

* Fri Jun 05 2026 Nikolay Strelkov <snk@altlinux.org> 3:26.04.2-alt1
- New version 26.04.2.

* Thu May 07 2026 Nikolay Strelkov <snk@altlinux.org> 3:26.04.1-alt1
- New version 26.04.1.

* Fri Apr 17 2026 Nikolay Strelkov <snk@altlinux.org> 3:26.04.0-alt1
- New version 26.04.0.

* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 3:25.12.3-alt1
- New version 25.12.3.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 3:25.12.2-alt1
- New version 25.12.2.

* Wed Feb 04 2026 Nikolay Strelkov <snk@altlinux.org> 3:25.12.1-alt1
- Initial build of kf6-based KDevelop for Sisyphus.
