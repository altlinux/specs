%def_enable qt5

Name: seappletsimple
Version: 0.2.2
Release: alt1%ubt

Summary: Simple applet for SELinux
License: GPL
Group: System/Configuration/Other

Requires: qt5-translations

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: libselinux-devel rpm-build-xdg
%if_disabled qt5
BuildRequires: gcc-c++ libqt4-devel
%else
BuildRequires: qt5-base-devel qt5-tools
%endif

%description
%summary.


%prep
%setup -q -n %name-%version
%if_disabled qt5
%qmake_qt4
%else
%qmake_qt5
%endif

%build
%make
%if_disabled qt5
lrelease-qt4 seappletsimple.pro
%else
lrelease-qt5 seappletsimple.pro
%endif

%install
%if_disabled qt5
%make install INSTALL_ROOT=%buildroot
%else
%installqt5
%endif

%if_disabled qt5
mkdir -p %buildroot/%_datadir/qt4/translations/
install -m644 translations/seappletsimple_??.qm %buildroot/%_datadir/qt4/translations/
%else
mkdir -p %buildroot/%_qt5_translationdir/
install -m644 translations/seappletsimple_??.qm %buildroot/%_qt5_translationdir/
%endif

mkdir -p %buildroot/%_xdgconfigdir/autostart/
install -m644 %name.desktop %buildroot/%_xdgconfigdir/autostart/%name.desktop

%find_lang --with-qt --all-name %name

%files -f %name.lang
%_bindir/%name
%_xdgconfigdir/autostart/%name.desktop

%changelog
* Thu Mar 09 2017 Sergey V Turchin <zerg at altlinux dot org> 0.2.2-alt1%ubt
- fix parse level

* Tue Mar 07 2017 Sergey V Turchin <zerg at altlinux dot org> 0.2.1-alt3%ubt
- build with Qt5

* Mon Feb 27 2017 Sergey V Turchin <zerg at altlinux dot org> 0.2.1-alt2%ubt
- build with Qt4

* Tue Feb 07 2017 Sergey V Turchin <zerg at altlinux dot org> 0.2.1-alt1%ubt
- change color scheme

* Mon Feb 06 2017 Sergey V Turchin <zerg at altlinux dot org> 0.2.0-alt1%ubt
- using custom colors
- cut range from tooltip level name

* Thu Feb 02 2017 Sergey V Turchin <zerg at altlinux dot org> 0.1.3-alt1%ubt
- update translation

* Thu Feb 02 2017 Sergey V Turchin <zerg at altlinux dot org> 0.1.2-alt1%ubt
- improve tooltip

* Wed Feb 01 2017 Sergey V Turchin <zerg at altlinux dot org> 0.1.1-alt1%ubt
- fix autostart

* Tue Jan 31 2017 Sergey V Turchin <zerg at altlinux dot org> 0.1.0-alt1%ubt
- initial build
