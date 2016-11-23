
%define lng uk
%define lngg Ukrainian

Name: kde5-i18n-%lng
Version: 16.08.3
Release: alt1

Group: Graphical desktop/KDE
Summary: %lngg language support for KDE Applications
License: GPL
Url: http://www.kde.org/

Conflicts: kf5-i18n-uk <= 5.6.3-alt1
Requires: kf5-filesystem
BuildArch: noarch

Source: kde-l10n-%lng-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: libdb4-devel qt5-tools-devel
BuildRequires: kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-ki18n-devel

%description
%lngg language support for KDE Applications.


%prep
%setup -q -n kde-l10n-%lng-%version
rm -rf 4 CMakeLists.txt
mv 5/%lng/* ./
rm -rf 5

find -type f -name CMakeLists.txt | \
while read cm; do
    dirs=`grep add_subdirectory "$cm" | sed 's|.*[(]\(.*\)[)].*|\1|'`
    if [ -n "$dirs" ]; then
	pushd `dirname "$cm"`
	for d in $dirs; do
	    mkdir -p $d
	done
	popd
    fi
done



%build
%K5build


%install
%K5install
%K5install_move data all

%files
%dir %_K5doc/%lng/
%lang(%lng) %_K5doc/%lng/*
#
%dir %_K5i18n/%lng/
#%_K5i18n/%lng/entry.desktop
#
%dir %_K5i18n/%lng/LC_MESSAGES/
%lang(%lng) %_K5i18n/%lng/LC_MESSAGES/*.mo
%lang(%lng) %_K5i18n/%lng/LC_MESSAGES/*.qm
%dir %_K5i18n/%lng/LC_SCRIPTS/
%lang(%lng) %_K5i18n/%lng/LC_SCRIPTS/*
#
%lang(%lng) %_K5data/apps/kvtml/%lng/
%lang(%lng) %_K5data/ktuberling/sounds/%lng
%lang(%lng) %_K5data/ktuberling/sounds/%lng.soundtheme
#%lang(%lng) %_K5data/khangman/%lng.txt
%lang(%lng) %_K5data/klettres/%lng
#%lang(%lng) %_K5data/katepart/syntax/logohighlightstyle.%lng.xml
#%lang(%lng) %_K5data/kturtle/data/logokeywords.%lng.xml
#%lang(%lng) %_K5data/kturtle/examples/%lng/
#%lang(%lng) %_K5data/autocorrect/%{lng}_*.xml

%changelog
* Wed Nov 23 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Tue Nov 01 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.2-alt1
- new version

* Thu Sep 29 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Fri Apr 01 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt1
- new version

* Tue Mar 15 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Tue Jan 19 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- initial build
