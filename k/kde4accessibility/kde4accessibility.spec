%define _kde_alternate_placement 1
%add_findpackage_path %_kde4_bindir

%define rname kdeaccessibility
Name: kde4accessibility
%define major 4
%define minor 8
%define bugfix 2
Version: %major.%minor.%bugfix
Release: alt1


Group: Graphical desktop/KDE
Summary: K Desktop Environment - Accessibility program
Url: http://www.kde.org
License: GPL

Requires: %name-jovie = %version-%release
Requires: %name-kaccessible = %version-%release
Requires: %name-kmag = %version-%release
Requires: %name-kmousetool = %version-%release
Requires: %name-kmouth = %version-%release

Source0: jovie-%version.tar
Source1: kaccessible-%version.tar
Source2: kmag-%version.tar
Source3: kmousetool-%version.tar
Source4: kmouth-%version.tar

# Automatically added by buildreq on Wed Oct 22 2008 (-bi)
#BuildRequires: festival flite gcc-c++ kde4base-runtime-devel kde4base-workspace-devel libXScrnSaver-devel libXcomposite-devel libXdamage-devel libXft-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libalsa-devel libxkbfile-devel rpm-build-ruby xorg-xf86vidmodeproto-devel
#BuildRequires: festival flite
BuildRequires(pre): kde4base-workspace-devel
BuildRequires: gcc-c++ libalsa-devel libspeechd-devel
BuildRequires: kde4base-runtime-devel >= %version kde4base-workspace-devel >= %version

%description
KDE Accessibility Aids:
- kmag, a screen magnifier,
- kmousetool, a program for people whom it hurts to click the mouse
- KMouth, a program that allows people who have lost their voice to let
  their computer speak for them.


%package common
Summary: %name common package
Group: System/Configuration/Other
Requires: kde-common >= %major.%minor
%description common
%name common package

%package core
Summary: Core files for %name
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description core
Core files for %name

%package kaccessible
Group: Graphical desktop/KDE
Summary: KDE accessibility services
Requires: %name-core = %version-%release
%description kaccessible
kaccessible implements a QAccessibleBridgePlugin to provide accessibility services like
focus tracking and a screenreader

%package kmag
Group: Graphical desktop/KDE
Summary: KMag Program
Requires: %name-core = %version-%release
%description kmag
KMag Program

%package kmouth
Group: Graphical desktop/KDE
Summary: KMag Program
Requires: %name-core = %version-%release
%description kmouth
Kmouth Program

%package kmousetool
Group: Graphical desktop/KDE
Summary: kmousetool program
Requires: %name-core = %version-%release
%description kmousetool
kmousetool program

%package -n libkttsd4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkttsd4
KDE 4 library.

%package jovie
Group: Graphical desktop/KDE
Summary: KTTS - KDE Text-to-Speech
Requires: %name-core = %version-%release
Provides: %name-kttsd = %version-%release
Obsoletes: %name-kttsd < %version-%release
%description jovie
KTTS -- KDE Text-to-Speech -- is a subsystem within the KDE desktop for
conversion of text to audible speech. KTTS is currently under development
and aims to become the standard subsystem for all KDE applications
to provide speech output.
User Features:
 - Speak any text from the KDE clipboard.
 - Speak any plain text file.
 - Speak all or any portion of a text file from Kate.
 - Speak all or any portion of an HTML page from Konqueror.
 - Use as the speech backend for KMouth and KSayIt.
 - Speak KDE notifications (KNotify).
 - Long text is parsed into sentences. User may backup by sentence or
   paragraph, replay, pause, and stop playing.
 - Audio output via aRts, ALSA, GStreamer (version 0.8.7 or later), or aKode.

%package devel
Group: Development/KDE and Qt
Summary: Header files for developing kaccessibility utils
Requires: %name-common = %version-%release
%description devel
Header files needed for developing ktts applications.


%prep
%setup -q -cT -n %rname-%version -a0 -a1 -a2 -a3 -a4

ls -d1 * | \
while read d
do
    [ "$d" == "${d#lib}" ] || continue
    [ -d "$d" ] || continue
    echo "add_subdirectory($d)" >> CMakeLists.txt
