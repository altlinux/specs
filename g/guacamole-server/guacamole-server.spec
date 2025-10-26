%define _unpackaged_files_terminate_build 1
%define abiversion 25
%define abiversion_terminal 2
%define soname %abiversion.0.0
%define soname_terminal %abiversion_terminal.0.0
%define username guacd
%def_with ffmpeg

Name: guacamole-server
Version: 1.6.0
Release: alt2

Summary: Server-side native components that form the Guacamole proxy
License: Apache-2.0
Group: Networking/Remote access
Url: https://guacamole.apache.org
VCS: https://github.com/apache/guacamole-server.git

Source0: %name-%version.tar
Source1: %name.sysconfig
Source2: %name.service
Source3: %name.conf
Patch: %name-%version.patch
# FAIL: test_libguac 65 - [socket] nested_send_instruction: Assertion failed
Patch1: guacamole-server-1.6.0-fix-nested-socket-initialization.patch
# From Fedora:
# src/libguac/wol.c: inet_pton called with a destination buffer size too small
# https://issues.apache.org/jira/browse/GUACAMOLE-2087
Patch2: guacamole-server-1.6.0-guacamole-2070.patch

Requires: guacd
Requires: libguac-client-ssh
Requires: libguac-client-rdp
Requires: libguac-client-vnc

BuildRequires: perl-Term-ReadLine-Gnu
BuildRequires: doxygen graphviz
BuildRequires: libjpeg-devel
BuildRequires: libwebsockets-devel
BuildRequires: systemd-devel
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(freerdp3)
BuildRequires: pkgconfig(freerdp-client3)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libssh2) >= 1.9.0
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(libtelnet)
BuildRequires: pkgconfig(libvncserver)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(vorbis)
BuildRequires: libwinpr3-devel
# for test
BuildRequires: CUnit-devel

%if_with ffmpeg
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libswscale)
%endif

%description
Guacamole is an HTML5 remote desktop gateway.

Guacamole provides access to desktop environments using remote desktop protocols
like VNC and RDP. A centralized server acts as a tunnel and proxy, allowing
access to multiple desktops through a web browser.

No browser plugins are needed, and no client software needs to be installed. The
client requires nothing more than a web browser supporting HTML5 and AJAX.

The main web application is provided by the "guacamole-client" package.

This is virtual package with depends on:
- guacd
- libguac-client-ssh
- libguac-client-rdp
- libguac-client-vnc

%package -n libguac%abiversion
Summary: The common library used by all C components of Guacamole
Group: System/Libraries
# monospace font for telnet, ssh, kubernetes
Requires: fonts-ttf-liberation
Obsoletes: libguac = 1.6.0

%description -n libguac%abiversion
libguac is the core library for guacd (the Guacamole proxy) and any protocol
support plugins for guacd. libguac provides efficient buffered I/O of text and
base64 data, as well as somewhat abstracted functions for sending Guacamole
instructions.

%package -n libguac-terminal%abiversion_terminal
Summary: Plugin for the Guacamole proxy which provides support for Terminal
Group: System/Libraries
Obsoletes: libguac = 1.6.0

%description -n libguac-terminal%abiversion_terminal
Is a protocol support plugin for the Guacamole proxy (guacd) which provides
support for Terminal via the libterminal library.

%package -n libguac-devel
Summary: Development files for %name
Group: Development/C
Requires: libguac%abiversion = %EVR

%description -n libguac-devel
The libguac-devel package contains libraries and header files for
developing applications that use %name.

%package -n libguac-client-kubernetes
Summary: Kubernetes pods terminal support for guacd
Group: System/Libraries
Requires: libguac%abiversion = %EVR

%description -n libguac-client-kubernetes
libguac-client-kubernetes is a protocol support plugin for the Guacamole proxy
(guacd) which provides support for attaching to terminals of containers running
in Kubernetes pods.

%package -n libguac-client-rdp
Summary: RDP support for guacd
Group: System/Libraries
Requires: libguac%abiversion = %EVR

%description -n libguac-client-rdp
libguac-client-rdp is a protocol support plugin for the Guacamole proxy (guacd)
which provides support for RDP, the proprietary remote desktop protocol used by
Windows Remote Deskop / Terminal Services, via the libfreerdp library.

%package -n libguac-client-ssh
Summary: SSH support for guacd
Group: System/Libraries
Requires: libguac%abiversion = %EVR

%description -n libguac-client-ssh
libguac-client-ssh is a protocol support plugin for the Guacamole proxy (guacd)
which provides support for SSH, the secure shell.

%package -n libguac-client-vnc
Summary: VNC support for guacd
Group: System/Libraries
Requires: libguac%abiversion = %EVR

%description -n libguac-client-vnc
libguac-client-vnc is a protocol support plugin for the Guacamole proxy (guacd)
which provides support for VNC via the libvncclient library (part of
libvncserver).

%package -n libguac-client-telnet
Summary: Telnet support for guacd
Group: System/Libraries
Requires: libguac%abiversion = %EVR

%description -n libguac-client-telnet
libguac-client-telnet is a protocol support plugin for the Guacamole proxy
(guacd) which provides support for Telnet via the libtelnet library.

%package -n guacd
Summary: Proxy daemon for Guacamole
Group: Networking/Remote access
Requires: libguac%abiversion = %EVR

%description -n guacd
guacd is the Guacamole proxy daemon used by the Guacamole web application and
framework to translate between arbitrary protocols and the Guacamole protocol.

%prep
%setup
%autopatch -p1

%build
%add_optflags -Wno-error=deprecated-declarations
%autoreconf
%configure \
  --disable-silent-rules \
  --disable-static

