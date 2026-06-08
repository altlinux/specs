%define rname massif-visualizer

Name: %rname
Version: 26.04.2
Release: alt1

Group: Development/Other
Summary: Tool for visualizing memory usage recorded by Valgrind Massif
License: GPL-2.0-or-later
Url: https://apps.kde.org/massif_visualizer/
VCS: https://invent.kde.org/sdk/massif-visualizer

# kgraphviewer part
Requires: kgraphviewer

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: qt6-declarative-devel
BuildRequires: qt6-5compat-devel
BuildRequires: qt6-svg-devel
BuildRequires: kf6-karchive-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kparts-devel
BuildRequires: kde6-kdiagram-devel
BuildRequires: kgraphviewer-devel
BuildRequires: pkgconfig(cups)
BuildRequires: /usr/bin/rst2man
BuildRequires: desktop-file-utils

%description
Massif Visualizer is a tool that visualizes massif data.

You run your application in Valgrind with "--tool=massif" and then open
the generated "massif.out.<pid>" in the visualizer. Gzip or Bzip2
compressed massif files can also be opened transparently.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install

desktop-file-install \
    --mode=0644 --dir %buildroot/%_K6xdgapp \
    --add-category=Profiling \
    %buildroot/%_desktopdir/org.kde.%rname.desktop

mkdir -pv %buildroot/%_man1dir/
rst2man README > %buildroot/%_man1dir/massif-visualizer.1

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc AUTHORS COPYING README
%_K6bin/*%{rname}*
%_K6xdgapp/*%{rname}*.desktop
%_K6cfg/*.kcfg
%_K6icon/*/*/apps/*%{rname}*.*
%_K6data/%rname/
%_K6xdgmime/*massif*.xml
%_datadir/metainfo/*.xml
%_man1dir/%rname.*

%changelog
* Fri Jun 05 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Sun May 10 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Wed Apr 08 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt3
- fix requires

* Wed Apr 08 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt2
- update packaging

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
