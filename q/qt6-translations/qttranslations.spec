
%global qt_module qttranslations

Name: qt6-translations
Version: 6.10.3
Release: alt1

Group: System/Libraries
Summary: Qt6 - QtTranslations module
Url: http://qt.io/
License: GPL-3.0-only WITH Qt-GPL-exception-1.0

BuildArch: noarch
Requires: qt6-base-common

Source: %qt_module-everywhere-src-%version.tar

BuildRequires: cmake qt6-base-devel qt6-tools qt6-tools-devel

%description
%{summary}.

%prep
%setup -qn %qt_module-everywhere-src-%version

%build
%Q6build \
    -DQT_GENERATE_SBOM:BOOL=OFF \
    #

%install
%Q6install_qt

%find_lang --with-qt --without-mo %name
find %buildroot/%_qt6_translationdir -type f -name \*.qm | sed 's|_.*||' | sort -u | \
while read f
do
    %find_lang --with-qt --without-mo --append --output=%name.lang `basename $f`
done
%find_lang --with-qt --without-mo --append --output=%name.lang qt_help

%files -f %name.lang
%doc LICENSES/*
%_qt6_translationdir/catalogs.json

%changelog
* Tue Apr 07 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.3-alt1
- new version

* Thu Feb 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.2-alt1
- new version

* Tue Jan 13 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.1-alt1
- new version

* Thu Nov 06 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.3-alt1
- new version

* Tue Aug 26 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.2-alt1
- new version

* Tue Jun 03 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.1-alt1
- new version

* Thu Feb 06 2025 Sergey V Turchin <zerg@altlinux.org> 6.8.2-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Feb 19 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt1
- new version

* Tue Dec 05 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.1-alt1
- new version

* Tue Oct 31 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

* Wed Feb 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Tue Jul 19 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt3
- fix compile translations

* Fri Jun 10 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt2
- fix build requires

* Mon Jun 06 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- initial build
