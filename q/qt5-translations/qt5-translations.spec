
%global qt_module qttranslations

Name: qt5-translations
Version: 5.4.0
Release: alt1

Group: System/Libraries
Summary: Qt5 - QtTranslations module
Url: http://qt-project.org/
License: LGPLv2 / GPLv3

BuildArch: noarch

Source: %qt_module-opensource-src-%version.tar

# Automatically added by buildreq on Fri Mar 14 2014 (-bi)
# optimized out: libqt5-core libqt5-xml python-base qt5-base-devel qt5-declarative-devel qt5-tools
#BuildRequires: qt5-script-devel qt5-tools-devel qt5-webkit-devel qt5-xmlpatterns-devel ruby ruby-stdlibs
BuildRequires: qt5-base-devel qt5-tools

%description
%{summary}.

%prep
%setup -qn %qt_module-opensource-src-%version

%build
%qmake_qt5
%make_build

%install
%install_qt5

%find_lang --with-qt --without-mo %name
find %buildroot/%_qt5_translationdir -type f -name \*.qm | sed 's|_.*||' | sort -u | \
while read f
do
    %find_lang --with-qt --without-mo --append --output=%name.lang `basename $f`
done
%find_lang --with-qt --without-mo --append --output=%name.lang qt_help

%files -f %name.lang

%changelog
* Tue Dec 16 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Wed Sep 17 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri Jun 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt0.M70P.1
- build for M70P

* Thu Jun 26 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Wed Jun 04 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Fri Mar 14 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt1
- initial build

