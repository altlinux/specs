%define _kde4_alternate_placement 1

%define lng es
%define lngg Spanish

Name: kde4-i18n-%lng
Version: 4.8.4
Release: alt1

Group: Graphical desktop/KDE
Summary: %lngg language support for KDE
License: GPL
Url: http://www.kde.org/

#Provides: kde-i18n-%lng = %version-%release
Requires: kde-common >= 4.1
BuildArch: noarch

Source: kde-l10n-%lng-%version.tar

BuildRequires: gcc-c++ kde4libs-devel

%description
%lngg language support for KDE.


%prep
%setup -q -n kde-l10n-%lng-%version
#find -type f -name *.gmo | while read f; do rm -f $f; done
#find -type f -name index.cache.bz2 | while read f; do rm -f $f; done
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

for d in docs messages
do
    [ -d $d ] || continue
    pushd $d
    grep -qe "^add_subdirectory([[:space:]]*kdepim[[:space:]]*)" CMakeLists.txt \
	|| echo "add_subdirectory( kdepim )" >> CMakeLists.txt
    popd
done


%build
%K4cmake
%K4make


%install
%K4install

if ! [ -e %buildroot/%_K4doc/%lng/common ]; then
    mkdir -p %buildroot/%_K4doc/%lng/common/
    pushd %_K4doc/en/common/
    for f in *; do
	ln -s %_K4doc/en/common/$f %buildroot/%_K4doc/%lng/common/$f
    done
    popd
fi


%files
%dir %_K4doc/%lng/*
%lang(%lng) %_K4doc/%lng/*
#
%dir %_K4i18n/%lng/
%_K4i18n/%lng/entry.desktop
#
%dir %_K4i18n/%lng/
%dir %_K4i18n/%lng/LC_MESSAGES/
%lang(%lng) %_K4i18n/%lng/LC_MESSAGES/*.mo
#
%lang(%lng) %_K4apps/kvtml/%lng/
#
%lang(%lng) %_K4apps/ktuberling/sounds/%lng/
%lang(%lng) %_K4apps/ktuberling/sounds/%lng.soundtheme
%lang(%lng) %_K4apps/khangman/%lng.txt
%lang(%lng) %_K4apps/klettres/%lng/


%changelog
* Sat Jun 09 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Tue May 15 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Thu Apr 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Tue Mar 13 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Fri Jan 27 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Wed Dec 14 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- built for M60P

* Mon Dec 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt0.M60P.1
- built for M60P

* Wed Nov 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt0.M60T.1
- built for M60T

* Tue Oct 11 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- new version

* Wed Sep 21 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Fri Jul 08 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1
- new version

* Wed Jun 15 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version

* Tue May 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version

* Tue Apr 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version

* Sat Mar 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt2
- update translations

* Fri Mar 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- bump version

* Thu Feb 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.5-alt1
- new version

* Mon Dec 06 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt2
- update sources

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt1
- bump version

* Wed Nov 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- new version

* Thu Oct 07 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- new version

* Wed Sep 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Wed Aug 11 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Thu Jul 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt0.M51.1
- built for M51

* Mon Jul 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1
- new version

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt0.M51.1
- built for M51

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- new version

* Thu May 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt0.M51.1
- built for M51

* Wed May 12 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1
- new version

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt0.M51.1
- built for M51

* Wed Mar 31 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version

* Wed Mar 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Fri Feb 12 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt1
- new version

* Tue Dec 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt0.M51.1
- built for M51

* Wed Dec 02 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
- new version

* Mon Nov 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt0.M51.1
- built for M51

* Thu Nov 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1
- new version

* Mon Oct 12 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt1
- new version

* Tue Sep 01 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt1
- new version

* Wed Aug 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- 4.3.0

* Thu Jul 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt1
- 4.2.98

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt0.M50.1
- built for M50

* Tue Jun 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt1
- new version

* Wed May 06 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt1
- new version

* Mon Apr 06 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt1
- new version

* Fri Mar 06 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.1-alt1
- initial specfile
