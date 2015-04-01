
%def_disable mod_ffmpeg

Name: freerdp
Version: 1.1.0
Release: alt1.beta1

Group: Networking/Remote access
Summary: Remote Desktop Protocol functionality
License: Apache License 2.0
URL: http://www.freerdp.com
Packager: Mikhail Kolchin <mvk@altlinux.org>

Source: FreeRDP-stable-1.1.tar

Requires: xfreerdp = %version-%release %name-plugins-standard = %version-%release

# Automatically added by buildreq on Sun Mar 22 2015
# optimized out: cmake cmake-modules glib2-devel gstreamer-devel libX11-devel libXext-devel libXrender-devel libcom_err-devel libgst-plugins libkrb5-devel libxml2-devel pkg-config xorg-kbproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-videoproto-devel xorg-xextproto-devel xorg-xproto-devel zlib-devel
BuildRequires: ctest docbook-style-xsl git-core gst-plugins-devel libXcursor-devel libXinerama-devel libXrandr-devel libXv-devel libalsa-devel libcups-devel libdirectfb-devel libjpeg-devel libpcsclite-devel libpulseaudio-devel libssl-devel libxkbfile-devel
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

This package contains DirectFB UI.


%package -n lib%name
Summary: Core libraries implementing the RDP protocol
Group: Networking/Remote access

%description -n lib%name
libfreerdp can be embedded in applications.


%package plugins-standard
Summary: Plugins for handling the standard RDP channels
Group: Networking/Remote access
Requires: lib%name = %version-%release

%description plugins-standard
A set of plugins to the channel manager implementing the standard virtual
channels extending RDP core functionality.  For example, sounds, clipboard
sync, disk/printer redirection, etc.


%package -n lib%name-devel
Summary: Libraries and header files for embedding and extending freerdp
Group: Development/Other
Requires: lib%name = %version-%release pkgconfig
Provides: freerdp-devel
Obsoletes: freerdp-devel

%description -n lib%name-devel
Header files and unversioned libraries for libfreerdp.


%prep
%setup -n FreeRDP-stable-1.1

%build
%cmake \
    -DMONOLITHIC_BUILD=OFF \
    -DWITH_ALSA=ON \
    -DWITH_CUPS=ON \
    -DWITH_CHANNELS=ON -DSTATIC_CHANNELS=OFF \
    -DWITH_DIRECTFB=ON \
%if_enabled mod_ffmpeg
    -DWITH_FFMPEG=ON \
%else
    -DWITH_FFMPEG=OFF \
%endif
    -DWITH_GSM=OFF \
    -DWITH_GSTREAMER_1_0=OFF \
    -DWITH_IPP=OFF \
    -DWITH_JPEG=ON \
    -DWITH_MANPAGES=OFF \
    -DWITH_OPENSSL=ON \
    -DWITH_PCSC=ON \
    -DWITH_PULSE=ON \
    -DWITH_X11=ON \
    -DWITH_XCURSOR=ON \
    -DWITH_XEXT=ON \
    -DWITH_XKBFILE=ON \
    -DWITH_XI=OFF \
    -DWITH_XINERAMA=ON \
    -DWITH_XRENDER=ON \
    -DWITH_XV=ON \
    -DWITH_ZLIB=ON \
%ifarch x86_64
    -DWITH_SSE2=ON \
%else
    -DWITH_SSE2=OFF \
%endif
%ifarch armh
    -DARM_FP_ABI=hard \
    -DWITH_NEON=OFF \
%endif
    #

%cmake_build

%install
%cmakeinstall_std

rm -f %buildroot%_libdir/*.a \
      %buildroot%_libdir/freerdp/*.a

%files

%files -n xfreerdp
%_bindir/xfreerdp
#%_mandir/*/*

%files -n dfreerdp
%_bindir/dfreerdp

%files -n lib%name
%doc LICENSE README ChangeLog
%_libdir/lib*.so.*
%dir %_libdir/freerdp

%files plugins-standard
%_libdir/freerdp/*.so

%files -n lib%name-devel
%_includedir/freerdp
%_includedir/winpr
%_libdir/lib*.so
%_libdir/pkgconfig/*

%changelog
* Sun Mar 22 2015 Mikhail Kolchin <mvk@altlinux.org> 1.1.0-alt1.beta1
- stable-1.1 snapshot 770c67d340d5f0a7b48d53a1ae0fc23aff748fc4

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
