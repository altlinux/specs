%define _unpackaged_files_terminate_build 1

Name: massif-visualizer
Version: 25.12.3
Release: alt1

Summary: Tool for visualizing memory usage recorded by Valgrind Massif
License: GPL-2.0-or-later
Group: Development/Other
Url: https://apps.kde.org/massif_visualizer/
VCS: https://invent.kde.org/sdk/massif-visualizer

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: qt6-declarative-devel
BuildRequires: qt6-5compat-devel
BuildRequires: qt6-svg-devel
BuildRequires: kf6-karchive-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kparts-devel
BuildRequires: kde6-kdiagram-devel
BuildRequires: pkgconfig(cups)
BuildRequires: /usr/bin/rst2man

%description
Massif Visualizer is a tool that visualizes massif data.

You run your application in Valgrind with "--tool=massif" and then open
the generated "massif.out.<pid>" in the visualizer. Gzip or Bzip2
compressed massif files can also be opened transparently.

%prep
%setup
sed -i "s|^Categories=.*|Categories=Qt;KDE;Development;Profiling;|" app/org.kde.massif-visualizer.desktop

%build
%K6build

%install
%K6install
mkdir -pv %buildroot/%_man1dir/
rst2man README > %buildroot/%_man1dir/massif-visualizer.1

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc AUTHORS COPYING README
%_K6bin/%name
%_man1dir/%{name}.*
%_K6xdgapp/org.kde.%{name}.desktop
%_K6cfg/*.kcfg
%_K6icon/*/*/apps/%{name}.*
%_datadir/metainfo/*.xml
%dir %_datadir/massif-visualizer
%_datadir/massif-visualizer/*
%_datadir/mime/packages/massif.xml

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
