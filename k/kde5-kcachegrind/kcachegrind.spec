%define rname kcachegrind

Name: kde5-%rname
Version: 17.12.3
Release: alt1%ubt
%K5init

Summary: GUI to profilers such as Valgrind
License: %gpl2only
Group: Development/Tools
Url: https://www.kde.org/applications/development/kcachegrind

%ifarch %ix86
Requires: valgrind
%endif

Source0: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5 rpm-build-ubt rpm-build-licenses
BuildRequires: qt5-tools-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf5-karchive-devel kf5-kdoctools-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-ki18n-devel
BuildRequires: kf5-kio-devel

%description
%rname is a profile data visualization tool, used to determine the most time
consuming execution parts of program.

%prep
%setup -n %rname-%version
#exclude examples from build
sed -i -e '/add_subdirectory([[:space:]]*cgview[[:space:]]*)\|add_subdirectory([[:space:]]*qcachegrind[[:space:]]*)/d' CMakeLists.txt

%build
%K5build

%install
%K5install
%K5install_move data %rname
rm -f %buildroot/%_datadir/locale/*/LC_MESSAGES/*.qm
rm -f %buildroot/%_K5i18n/*/LC_MESSAGES/*.qm
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5bin/dprof2calltree
%_K5bin/hotshot2calltree
%_K5bin/kcachegrind
%_K5bin/memprof2calltree
%_K5bin/op2calltree
%_K5bin/pprof2calltree
%_K5xdgapp/org.kde.%{rname}.desktop
%_K5icon/hicolor/*/*/%{rname}*.*
%_K5xmlgui/%rname/
%_K5data/%rname/

%changelog
* Mon Mar 12 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Fri Nov 17 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Mon Aug 28 2017 Stanislav Levin <slev@altlinux.org> 17.08.0-alt1%ubt
- Initial build

