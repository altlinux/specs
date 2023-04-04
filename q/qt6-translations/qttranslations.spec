
%global qt_module qttranslations

Name: qt6-translations
Version: 6.4.2
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
%Q6build

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

%changelog
* Wed Feb 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Tue Jul 19 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt3
- fix compile translations

* Fri Jun 10 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt2
- fix build requires

* Mon Jun 06 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- initial build
