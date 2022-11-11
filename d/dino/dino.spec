%def_disable snapshot

%define rdn_name im.dino.Dino

Name: dino
Version: 0.3.1
Release: alt1

Summary: Modern Jabber/XMPP client
License: GPL-3.0
Group: Networking/Instant messaging
Url: https://dino.im

%if_disabled snapshot
Source: https://github.com/%name/%name/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

%define gst_api_ver 1.0
%define webrtc_ver 0.2
%define qrencode_ver 4.0

Requires: lib%name = %EVR
# VPx codecs
Requires: gst-plugins-good%gst_api_ver

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ vala-tools libgtk+3-devel libgee0.8-devel
BuildRequires: libsoup3.0-devel libidn2-devel
BuildRequires: libicu-devel pkgconfig(libqrencode) >= %qrencode_ver 
BuildRequires: gst-plugins%gst_api_ver-devel libnice-devel
BuildRequires: pkgconfig(webrtc-audio-processing) >= %webrtc_ver
BuildRequires: libgcrypt-devel libgpgme-devel libgnutls-devel
BuildRequires: libsignal-protocol-c-devel libsqlite3-devel libsrtp2-devel
BuildRequires: libenchant-devel libgspell-devel

%description
Dino is a modern open-source chat client for the desktop. It focuses on
providing a clean and reliable Jabber/XMPP experience while having your
privacy in mind.

%package -n lib%name
Summary: Dino shared libraries
Group: System/Libraries

%description -n lib%name
Dino is a modern open-source chat client for the desktop.
This package provides shared libraries for Dino.

%package -n lib%name-devel
Summary: Development files for Dino libraries
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Dino is a modern open-source chat client for the desktop.
This package provides libraries and headers needed to develop Dino plugins.

%prep
%setup -n %name-%version

%build
%cmake
# SMP-incompatible build
%cmake_build -j1

%install
%cmake_install
%find_lang --all-name --output=%name.lang %name


%files -f %name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/metainfo/%rdn_name.appdata.xml
%_iconsdir/hicolor/*/*/*.svg
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/http-files.so
%_libdir/%name/plugins/omemo.so
%_libdir/%name/plugins/openpgp.so
%_libdir/%name/plugins/ice.so
%_libdir/%name/plugins/rtp.so
%doc README*

%files -n lib%name
%_libdir/lib%name.so.*
%_libdir/libqlite.so.*
%_libdir/libxmpp-vala.so.*
%_libdir/libcrypto-vala.so.*

%files -n lib%name-devel
%_includedir/*.h
%_libdir/lib%name.so
%_libdir/libqlite.so
%_libdir/libxmpp-vala.so
%_libdir/libcrypto-vala.so
#%_datadir/vala/vapi/crypto-vala.deps
#%_datadir/vala/vapi/crypto-vala.vapi
#%_datadir/vala/vapi/dino.deps
#%_datadir/vala/vapi/dino.vapi
#%_datadir/vala/vapi/qlite.deps
#%_datadir/vala/vapi/qlite.vapi
#%_datadir/vala/vapi/xmpp-vala.deps
#%_datadir/vala/vapi/xmpp-vala.vapi

%changelog
* Fri Nov 11 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Wed May 04 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1.1
- updated {build,}dependencies

* Tue Mar 01 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Thu Sep 23 2021 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- 0.2.2

* Mon Jun 07 2021 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1 (fixed CVE-2021-33896)

* Tue May 11 2021 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt2.1
- rebuild with new cmake macros

* Tue Apr 13 2021 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt2
- fixed build with vala >= 0.50.4 (upstream patch)

* Fri Nov 13 2020 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- 0.2.0

* Sat Oct 31 2020 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt3
- updated to v0.1.0-157-gdba63b1

* Mon Aug 03 2020 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt2
- updated to v0.1.0-125-gff9a9a0

* Fri Jan 31 2020 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- first build for Sisyphus

