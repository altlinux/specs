%define rname kgraphviewer

%define sover 0
%define libkgraphviewer libkgraphviewer%sover

Name: %rname
Version: 26.04.2
Release: alt1

Group: Publishing
Summary: GraphViz dot graph viewer
License: GPL-2.0-only
VCS: https://invent.kde.org/graphics/kgraphviewer
Url: https://apps.kde.org/kgraphviewer/

Requires: /usr/bin/dot

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake
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
BuildRequires: desktop-file-utils

%description
KGraphViewer is a tool to display graphviz .dot graphs.

It is more generally a KPart able to display any graph data that
graphviz can handle.

%package -n %libkgraphviewer
Group: System/Libraries
Summary: Graphviz dot graph file viewer (shared library)
%description -n %libkgraphviewer
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
%setup -n %rname-%version

%build
%K6build

%install
%K6install
desktop-file-install \
    --mode=0644 --dir %buildroot/%_K6xdgapp \
    --add-category=Science \
    %buildroot/%_desktopdir/org.kde.%{rname}.desktop

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING* README TODO
%_K6bin/%name
%_K6xdgapp/*%{rname}*.desktop
%_K6icon/*/*/apps/*%{rname}*.*
%_K6cfg/*%{rname}*.kcfg
%_K6plug/kf6/parts/*%{rname}*.so
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*%{rname}*.xml

%files -n %libkgraphviewer
%_K6lib/libkgraphviewer.so.%sover
%_K6lib/libkgraphviewer.so.*

%files devel
%_includedir/%{rname}/
%_K6lib/cmake/KGraphViewerPart/
%_K6link/lib*.so

%changelog
* Fri Jun 05 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Sun May 10 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Wed Apr 08 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt3
- update requires

* Tue Apr 07 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt2
- move sources to tarball
- update packageng

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
