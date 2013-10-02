
%def_disable mod_ffmpeg

Name: freerdp
Version: 1.0.2
Release: alt4

Group: Networking/Remote access
Summary: Remote Desktop Protocol functionality
License: Apache License 2.0
Url: http://freerdp.sourceforge.net/
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Requires: xfreerdp = %version-%release %name-plugins-standard = %version-%release

Source: http://downloads.sourceforge.net/%name/%name-%version.tar
# SuSE
Patch1: freerdp_branch-1.0.x_fix-kpdivide-issue831.patch
Patch2: freerdp-fix-FindPCSC-macro.patch
Patch3: freerdp-handle-null-device-name.patch
# ALT
Patch100: freerdp-1.0.2-alt-fix-compile.patch

BuildRequires: cmake ctest xmlto openssl-devel libX11-devel libXcursor-devel libXdamage-devel libXext-devel libXv-devel libXinerama-devel libxkbfile-devel cups-devel zlib-devel libalsa-devel libdirectfb-devel libICE-devel libao-devel libsamplerate-devel libpcsclite-devel libpulseaudio-devel CUnit-devel
%if_enabled mod_ffmpeg
libavcodec-devel libavutil-devel
%endif

%description
freerdp implements Remote Desktop Protocol (RDP), used in a number of Microsoft
products. Rdesktop analog.

This is metapackage.


%package -n xfreerdp
Summary: Remote Desktop Protocol client
Group: Networking/Remote access
#Requires: %name-plugins-standard
%description -n xfreerdp
xfreerdp is a client for Remote Desktop Protocol (RDP), used in a number of
Microsoft products.

This package contains X11 UI.

%package -n dfreerdp
Summary: Remote Desktop Protocol client
Group: Networking/Remote access
Provides: dfbfreerdp

%description -n dfreerdp
dfbfreerdp is a client for Remote Desktop Protocol (RDP), used in a number of
Microsoft products.

This package contains  DirectFB UI.

%package -n lib%name
Summary: Core libraries implementing the RDP protocol
Group: Networking/Remote access

%description -n lib%name
libfreerdp can be embedded in applications.


%package -n lib%name-devel
Summary: Libraries and header files for embedding and extending freerdp
Group: Development/Other
Requires: lib%name = %version-%release pkgconfig
Provides: freerdp-devel
Obsoletes: freerdp-devel

%description -n lib%name-devel
Header files and unversioned libraries for libfreerdp.

%package plugins-standard
Summary: Plugins for handling the standard RDP channels
Group: Networking/Remote access
Requires: lib%name = %version-%release

%description plugins-standard
A set of plugins to the channel manager implementing the standard virtual
channels extending RDP core functionality.  For example, sounds, clipboard
sync, disk/printer redirection, etc.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch100 -p1

%build
%cmake	-DWITH_ALSA=ON \
	-DWITH_PULSEAUDIO=ON \
	-DWITH_PCSC=ON \
	-DWITH_CUNIT=ON \
	-DWITH_CUPS=ON \
%if_enabled mod_ffmpeg
	-DWITH_FFMPEG=ON \
%else
	-DWITH_FFMPEG=OFF \
%endif
	-DWITH_X11=ON \
	-DWITH_XKBFILE=ON \
	-DWITH_XINERAMA=ON \
	-DWITH_XEXT=ON \
	-DWITH_XCURSOR=ON \
	-DWITH_XV=ON \
	-DWITH_DIRECTFB=ON \
	-DWITH_XDAMAGE=ON \
%ifarch x86_64
	-DWITH_SSE2=ON \
%else
	-DWITH_SSE2=OFF \
%endif
	-DWITH_SERVER=OFF \
%ifarch armh
	-DARM_FP_ABI=hard \
	-DWITH_NEON=OFF \
%endif
	#

%make_build -C BUILD

%install
%makeinstall_std -C BUILD

%files

%files -n xfreerdp
%_bindir/xfreerdp
%_datadir/freerdp/keymaps
%_mandir/*/*

%files -n dfreerdp
%_bindir/dfreerdp

%files -n lib%name
%doc LICENSE README
%_libdir/lib*.so.*
%dir %_libdir/freerdp
#_datadir/freerdp/

%files plugins-standard
%_libdir/freerdp/*.so

%files -n lib%name-devel
%_includedir/freerdp
%_libdir/lib*.so
%_libdir/pkgconfig/*

%changelog
* Wed Oct 02 2013 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt4
- fix typo for compile on arm

* Wed Oct 02 2013 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt3
- don't build ffmpeg module (ALT#29416)

* Mon Sep 30 2013 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt2
- separate patches
- fix compile flags

* Wed Sep 18 2013 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- New verson (ALT #28716)
- Pack freerdp keymaps

* Thu Mar 22 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.1-alt2
- Build git fd465f551c34b1ae415f76be4aefeb0fef770de7

* Tue Feb 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.1-alt1
- New release

* Tue Jan 17 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt2
- New release

* Sun Jan 08 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt1.beta5
- New version

* Sat Dec 10 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt1.beta3
- New version

* Sat Nov 12 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt1.beta1
- New version (ALT #24784)
- Update spec for use cmake
- Change license
- Rename subpackage dfbfreerdp -> dfreerdp

* Mon Nov 15 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.2-alt1
- new version

* Thu Oct 28 2010 Mykola Grechukh <gns@altlinux.ru> 0.8.1-alt2
- added patch

* Thu Oct 28 2010 Mykola Grechukh <gns@altlinux.ru> 0.8.1-alt1
- new version

* Fri Aug 06 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.3-alt2
- Rename subpackage freerdp-devel -> libfreerdp-devel

* Thu Aug 05 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.3-alt1
- New version

* Fri Jul 16 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.2-alt2
- Fix undefined symbols

* Fri Jul 16 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.2-alt1
- Build for ALT

* Tue Mar 16 2010 Mads Kiilerich <mads@kiilerich.com> - 0.0.1-1
- Initial "upstream" freerdp spec - made and tested for Fedora 12
