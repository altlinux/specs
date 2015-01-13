%define _optlevel s

Name: stellarium
Version: 0.13.1
Release: alt1

Group: Education
Summary: Astronomical Sky Simulator
Url: http://www.stellarium.org/
License: GPL
Packager: Mikhail E. Rudachenko (ali) <ali@altlinux.org>

Source0: %name-%version.tar.gz

Patch1: %name-0.13.0-desktop.patch

BuildPreReq: cmake rpm-macros-cmake


# Automatically added by buildreq on Mon Dec 29 2014
# optimized out: cmake-modules libEGL-devel libGL-devel libcloog-isl4 libqt5-concurrent libqt5-core libqt5-declarative libqt5-gui libqt5-network libqt5-opengl libqt5-script libqt5-sql libqt5-test libqt5-widgets libqt5-xml libqt5-xmlpatterns libstdc++-devel perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-Pod-Usage qt5-base-devel qt5-script-devel qt5-tools
BuildRequires: cmake gcc-c++ perl-podlators qt5-quick1-devel qt5-tools-devel zlib-devel


%description
Stellarium is a free software available for Windows, Linux/Unix and MacOSX.
It renders 3D photo-realistic skies in real time. With stellarium, you
really see what you can see with your eyes, binoculars or a small
telescope.

%prep
%setup -q
%patch1  -p1 -b .dsk

%build
%cmake -DQT5_LIBS=%_libdir/qt5 -DCMAKE_INSTALL_PREFIX=/usr
%make_build -C BUILD VERBOSE=1

%install
pushd BUILD
%makeinstall_std 
popd

# Remove unwanted files
rm -f $RPM_BUILD_ROOT%_datadir/pixmaps/stellarium.xpm


%find_lang %name
%find_lang %name-skycultures

%post

%postun


%files -f %name.lang
%doc AUTHORS ChangeLog README
%_bindir/%name
%_datadir/%name
%_mandir/man1/%name.1.gz
%_datadir/applications/%name.desktop
%_datadir/appdata/stellarium.appdata.xml
%_datadir/icons/hicolor/*/apps/stellarium.png

%changelog
* Fri Jan 09 2015 Mikhail E. Rudachenko (ali) <ali@altlinux.org> 0.13.1-alt1
- new version
- specfile cleanup
- removed .png and .desktop files
- added patch for desktop file fix (Fedora)

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

