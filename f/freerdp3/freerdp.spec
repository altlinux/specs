%define _unpackaged_files_terminate_build 1
%def_with ffmpeg
%def_with x264
%def_without directfb
%def_with gss
# Conflicts with openssl
%def_without mbedtls
%def_with SDL
%def_without uwac
%define sover 3
%define oname freerdp

Name: freerdp%sover
Version: 3.7.0
Release: alt1

Group: Networking/Remote access
Summary: Remote Desktop Protocol functionality
License: Apache-2.0
URL: http://www.freerdp.com
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %oname-%version.tar
Source1: freerdp-server.service
Patch0: freerdp-alt-pam-check.patch
Patch2000: freerdp-e2k.patch

Requires: xfreerdp%sover = %EVR
Requires: wlfreerdp%sover = %EVR

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: docbook-style-xsl git-core xmlto libpcre-devel
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libpcsclite)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xv)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(libpulse)
%{?_with_directfb:BuildRequires: pkgconfig(directfb)}
BuildRequires: libcups-devel libjpeg-devel zlib-devel
%{?_with_ffmpeg:BuildRequires: libavcodec-devel libavutil-devel libswresample-devel}
%{?_with_x264:BuildRequires: libx264-devel}
BuildRequires: libkrb5-devel
BuildRequires: wayland-devel
%if_with mbedtls
BuildRequires: libmbedtls-compat-devel
%endif
BuildRequires: libgsm-devel
BuildRequires: liblame-devel
BuildRequires: libfaad-devel
BuildRequires: libfaac-devel
BuildRequires: libsoxr-devel
BuildRequires: libffi-devel
BuildRequires: liborc-devel
BuildRequires: libicu-devel
BuildRequires: libcairo-devel
BuildRequires: libpixman-devel
BuildRequires: libexpat-devel
BuildRequires: libXdmcp-devel
BuildRequires: bzlib-devel
BuildRequires: libuuid-devel
BuildRequires: libudev-devel
BuildRequires: libusb-devel
BuildRequires: libpam-devel
BuildRequires: libdbus-glib-devel
%ifarch %e2k
BuildRequires: chrpath
%else
BuildRequires: patchelf
%endif
%if_with SDL
BuildRequires: libSDL2-devel
BuildRequires: libSDL2_ttf-devel
BuildRequires: libwebkit2gtk-devel
%endif
BuildRequires: libcjson-devel
BuildRequires: libfuse3-devel
BuildRequires: libopenh264-devel
BuildRequires: libpkcs11-helper-devel
BuildRequires: libswscale-devel
BuildRequires: liburiparser-devel

%description
freerdp implements Remote Desktop Protocol (RDP), used in a number of Microsoft
products. Rdesktop analog.

This is metapackage.

%package -n xfreerdp%sover
Summary: Remote Desktop Protocol client
Group: Networking/Remote access
Requires: lib%name = %EVR
Conflicts: xfreerdp

%description -n xfreerdp%sover
xfreerdp is a client for Remote Desktop Protocol (RDP), used in a number of
Microsoft products.

This package contains X11 UI.

%package -n dfreerdp%sover
Summary: Remote Desktop Protocol client
Group: Networking/Remote access
Requires: lib%name = %EVR
Conflicts: dfreerdp

%description -n dfreerdp%sover
dfbfreerdp is a client for Remote Desktop Protocol (RDP), used in a number of
Microsoft products.

This package contains DirectFB UI.

%package -n wlfreerdp%sover
Summary: Remote Desktop Protocol client
Group: Networking/Remote access
Requires: lib%name = %EVR
Conflicts: wlfreerdp

%description -n wlfreerdp%sover
wlfreerdp is a client for Remote Desktop Protocol (RDP), used in a number of
Microsoft products.

This package contains Wayland UI.

%package -n lib%name
Summary: Core libraries implementing the RDP protocol
Group: System/Libraries

%description -n lib%name
libfreerdp can be embedded in applications.

%package -n lib%name-server
Summary: Remote Desktop Viewer server library
Group: System/Libraries

%description -n lib%name-server
FreeRDP is a client-side implementation of the Remote Desktop Protocol (RDP)
following the Microsoft Open Specifications. This package provides the shared
libraries used by the server.

%package -n libwinpr%sover
Summary: Windows Portable Runtime
Group: System/Libraries

