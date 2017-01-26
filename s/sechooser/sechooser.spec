Name: sechooser
Version: 0.2.1
Release: alt1%ubt

Summary: Selinux user range chooser
License: GPL
Group: System/Configuration/Other

Requires: qt5-translations

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: qt5-base-devel qt5-tools libselinux-devel

%description
%summary.


%prep
%setup -q -n %name-%version
%qmake_qt5

%build
%make
lrelease-qt5 sechooser.pro

%install
%make INSTALL_ROOT=%buildroot install

mkdir -p %buildroot/%_qt5_translationdir/
install -m644 translations/sechooser_??.qm %buildroot/%_qt5_translationdir/

%find_lang --with-qt --all-name %name

%files -f %name.lang
%_bindir/*

%changelog
* Thu Jan 26 2017 Sergey V Turchin <zerg at altlinux dot org> 0.2.1-alt1.S1
- don't ignore minimal selected level

* Fri Jan 20 2017 Sergey V Turchin <zerg at altlinux dot org> 0.2.0-alt1%ubt
- add level names translation

* Tue Jan 17 2017 Sergey V Turchin <zerg at altlinux dot org> 0.1.0-alt1%ubt
- add russian translation
- ignore minimum range

* Wed Jan 11 2017 Sergey V Turchin <zerg at altlinux dot org> 0.0.1-alt1%ubt
- initial build
