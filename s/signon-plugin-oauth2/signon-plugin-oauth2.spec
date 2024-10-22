
%define optflags_lto %nil

Name: signon-plugin-oauth2
Version: 0.25
Release: alt10

Group: System/Libraries
Summary: OAuth2 plugin for the Accounts framework
Url: https://gitlab.com/accounts-sso/signon-plugin-oauth2
License: LGPL-2.1-or-later

%ifarch %qt6_qtwebengine_arches
Requires: signon-ui
%endif

Source: signon-oauth2-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6
BuildRequires(pre): rpm-macros-qt6-webengine
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: signon-devel libproxy-devel
BuildRequires: doxygen graphviz

%description
%summary.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
%summary.

%prep
%setup -qn signon-oauth2-%version
sed -i '/^SUBDIRS/s/tests//' signon-oauth2.pro
sed -i '/^SUBDIRS/s/example//' signon-oauth2.pro

%build
export PATH=%_qt6_bindir:$PATH
%ifarch %e2k
# moc_base-plugin.cpp:30: offsetof against non-POD
%add_optflags -Wno-error=invalid-offsetof
%endif
%qmake_qt6 \
    QMF_INSTALL_ROOT=%prefix \
    PREFIX=%prefix \
    CONFIG+=release \
    LIBDIR=%_libdir \
    signon-oauth2.pro

%make_build

%install
%install_qt6

sed -i 's|/lib|/%_lib|' %buildroot/%_pkgconfigdir/signon-oauth2plugin.pc
sed -i 's|^Version:.*|Version: %version|' %buildroot/%_pkgconfigdir/signon-oauth2plugin.pc

%files
%_libdir/signon/liboauth2plugin.so

%files devel
%_includedir/signon-plugins/*.h
%_libdir/pkgconfig/signon-oauth2plugin.pc

%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 0.25-alt10
- build with Qt6

* Thu Jun 09 2022 Sergey V Turchin <zerg@altlinux.org> 0.25-alt2
- update requires

* Thu Sep 30 2021 Sergey V Turchin <zerg@altlinux.org> 0.25-alt1
- new version

* Wed Aug 26 2020 Sergey V Turchin <zerg@altlinux.org> 0.24-alt7
- apply ftbfs patch only with Qt-5.15

* Wed Aug 26 2020 Sergey V Turchin <zerg@altlinux.org> 0.24-alt6
- fix compile with Qt 5.15

* Tue Jun 25 2019 Sergey V Turchin <zerg@altlinux.org> 0.24-alt5
- fix minor spec cleanup

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.24-alt4
- NMU: remove rpm-build-ubt from BR:

* Tue Jun 18 2019 Michael Shigorin <mike@altlinux.org> 0.24-alt3
- E2K: ftbfs workaround
- minor spec cleanup

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.24-alt2
- NMU: remove ubt macro from release

* Mon Jun 19 2017 Sergey V Turchin <zerg@altlinux.org> 0.24-alt1
- new version

* Mon Jan 25 2016 Sergey V Turchin <zerg@altlinux.org> 0.22-alt1
- new version

* Thu Jul 09 2015 Sergey V Turchin <zerg@altlinux.org> 0.21-alt1
- initial build
