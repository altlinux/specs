
%def_disable qt5

%if_disabled qt5
%define qtmajor 6
%define qmake_qt %qmake_qt6
%define install_qt %install_qt6
%define qt_translationdir %_qt6_translationdir
%else
%define qtmajor 5
%define qmake_qt %qmake_qt5
%define install_qt %installqt5
%define qt_translationdir %_qt5_translationdir
%endif

Name: sechooser
Version: 0.3.3
Release: alt1

Summary: Selinux user range chooser
License: GPL
Group: System/Configuration/Other

Requires: qt%{qtmajor}-translations

Source: %name-%version.tar

BuildRequires: libselinux-devel
BuildRequires: qt%{qtmajor}-base-devel qt%{qtmajor}-tools

%description
%summary.


%prep
%setup -q -n %name-%version
%qmake_qt CONFIG+=nostrip

%build
%make
lrelease-qt%{qtmajor} sechooser.pro

%install
%install_qt

mkdir -p %buildroot/%qt_translationdir/
install -m644 translations/sechooser_??.qm %buildroot/%qt_translationdir/

%find_lang --with-qt --all-name %name

%files -f %name.lang
%_bindir/*

%changelog
* Wed Oct 30 2024 Sergey V Turchin <zerg at altlinux dot org> 0.3.3-alt1
- build with Qt6

* Mon Feb 01 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.2-alt1
- Enabled keyboard navigation and introduced active elements focus order.
- Enabled building debuginfo package.

* Wed Oct 21 2020 Denis Medvedev <nbr@altlinux.org> 0.3.1-alt1
- replaced unstable getlogin with reliable proc data read.

* Tue Oct 20 2020 Sergey V Turchin <zerg at altlinux dot org> 0.3.0-alt1
- disable shared memory holder

* Fri Jan 24 2020 Denis Medvedev <nbr@altlinux.org> 0.2.2-alt7
- revert DRI3 commit, it should be done system-wide.

* Fri Jan 24 2020 Denis Medvedev <nbr@altlinux.org> 0.2.2-alt6
- Force disabling of DRI3 by setting the corresponding value in ENV

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt5
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt4
- NMU: remove %ubt from release

* Tue Mar 07 2017 Sergey V Turchin <zerg at altlinux dot org> 0.2.2-alt3%ubt
- build with Qt5

* Mon Feb 27 2017 Sergey V Turchin <zerg at altlinux dot org> 0.2.2-alt2%ubt
- build with Qt4

* Thu Jan 26 2017 Sergey V Turchin <zerg at altlinux dot org> 0.2.2-alt1%ubt
- ignore lowest level again

* Thu Jan 26 2017 Sergey V Turchin <zerg at altlinux dot org> 0.2.1-alt2%ubt
- fix packaging

* Thu Jan 26 2017 Sergey V Turchin <zerg at altlinux dot org> 0.2.1-alt1.S1
- don't ignore minimal selected level

* Fri Jan 20 2017 Sergey V Turchin <zerg at altlinux dot org> 0.2.0-alt1%ubt
- add level names translation

* Tue Jan 17 2017 Sergey V Turchin <zerg at altlinux dot org> 0.1.0-alt1%ubt
- add russian translation
- ignore minimum range

* Wed Jan 11 2017 Sergey V Turchin <zerg at altlinux dot org> 0.0.1-alt1%ubt
- initial build
