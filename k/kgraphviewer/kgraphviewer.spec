%define _unpackaged_files_terminate_build 1

Name: kgraphviewer
Version: 25.12.3
Release: alt1

Summary: GraphViz dot graph viewer
License: GPL-2.0
Group: Publishing
VCS: https://invent.kde.org/graphics/kgraphviewer
Url: https://apps.kde.org/kgraphviewer/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: qt6-declarative-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-5compat-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kparts-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-kdoctools-devel
BuildRequires: boost-devel
BuildRequires: pkgconfig(cups)
BuildRequires: pkgconfig(libgvc)

Requires: graphviz

%description
KGraphViewer is a tool to display graphviz .dot graphs.

It is more generally a KPart able to display any graph data that
graphviz can handle.

%package -n libkgraphviewer0
Group: System/Libraries
Summary: Graphviz dot graph file viewer (shared library)

%description -n libkgraphviewer0
KGraphViewer is a tool to display graphviz .dot graphs.

It is more generally a KPart able to display any graph data that
graphviz can handle.

This package contains the shared library for KGraphViewer.

%package devel
Summary: GraphViz dot graph viewer - devel files
Group: Development/KDE and QT
Requires: kgraphviewer = %{version}
Requires: libkgraphviewer0 = %{version}

%description devel
KGraphViewer is a tool to display graphviz .dot graphs.

It is more generally a KPart able to display any graph data that
graphviz can handle.

This package contains the development files for KGraphViewer.

%prep
%setup
sed -i "s/Categories=.*/Categories=Qt;KDE;DataVisualization;Science;/" src/org.kde.kgraphviewer.desktop
sed -i "/^GenericName\[/d" src/org.kde.kgraphviewer.desktop

%build
%K6build

%install
%K6install

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING COPYING.DOC README TODO
%_K6bin/%name
%_K6xdgapp/org.kde.%{name}.desktop
%_K6icon/*/*/apps/%{name}.*
%_K6cfg/*.kcfg
%_K6plug/kf6/parts/*.so
%_K6data/qlogging-categories6/*.*categories
%_datadir/metainfo/*.xml

%files -n libkgraphviewer0
%_K6lib/libkgraphviewer.so.*

%files devel
%_includedir/kgraphviewer/
%dir %_K6lib/cmake/KGraphViewerPart
%_K6lib/cmake/KGraphViewerPart/*
%_K6link/lib*.so

%changelog
* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 25.12.3-alt1
- New version 25.12.3.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 25.12.2-alt1
- New version 25.12.2.

* Thu Jan 08 2026 Nikolay Strelkov <snk@altlinux.org> 25.12.1-alt1
- New version 25.12.1.

* Sat Dec 13 2025 Nikolay Strelkov <snk@altlinux.org> 25.12.0-alt1
- New version 25.12.0.

* Fri Dec 05 2025 Nikolay Strelkov <snk@altlinux.org> 25.11.90-alt1
- New version 25.11.90.

* Sun Nov 09 2025 Nikolay Strelkov <snk@altlinux.org> 25.08.3-alt1
- New version 25.08.3.

* Thu Oct 16 2025 Nikolay Strelkov <snk@altlinux.org> 25.08.2-alt1
- New version 25.08.2.

* Fri Sep 12 2025 Nikolay Strelkov <snk@altlinux.org> 25.08.1-alt1
- New version 25.08.1.

* Mon Aug 18 2025 Nikolay Strelkov <snk@altlinux.org> 25.08.0-alt1
- New version 25.08.0.

* Thu Jul 31 2025 Nikolay Strelkov <snk@altlinux.org> 25.07.90-alt1
- New version 25.07.90.

* Sat Jul 12 2025 Nikolay Strelkov <snk@altlinux.org> 25.07.80-alt1
- New version 25.07.80.

* Wed Jul 02 2025 Nikolay Strelkov <snk@altlinux.org> 25.04.2-alt1
- Initial build for Sisyphus
