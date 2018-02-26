Name: qutecom
Version: 2.2.1
Release: alt3.3
Summary: SIP softphone
License: GPLv2+
Group: Networking/Instant messaging
Url: http://www.qutecom.org/
Packager: Aeliya Grevnyov <gray_graff@altlinux.org>

Source: %name-%version.tar
Patch1: install-70QuteCom-permissions.patch
Patch2: remove-extra-copying-file.patch
Patch3: ffmpeg-0.7.1.patch
Patch4: %name-2.2.1-alt-glib2-2.32.0.patch
Patch5: %name-2.2.1-alt-v4l.patch

BuildRequires(pre): rpm-macros-cmake
# Automatically added by buildreq on Fri Aug 13 2010
BuildRequires: boost-filesystem-devel boost-program_options-devel boost-signals-devel cmake gcc-c++ glib2-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libalsa-devel libavformat-devel libcurl-devel libgnutls-devel libqt4-devel libsamplerate-devel libsndfile-devel libspeex-devel libswscale-devel libuuid-devel libxkbfile-devel libxml2-devel mercurial python-devel qt4-assistant
BuildRequires: pm-utils libv4l-devel

Requires: %name-data = %version-%release

%add_optflags %optflags_shared

%description
QuteCom is a SIP softphone which allows you to make free PC to PC
video and voice calls, and to integrate all your IM contacts in one
place.

%package data
Group: Networking/Instant messaging
Summary: noarch files for %name
Requires: %name = %version-%release
BuildArch: noarch
%description data
noarch files for %name

%package pm-utils
Group: Networking/Instant messaging
Summary: pm-utils support
Requires: %name = %version-%release
Requires: pm-utils
%description pm-utils
pm-utils support for %name

%prep
%setup -q -n %name-%version
%patch1 -p1
%patch2 -p1
%patch3 -p2
%patch4 -p2
%patch5 -p2

%build
%cmake \
%if %_lib == lib64
        -DLIB_SUFFIX=64 \
%endif
	-DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
	-DCMAKE_INSTALL_RPATH=%_libdir/qutecom \
	-DCMAKE_SKIP_RPATH:BOOL=no \
	-DBUILDID_SUPPORT=OFF \
	-DPHAPI_QOS_DEBUG_SUPPORT=OFF \
	-DPHAPI_CODEC_ILBC_SUPPORT=ON \
	-DPHAPI_CODEC_AMR_SUPPORT=OFF \
	-DOWSOUND_PORTAUDIO_SUPPORT=OFF \
	-DSAMPLERATE_INTERNAL=OFF \
	-DCURL_INTERNAL=OFF \
	-DFFMPEG_INTERNAL=OFF \
	-DENABLE_CRASHREPORT=OFF \
	-DWENGOPHONE_RESOURCEDIR_PATH=ON \
	-DLIBPURPLE_INTERNAL=ON \
	-DOSIP2_INTERNAL=ON \
	-DDISABLE_VOICE_MAIL=OFF \
	-DENABLE_FACEBOOK=ON \
	-DENABLE_MYSPACE=ON \
	-DENABLE_TWITTER=ON \
	-DENABLE_SKYPE=ON \
        ..

%make_build -C BUILD VERBOSE=1

%install
%make_install -C BUILD DESTDIR="%buildroot/" install

%files
%_bindir/%name
%_libdir/%name

%files data
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/??x??/apps/%name.png
%doc COPYING README

%files pm-utils
%_libdir/pm-utils/sleep.d/70QuteCom

%changelog
* Tue Jun 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt3.3
- Rebuilt

* Tue Jun 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt3.2
- Fixed build

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt3.1
- Rebuilt with Boost 1.49.0
- Fixed build with new glib2

* Wed Jan 25 2012 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.1-alt3
- Fix requires

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt2.2
- Rebuilt with Boost 1.48.0

* Wed Aug 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt2.1
- Rebuilt with new ffmpeg

* Mon Aug 01 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.1-alt2
- Rebuilt with Boost 1.47.0

* Tue Jun 28 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.1-alt1
- QuteCom-2.2.1 release

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt13.1
- Rebuilt with Boost 1.46.1 and for debuginfo

* Wed Dec 15 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2-alt13
- Build with new libboost

* Mon Nov 08 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2-alt12
- Fix repocop info (arch-dep-package-consists-of-usr-share)

* Wed Oct 20 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2-alt11
- QuteCom-2.2 release (ALT#23782)

* Fri Aug 13 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2-alt10.hg639
- Fix Twitter, Facebook, Myspace, Skype support

* Fri Jul 23 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2-alt9.hg639
- Update to hg commit 639:adfe29945e89
- Fix import config (ALT #23781)
- Added subpackages (data and pm-utils)

* Mon Jul 12 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2-alt8.hg636
- Update to hg commit 636:e80b46992dbf

* Thu Jun 17 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2-alt7.hg627
- Update to hg commit 627:41b59125a957
- Update requires (ALT#23629)

* Sun Feb 07 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2-alt6.hg477
- Update to hg commit 477:5c9f01eff560

* Tue Sep 08 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2-alt5.hg440
- Remove portaudio from requires
- Update to hg commit 440:8dc2ab379202

* Mon Jun 08 2009 gray_graff <gray_graff@altlinux.org> 2.2-alt4.rc3
- Switch back to gcc4.4
- Disable ILBC plugin
- Update to hg commit 410:16afed46a4e9
- Enable voice mail

* Fri May 08 2009 gray_graff <gray_graff@altlinux.org> 2.2-alt3.rc3
- Switch to gcc4.3
- Remove install_x86_64_and_install_ilbc_plugin.patch (fix in upstream)
- Update to hg commit 364:e0315d53a061

* Mon Apr 27 2009 gray_graff <gray_graff@altlinux.org> 2.2-alt2.rc3
- Fix build on x86_64

* Sat Mar 28 2009 gray_graff <gray_graff@altlinux.org> 2.2-alt1.rc3
- Initial build for sisyphus
