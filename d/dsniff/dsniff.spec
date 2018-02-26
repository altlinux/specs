Name: dsniff
Version: 2.4
%define beta_ver b1
Release: alt0.12.b1

Summary: Network audit tools
License: BSD-like
Group: Monitoring
Url: http://www.monkey.org/~dugsong/dsniff/
Packager: Dmitry V. Levin <ldv@altlinux.org>

# http://www.monkey.org/~dugsong/dsniff/beta/dsniff-2.4b1.tar.gz
Source: dsniff-2.4b1.tar
Source1: dsniff-faq.html

Patch0: dsniff-2.4-alt-configure.patch
Patch1: dsniff-2.4-alt-makefile.patch
Patch2: dsniff-2.4-alt-fixes.patch
Patch3: dsniff-2.4b1-alt-CLK_TCK.patch
Patch4: dsniff-2.4b1-deb-mailsnarf.patch
Patch5: dsniff-2.4b1-deb-pcap-read-dump.patch
Patch6: dsniff-2.4b1-deb-arp.patch
Patch7: dsniff-2.4b1-deb-urlsnarf.patch
Patch8: dsniff-2.4b1-deb-libnet.patch
Patch9: dsniff-2.4b1-deb-openssl.patch
Patch10: dsniff-2.4b1-deb-checksum.patch
Patch11: dsniff-2.4b1-deb-urlsnarf-escape.patch
Patch12: dsniff-2.4b1-deb-pop-version.patch
Patch13: dsniff-2.4b1-deb-checksum-libnids.patch

# Automatically added by buildreq on Mon Mar 22 2010
BuildRequires: imake libXmu-devel libdb4-devel libnids-devel libssl-devel xorg-cf-files

%package X11
Summary: Network audit tools for X11
Group: Monitoring
Requires: dsniff = %version-%release

%description
Dsniff is a sophisticated set of programs which, combined with other
standard utilities like tcpdump (a standard packet sniffer), allow
you to monitor and redirect network traffic so you can analyze it:
+ arpspoof - intercept packets on a switched LAN;
+ dnsspoof - forge replies to DNS address / pointer queries;
+ dsniff - password sniffer;
+ filesnarf - sniff files from NFS traffic;
+ macof - flood a switched LAN with random MAC addresses;
+ mailsnarf - sniff mail messages in Berkeley mbox format;
+ msgsnarf - sniff chat messages;
+ sshmitm - SSH monkey-in-the-middle;
+ sshow - SSH traffic analysis tool;
+ tcpkill - kill TCP connections on a LAN;
+ tcpnice - slow down TCP connections on a LAN;
+ urlsnarf - sniff HTTP requests in Common Log Format;
+ webmitm - HTTP / HTTPS monkey-in-the-middle.

%description X11
Dsniff is a sophisticated set of programs which, combined with other
standard utilities like tcpdump (a standard packet sniffer), allow
you to monitor and redirect network traffic so you can analyze it:
+ webspy - display sniffed URLs in Netscape in real-time.

%prep
%setup -q
install -pm644 %_sourcedir/dsniff-faq.html faq.html
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
grep -FZl /usr/local/lib/ *.* |
	xargs -r0 sed -i 's,/usr/local/lib/,%_datadir/dsniff/,' --
sed -i 's/dn_expand/__&/g' configure.in

%build
%set_autoconf_version 2.13
autoconf
%configure --libdir=%_datadir/dsniff
sed -i 's,[[:space:]]\+-\(I/usr/include\|L/usr/lib\)\([[:space:]]\|$\),\2,g' Makefile
%make_build

%install
%make_install install install_prefix=%buildroot

