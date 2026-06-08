%define rname kcachegrind

%add_findreq_skiplist %_K6bin/hotshot2calltree

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Development/Tools
Summary: GUI to profilers such as Valgrind
Url: https://www.kde.org/applications/development/kcachegrind
License: GPL-2.0-only AND BSD-4-Clause AND GFDL-1.2-only

%ifnarch %e2k
Requires: valgrind
%endif
Provides:  kde5-kcachegrind = %EVR
Obsoletes: kde5-kcachegrind < %EVR

Source0: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-build-python3
BuildRequires: qt6-declarative-devel qt6-tools-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf6-karchive-devel kf6-kdoctools-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kio-devel kf6-kdbusaddons-devel

%description
%rname is a profile data visualization tool, used to determine the most time
consuming execution parts of program.

%prep
%setup -n %rname-%version
#exclude examples from build
sed -i -e '/add_subdirectory([[:space:]]*cgview[[:space:]]*)\|add_subdirectory([[:space:]]*qcachegrind[[:space:]]*)/d' CMakeLists.txt
# fix shebang
sed -i \
  -e "s|^#![[:space:]]*/usr/bin/env python$|#!%{__python3}|g" \
  converters/hotshot2calltree.in

%build
%K6build

%install
%K6install
%K6install_move data %rname

%find_lang %name --with-kde --all-name
%K6find_qtlang %name --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/dprof2calltree
%_K6bin/hotshot2calltree
%_K6bin/kcachegrind
%_K6bin/memprof2calltree
%_K6bin/op2calltree
%_K6bin/pprof2calltree
%_K6xdgapp/org.kde.%{rname}.desktop
%_K6icon/hicolor/*/*/*%{rname}*.*
%_K6data/%rname/
%_datadir/metainfo/*.xml

%changelog
* Fri Jun 05 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Sun May 10 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Nov 19 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Mon Oct 13 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Sep 23 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Fri Jul 25 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Wed Jun 11 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Tue Mar 11 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Thu Mar 06 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Wed Jan 29 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Mon Nov 18 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build
