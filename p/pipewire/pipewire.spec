%def_disable snapshot
%define _unpackaged_files_terminate_build 1

%ifarch armh
%define optflags_lto %nil
%endif

%define _libexecdir %prefix/libexec
%define ver_major 1.2
%define ms_ver 0.4.2
%define api_ver 0.3
%define spa_api_ver 0.2
%define gst_api_ver 1.0
%define libcamera_ver 0.2.0

%def_enable gstreamer
%def_enable systemd
%def_enable jack_devel
%define jackit_ver 1:1.9.22-alt1
%define jack_ver 1.9.17
%def_disable wireplumber
%def_enable libusb
%def_enable libffado
%def_enable libcamera
%def_enable avahi
%def_enable webrtc
%def_enable sdl
%def_enable lv2
%def_enable libcanberra
%def_enable lc3
# bluez5-backend-native-mm
# https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/1379
%def_enable mm
#system service: not recommended and disabled by default
%def_disable systemd_system_service
%def_enable selinux
# disabled by default
%def_disable vulkan
# libapparmor required
%def_disable snap
%ifarch %e2k
%def_disable examples
%else
%def_enable examples
%endif
%def_disable docs
%def_enable man
%def_enable check

Name: pipewire
Version: %ver_major.6
Release: alt1

Summary: Media Sharing Server
Group: System/Servers
License: MIT
Url: https://pipewire.org/

Vcs: https://github.com/PipeWire/pipewire.git

%if_disabled snapshot
Source: https://github.com/PipeWire/pipewire/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
#https://gitlab.freedesktop.org/pipewire/media-session.git
# 0.4.1-15
Source1: media-session-%ms_ver.tar
Patch: %name-0.3.19-alt-rpath.patch

Requires: %name-libs = %EVR
%{?_enable_wireplumber:Requires: wireplumber}
Requires: rtkit
%{?_enable_gstreamer:%{?_enable_libcamera:Requires: gst-plugins-libcamera1.0}}

%define meson_ver 0.59
%define gst_ver 1.10
%define mm_ver 1.10.0

BuildRequires(pre): rpm-macros-meson rpm-build-systemd
BuildRequires: meson >= %meson_ver libgio-devel libudev-devel libdbus-devel
BuildRequires: libalsa-devel libpulseaudio-devel
BuildRequires: libv4l-devel libsamplerate-devel libsndfile-devel
BuildRequires: libavformat-devel libavcodec-devel libavfilter-devel
BuildRequires: libbluez-devel
BuildRequires: libmysofa-devel
# BT codecs
BuildRequires: libsbc-devel libfdk-aac-devel libldac-devel
BuildRequires: libfreeaptx-devel libopus-devel
%{?_enable_lc3:BuildRequires: liblc3-devel}
%{?_enable_mm:BuildRequires: pkgconfig(ModemManager) >= %mm_ver}
# LC3plus BT codec
# BuildRequires: lc3plus-devel
# for pw-top
BuildRequires: libncursesw-devel libncurses-devel
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
%{?_enable_libffado:BuildRequires: pkgconfig(libffado)}
%{?_enable_libcamera:BuildRequires: libcamera-devel >= %libcamera_ver libdrm-devel}
%{?_enable_avahi:BuildRequires: pkgconfig(avahi-client)}
%{?_enable_webrtc:BuildRequires: pkgconfig(webrtc-audio-processing-1)}
%{?_enable_sdl:BuildRequires: libSDL2-devel}
%{?_enable_lv2:BuildRequires: liblilv-devel}
%{?_enable_libcanberra:BuildRequires: libcanberra-devel}
%{?_enable_selinux:BuildRequires: libselinux-devel}
%{?_enable_snap:BuildRequires: pkgconfig(snapd-glib-2) pkgconfig(libapparmor)}
%{?_enable_docs:BuildRequires: doxygen graphviz /usr/bin/dot fonts-otf-adobe-source-sans-pro fonts-ttf-google-droid-sans}
%{?_enable_man:BuildRequires: doxygen}
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
Requires: %name-libs = %EVR

%description libs-devel
Headers and libraries for developing applications that can communicate with
a PipeWire media server.

%package libs-devel-doc
Summary: PipeWire media server documentation
Group: Documentation
# https://bugzilla.altlinux.org/34101
# "dot output is inconsistent across architectures"
BuildArch: noarch
Conflicts: %name-libs-devel < %version

