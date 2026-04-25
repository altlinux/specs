Name: dsniff
Version: 2.4
%define beta_ver b1
Release: alt0.14.b1.2

Summary: Network audit tools
License: BSD
Group: Monitoring
Url: http://www.monkey.org/~dugsong/dsniff/

# http://www.monkey.org/~dugsong/dsniff/beta/dsniff-2.4b1.tar.gz
Source: dsniff-2.4b1.tar
Source1: dsniff-faq.html

Patch0: dsniff-2.4-alt-configure.patch
## Patch1: dsniff-2.4-alt-makefile.patch
## Patch3: dsniff-2.4b1-alt-CLK_TCK.patch

Patch101: 01_time.h.patch
Patch102: 02_mailsnarf_corrupt.patch
Patch103: 03_pcap_read_dump.patch
Patch104: 04_multiple_intf.patch
Patch105: 05_amd64_fix.patch
Patch106: 06_urlsnarf_zeropad.patch
Patch107: 07_libnet_1.1.patch
Patch108: 08_openssl-0.9.8.patch
Patch109: 09_sysconf_clocks.patch
Patch110: 10_urlsnarf_escape.patch
Patch111: 11_string_header.patch
Patch112: 12_arpa_inet_header.patch
Patch113: 13_pop_with_version.patch
Patch114: 14_obsolete_time.patch
Patch115: 15_checksum_libnids.patch
Patch116: 16_TDS_decoder.patch
Patch117: 17_checksum.patch
Patch118: 18_sshcrypto.patch
Patch119: 19_rewrite-and-modernize-POP-decoder.patch
Patch120: 20_debian_dirs.patch
Patch121: 21_msgsnarf_segfault.patch
Patch122: 22_handlepp.patch
Patch123: 23_urlsnarf_timestamp.patch
Patch124: 24_Fix-OpenSSL1.1.0-Build.patch
Patch125: 25_fix-spelling-errors.patch
Patch126: 26_arpspoof-add-r-switch-to-poison-both-directions.patch
Patch127: 27_arpspoof-allow-use-of-of-multiple-targets.patch
Patch128: 28_arpspoof-allow-selection-of-source-hw-address.patch
Patch129: 29_libnet_name2addr4.patch
Patch130: 30_pntohl_shift.patch
Patch131: 31_sysconf_clocks.patch
Patch132: 32_rpc_segfault.patch
Patch133: 33_sshcrypto_DES.patch
Patch134: 34_fix-parallel-FTBFS.patch
Patch135: 35_Add_CPPFLAGS.patch
Patch136: 36_implicit_declarations.patch
Patch137: 37_fix-lib-and-share-dirs.patch
Patch138: 38_fix-pcap_init.patch
Patch139: 39_libtirpc.patch
Patch140: 40_fix-ftbfs-with-gcc-14.patch

# Automatically added by buildreq on Tue Apr 13 2021
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libICE-devel libSM-devel libX11-devel libXt-devel libgpg-error libnet2-devel libpcap-devel python2-base sh4 xorg-proto-devel
BuildRequires: imake libXmu-devel libdb4-devel libnids-devel libnsl2-devel libssl-devel libtirpc-devel rpcgen xorg-cf-files gcc14

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
%set_gcc_version 14
%setup -q
install -pm644 %_sourcedir/dsniff-faq.html faq.html

%autopatch -p1

grep -FZl /usr/local/lib/ *.* |
	xargs -r0 sed -i 's,/usr/local/lib/,%_datadir/dsniff/,' --
sed -i 's/dn_expand/__&/g' configure.in

%build
#set_autoconf_version 2.13
export CC=%__cc
%autoreconf
%add_optflags -I%_includedir/nsl
%add_optflags -I%_includedir/tirpc
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
* Sat Apr 25 2026 Fr. Br. George <george@altlinux.org> 2.4-alt0.14.b1.2
- Fixed FTBFS

* Fri May 09 2025 Fr. Br. George <george@altlinux.org> 2.4-alt0.14.b1.1
- Ressurrected from FTBFS
- Patches updated from Debian build

* Tue Apr 13 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.4-alt0.14.b1
- Fixed FTBFS.
- spec: Removed packager field.

* Fri Feb 08 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.4-alt0.13.b1
- Rebuilt against libssl.so.1.1.
- Rebuilt against libnsl2.
- Applied some patches from Debian dsniff-2.4b1-29 and Fedora
  dsniff-2.4-0.29.b1.

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