%description -n libwinpr%sover
WinPR provides API compatibility for applications targeting non-Windows
environments. When on Windows, the original native API is being used instead of
the equivalent WinPR implementation, without having to modify the code using it.

%package -n libwinpr%sover-devel
Summary: Windows Portable Runtime development files
Group: Development/C
Requires: libwinpr%sover = %EVR

%description -n libwinpr%sover-devel
The libwinpr-devel package contains libraries and header files for
developing applications that use libwinpr.

%package -n libuwac%sover
Summary: Use wayland as a client
Group: System/Libraries

%description -n libuwac%sover
Remote Desktop Toolkit library. Contains the libuwac libraries.

%package -n libuwac%sover-devel
Summary: Remote Desktop Toolkit libuwac development files
Group: Development/C
Requires: libuwac%sover = %EVR

%description -n libuwac%sover-devel
The libuwac-devel package contains libraries and header files for
developing applications that use libuwac.

%package -n librdtk%sover
Summary: Use wayland as a client
Group: System/Libraries

%description -n librdtk%sover
Remote Desktop Toolkit library. Contains the librdtk libraries.

%package -n librdtk%sover-devel
Summary: Remote Desktop Toolkit librdtk development files
Group: Development/C
Requires: librdtk%sover = %EVR

%description -n librdtk%sover-devel
The librdtk-devel package contains libraries and header files for
developing applications that use librdtk.

%package -n lib%name-devel
Summary: Libraries and header files for embedding and extending freerdp
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Header files and unversioned libraries for libfreerdp.

%package -n %name-server
Summary: Server support for %{name}
Group: Networking/Remote access
Requires: lib%name = %EVR
Requires: lib%name-server = %EVR
Conflicts: freerdp-server

%description -n %name-server
The %{name}-server package contains servers which can export a desktop via
the RDP protocol.

%prep
%setup -n %oname-%version
%patch0 -p1
%ifarch %e2k
%patch2000 -p1
%endif

%build
%cmake \
    -GNinja \
    -Wno-dev \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_SKIP_RPATH=FALSE \
%ifarch %e2k
    -DCMAKE_SKIP_INSTALL_RPATH=FALSE \
    -DCMAKE_INSTALL_RPATH:PATH='$ORIGIN' \
%else
    -DCMAKE_SKIP_INSTALL_RPATH=TRUE \
%endif
    -DWITH_ALSA=ON \
    -DWITH_CAIRO=ON \
    -DWITH_CUPS=ON \
    -DWITH_CHANNELS=ON \
    -DWITH_CLIENT_CHANNELS=ON \
    -DWITH_DEBUG_CHANNELS=OFF \
    -DWITH_CLIENT=ON \
    %{?_without_directfb:-DWITH_DIRECTFB=OFF} \
    %{?_without_ffmpeg:-DWITH_FFMPEG=OFF} \
%if_with x264
    -DWITH_X264=ON \
%else
    -DWITH_X264=OFF \
%endif
    -DWITH_GSM=ON \
    %{?_without_gss:-DWITH_KERBEROS=OFF} \
%if_without uwac
	-DUWAC_FORCE_STATIC_BUILD=ON \
%endif
    -DWITH_FAAC=ON \
    -DWITH_FAAD2=ON \
    -DWITH_GSTREAMER_1_0=ON \
    -DWITH_ICU=ON \
    -DWITH_IPP=OFF \
    -DWITH_JPEG=ON \
    -DWITH_LAME=ON \
    -DWITH_LIBRARY_VERSIONING=ON \
    -DWITH_MANPAGES=ON \
    %{?_with_mbedtls:-DWITH_MBEDTLS=ON} \
    -DWITH_OPENH264=ON \
    -DWITH_OPENCL=OFF \
    -DWITH_OPENSSL=ON \
    -DWITH_PCSC=ON \
    -DWITH_PULSE=ON \
    -DWITH_SERVER=ON \
    -DWITH_SERVER_INTERFACE=ON \
    -DWITH_SERVER_CHANNELS=ON \
    -DWITH_SHADOW_X11=ON \
    -DWITH_SHADOW_MAC=ON \
    -DWITH_XTEST=ON \
    -DCHANNEL_URBDRC=ON \
    -DCHANNEL_URBDRC_CLIENT=ON \
    -DWITH_SHADOW_X11=ON \
    -DWITH_SHADOW_MAC=ON \
    -DWITH_SOXR=ON \
    -DWITH_WAYLAND=ON \
    -DWITH_X11=ON \
    -DWITH_XCURSOR=ON \
    -DWITH_XEXT=ON \
    -DWITH_XI=ON \
    -DWITH_XINERAMA=ON \
    -DWITH_XKBFILE=ON \
    -DWITH_XRENDER=ON \
    -DWITH_XV=ON \
    -DWITH_ZLIB=ON \
