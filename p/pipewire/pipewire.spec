%def_disable snapshot

%define _libexecdir %_prefix/libexec
%define ver_major 0.1
%define api_ver 0.1

%def_enable systemd

Name: pipewire
Version: %ver_major.5
Release: alt1

Summary: Media Sharing Server
Group: System/Servers
License: LGPLv2.1
Url: http://www.freedesktop.org/wiki/Software/PipeWire

%if_disabled snapshot
Source: http://freedesktop.org/software/%name/releases/%name-%version.tar.gz
%else
# VCS:  https://github.com/wtay/pipewire.git
Source: %name-%version.tar
%endif

Requires: %name-libs = %version-%release
Requires: rtkit

%define gst_ver 1.10

BuildRequires: meson >= 0.35.0
BuildRequires: libgio-devel libudev-devel libdbus-devel
BuildRequires: pkgconfig(gstreamer-1.0) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-base-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(gstreamer-net-1.0)
BuildRequires: pkgconfig(gstreamer-allocators-1.0)
%{?_enable_systemd:BuildRequires: libsystemd-devel}
BuildRequires: libalsa-devel libv4l-devel
BuildRequires: libavformat-devel libavcodec-devel libavfilter-devel
BuildRequires: libjack-devel
BuildRequires: doxygen xmltoman graphviz

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
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -n -g %name -d / \
	-s /dev/null -c "PipeWire System Daemon" %name 2>/dev/null ||:

%files
%_bindir/%name
%_libdir/gstreamer-1.0/libgst%name.so
%dir %_sysconfdir/%name/
%_sysconfdir/%name/%name.conf
%if_enabled systemd
%_prefix/lib/systemd/user/pipewire.service
%_prefix/lib/systemd/user/pipewire.socket
%endif
%_man1dir/%name.1*
%doc README

%files libs
%_libdir/lib%name-%api_ver.so.*
%_libdir/libspa-lib.so.*
%_libdir/%name-%api_ver/
%_libdir/spa/

%files libs-devel
%_libdir/lib%name-%api_ver.so
%_libdir/libspa-lib.so
%_includedir/%name/
%_includedir/spa/
%_pkgconfigdir/lib%name-%api_ver.pc
%_pkgconfigdir/libspa-%api_ver.pc

%files libs-devel-doc
%_datadir/doc/%name/html

%files utils
%_bindir/%name-monitor
%_bindir/%name-cli
%_bindir/spa-monitor
%_bindir/spa-inspect
%_man1dir/%name-monitor.1*
%_man1dir/%name-cli.1*

%changelog
* Tue Sep 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt1
- first build for Sisyphus

