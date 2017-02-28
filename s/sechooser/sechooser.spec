
%def_disable qt5

Name: sechooser
Version: 0.2.2
Release: alt2%ubt

Summary: Selinux user range chooser
License: GPL
Group: System/Configuration/Other

Requires: qt5-translations

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: libselinux-devel
%if_enabled qt5
BuildRequires: qt5-base-devel qt5-tools
%else
BuildRequires: gcc-c++ libqt4-devel
%endif

%description
%summary.


%prep
%setup -q -n %name-%version
%if_enabled qt5
%qmake_qt5
%else
%qmake_qt4
%endif

%build
%make
%if_enabled qt5
lrelease-qt5 sechooser.pro
%else
lrelease-qt4 sechooser.pro
%endif

%install
%if_enabled qt5
%installqt5
%else
%make install INSTALL_ROOT=%buildroot
%endif

%if_enabled qt5
mkdir -p %buildroot/%_qt5_translationdir/
install -m644 translations/sechooser_??.qm %buildroot/%_qt5_translationdir/
%else
mkdir -p %buildroot/%_datadir/qt4/translations/
install -m644 translations/sechooser_??.qm %buildroot/%_datadir/qt4/translations/
%endif

%find_lang --with-qt --all-name %name

%files -f %name.lang
%_bindir/*

%changelog
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