%description libs-devel-doc
This package contains documentation for the PipeWire media server.

%package utils
Summary: PipeWire media server utilities
Group: System/Servers
Requires: %name-libs = %EVR

%description utils
This package contains command line utilities for the PipeWire media server.

%package jack
Summary: PipeWire JACK
Group: System/Servers
Requires: %name-jack-libs = %EVR
Conflicts: jack-audio-connection-kit
Obsoletes: jack-audio-connection-kit < %jackit_ver
Obsoletes: jackd < %jackit_ver
Provides: jackd = %EVR

%description jack
This package provides a JACK implementation based on PipeWire.

%package jack-libs
Summary: PipeWire JACK libraries
Group: System/Libraries
Requires: %name-libs = %EVR
Conflicts: libjack
Obsoletes: libjack < %jackit_ver

%description jack-libs
This package provides PipeWire JACK libraries

%package jack-libs-devel
Summary: development files for PipeWire JACK
Group: Development/C
Requires: %name-libs-devel = %EVR
Requires: %name-jack-libs = %EVR
Conflicts: libjack-devel
Obsoletes: libjack-devel < %jackit_ver
Provides: jackit-devel = %jack_ver
Provides: libjack-devel = %jack_ver

%description jack-libs-devel
This package provides development files for PipeWire JACK.

%prep
%setup -a1

%ifarch %e2k
# no attribute cleanup in C++ mode, but it's only used in C sources
sed -i 's/__has_attribute(__cleanup__)/!defined(__cplusplus)/' spa/include/spa/utils/cleanup.h
sed -i -E 's/static const char \*const (.*) =/#define \1 /;T;:a;s/;$//;t;s/$/\\/;n;ba' \
    src/modules/module-protocol-pulse/modules/module-*.c
%endif

mv media-session-%ms_ver subprojects/media-session

%build
export LIB=%_lib
%meson \
	%{subst_enable_meson_feature docs docs} \
	%{subst_enable_meson_feature man man} \
	%{subst_enable_meson_bool jack_devel jack-devel} \
	%{subst_enable_meson_feature gstreamer gstreamer} \
	%{subst_enable_meson_feature vulkan vulkan} \
	%{subst_enable_meson_feature libusb libusb} \
	%{subst_enable_meson_feature libffado libffado} \
	%{subst_enable_meson_feature libcamera libcamera} \
	%{subst_enable_meson_feature avahi avahi} \
	%{subst_enable_meson_feature webrtc echo-cancel-webrtc} \
	%{subst_enable_meson_feature sdl sdl2} \
	%{subst_enable_meson_feature lv2 lv2} \
	%{subst_enable_meson_feature libcanberra libcanberra} \
	%{subst_enable_meson_feature lc3 bluez5-codec-lc3} \
	%{subst_enable_meson_feature mm bluez5-backend-native-mm} \
	%{subst_enable_meson_feature systemd systemd} \
	%{subst_enable_meson_feature selinux selinux} \
	%{subst_enable_meson_feature snap snap} \
	%{subst_enable_meson_feature systemd_system_service systemd-system-service} \
	%{subst_enable_meson_feature examples examples} \
	-Dsession-managers='media-session' \
	-Dudevrulesdir='%_udevrulesdir' \
	-Dsystemd-system-unit-dir='%_unitdir' \
	-Dsystemd-user-unit-dir='%_userunitdir'
%nil
%meson_build

%install
%meson_install
mkdir -p %buildroot%_sysconfdir/%name/{media-session.d,filter-chain}
%find_lang %name media-session --output=%name.lang

# https://bugzilla.altlinux.org/47286
mkdir -p %buildroot%_sysconfdir/ld.so.conf.d/
echo %_libdir/pipewire-%api_ver/jack/ > %buildroot%_sysconfdir/ld.so.conf.d/pipewire-jack-%_arch.conf

%check
%__meson_test

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -N -g %name -d / \
	-s /dev/null -c "PipeWire System Daemon" %name 2>/dev/null ||:

%files -f %name.lang
%_bindir/%name
%_bindir/%name-aes67
%_bindir/%name-avb
%_bindir/%name-pulse
%{?_enable_vulkan:%_bindir/%name-vulkan}
%_bindir/%name-media-session
%{?_enable_gstreamer:%_libdir/gstreamer-%gst_api_ver/libgst%name.so}
%_sysconfdir/security/limits.d/25-pw-rlimits.conf
%dir %_sysconfdir/%name/
%dir %_sysconfdir/%name/media-session.d
%dir %_sysconfdir/%name/filter-chain
%dir %_datadir/%name
%_datadir/%name/%name.conf
%_datadir/%name/%name-aes67.conf
%_datadir/%name/client.conf
%_datadir/%name/client-rt.conf

%_datadir/%name/minimal.conf
%_datadir/%name/%name-avb.conf
%_datadir/%name/%name-pulse.conf
%{?_enable_vulkan:%_datadir/%name/%name-vulkan.conf}
%_datadir/%name/filter-chain.conf

%dir %_datadir/%name/client-rt.conf.avail
%_datadir/%name/client-rt.conf.avail/20-upmix.conf

%dir %_datadir/%name/client.conf.avail
%_datadir/%name/client.conf.avail/20-upmix.conf

%dir %_datadir/%name/%name-pulse.conf.avail
%_datadir/%name/%name-pulse.conf.avail/20-upmix.conf

%dir %_datadir/%name/%name.conf.avail
%_datadir/%name/%name.conf.avail/10-rates.conf
%_datadir/%name/%name.conf.avail/20-upmix.conf

%dir %_datadir/%name/media-session.d
%_datadir/%name/media-session.d/alsa-monitor.conf
%_datadir/%name/media-session.d/bluez-monitor.conf
%_datadir/%name/media-session.d/media-session.conf
%_datadir/%name/media-session.d/v4l2-monitor.conf

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
%_man5dir/%name.conf.5*
%_man5dir/%name-pulse.conf.5*
%_man5dir/%name-client.conf.5.xz
%_man5dir/%name-filter-chain.conf.5.xz
%_man5dir/%name-jack.conf.5.xz
%endif
%doc README* NEWS

%files libs
%_libdir/lib%name-%api_ver.so.*
%_libdir/%name-%api_ver/
%exclude %_libdir/%name-%api_ver/jack
%_libdir/spa-%spa_api_ver/
%_libdir/alsa-lib/