done


%build
%K4build


%install
%K4install


%files
%files common

%files core
%_kde4_iconsdir/hicolor/*/actions/followmouse.*
%_kde4_iconsdir/hicolor/*/actions/hidemouse.*
%_kde4_iconsdir/hicolor/*/actions/window.*
%_kde4_iconsdir/hicolor/*/actions/speak.*
%_kde4_iconsdir/hicolor/*/actions/nospeak.*
%_kde4_iconsdir/hicolor/*/actions/female.png
%_kde4_iconsdir/hicolor/*/actions/male.png

%files kaccessible
%doc kaccessible*/README
%_K4exec/kaccessibleapp
%_K4lib/plugins/accessiblebridge/kaccessiblebridge.so
%_K4dbus_services/org.kde.kaccessible.service

%files kmag
%_kde4_bindir/kmag
%_kde4_xdg_apps/kmag.desktop
%_kde4_iconsdir/hicolor/*/apps/kmag.*
%_K4apps/kmag
%_K4doc/en/kmag

%files kmouth
%_kde4_bindir/kmouth
%_kde4_xdg_apps/kmouth.desktop
%_K4apps/kmouth
%_K4conf/kmouthrc
%_kde4_iconsdir/hicolor/*/apps/kmouth.png
%_K4doc/en/kmouth

%files kmousetool
%_kde4_bindir/kmousetool
%_kde4_xdg_apps/kmousetool.desktop
%_K4apps/kmousetool
%_kde4_iconsdir/hicolor/*/*/kmousetool*.*
%_K4doc/en/kmousetool

%files jovie
%_kde4_bindir/jovie
%_K4lib/jovie_xmltransformerplugin.so
%_K4lib/jovie_talkerchooserplugin.so
%_K4lib/jovie_stringreplacerplugin.so
%_K4lib/kcm_kttsd.so
%_kde4_xdg_apps/jovieapp.desktop
%_K4apps/jovie
%_K4apps/kttsd
%_K4srv/jovie_talkerchooserplugin.desktop
%_K4srv/jovie.desktop
%_K4srv/jovie_stringreplacerplugin.desktop
%_K4srv/jovie_xmltransformerplugin.desktop
%_K4srv/kcmkttsd.desktop
%_K4srv/kttsd.desktop
%_K4srvtyp/jovie_filterplugin.desktop
%_K4doc/en/jovie

%files -n libkttsd4
%_K4libdir/libkttsd.so.*

#%files devel
#%_K4link/*.so

%changelog
* Thu Apr 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt0.M60P.1
- built for M60P

* Fri Jan 27 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60P.1
- built for M60P

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Mon Sep 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Wed Jun 15 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version

* Fri May 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version

* Mon Apr 11 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version

* Thu Mar 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- new version

* Wed Feb 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.5-alt1
- new version

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt1
- new version

* Wed Nov 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- new version

* Thu Oct 07 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- new version

* Wed Sep 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Mon Aug 09 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Thu Jul 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt0.M51.1
- built for M51

* Mon Jul 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1
- new version

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt0.M51.1
- built for M51

* Wed Jun 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- new version

* Thu May 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt0.M51.1
- built for M51

* Wed May 12 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1
- new version

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt0.M51.1
- built for M51

* Wed Mar 31 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version

* Tue Mar 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Fri Feb 12 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt1
- new version

* Mon Jan 25 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.90-alt1
- new version

* Tue Dec 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt0.M51.1
- built for M51

* Tue Dec 01 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
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

* Fri Jul 17 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.96-alt1
- 4.2.96

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt0.M50.1
- built for M50

* Tue Jun 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt1
- new version

* Tue May 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt1
- new version

* Mon Apr 06 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt1
- new version

* Thu Mar 05 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.1-alt1
- new version

* Thu Jan 29 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- new version

* Thu Jan 22 2009 Sergey V Turchin <zerg at altlinux dot org> 4.1.96-alt1
- new version

* Fri Nov 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- new version

* Thu Oct 23 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt1
- initial specfile