%ifarch x86_64 %e2k
    -DWITH_SSE2=ON \
%else
    -DWITH_SSE2=OFF \
%endif
%ifarch x86_64
    -DWITH_VAAPI=%{?_with_ffmpeg:ON}%{?!_with_ffmpeg:OFF} \
%endif
%ifarch armh
    -DARM_FP_ABI=hard \
    -DWITH_NEON=OFF \
%endif
%ifarch %e2k
    -DCMAKE_C_FLAGS_RELEASE="-O%_optlevel -DNDEBUG"
%endif
    #

%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"

rm -f %buildroot%_libdir/*.a \
      %buildroot%_libdir/freerdp/*.a

%ifarch %e2k
# patchelf damages e2k binaries
setrpath="chrpath -r"
%else
setrpath="patchelf --set-rpath"
%endif

# Set rpath to %_libdir/freerdp3 for freerdp-proxy executable
$setrpath %_libdir/freerdp3 %buildroot%_bindir/freerdp-proxy

# Install freerdp-server.service
install -Dpm0644 %SOURCE1 %buildroot%_libexecdir/systemd/user/freerdp-server.service

# Remove sample server
rm -f %buildroot%_bindir/sfreerdp*

# Remove icons
rm -rf %buildroot%_datadir/FreeRDP/images/test_*.*

%if_with SDL
rm -f %buildroot%_bindir/sdl-freerdp %buildroot%_man1dir/sdl-freerdp.1*
%endif

%files

%files -n xfreerdp%sover
%_bindir/xfreerdp
%_man1dir/xfreerdp*
%_bindir/winpr-*
%_man1dir/winpr-*
%_man7dir/wlog*

%files -n wlfreerdp%sover
%_bindir/wlfreerdp
%_man1dir/wlfreerdp*

%if_with directfb
%files -n dfreerdp%sover
%_bindir/dfreerdp
%endif

%files -n %name-server
%_bindir/freerdp-proxy
%config(noreplace) %_libexecdir/systemd/user/freerdp-server.service
%attr(2711, root, chkpwd) %_bindir/freerdp-shadow-cli
%_man1dir/freerdp-shadow-cli.1*
%_man1dir/freerdp-proxy.1*
%_libdir/freerdp*/proxy

%files -n lib%name
%doc LICENSE README.md ChangeLog
%_libdir/lib%{oname}3.so.*
%_libdir/lib%{oname}-client3.so.*
%dir %_libdir/freerdp*

%files -n lib%name-server
%_libdir/lib%{oname}-server3.so.*
%_libdir/lib%{oname}-server-proxy3.so.*
%_libdir/lib%{oname}-shadow-subsystem3.so.*
%_libdir/lib%{oname}-shadow3.so.*

%files -n libwinpr%sover
%_libdir/libwinpr3.so.*
%_libdir/libwinpr-tools3.so.*

%files -n libwinpr%sover-devel
%_libdir/cmake/WinPR*
%_includedir/winpr*
%_libdir/libwinpr3.so
%_libdir/libwinpr-tools3.so
%_pkgconfigdir/winpr*.pc

%if_with uwac
%files -n libuwac%sover
%_libdir/libuwac0.so.*

%files -n libuwac%sover-devel
%_libdir/cmake/uwac*
%_includedir/uwac*
%_libdir/libuwac0.so
%_pkgconfigdir/uwac*.pc
%endif

%files -n librdtk%sover
%_libdir/librdtk0.so.*

%files -n librdtk%sover-devel
%_libdir/cmake/rdtk*
%_includedir/rdtk*
%_libdir/librdtk0.so
%_pkgconfigdir/rdtk*.pc

%files -n lib%name-devel
%_libdir/cmake/FreeRDP*
%_includedir/%{name}*
%_libdir/libfreerdp*.so
%_pkgconfigdir/freerdp*.pc

%changelog
* Fri Aug 09 2024 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- New version.