%files libs-devel
%_libdir/lib%name-%api_ver.so
%_includedir/%name-%api_ver/
%_includedir/spa-%spa_api_ver/
%_pkgconfigdir/lib%name-%api_ver.pc
%_pkgconfigdir/libspa-%spa_api_ver.pc
%_man7dir/*

%if_enabled docs
%files libs-devel-doc
%dir %_datadir/doc/%name
%_datadir/doc/%name/html/
%endif

%files utils
%_bindir/pw-cat
%_bindir/pw-cli
%_bindir/pw-config
%_bindir/pw-container
%_bindir/pw-dot
%_bindir/pw-dsdplay
%_bindir/pw-dump
%_bindir/pw-encplay
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
%_bindir/pw-reserve
%_bindir/pw-top
%_bindir/pw-v4l2
%_bindir/spa-acp-tool
%_bindir/spa-inspect
%_bindir/spa-json-dump
%_bindir/spa-monitor
%_bindir/spa-resample
%if_enabled man
%_man1dir/pw-cat.1.*
%_man1dir/pw-cli.1*
%_man1dir/pw-config.1*
%_man1dir/pw-container.1*
%_man1dir/pw-dot.1.*
%_man1dir/pw-dump.1.*
%_man1dir/pw-link.1.*
%_man1dir/pw-loopback.1.*
%_man1dir/pw-metadata.1.*
%_man1dir/pw-mididump.1.*
%_man1dir/pw-mon.1*
%_man1dir/pw-profiler.1.*
%_man1dir/pw-reserve.1*
%_man1dir/pw-top.1.*
%_man1dir/pw-v4l2.1*
%_man1dir/spa-acp-tool.1*
%_man1dir/spa-inspect.1*
%_man1dir/spa-json-dump.1*
%_man1dir/spa-monitor.1*
%_man1dir/spa-resample.1*
%endif

%files jack
%_bindir/pw-jack
%_datadir/%name/jack.conf
%_datadir/%name/media-session.d/with-jack
%{?_enable_man:%_man1dir/pw-jack.1*}

%files jack-libs
%_sysconfdir/ld.so.conf.d/%name-jack-%_arch.conf
%_libdir/%name-%api_ver/jack/*.so.*

%files jack-libs-devel
%_includedir/jack/
%_libdir/%name-%api_ver/jack/*.so
%_pkgconfigdir/jack.pc


%changelog
* Wed Oct 23 2024 Yuri N. Sedunov <aris@altlinux.org> 1.2.6-alt1
- 1.2.6

* Tue Oct 15 2024 Yuri N. Sedunov <aris@altlinux.org> 1.2.5-alt1.1
- E2K: ftbfs workaround by ilyakurdyukov@

* Fri Sep 27 2024 Yuri N. Sedunov <aris@altlinux.org> 1.2.5-alt1
- 1.2.5

* Thu Sep 19 2024 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4

* Thu Aug 22 2024 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Wed Jul 31 2024 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Fri Jul 12 2024 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Thu Jun 27 2024 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Sat Jun 22 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.7-alt1.1
- rebuilt with new systemd macros

* Fri May 24 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.7-alt1
- 1.0.7

* Thu May 09 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.6-alt1
- 1.0.6

* Mon Apr 15 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- 1.0.5

* Wed Mar 13 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt1
- 1.0.4

* Fri Feb 02 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Wed Jan 31 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Thu Jan 11 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1
- built with libcamera-0.2.0

* Thu Nov 30 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt2.2
- enabled ModemManager in native backend in bluez5 spa plugin

* Tue Nov 28 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt2.1
- E2K: ftbfs workaround by ilyakurdyukov@ (mcst#8330, #8500)

* Mon Nov 27 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt2
- rebuild against libopus with custom modes enabled
- enabled selinux support
- fixed build with -Dexamples=disabled

* Sun Nov 26 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Thu Nov 16 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.85-alt1
- 0.3.85

* Thu Nov 02 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.84-alt1
- updated to 0.3.84-2-g38157a893

* Thu Nov 02 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.83-alt1.1
- ilyakurdyukov@: fixed build for %%e2k

* Thu Oct 19 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.83-alt1
- updated to 0.3.83-1-gb92b66cf5

* Fri Oct 13 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.82-alt1
- updated to 0.3.82-8-gc94d5d9d3

* Sun Oct 08 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.81-alt1
- 0.3.81

* Thu Sep 14 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.80-alt1.1
- rebuilt against webrtc-audio-processing-1

* Thu Sep 14 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.80-alt1
- updated to 0.3.80-2-ga4f3b78df
- enabled firewire support using libffado library

* Tue Aug 29 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.79-alt1
- updated to 0.3.79-2-g6bf42e9bc

* Wed Aug 23 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.78-alt2
- new -jack* subpackages obsolete jack-audio-connection-kit

* Tue Aug 22 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.78-alt1
- updated to 0.3.78-5-gf9c21789d

* Fri Aug 04 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.77-alt1
- updated to 0.3.77-1-g140374d20

* Fri Jul 28 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.76-alt1
- 0.3.76

* Sun Jul 23 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.75-alt1
- updated to 0.3.75-1-g55812195c

* Fri Jul 14 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.74-alt1.1
- ilyakurdyukov@: fixed build for %%e2k

* Wed Jul 12 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.74-alt1
- 0.3.74

* Tue Jul 11 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.73-alt2
- updated to 0.3.73-17-g17bc9d520 (also fixed:
  "Audio randomly cuts out for no reason"
  (https://gitlab.freedesktop.org/pipewire/pipewire/-/issues/3316))

* Thu Jul 06 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.73-alt1
- 0.3.73

* Wed Jun 28 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.72-alt1.1
- updated to 0.3.72-11-gb160a7201

* Mon Jun 26 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.72-alt1
- 0.3.72

* Wed May 17 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.71-alt1
- 0.3.71

* Thu Apr 20 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.70-alt1
- 0.3.70

* Thu Apr 13 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.69-alt1
- 0.3.69

* Thu Apr 06 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.68-alt1
- 0.3.68

* Thu Mar 09 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.67-alt1
- 0.3.67

* Mon Feb 27 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.66-alt2
- updated media-session to 0.4.2 (ALT #45411)

* Thu Feb 16 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.66-alt1
- 0.3.66

* Thu Jan 26 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.65-alt1
- updated to 0.3.65 + media-session-0.4.1-22-g8ca57ad13

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

