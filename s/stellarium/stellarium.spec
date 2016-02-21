%define _optlevel s

Name: stellarium
Version: 0.14.2
Release: alt1

Group: Education
Summary: Astronomical Sky Simulator
Url: http://www.stellarium.org/
License: GPL

Source0: %name-%version.tar.gz

BuildPreReq: cmake rpm-macros-cmake


# Automatically added by buildreq on Sun Feb 07 2016
# optimized out: cmake-modules gcc-c++ libEGL-devel libGL-devel libqt5-concurrent libqt5-core libqt5-gui libqt5-network libqt5-opengl libqt5-script libqt5-serialport libqt5-test libqt5-widgets libqt5-xml libstdc++-devel perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-podlators qt5-base-devel qt5-tools qt5-script-devel
BuildRequires: cmake perl-Pod-Usage qt5-script-devel qt5-serialport-devel qt5-tools-devel zlib-devel libdrm-devel


%description
Stellarium is a free software available for Windows, Linux/Unix and MacOSX.
It renders 3D photo-realistic skies in real time. With stellarium, you
really see what you can see with your eyes, binoculars or a small
telescope.

%prep
%setup -q

%build
%cmake -DQT5_LIBS=%_libdir/qt5 -DCMAKE_INSTALL_PREFIX=/usr
%make_build -C BUILD VERBOSE=1

%install
pushd BUILD
%makeinstall_std 
popd

%find_lang %name
%find_lang %name-skycultures

%files -f %name.lang
%doc AUTHORS ChangeLog README
%_bindir/%name
%_datadir/%name
%_mandir/man1/%name.1.xz
%_datadir/applications/%name.desktop
%_datadir/appdata/%name.appdata.xml
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/pixmaps/%name.xpm

%changelog
* Sun Feb 21 2016 Mikhail E. Rudachenko (ali) <ali@altlinux.org> 0.14.2-alt1
 - new version


* Sun Oct 25 2015 Alexei Takaseev <taf@altlinux.org> 0.14.0-alt1
- 0.14.0

* Fri Feb 20 2015 Mikhail E. Rudachenko (ali) <ali@altlinux.org> 0.13.2-alt1
- new version
- specfile cleanup
- removed patch for desktop file fix

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