%files
%_sbindir/*
%_mandir/man?/*
%exclude %_sbindir/webspy
%exclude %_mandir/man?/webspy.*
%config(noreplace) %_datadir/dsniff
%doc README CHANGES faq.html

%files X11
%_sbindir/webspy
%_mandir/man?/webspy.*

%changelog
* Sun Nov 07 2010 Dmitry V. Levin <ldv@altlinux.org> 2.4-alt0.12.b1
- Rebuilt for soname set-versions.

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 2.4-alt0.11.b1
- Rebuilt with libcrypto.so.10.

* Mon Mar 22 2010 Dmitry V. Levin <ldv@altlinux.org> 2.4-alt0.10.b1
- Synced with Debian dsniff-2.4b1-18 package.
- Built with libnids-1.24.

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.4-alt0.9.b1.1.1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Sat Jun 14 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.4-alt0.9.b1.1.1
- Automated rebuild with libdb-4.7.so.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.4-alt0.9.b1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sun Nov 12 2006 Dmitry V. Levin <ldv@altlinux.org> 2.4-alt0.9.b1
- Disabled packets filtering with incorrect checksum (Debian#372536).

* Thu Oct 05 2006 Dmitry V. Levin <ldv@altlinux.org> 2.4-alt0.8.b1
- Use sysconf(_SC_CLK_TCK) instead of CLK_TCK when _SC_CLK_TCK is
  known to be available or CLK_TCK is not (needed for glibc 2.3.90+).

* Tue Jun 20 2006 Dmitry V. Levin <ldv@altlinux.org> 2.4-alt0.7.b1
- Applied patches from Debian dsniff-2.4b1-14 package.
- Updated build dependencies.

* Sat Mar 25 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.4-alt0.6.b1.1.1
- Rebuilt with libdb4.4.

* Thu Feb 10 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.4-alt0.6.b1.1
- Rebuilt with libdb4.3.

* Sun Sep 05 2004 Dmitry V. Levin <ldv@altlinux.org> 2.4-alt0.6.b1
- Fixed manpage references.
- Applied arp fixes from Debian.
- Fixed few issues found by compiler.
- Rebuilt with libnids.so.1.19.

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 2.4-alt0.5.b1.1
- Rebuilt with openssl-0.9.7d.

* Tue May 04 2004 Dmitry V. Levin <ldv@altlinux.org> 2.4-alt0.5.b1
- Patched configure to enable libdb4 build support and built with libdb4.

* Tue Jan 13 2004 Dmitry V. Levin <ldv@altlinux.org> 2.4-alt0.4.b1
- Rebuilt with libpcap.so.0.8.

* Sat Oct 18 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4-alt0.3.b1
- Rebuilt with libnids.so.1.18.

* Mon Dec 02 2002 Dmitry V. Levin <ldv@altlinux.org> 2.4-alt0.2.b1
- Moved webspy to X11 subpackage (#0001641).

* Mon Nov 25 2002 Dmitry V. Levin <ldv@altlinux.org> 2.4-alt0.1.b1
- Updated to 2.4b1.
- Patched configure and sources to reenable build.
- Updated description.

* Tue Apr 09 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.3-ipl6
- Rebuilt with libpcap-0.7.1.

* Thu Feb 07 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.3-ipl5
- Updated buildrequires.

* Fri Feb 02 2001 Dmitry V. Levin <ldv@fandra.org> 2.3-ipl4
- Fixed db autoconfiguration.
- Now build with db1.

* Tue Jan 09 2001 Dmitry V. Levin <ldv@fandra.org> 2.3-ipl3
- Rebuilt with libpcap-0.6.1.

* Fri Jan 05 2001 Dmitry V. Levin <ldv@fandra.org> 2.3-ipl2
- Rebuilt with db3-3.2.3e.

* Mon Dec 18 2000 Dmitry V. Levin <ldv@fandra.org> 2.3-ipl1
- 2.3
- Compilation fixes.

* Tue Jun 27 2000 Dmitry V. Levin <ldv@fandra.org>
- 2.2
- FHSification.

* Tue May 23 2000 Dmitry V. Levin <ldv@fandra.org>
- 2.1

* Mon Apr 17 2000 Dmitry V. Levin <ldv@fandra.org>
- initial revision
