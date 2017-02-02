Name: seappletsimple
Version: 0.1.3
Release: alt1%ubt

Summary: Simple applet for SELinux
License: GPL
Group: System/Configuration/Other

Requires: qt5-translations

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: qt5-base-devel qt5-tools libselinux-devel rpm-build-xdg

%description
%summary.


%prep
%setup -q -n %name-%version
%qmake_qt5

%build
%make
lrelease-qt5 seappletsimple.pro

%install
%installqt5

mkdir -p %buildroot/%_qt5_translationdir/
install -m644 translations/seappletsimple_??.qm %buildroot/%_qt5_translationdir/

mkdir -p %buildroot/%_xdgconfigdir/autostart/
install -m644 %name.desktop %buildroot/%_xdgconfigdir/autostart/%name.desktop

%find_lang --with-qt --all-name %name

%files -f %name.lang
%_bindir/%name
%_xdgconfigdir/autostart/%name.desktop

%changelog
* Thu Feb 02 2017 Sergey V Turchin <zerg at altlinux dot org> 0.1.3-alt1%ubt
- update translation

* Thu Feb 02 2017 Sergey V Turchin <zerg at altlinux dot org> 0.1.2-alt1%ubt
- improve tooltip

* Wed Feb 01 2017 Sergey V Turchin <zerg at altlinux dot org> 0.1.1-alt1%ubt
- fix autostart

* Tue Jan 31 2017 Sergey V Turchin <zerg at altlinux dot org> 0.1.0-alt1%ubt
- initial build
