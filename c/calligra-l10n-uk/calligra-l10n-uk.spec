%define lng uk
%define lngg Ukrainian

Name: calligra-l10n-%lng
Version: 2.9.11
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
* Thu Feb 18 2016 Sergey V Turchin <zerg@altlinux.org> 2.9.11-alt1
- new version

* Tue Jan 19 2016 Sergey V Turchin <zerg@altlinux.org> 2.9.10-alt1
- new version

* Tue Nov 10 2015 Sergey V Turchin <zerg@altlinux.org> 2.9.9-alt1
- new version

* Fri Sep 04 2015 Sergey V Turchin <zerg@altlinux.org> 2.9.7-alt1
- new version

* Fri Jun 19 2015 Sergey V Turchin <zerg@altlinux.org> 2.9.5-alt1
- new version

* Wed Apr 15 2015 Sergey V Turchin <zerg@altlinux.org> 2.9.2-alt1
- new version

* Fri Mar 27 2015 Sergey V Turchin <zerg@altlinux.org> 2.9.1-alt1
- new version

* Tue Mar 10 2015 Sergey V Turchin <zerg@altlinux.org> 2.9.0-alt1
- new version

* Fri Dec 12 2014 Sergey V Turchin <zerg@altlinux.org> 2.8.7-alt1
- new version

* Fri Nov 28 2014 Sergey V Turchin <zerg@altlinux.org> 2.8.6-alt1
- new version

* Mon Jul 07 2014 Sergey V Turchin <zerg@altlinux.org> 2.8.5-alt1
- new version

* Thu May 22 2014 Sergey V Turchin <zerg@altlinux.org> 2.8.3-alt1
- new version

* Thu Apr 24 2014 Sergey V Turchin <zerg@altlinux.org> 2.8.2-alt1
- new version

* Wed Apr 02 2014 Sergey V Turchin <zerg@altlinux.org> 2.8.1-alt1
- new version

* Tue Mar 18 2014 Sergey V Turchin <zerg@altlinux.org> 2.8.0-alt1
- new version

* Thu Dec 19 2013 Sergey V Turchin <zerg@altlinux.org> 2.7.5-alt1
- new version

* Mon Nov 11 2013 Sergey V Turchin <zerg@altlinux.org> 2.7.4-alt1
- new version

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

* Mon Feb 04 2013 Sergey V Turchin <zerg@altlinux.org> 2.5.5-alt1
- new version

* Mon Dec 17 2012 Sergey V Turchin <zerg@altlinux.org> 2.5.4-alt1
- new version

* Wed Nov 07 2012 Sergey V Turchin <zerg@altlinux.org> 2.5.3-alt1
- initial build
