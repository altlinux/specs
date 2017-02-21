%define _libexecdir %_prefix/libexec
Name: lmms
Version: 1.2.0
Release: alt1.rc2.1

Summary: Linux MultiMedia Studio
License: GPL
Group: Sound
Url: http://lmms.sourceforge.net

# https://github.com/LMMS/lmms.git
Source: %name-%version.tar
Source4: %name-16x16.png
Source5: %name-32x32.png
Source6: %name-48x48.png
Patch1: %name-%version-no_werror.patch
Patch2: %name-%version-vst-nowine.patch

BuildPreReq: rpm-build-lmms libfltk-devel
# Automatically added by buildreq on Sun Mar 27 2011
BuildRequires: cmake gcc-c++ libSDL-devel libfluidsynth-devel libpulseaudio-devel libqt4-opengl libqt4-qt3support libqt4-script libqt4-svg libqt4-xml libsamplerate-devel libsndfile-devel libstk-devel libvorbis-devel phonon-devel libfftw3-devel libportaudio2-devel libXft-devel libjpeg-devel
#BuildRequires: libwine-vanilla-devel

%add_verify_elf_skiplist %_libdir/%name/*

%description
LMMS aims to be a free alternative to popular (but commercial and closed-
source) programs like FruityLoops, Cubase and Logic giving you the ability of
producing music with your computer by creating/synthesizing sounds, arranging
samples, using effects, playing live with keyboard and much more...

%package devel
Summary:	Development package for %name
Group:		Development/C
Requires: %name = %version-%release

%description devel
Development files and headers for %name

%prep
%setup
%patch1 -p1
#%%patch2 -p1

##find ./plugins -type f -print0 | xargs -r0 %__subst "s|(LDFLAGS)|(LDFLAGS) \$(QT_LDADD) -lpthread |g"
##find ./plugins -type f -print0 | xargs -r0 %__subst "s|(LIBS)|(LIBS) \$(QT_LDADD) -lpthread |g"
# (tpg) fix ladspa plugins path
#__subst "s|/usr/lib|%{_libdir}|g" src/core/ladspa_manager.cpp

%build
%cmake_insource \
        -DWANT_FFTW3F:BOOL=OFF \
        -DWANT_CMT:BOOL=OFF \
%ifarch %ix86
        -DWANT_VST:BOOL=ON \
%else
        -DWANT_VST:BOOL=OFF \
%endif
        -DCMAKE_INSTALL_LIBDIR=%_lib \
        -Wno-dev \
        -DWANT_VST_NOWINE:BOOL=ON \
#%%ifarch x86_64
#        -DWANT_VST_NOWINE:BOOL=ON \
#%%endif
#-DWANT_CAPS:BOOL=OFF  -DWANT_SWH:BOOL=OFF -DWANT_TAP:BOOL=OFF
%make_build VERBOSE=1

%install
%makeinstall_std

#%%if "%_libexecdir" != "%_libdir"
#install -d %buildroot%_libdir
#mv %buildroot%_libexecdir/%name %buildroot%_libdir/
#%%endif

%find_lang %name

%__mkdir_p %buildroot%_pixmapsdir
%__install -p -m 644 data/themes/default/icon.png %buildroot%_pixmapsdir/%name.png
#icons
%__mkdir_p %buildroot%_miconsdir
%__mkdir_p %buildroot%_liconsdir
%__mkdir_p %buildroot%_niconsdir
%__install -p -m 644 %SOURCE4 %buildroot%_miconsdir/%name.png
%__install -p -m 644 %SOURCE5 %buildroot%_niconsdir/%name.png
%__install -p -m 644 %SOURCE6 %buildroot%_liconsdir/%name.png


# menu
%__mkdir_p %buildroot%_desktopdir
%__cat << EOF > %buildroot%_desktopdir/%name.desktop
[Desktop Entry]
Name=LMMS
GenericName=Linux MultiMedia Studio
Comment=Free cross-platform alternative to commercial programs like FL Studio®
TryExec=lmms
Exec=lmms
Icon=lmms
Terminal=false
StartupNotify=true
Type=Application
Categories=AudioVideo;Audio;Midi;Sequencer;Recorder;
EOF

%files -f %name.lang
%doc README.md LICENSE.txt
%_bindir/*
%_libdir/%name/
%_datadir/%name/
%_man1dir/*
%_pixmapsdir/*
%_miconsdir/*
%_liconsdir/*
%_niconsdir/*
%_desktopdir/*
%_datadir/mime/packages/*

%files devel
%_includedir/%name

%changelog
* Tue Feb 21 2017 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt1.rc2.1
- new snapshot 1.2.0-rc2

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.95-alt2.git20140910.1
- (AUTO) subst_x86_64.

* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.95-alt2.git20140910
- Rebuilt with new stk

* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.95-alt1.git20140910
- Version 1.0.95

* Sun Sep 15 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.15-alt1
- 0.4.15

* Mon Jul 29 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.14-alt1
- 0.4.14

* Sat Feb 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.13-alt1
- 0.4.13

* Wed Oct 19 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.12-alt1
- 0.4.12

* Thu Jun 23 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.11-alt1
- 0.4.11
- Fix repocop warnings

* Sun Mar 27 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.10-alt1
- 0.4.10
- Fix BuildRequires

* Sun Dec 19 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.9-alt1
- 0.4.9

* Mon Oct 11 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.8-alt1
- 0.4.8

* Fri Aug 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.7-alt1
- 0.4.7

* Sat Jan 16 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.6-alt1
- 0.4.6

* Wed Aug 26 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.4.5-alt1
- 0.4.5
- Switch off system ladspa
- Remove all patches

* Mon Mar 09 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.3-alt1
- 0.4.3
- Add Patch1: lmms-0.4.2-literal.patch from lmms-0.4.3-1mdv2009.1
- Add subpackage %name-devel
- Switch to system ladspa
- Add Requires: ladspa-caps ladspa-mcp-plugins ladspa-tap-plugins ladspa-swh-plugins ladspa-rev-plugins ladspa-vco-plugins

* Wed Dec 17 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.0-alt2
- Fix build in x86_64.

* Mon Dec 15 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.0-alt1
- 0.4.0
- Fix repocop tests: iconsdir, shared-mime-info, update_menus, freedesktop-categories et ctr.
- Update spec

* Thu Sep 11 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.3.2-alt2
- Fix for repocop solution
- Update BuildRequires

* Wed Jun 25 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.3.2-alt1
- 0.3.2

* Tue Dec 11 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.3.1-alt3
- Fix build in x86_64.
- Remove BuildPreReq: libwine-devel
- Add BuildPreReq: rpm-build-lmms

* Fri Dec 07 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.3.1-alt2
- Fix build in x86_64.
- Remove BuildPreReq: libwine-devel for x86_64

* Mon Nov 19 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.3.1-alt1
- 0.3.1
- update spec

* Tue Sep 11 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.3.0-alt1
- 0.3.0
- update spec

* Mon Jun 11 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2.1-alt1
- 0.2.1
- update spec

* Fri Jul 21 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.2.0-alt0
- 0.2.0
- Removed ALT menu file

* Thu Mar 23 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.1.4-alt2
- Removed BuildRequires: libqt4-core

* Tue Mar 21 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.1.4-alt1
- Removed BuildPreReq: wine

* Fri Feb 17 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.1.4-alt0
- initial build