%make_build
for i in libguac libguac-terminal; do
    pushd doc/$i
    doxygen Doxyfile
    popd
done

%install
%makeinstall_std
find %buildroot -type f -name "*.la" -delete
mkdir -p html
for i in libguac libguac-terminal; do
    cp -fr doc/$i/doxygen-output/html html/$i
done

mkdir -p %buildroot%_sysconfdir/sysconfig
install -p -m 644 -D %SOURCE1 %buildroot%_sysconfdir/sysconfig/guacd
mkdir -p %buildroot%_sharedstatedir/guacd/share

# Systemd unit files
mkdir -p %buildroot%_unitdir
install -p -m 644 -D %SOURCE2 %buildroot%_unitdir/guacd.service

# Config
mkdir -p %buildroot%_sysconfdir/guacamole
install -p -m 644 -D %SOURCE3 %buildroot%_sysconfdir/guacamole/guacd.conf

%check
%make check

%pre -n guacd
groupadd -r -f %username 2>/dev/null ||:
useradd -r -g %username -c 'Guacamole proxy daemon' \
        -s /sbin/nologin -d %_sharedstatedir/guacd -M %username 2>/dev/null ||:

%post -n guacd
%post_service guacd.service

%preun -n guacd
%preun_service guacd.service

%files
%nil

%files -n libguac%abiversion
%doc LICENSE
%doc README CONTRIBUTING
%_libdir/libguac.so.%abiversion
%_libdir/libguac.so.%soname

%files -n libguac-terminal%abiversion_terminal
%_libdir/libguac-terminal.so.%abiversion_terminal
%_libdir/libguac-terminal.so.%soname_terminal

%files -n libguac-devel
%doc html
%_includedir/*
%_libdir/libguac.so
%_libdir/libguac-terminal.so

# The libguac source code dlopen's these plugins, and they are named without
# the version in the shared object; i.e. "libguac-client-$(PROTOCOL).so".

%files -n libguac-client-kubernetes
%_libdir/libguac-client-kubernetes.so
%_libdir/libguac-client-kubernetes.so.*

%files -n libguac-client-rdp
%_libdir/libguac-client-rdp.so
%_libdir/libguac-client-rdp.so.*
%_libdir/freerdp3/*.so

%files -n libguac-client-ssh
%_libdir/libguac-client-ssh.so
%_libdir/libguac-client-ssh.so.*

%files -n libguac-client-vnc
%_libdir/libguac-client-vnc.so
%_libdir/libguac-client-vnc.so.*

%files -n libguac-client-telnet
%_libdir/libguac-client-telnet.so
%_libdir/libguac-client-telnet.so.*

%files -n guacd
%config(noreplace) %_sysconfdir/sysconfig/guacd
%dir %_sysconfdir/guacamole
%config(noreplace) %_sysconfdir/guacamole/guacd.conf
%_bindir/guaclog
%if_with ffmpeg
%_bindir/guacenc
%_mandir/man1/guacenc.1.*
%endif
%_mandir/man1/guaclog.1.*
%_mandir/man5/guacd.conf.5.*
%_mandir/man8/guacd.8.*
%_sbindir/guacd
%_unitdir/guacd.service
%attr(750,%username,%username) %_sharedstatedir/guacd
%attr(750,%username,%username) %_sharedstatedir/guacd/share

%changelog
* Sun Oct 26 2025 Constantin Sunzow <protvin@altlinux.org> 1.6.0-alt2
- Split libguac with complience SharedLibsPolicy.
- Fix FTBFS.

* Tue Aug 05 2025 Constantin Sunzow <protvin@altlinux.org> 1.6.0-alt1
- New version.

* Sun May 19 2024 Alexey Shabalin <shaba@altlinux.org> 1.5.5-alt1
- New version 1.5.5.

* Mon Dec 25 2023 Alexander Burmatov <thatman@altlinux.org> 1.5.4-alt1
- New version 1.5.4 (Fixes: CVE-2023-43826).

* Mon Oct 02 2023 Alexey Shabalin <shaba@altlinux.org> 1.5.3-alt2
- Add requires to fonts-ttf-liberation (ALT#47735).

* Fri Aug 18 2023 Alexey Shabalin <shaba@altlinux.org> 1.5.3-alt1
- New version 1.5.3 (Fixes: CVE-2023-30575, CVE-2023-30576).

* Tue Dec 20 2022 Alexey Shabalin <shaba@altlinux.org> 1.4.0-alt3
- package /var/lib/guacd/share for file sharing

* Mon Nov 14 2022 Alexey Shabalin <shaba@altlinux.org> 1.4.0-alt2
- Add requires on freerdp-plugins-standard for libguac-client-rdp package.

* Thu Oct 13 2022 Alexey Shabalin <shaba@altlinux.org> 1.4.0-alt1
- new version 1.4.0

* Thu Apr 15 2021 Alexey Shabalin <shaba@altlinux.org> 1.3.0-alt3
- Build with libuuid instead ossp-uuid.

* Mon Apr 05 2021 Alexey Shabalin <shaba@altlinux.org> 1.3.0-alt2
- fix build with freerdp-2.0.0

* Tue Jan 19 2021 Alexey Shabalin <shaba@altlinux.org> 1.3.0-alt1
- new version 1.3.0

* Tue Dec 08 2020 Alexey Shabalin <shaba@altlinux.org> 1.2.0-alt2
- Add virtual package guacamole-server with depends on:
  + guacd
  + libguac-client-ssh
  + libguac-client-rdp
  + libguac-client-vnc

* Wed Nov 18 2020 Alexey Shabalin <shaba@altlinux.org> 1.2.0-alt1
- Initial build
