%define rname kcachegrind

%add_findreq_skiplist %_K6bin/hotshot2calltree

Name: %rname
Version: 24.08.2
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
%_K6icon/hicolor/*/*/%{rname}*.*
%_K6data/%rname/
%_datadir/metainfo/*.xml

%changelog
* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build
