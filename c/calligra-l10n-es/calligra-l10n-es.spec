%define lng es
%define lngg Spanish

Name: calligra-l10n-%lng
Version: 2.7.3
Release: alt1
%define beta %nil

Group: Graphical desktop/KDE
Summary: %lngg language support for Calligra
License: GPL
Url: http://www.calligra.org/

Provides: calligra-i18n-%lng = %version-%release
Provides: calligra-i18n-lang = %version-%release
Obsoletes: calligra-i18n-%lngg
Provides: koffice-i18n-%lng = %version-%release
Obsoletes: koffice-i18n-%lng < %version-%release
Requires: calligra-common

Source: calligra-l10n-%lng-%version.tar

BuildArch: noarch
BuildRequires: gcc-c++ kde4base-runtime-devel kde4libs-devel

%description
%lngg language support for Calligra.


%prep
%setup -q
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
%K4build

%install
%K4install

%files
%lang(%lng) %_K4i18n/%lng/LC_MESSAGES/*.mo
%lang(%lng) %_K4doc/%lng
#%lang(%lng) %_K4apps/calligra/autocorrect/%{lng}*.xml

%changelog
* Mon Sep 16 2013 Sergey V Turchin <zerg@altlinux.org> 2.7.3-alt1
- new version

* Wed Sep 11 2013 Sergey V Turchin <zerg@altlinux.org> 2.7.2-alt1
- new version

* Mon Jul 29 2013 Sergey V Turchin <zerg@altlinux.org> 2.6.4-alt1
- new version

* Tue May 21 2013 Sergey V Turchin <zerg@altlinux.org> 2.6.3-alt1
- new version

* Wed Feb 27 2013 Sergey V Turchin <zerg@altlinux.org> 2.6.1-alt1
- new version

* Fri Feb 08 2013 Sergey V Turchin <zerg@altlinux.org> 2.6.0-alt1
- new version

* Mon Dec 17 2012 Sergey V Turchin <zerg@altlinux.org> 2.5.4-alt1
- new version

* Wed Nov 07 2012 Sergey V Turchin <zerg@altlinux.org> 2.5.3-alt1
- initial build
