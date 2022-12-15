%def_enable snapshot
%define _unpackaged_files_terminate_build 1

%ifarch armh
%define optflags_lto %nil
%endif

%define _libexecdir %_prefix/libexec
%define ver_major 0.3
%define ms_ver 0.4.1
%define api_ver 0.3
%define spa_api_ver 0.2
%define gst_api_ver 1.0
%define libcamera_ver 1:0.0.1

%def_enable gstreamer
%def_enable systemd
%def_disable wireplumber
%def_enable libusb
%def_enable libcamera
%def_enable avahi
%def_enable webrtc
%def_enable sdl
%def_enable lv2
%def_enable libcanberra
%def_enable lc3
#system service: not recommended and disabled by default
%def_disable systemd_system_service
%def_enable vulkan
%ifarch %e2k
%def_disable examples
%else
%def_enable examples
%endif
%def_disable docs
%def_enable man
%def_enable check

Name: pipewire
Version: %ver_major.63
Release: alt1

Summary: Media Sharing Server
Group: System/Servers
License: MIT
Url: https://pipewire.org/

%if_disabled snapshot
Source: https://github.com/PipeWire/pipewire/archive/%version/%name-%version.tar.gz
%else
Vcs: https://github.com/PipeWire/pipewire.git
Source: %name-%version.tar
%endif
#https://gitlab.freedesktop.org/pipewire/media-session.git
# 0.4.1-15
Source1: media-session-%ms_ver.tar
Patch: %name-0.3.19-alt-rpath.patch

Requires: %name-libs = %version-%release
%{?_enable_wireplumber:Requires: wireplumber}
Requires: rtkit
%{?_enable_gstreamer:%{?_enable_libcamera:Requires: gst-plugins-libcamera1.0}}

%define meson_ver 0.59
%define gst_ver 1.10

BuildRequires(pre): rpm-macros-meson rpm-build-systemd
BuildRequires: meson >= %meson_ver libgio-devel libudev-devel libdbus-devel
BuildRequires: libalsa-devel libpulseaudio-devel
BuildRequires: libjack-devel
BuildRequires: libv4l-devel libsamplerate-devel libsndfile-devel
BuildRequires: libavformat-devel libavcodec-devel libavfilter-devel
BuildRequires: libbluez-devel
# BT codecs
BuildRequires: libsbc-devel libfdk-aac-devel libldac-devel
BuildRequires: libfreeaptx-devel libopus-devel
%{?_enable_lc3:BuildRequires: liblc3-devel}
# LC3plus BT codec
# BuildRequires: lc3plus-devel
# for pw-top
BuildRequires: libncursesw-devel
# for pw-cli
BuildRequires: libreadline-devel
%if_enabled gstreamer
BuildRequires: pkgconfig(gstreamer-%gst_api_ver) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-base-%gst_api_ver)
BuildRequires: pkgconfig(gstreamer-plugins-base-%gst_api_ver)
BuildRequires: pkgconfig(gstreamer-net-%gst_api_ver)
BuildRequires: pkgconfig(gstreamer-allocators-%gst_api_ver)
%endif
%{?_enable_systemd:BuildRequires: pkgconfig(systemd)}
%{?_enable_wireplumber:BuildRequires: libwireplumber-devel}
%{?_enable_vulkan:BuildRequires: libvulkan-devel}
%{?_enable_libusb:BuildRequires: pkgconfig(libusb-1.0)}
%{?_enable_libcamera:BuildRequires: libcamera-devel >= %libcamera_ver libdrm-devel}
%{?_enable_avahi:BuildRequires: pkgconfig(avahi-client)}
%{?_enable_webrtc:BuildRequires: pkgconfig(webrtc-audio-processing)}
%{?_enable_sdl:BuildRequires: libSDL2-devel}
%{?_enable_lv2:BuildRequires: liblilv-devel}
%{?_enable_libcanberra:BuildRequires: libcanberra-devel}
%{?_enable_docs:BuildRequires: doxygen graphviz fonts-otf-adobe-source-sans-pro fonts-ttf-google-droid-sans}
%{?_enable_man:BuildRequires: python3-module-docutils}
%{?_enable_check:BuildRequires: /proc gcc-c++ libcap-devel}

%description
PipeWire is a multimedia server for Linux and other Unix like operating
systems.

%package libs
Summary: Libraries for PipeWire clients
Group: System/Libraries

%description libs
This package contains the runtime libraries for any application that wishes
to interface with a PipeWire media server.

