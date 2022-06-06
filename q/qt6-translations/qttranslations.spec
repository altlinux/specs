
%global qt_module qttranslations

Name: qt6-translations
Version: 6.2.4
Release: alt1

Group: System/Libraries
Summary: Qt6 - QtTranslations module
Url: http://qt.io/
License: GPL-3.0-only WITH Qt-GPL-exception-1.0

BuildArch: noarch

Source: %qt_module-everywhere-src-%version.tar

BuildRequires: cmake qt6-base-devel qt6-tools

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

%changelog
* Mon Jun 06 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- initial build
