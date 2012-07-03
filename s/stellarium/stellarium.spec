%define _optlevel s

Name: stellarium
Version: 0.11.2
Release: alt1

Group: Education
Summary: Astronomical Sky Simulator
Url: http://www.stellarium.org/
License: GPL
Packager: Alex Karpov <karpov@altlinux.ru>

Source0: %name-%version.tar.gz
Source2: %name.16.png
Source3: %name.32.png
Source4: %name.48.png
Source5: %name.desktop

Patch1: stellarium-0.9.0-prefix.patch
Patch2: %name-0.9.1-locale_numeric.patch

# Automatically added by buildreq on Thu Aug 25 2011
# optimized out: cmake-modules fontconfig libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXau-devel libXcursor-devel libXext-devel libXfixes-devel libXi-devel libXinerama-devel libXrandr-devel libXrender-devel libXv-devel libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-test libstdc++-devel perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-podlators xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
BuildRequires: cmake gcc-c++ glibc-devel-static libXScrnSaver-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXft-devel libXpm-devel libXt-devel libXtst-devel libXxf86misc-devel libXxf86vm-devel libqt4-sql-mysql libxkbfile-devel perl-Pod-Parser phonon-devel

BuildRequires: perl-podlators

Requires: fonts-ttf-dejavu

%description
Stellarium is a free software available for Windows, Linux/Unix and MacOSX.
It renders 3D photo-realistic skies in real time. With stellarium, you
really see what you can see with your eyes, binoculars or a small
telescope.

%prep
%setup -q
%patch1 
#patch2 -p1

%build
cmake .
%make_build


%install
%make_install DESTDIR="%buildroot" install

mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir,%_datadir/applications}
install -m 644 %SOURCE2 %buildroot/%_miconsdir/%name.png
install -m 644 %SOURCE3 %buildroot/%_niconsdir/%name.png
install -m 644 %SOURCE4 %buildroot/%_liconsdir/%name.png
install -m 644 %SOURCE5 %buildroot/%_datadir/applications/%name.desktop

%find_lang %name
%find_lang --append --output=%name.lang %name-skycultures

%post

%postun


%files -f %name.lang
%doc AUTHORS ChangeLog
%_bindir/%name
%_datadir/%name
%exclude %_datadir/%name/data/*.ttf
%_miconsdir/%name.*
%_niconsdir/%name.*
%_liconsdir/%name.*
%_mandir/man1/%name.1.gz
%_datadir/applications/%name.desktop

%changelog
* Thu Mar 15 2012 Alex Karpov <karpov@altlinux.ru> 0.11.2-alt1
- new version

* Tue Nov 08 2011 Alex Karpov <karpov@altlinux.ru> 0.11.1-alt1
- new version

* Thu Aug 25 2011 Alex Karpov <karpov@altlinux.ru> 0.11.0-alt1
- new version
    + update buildreq

* Sun Apr 03 2011 Alex Karpov <karpov@altlinux.ru> 0.10.6-alt1.1
- exclude dejavu fonts from packaging

* Tue Dec 07 2010 Alex Karpov <karpov@altlinux.ru> 0.10.6-alt1
- new version

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 0.10.5-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Jun 09 2010 Alex Karpov <karpov@altlinux.ru> 0.10.5-alt1
- new version
    + sky-cultures translations now packed

* Thu Mar 11 2010 Alex Karpov <karpov@altlinux.ru> 0.10.4-alt1
- new version

* Wed Feb 03 2010 Alex Karpov <karpov@altlinux.ru> 0.10.3-alt1
- new version

* Mon Oct 12 2009 Alex Karpov <karpov@altlinux.ru> 0.10.2-alt1.1
- updated build requirements

* Wed Jun 24 2009 Alex Karpov <karpov@altlinux.ru> 0.10.2-alt1
- new version

* Sat Feb 07 2009 Alex Karpov <karpov@altlinux.ru> 0.10.1-alt1
- new version

* Mon Dec 15 2008 Alex Karpov <karpov@altlinux.ru> 0.10.0-alt0.2
- added .desktop file (#18212)
    + removed obsoleted macros

* Tue Sep 30 2008 Alex Karpov <karpov@altlinux.ru> 0.10.0-alt0.1
- 0.10.0

* Thu Jul 31 2008 Alex Karpov <karpov@altlinux.ru> 0.9.1-alt1.1
- added patch (thanks Turkov Oleg) for blank screen on start fix (#16473)

* Tue Jan 22 2008 Alex Karpov <karpov@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Tue Sep 11 2007 Alex Karpov <karpov@altlinux.ru> 0.9.0-alt2.2
- first build of 0.9.0 for Sisyphus

* Tue Jun 26 2007 Alex Karpov <karpov@altlinux.ru> 0.9.0-alt2.1
- first build of 0.9.0 for Daedalus

* Fri Jun 15 2007 Alex Karpov <karpov@altlinux.ru> 0.9.0-alt2
- spec cleanup
- updated build requirements

* Thu Jun 14 2007 Alex Karpov <karpov@altlinux.ru> 0.9.0-alt1
- new version

* Mon Jul 03 2006 Sergey V Turchin <zerg at altlinux dot org> 0.8.1-alt1
- new version

* Thu Jan 27 2005 Sergey V Turchin <zerg at altlinux dot org> 0.6.2-alt1
- new version

* Tue Aug 17 2004 Sergey V Turchin <zerg at altlinux dot org> 0.6.0-alt1
- new version
- fix menu section

* Wed Oct 01 2003 Sergey V Turchin <zerg at altlinux dot org> 0.5.2-alt1
- new version
- fix build requires

* Fri Jan 17 2003 Sergey V Turchin <zerg@altlinux.ru> 0.5.0-alt1
- new version

* Mon Oct 14 2002 Sergey V Turchin <zerg@altlinux.ru> 0.4.9-alt1
- new version
- build with gcc3.2

* Tue Aug 13 2002 Sergey V Turchin <zerg@altlinux.ru> 0.4.7-alt1
- initial spec