%package libs-devel
Summary: Headers and libraries for PipeWire client development
Group: Development/C
Requires: %name-libs = %version-%release

%description libs-devel
Headers and libraries for developing applications that can communicate with
a PipeWire media server.

%package libs-devel-doc
Summary: PipeWire media server documentation
Group: Documentation
# https://bugzilla.altlinux.org/34101
BuildArch: noarch
Conflicts: %name-libs-devel < %version

%description libs-devel-doc
This package contains documentation for the PipeWire media server.

%package utils
Summary: PipeWire media server utilities
Group: System/Servers
Requires: %name-libs = %version-%release

%description utils
This package contains command line utilities for the PipeWire media server.

%prep
%setup -a1
mv media-session-%ms_ver subprojects/media-session

#echo -e "SHORT_NAMES = YES\nDIRECTORY_GRAPH = NO\n" >> doc/Doxyfile.in
#%%patch

%build
export LIB=%_lib
%meson \
	%{?_enable_docs:-Ddocs=enabled} \
	%{?_disable_man:-Dman=disabled} \
	%{?_enable_gstreamer:-Dgstreamer=enabled} \
	%{?_disable_vulkan:-Dvulkan=disabled} \
	%{?_disable_libusb:-Dlibusb=disabled} \
	%{?_disable_libcamera:-Dlibcamera=disabled} \
	%{?_disable_avahi:-Davahi=disabled} \
	%{?_disable_webrtc:-Decho-cancel-webrtc=disabled} \
	%{?_disable_sdl:-Dsdl=disabled} \
	%{?_disable_lv2:-Dlv2=disabled} \
	%{?_disable_libcanberra:-Dlibcanberra=disabled} \
	%{?_enable_lc3:-Dbluez5-codec-lc3=enabled} \
	%{?_disable_systemd:-Dsystemd=disabled} \
	%{?_enable_systemd_system_service:-Dsystemd-system-service=enabled} \
	%{?_disable_examples:-Dexamples=disabled} \
	-Dsession-managers='media-session'
%nil
%meson_build

%install
%meson_install
mkdir -p %buildroot%_sysconfdir/%name/{media-session.d,filter-chain}
%find_lang %name media-session --output=%name.lang

%check
%__meson_test

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -N -g %name -d / \
	-s /dev/null -c "PipeWire System Daemon" %name 2>/dev/null ||:

%files -f %name.lang
%_bindir/%name
%_bindir/pw-jack
%_bindir/%name-avb
%_bindir/%name-pulse
%_bindir/%name-media-session
%{?_enable_gstreamer:%_libdir/gstreamer-%gst_api_ver/libgst%name.so}
%dir %_sysconfdir/%name/
%dir %_sysconfdir/%name/media-session.d
%dir %_sysconfdir/%name/filter-chain
%dir %_datadir/%name
%_datadir/%name/%name.conf
%_datadir/%name/client.conf
%_datadir/%name/client-rt.conf
%_datadir/%name/jack.conf
%_datadir/%name/minimal.conf
%_datadir/%name/%name-avb.conf
%_datadir/%name/%name-pulse.conf
%_datadir/%name/filter-chain.conf

%dir %_datadir/%name/media-session.d
%_datadir/%name/media-session.d/alsa-monitor.conf
%_datadir/%name/media-session.d/bluez-monitor.conf
%_datadir/%name/media-session.d/media-session.conf
%_datadir/%name/media-session.d/v4l2-monitor.conf
%_datadir/%name/media-session.d/with-jack
%_datadir/%name/media-session.d/with-pulseaudio
%dir %_datadir/%name/filter-chain
%_datadir/%name/filter-chain/demonic.conf
%_datadir/%name/filter-chain/sink-dolby-surround.conf
%_datadir/%name/filter-chain/sink-eq6.conf
%_datadir/%name/filter-chain/sink-make-LFE.conf
%_datadir/%name/filter-chain/sink-matrix-spatialiser.conf
%_datadir/%name/filter-chain/sink-mix-FL-FR.conf
%_datadir/%name/filter-chain/sink-virtual-surround-5.1-kemar.conf
%_datadir/%name/filter-chain/sink-virtual-surround-7.1-hesuvi.conf
%_datadir/%name/filter-chain/source-rnnoise.conf
%_datadir/%name/filter-chain/source-duplicate-FL.conf

%dir %_datadir/spa-%spa_api_ver
%dir %_datadir/spa-%spa_api_ver/bluez5
%_datadir/spa-%spa_api_ver/bluez5/bluez-hardware.conf

