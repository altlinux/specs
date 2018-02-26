%define snap 20051105

Name: hping3
Version: 0.0.%snap
Release: alt5

Packager: Victor Forsyuk <force@altlinux.org>

Summary: TCP/IP stack auditing and much more
License: GPLv2
Group: Security/Networking

URL: http://www.hping.org
Source: %url/hping3-%snap.tar.gz
Patch1: hping3-20051105-cflags.patch
Patch2: hping3-bytesex.patch
Patch3: hping3-20051105-pcap.patch
Patch4: hping3-20051105-willalwaysoverflow.patch

# Automatically added by buildreq on Sat Jan 10 2009
BuildRequires: libpcap-devel tcl-devel

%description
hping3 is a network tool able to send custom TCP/IP packets and to display
target replies like ping do with ICMP replies. hping3 can handle fragmentation,
and almost arbitrary packet size and content, using the command line interface.

Since version 3, hping implements scripting capabilties.

%prep
%setup -n hping3-%snap
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
# Teach configure to recognize tcl 8.5 :)
%__subst 's/"8.4"/"8.5"/' configure
# Fix man page
%__subst 's/hping2/hping3/g; s/HPING2 /HPING3 /;' docs/hping3.8
./configure
%make_build CFLAGS="%optflags -D_FORTIFY_SOURCE=2"

%install
install -pD -m755 hping3 %buildroot%_sbindir/hping3
install -pD -m644 docs/hping3.8 %buildroot%_man8dir/hping3.8

%files
%_sbindir/*
%_man8dir/*
%doc NEWS README lib/*.htcl
%doc docs/A* docs/HPING2-HOWTO.txt docs/[M-Z]* docs/hping2rc.example

%changelog
* Tue Dec 14 2010 Terechkov Evgenii <evg@altlinux.org> 0.0.20051105-alt5
- Fix build

* Sat Jan 10 2009 Victor Forsyuk <force@altlinux.org> 0.0.20051105-alt4
- Exclude CVS directory from packaged docs, include .htcl scripts.
- Fix man page to talk about hping3 rather than hping2.
- Change hping3 permissions from 700 to usual 755.

* Wed Mar 12 2008 Victor Forsyuk <force@altlinux.org> 0.0.20051105-alt3
- Rebuild with tcl 8.5.

* Mon Apr 23 2007 Victor Forsyuk <force@altlinux.org> 0.0.20051105-alt2
- Fix 64 bit build.

* Mon Apr 23 2007 Victor Forsyuk <force@altlinux.org> 0.0.20051105-alt1
- Initial build.
