# SPEC-file for Janus WebRTC server

%def_with    websockets
%def_without aes_gcm

Name: janus
Version: 1.1.0
Release: alt1

Summary: Janus WebRTC Server

License: %gpl3only
Group: Networking/Other
URL: https://github.com/meetecho/janus-gateway
#URL: https://janus.conf.meetecho.com/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Source1: %name.service

Patch1: janus-0.10.0-debian-2004_avoid_stun_privacy_breach.patch
Patch2: janus-0.10.0-debian-2005_avoid_npm.patch
Patch3: janus-0.10.0-debian-2006_avoid_doc_privacy_breach.patch
Patch4: janus-0.10.0-debian-2002_force_tolerate_recent_doxygen.patch


BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sat May 23 2020
# optimized out: fontconfig glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libavcodec-devel libavutil-devel libcairo-gobject libgdk-pixbuf libgio-devel libgpg-error libgupnp-igd libopencore-amrnb0 libopencore-amrwb0 libp11-kit libsasl2-3 libssl-devel libx265-176 perl pkg-config python-modules python2-base python3 python3-base python3-dev ruby ruby-stdlibs sh4
BuildRequires: doxygen fonts-bitmap-cyrillic fonts-ttf-dejavu gengetopt glibc-devel-static graphviz libavformat-devel libconfig-devel libcurl-devel libjansson-devel libmicrohttpd-devel libnice-devel libogg-devel libpcap-devel libsrtp2-devel zlib-devel
BuildRequires: libssl-devel

%{?_with_websockets:BuildRequires: libwebsockets-devel}

%description
Janus is a general purpose WebRTC Gateway with a minimal footprint.

As such, it provides no functionality per se other than implementing
the means to set up a WebRTC media communication with a browser,
exchanging JSON messages with it, and relaying RTP/RTCP and messages
between browsers and the server-side application logic they are
attached to. Any specific feature/application are implemented in
server side plugins, that browsers contact via the gateway to take
advantage of the functionality they provide.

Example uses for Janus are applications involving echo tests,
conference bridges, media recorders, and SIP gateways.


%package utilities
Summary: Janus WebRTC server post-processing utilities
Group: Networking/Other
Requires: %name = %version-%release

%description utilities
Janus is a general purpose WebRTC Gateway with a minimal footprint.

This package contains Janus post-processing utilities.


%package docs
Summary: Janus WebRTC server documentation
Group: Networking/Other
Requires: %name = %version-%release
BuildArch: noarch

%description docs
Janus is a general purpose WebRTC Gateway with a minimal footprint.

This package contains Janus documentation in HTML format.



%package devel
Summary: Janus WebRTC server header files
Group: Development/C
Requires: %name = %version-%release
BuildArch: noarch

%description devel
Janus is a general purpose WebRTC Gateway with a minimal footprint.

This package contains Janus  header files for third-party plugin
development.



%define janus_user      _janus
%define janus_group     _janus

%prep
%setup
%patch0 -p1

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1


mv -f COPYING COPYING.GPL.orig
ln -s $(relative %_licensedir/GPL-3 %_docdir/%name/COPYING.GPL) COPYING.GPL

%build
%autoreconf
%configure \
  --enable-docs \
  --enable-rest \
  --enable-post-processing \
  %{?_without_aes_gcm:--disable-aes-gcm} \
  %{?_without_websockets:--disable-websockets} \
  %nil

%make_build

%install
%makeinstall

cp -a -- %buildroot%_sysconfdir/%name/janus.jcfg.sample  %buildroot%_sysconfdir/%name/janus.jcfg

mkdir -p  %buildroot%_unitdir
install -m 0644 %SOURCE1 %buildroot%_unitdir/%name.service

mv -f -- html html.src
mv -f -- %buildroot%_docdir/janus-gateway/janus-gateway-%version/html .
rm -f -- %buildroot%_docdir/janus-gateway/README.md

mkdir -p -- %buildroot/%_logdir/%name
mkdir -p -- %buildroot%_localstatedir/%name/recordings



%pre
# Add the "_janus" user
%_sbindir/groupadd -r -f %janus_group 2>/dev/null ||:
%_sbindir/useradd  -r -g %janus_group -c 'Janus RTC daemon' \
        -s /dev/null -d /var/lib/janus %janus_user 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc CHANGELOG.md README.md
%doc --no-dereference COPYING.GPL

%attr(0750,root,%janus_group) %dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*.jcfg
%config %_sysconfdir/%name/*.jcfg.sample

%_unitdir/%name.service

%_bindir/%name
%_bindir/%name-cfgconv

%_libdir/%name/*/*.so
%_libdir/%name/*/*.so.*

%exclude %_libdir/%name/*/*.la
%exclude %_includedir/%name/*

%_datadir/%name

%_man1dir/%name.*
%_man1dir/%name-cfgconv.*

%attr(0770,root,%janus_group) %dir %_localstatedir/%name
%attr(1770,root,%janus_group) %dir %_logdir/%name


%files docs
%doc html/


%files utilities
%_bindir/mjr2pcap
%_bindir/pcap2mjr
%_bindir/janus-pp-rec

%_man1dir/mjr2pcap*
%_man1dir/pcap2mjr.*
%_man1dir/janus-pp-rec*


%files devel
%_includedir/%name



%changelog
* Tue Dec 06 2022 Nikolay A. Fetisov <naf@altlinux.org> 1.1.0-alt1
- New version

* Tue Feb 01 2022 Nikolay A. Fetisov <naf@altlinux.org> 0.11.7-alt1
- New version

* Sun Nov 07 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.11.5-alt1
- New version

* Fri Oct 15 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.11.4-alt1
- New version

* Sat Jul 03 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.11.3-alt3
- Re-enable websockets support

* Fri Jul 02 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.11.3-alt2
- Disable websockets support

* Tue Jun 29 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.11.3-alt1
- New version

* Mon Mar 15 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.10.10-alt1
- New version

* Thu Nov 05 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.10.7-alt1
- New version

* Sat Aug 08 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.10.4-alt1
- New version

* Sun Jun 28 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.10.2-alt1
- New version

* Mon Jun 15 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.10.1-alt1
- New version

* Tue Jun 09 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.10.0-alt1
- New version

* Sat May 23 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.9.5-alt1
- New version

* Sun May 17 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.9.4-alt1
- New version

* Tue Apr 28 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.9.3-alt1
- New version
- Enable websockets support

* Wed Apr 08 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.9.2-alt2
- Build post-processing utilities

* Sun Apr 05 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.9.2-alt1
- Initial build for ALT Linux Sisyphus