%_udevrulesdir/90-%name-alsa.rules
%_datadir/alsa-card-profile/
%if_enabled systemd
%_userunitdir/%name.service
%_userunitdir/%name.socket
%_userunitdir/%name-pulse.service
%_userunitdir/%name-pulse.socket
%_userunitdir/%name-media-session.service
%_userunitdir/filter-chain.service

%{?_enable_systemd_system_service:
%_unitdir/%name.service
%_unitdir/%name.socket}
%endif
%_datadir/alsa/alsa.conf.d/50-pipewire.conf
%_datadir/alsa/alsa.conf.d/99-pipewire-default.conf
%if_enabled man
%_man1dir/%name.1*
%_man1dir/%name-pulse.1*
%_man1dir/pw-jack.1*
%_man5dir/%name.conf.5*
%endif
%doc README* NEWS

%files libs
%_libdir/lib%name-%api_ver.so.*
%_libdir/%name-%api_ver/
%_libdir/spa-%spa_api_ver/
%_libdir/alsa-lib/

%files libs-devel
%_libdir/lib%name-%api_ver.so
%_includedir/%name-%api_ver/
%_includedir/spa-%spa_api_ver/
%_pkgconfigdir/lib%name-%api_ver.pc
%_pkgconfigdir/libspa-%spa_api_ver.pc

%if_enabled docs
%files libs-devel-doc
%dir %_datadir/doc/%name
%_datadir/doc/%name/html/
%endif

%files utils
%_bindir/pw-cat
%_bindir/pw-cli
%_bindir/pw-dot
%_bindir/pw-dsdplay
%_bindir/pw-dump
%_bindir/pw-link
%_bindir/pw-loopback
%_bindir/pw-metadata
%_bindir/pw-mididump
%_bindir/pw-midiplay
%_bindir/pw-midirecord
%_bindir/pw-mon
%_bindir/pw-play
%_bindir/pw-profiler
%_bindir/pw-record
%_bindir/pw-top
%_bindir/pw-v4l2
%_bindir/pw-reserve
%_bindir/spa-inspect
%_bindir/spa-json-dump
%_bindir/spa-monitor
%_bindir/spa-resample
%_bindir/spa-acp-tool
%if_enabled man
%_man1dir/pw-cat.1.*
%_man1dir/pw-cli.1*
%_man1dir/pw-dot.1.*
%_man1dir/pw-link.1.*
%_man1dir/pw-metadata.1.*
%_man1dir/pw-mididump.1.*
%_man1dir/pw-mon.1*
%_man1dir/pw-profiler.1.*
%_man1dir/pw-top.1.*
%endif


%changelog
* Thu Dec 15 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.63-alt1
- updated to 0.3.63-2-gf7c49bbdd

* Fri Dec 09 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.62-alt1
- 0.3.62

* Thu Nov 24 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.61-alt1
- 0.3.61

* Thu Nov 10 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.60-alt1
- 0.3.60-2-g518ccdf62 + media-session-0.4.1-15-ge380ca4d7

* Mon Oct 17 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.59-alt2
- enabled libcamera support again
- enabled LC3 BT codec support

* Fri Sep 30 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.59-alt1
- 0.3.59

* Fri Sep 02 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.57-alt1
- updated to 0.3.57-3-g3f6fe3920

* Tue Jul 19 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.56-alt1
- 0.3.56

* Tue Jul 12 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.55-alt1
- 0.3.55

* Thu Jul 07 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.54-alt1
- 0.3.54

* Thu Jun 30 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.53-alt1
- 0.3.53

* Thu Jun 09 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.52-alt1
- 0.3.52

* Thu Apr 28 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.51-alt1
- updated to 0.3.51-2-gb7845bd70

* Wed Apr 13 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.50-alt1
- updated to 0.3.50-2-g339c22dce

* Tue Mar 29 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.49-alt1.1
- 0.3.49 + media-session-0.4.1-10-gf71506321

* Sat Mar 05 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.48-alt1.1
- pw-reserve is a tool, not example

* Thu Mar 03 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.48-alt1
- updated to 0.3.48-3-gce2f1b373

* Wed Mar 02 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.47-alt1
- 0.3.47

* Thu Jan 27 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.44-alt1
- updated to 0.3.44-4-gbb5c43b5b + media-session-0.4.1-8-gc0d036ebd

* Wed Jan 05 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.43-alt1
- updated to 0.3.43-3-gaf11fb480

* Tue Dec 14 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.41-alt1
- 0.3.41

