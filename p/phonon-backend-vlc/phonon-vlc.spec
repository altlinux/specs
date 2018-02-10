%ifndef EVR
%define EVR %{?epoch:%epoch:}%{version}-%{release}
%endif

Name: phonon-backend-vlc
Version: 0.8.2
Release: alt4%ubt

Group: Sound
Summary: VLC plugin for Phonon
Url: http://phonon.kde.org/
License: LGPLv2+

Source: %name-%version.tar.bz2

Provides: phonon-backend = %{get_version phonon-devel}
#Provides: phonon-xine = 4.4.4.1 phonon-backend-xine = 4.4.4.1
#Obsoletes: phonon-xine < 4.4.4.1 phonon-backend-xine < 4.4.4.1

BuildRequires(pre): libqt4-devel phonon-devel rpm-build-ubt
BuildRequires: cmake gcc-c++ automoc
BuildRequires: libvlc-devel >= 1.1
BuildRequires: kde-common-devel



%description
Phonon-VLC is a backend for KDE4 Multimedia Framework

%package -n phonon-backend-3-vlc
Group: System/Libraries
Summary: VLC Phonon backend
Provides: phonon-backend = %{get_version phonon-devel}
Provides: phonon-backend-vlc = %EVR
Provides: phonon-vlc = %EVR
Obsoletes: phonon-vlc < %EVR
#
Requires: vlc-mini
#
Requires: vlc-plugin-alsa
Requires: vlc-plugin-pulseaudio
#
Requires: vlc-plugin-ffmpeg
Requires: vlc-plugin-flac
Requires: vlc-plugin-mpeg2
Requires: vlc-plugin-ogg
#
Requires: vlc-plugin-dvdnav
Requires: vlc-plugin-dvdread
Requires: vlc-plugin-audiocd
#
Requires: vlc-plugin-v4l
Requires: vlc-plugin-xcb
Requires: vlc-plugin-ts
Requires: vlc-plugin-live555
Requires: vlc-plugin-xml
Requires: vlc-plugin-dbus
Requires: vlc-plugin-taglib
%description -n phonon-backend-3-vlc
Phonon-VLC is a backend for KDE4 Multimedia Framework

%prep
%setup -q

%build
%K4build \
	-DPHONON_INCLUDE_DIR=%_K4includedir \
	-DCMAKE_INSTALL_PREFIX=%_prefix \
	-DPLUGIN_INSTALL_DIR=%_qt4dir

%install
%K4install

%files -n phonon-backend-3-vlc
%_qt4dir/plugins/phonon_backend/phonon_vlc.so
%_K4srv/phononbackends/vlc.desktop

%changelog
* Sat Feb 10 2018 Sergey V Turchin <zerg@altlinux.org> 0.8.2-alt4%ubt
- rebuild with new vlc

* Tue Nov 07 2017 Oleg Solovyov <mcpain@altlinux.org> 0.8.2-alt3
- fix build

* Thu Mar 05 2015 Sergey V Turchin <zerg@altlinux.org> 0.8.2-alt2
- rebuild with new vlc

* Tue Dec 09 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.2-alt1
- new version

* Mon Nov 10 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt1
- new version

* Fri Sep 12 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1
- new version

* Tue Jun 24 2014 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt1
- new version

* Mon Dec 16 2013 Sergey V Turchin <zerg@altlinux.org> 0.7.1-alt1
- new version

* Mon Sep 23 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.2-alt2
- rebuilt with vlc 2.1

* Mon Mar 04 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.2-alt0.M60P.1
- build for M60P

* Fri Mar 01 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.2-alt1
- new version

* Wed Nov 28 2012 Sergey V Turchin <zerg@altlinux.org> 0.6.1-alt1
- new version

* Sat Feb 25 2012 Sergey V Turchin <zerg@altlinux.org> 0.5.0-alt0.1.M60P.1
- built for M60P

* Fri Feb 24 2012 Sergey V Turchin <zerg@altlinux.org> 0.5.0-alt0.2
- update from 0.5 branch

* Tue Feb 21 2012 Sergey V Turchin <zerg@altlinux.org> 0.5.0-alt0.0.M60P.1
- built for M60P

* Fri Jan 13 2012 Sergey V Turchin <zerg@altlinux.org> 0.5.0-alt0.1
- update code from master branch (ALT#26568)

* Fri Nov 11 2011 Sergey V Turchin <zerg@altlinux.org> 0.4.1-alt4
- don't obsolete xine plugin

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 0.4.1-alt3
- update requires

* Fri Oct 21 2011 Sergey V Turchin <zerg@altlinux.org> 0.4.1-alt2
- obsolete phonon-xine

* Mon Aug 08 2011 Sergey V Turchin <zerg@altlinux.org> 0.4.1-alt1
- new version

* Tue Apr 05 2011 Sergey V Turchin <zerg@altlinux.org> 0.3.2-alt1
- new version

* Tue Feb 01 2011 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt1
- new version

* Fri Dec 03 2010 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt2
- update requires

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- new version
- provides phonon-backend according phonon version

* Wed Jun 23 2010 Konstantin Pavlov <thresh@altlinux.org> 0.2-alt2
- git revision e633c561.

* Mon Apr 19 2010 Konstantin Pavlov <thresh@altlinux.org> 0.2-alt1
- git revision 5aa4fb2c.

* Tue Mar 30 2010 Konstantin Pavlov <thresh@altlinux.org> 0.0-alt2.git0a9da883
- git revision 0a9da883.

* Wed Mar 17 2010 Konstantin Pavlov <thresh@altlinux.org> 0.0-alt1.git7ed2b974
- Initial build for ALT Linux Sisyphus.