* Wed Jul 10 2024 Andrey Cherepanov <cas@altlinux.org> 3.6.3-alt1
- New version.

* Sat Jul 06 2024 Andrey Cherepanov <cas@altlinux.org> 3.6.2-alt1
- New version.

* Wed Apr 24 2024 Andrey Cherepanov <cas@altlinux.org> 3.5.1-alt1
- New version.

* Thu Apr 18 2024 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt1
- New version.
- Security fixes:
  + CVE-2024-32041 OutOfBound Read in zgfx_decompress_segment
  + CVE-2024-32039 Integer overflow & OutOfBound Write in clear_decompress_residual_data
  + CVE-2024-32040 integer underflow in nsc_rle_decode
  + CVE-2024-32458 OutOfBound Read in planar_skip_plane_rle
  + CVE-2024-32459 OutOfBound Read in ncrush_decompress
  + CVE-2024-32460 OutOfBound Read in interleaved_decompress

* Wed Mar 20 2024 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version.
- Renamed to freerdp3.

* Thu Dec 14 2023 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- New version (ALT #48801).
- Enabled GSSAPI support.
- Using Ninja for build.

* Wed Sep 20 2023 Andrey Cherepanov <cas@altlinux.org> 2.11.2-alt1
- New version.

* Tue Sep 19 2023 Andrey Cherepanov <cas@altlinux.org> 2.11.1-alt2
- Added freerdp-server.service - user service for remote access to desktop via RDP.

* Tue Sep 05 2023 Andrey Cherepanov <cas@altlinux.org> 2.11.1-alt1
- New version.

* Tue Aug 29 2023 Andrey Cherepanov <cas@altlinux.org> 2.11.0-alt1
- New version.

* Fri Jun 09 2023 Andrey Cherepanov <cas@altlinux.org> 2.10.0-alt3
- Used PAM for authenticate freerdp-shadow-cli (ALT #46465).

* Fri Jun 02 2023 Andrey Cherepanov <cas@altlinux.org> 2.10.0-alt2
- Moved freerdp-proxy to freerdp-server.

* Tue Mar 21 2023 Andrey Cherepanov <cas@altlinux.org> 2.10.0-alt1
- New version (ALT #45580).

* Fri Nov 18 2022 Andrey Cherepanov <cas@altlinux.org> 2.9.0-alt1
- New version.
- Fixed multiple client side input validation issues
  (CVE-2022-39316, CVE-2022-39317, CVE-2022-39318, CVE-2022-39319,
  CVE-2022-39320, CVE-2022-41877, CVE-2022-39347).

* Mon Nov 07 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.8.1-alt1.1
- E2K: use chrpath instead of patchelf

* Fri Oct 14 2022 Andrey Cherepanov <cas@altlinux.org> 2.8.1-alt1
- New version.
- Security fixes for CVE-2022-39282, CVE-2022-39283.

* Fri Jul 29 2022 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt1
- New version.

* Mon Apr 25 2022 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt1
- New version.
- Security fixes for CVE-2022-24882, CVE-2022-24883.

* Sun Mar 13 2022 Andrey Cherepanov <cas@altlinux.org> 2.6.1-alt1
- New version.

* Tue Feb 22 2022 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt1
- New version.

* Wed Jan 12 2022 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- New version.

* Thu Oct 21 2021 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1
- New version.
- Security fixes:
  + CVE-2021-41159 Improper client input validation for gateway connections allows to overwrite memory
  + CVE-2021-41160 Improper region checks in all clients allow out of bound write to memory

* Thu Jul 29 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.3.2-alt3
- Fixed build for Elbrus.

* Thu Jul 08 2021 Andrey Cherepanov <cas@altlinux.org> 2.3.2-alt2
- FTBFS: disable build with mbedtls-3.0.0 (https://github.com/FreeRDP/FreeRDP/issues/7163).

* Tue Mar 16 2021 Andrey Cherepanov <cas@altlinux.org> 2.3.2-alt1
- New version.

* Wed Mar 03 2021 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1
- New version.

* Thu Feb 25 2021 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt1
- New version.

* Tue Jul 21 2020 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- New version.
- Fixes:
  + CVE-2020-15103 - Integer overflow due to missing input sanitation in rdpegfx channel

* Wed Jul 01 2020 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt2
- Fix connect to Windows 7 (see https://github.com/FreeRDP/FreeRDP/issues/6299).

* Tue Jun 23 2020 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt1
- New version.
- Fixes:
  + CVE-2020-4033 Out of bound read in RLEDECOMPRESS
  + CVE-2020-4031 Use-After-Free in gdi_SelectObject
  + CVE-2020-4032 Integer casting vulnerability in `update_recv_secondary_order`
  + CVE-2020-4030 OOB read in `TrioParse`
  + CVE-2020-11099 OOB Read in license_read_new_or_upgrade_license_packet
  + CVE-2020-11098 Out-of-bound read in glyph_cache_put
  + CVE-2020-11097 OOB read in ntlm_av_pair_get
  + CVE-2020-11095 Global OOB read in update_recv_primary_order
  + CVE-2020-11096 Global OOB read in update_read_cache_bitmap_v3_order
  + Gateway RPC fixes for windows
  + Fixed resource fee race resulting in double free in USB redirection
  + Fixed wayland client crashes
  + Fixed X11 client mouse mapping issues (X11 mapping on/off)
  + Some proxy related improvements (capture module)
  + Code cleanup (use getlogin_r, ...)

* Wed May 20 2020 Andrey Cherepanov <cas@altlinux.org> 2.1.1-alt1
- New version.
- Fixes:
  + CVE: GHSL-2020-100 OOB Read in ntlm_read_ChallengeMessage
  + CVE: GHSL-2020-101 OOB Read in security_fips_decrypt due to uninitialized value
  + CVE: GHSL-2020-102 OOB Write in crypto_rsa_common

* Sun May 10 2020 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- New version (2.1.0) (Fixes: CVE-2020-11039, CVE-2020-11038, CVE-2020-11043, CVE-2020-11040, CVE-2020-11041, CVE-2020-11019, CVE-2020-11017, CVE-2020-11018).

* Fri Apr 10 2020 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt5
- New version (2.0.0) (Fixes: CVE-2020-11521, CVE-2020-11522, CVE-2020-11523, CVE-2020-11524, CVE-2020-11525, CVE-2020-11526).

* Wed Nov 20 2019 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt4.git20190806
- Enable support of icu and vaapi.
- Build liburbdrc-client.so (ALT #34230).
- Change maintainer.
- Set package license according to SPDX.

* Mon Aug 12 2019 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt3.git20190806
- New snapshot from upstream git repository.
- Build from upstream git.
- Enable support of ffmpeg, wayland, mbedtls, gsm, lame, faad, faac, soxr.

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2.git20181120
- NMU: remove rpm-build-ubt from BR:

* Wed Nov 21 2018 Pavel Nakonechnyi <zorg@altlinux.org> 2.0.0-alt1.git20181120
- Fifth release candidate for 2.0.0:
- multiple CVE fixes
- various bugfixes and improvements

* Thu Aug 30 2018 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1.git20180801.S1.1
- NMU: Rebuild with new openssl 1.1.0.

* Thu Aug 02 2018 Pavel Nakonechnyi <zorg@altlinux.org> 2.0.0-alt1.git20180801.S1
- Fourth release candidate for 2.0.0

* Tue Apr 17 2018 Pavel Nakonechnyi <zorg@altlinux.org> 2.0.0-alt1.git20180411.S1
- Third release candidate for 2.0.0
- Fix gstreamer-1.0 detection is not needed now

* Tue Sep 26 2017 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1.git20170724.S1
- Fix gstreamer-1.0 detection
- increase release number for allow backport to p8

* Wed Jul 26 2017 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt0.git20170724
- First release candidate for 2.0.0

* Wed Jan 11 2017 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt0.git20170109.2
- move libfreerdp-shadow.so.* to libfreerdp-server package

* Tue Jan 10 2017 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt0.git20170109
- upstream git snapshot 8fd926f08524bcdad8adbb5d908ebb1ad2ce6106

* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt0.git20160411
- upstream git snapshot 11d113872fe254a2472e99a40f8be7237d5a82d3

* Wed Apr 06 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt0.git20160331
- upstream git snapshot a0d9969a3030a8056eacbe8b2e7362274d0a9c4b
- drop directfb dfreerdp package
- build with wayland support
- build with gstreamer-1.0 support
- split libwinpr,librdtk,libuwac library and devel files
- build server package

* Mon Jun 15 2015 Mikhail Kolchin <mvk@altlinux.org> 1.1.0-alt2.beta1
- disable gstreamer support (ALT #31013)

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