* Fri Nov 12 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.40-alt1
- 0.3.40 + media-session-0.4.1-4-ge4b49a306

* Thu Oct 21 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.39-alt1
- updated to 0.3.39-1-g651f0dece + media-session-0.4.0-1-g4bf1b2954

* Fri Oct 01 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.38-alt1
- updated to 0.3.38-12-g9a76feb91

* Fri Sep 24 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.37-alt1
- updated to 0.3.37-5-gf1f5cbc0a

* Thu Sep 16 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.36-alt1
- 0.3.36

* Thu Sep 09 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.35-alt1
- 0.3.35

* Thu Aug 26 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.34-alt1
- 0.3.34
- disabled LTO for armh

* Thu Aug 05 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.33-alt1
- 0.3.33
- temporarily disabled libcamera support

* Wed Jul 21 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.32-alt1
- 0.3.32

* Mon Jun 28 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.31-alt1
- updated to 0.3.31-2-g5497d2d90

* Wed May 19 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.28-alt1
- 0.3.28

* Thu May 06 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.27-alt1
- 0.3.27

* Fri Apr 23 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.26-alt1
- updated to 0.3.26-11-gab7bc6ed

* Fri Mar 19 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.24-alt1
- updated to 0.3.24-6-gdb85339f

* Thu Mar 04 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.23-alt1
- updated to 0.3.23-2-g0ad60337

* Thu Feb 18 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.22-alt1
- 0.3.22
- lakostis@: Don't overwrite configs in /etc/pipewire
             add unowned doc dir

* Wed Feb 10 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.21-alt1.1
- enabled aptX BT codec support

* Thu Feb 04 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.21-alt1
- 0.3.21

* Thu Jan 21 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.20-alt1
- 0.3.20

* Tue Jan 05 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.19-alt1
- updated to 0.3.19-4-g18b5199d

* Tue Dec 15 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.18-alt1
- updated to 0.3.18-1-g13cb51ef

* Fri Nov 27 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.17-alt1
- 0.3.17

* Fri Nov 20 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.16-alt1
- updated to 0.3.16-1-g4d085816

* Wed Nov 04 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.15-alt1
- updated to 0.3.15-2-g7a437696

* Sat Oct 31 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.14-alt1
- 0.3.14

* Mon Sep 28 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.13-alt1
- updated to 0.3.13-1-g81ca70af

* Sat Sep 19 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.12-alt1
- updated to 0.3.12-4-g99b3f4a6

* Fri Sep 11 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.11-alt1
- updated to 0.3.11-1-gc979f181

* Tue Aug 04 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.9-alt1
- updated to 0.3.9-7-g92901379

* Wed Jul 29 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.8-alt1
- updated to 0.3.8-1-gc04d57d5

* Tue Jul 21 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.7-alt1
- updated to 0.3.7-5-gcc0727e6

* Wed Jun 10 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.6-alt1
- updated to 0.3.6-5-gda9d17e7

* Tue May 12 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.5-alt1
- updated 0.3.5-2-gfdb3985f

* Fri May 01 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.4-alt1
- updated to 0.3.4-5-gf11cd322

* Fri Mar 27 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Tue Mar 24 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt3
- made examples build optional and disabled on %%e2k (
  Checking for function "memfd_create" : NO)

* Mon Mar 23 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt2
- made vulkan support optional
- fixed License tag

* Sun Mar 08 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Fri Sep 27 2019 Yuri N. Sedunov <aris@altlinux.org> 0.2.7-alt1
- 0.2.7

* Mon May 27 2019 Yuri N. Sedunov <aris@altlinux.org> 0.2.6-alt1
- updated to 0.2.6-1-g37613b67

* Mon May 06 2019 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1.2
- fixed build without docs

* Mon May 06 2019 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1.1
- fixed build without mans

* Mon Dec 24 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1
- updated to 0.2.5-2-gf8b156ac

* Fri Nov 23 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2.4-alt1
- 0.2.4

* Fri Sep 21 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- updated to 0.2.3-7-g58efa8c2

* Sat Aug 04 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- 0.2.2

* Mon Jun 04 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.9-alt2
- rebuilt with ffmpeg-4.0

* Fri Mar 02 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.9-alt1
- 0.1.9

* Thu Jan 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.8-alt1
- 0.1.8

* Sun Nov 26 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt1
- 0.1.7

* Mon Nov 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.6-alt1
- 0.1.6

* Tue Sep 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt1
- first build for Sisyphus

