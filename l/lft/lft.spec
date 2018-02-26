Name: lft
Version: 3.33
Release: alt1
Serial: 1

Summary: Alternative traceroute tool for network (reverse) engineers
License: VOSTROM Public License for Open Source
# maybe even GPL-substitutable, see p. 6 of the license?
Group: Networking/Other

Url: http://pwhois.org/lft
Source0: %name-%version.tar.gz
Source1: %name.control
Packager: Michael Shigorin <mike@altlinux.org>
# please read COPYING (it's not exactly GPL)
# when adding patches, authors require that 
# modified versions be tagged so they are 
# easily identified as such

# Automatically added by buildreq on Tue Apr 07 2009
BuildRequires: libpcap-devel

Obsoletes: fft

%description
LFT, short for Layer Four Traceroute, is a sort of 'traceroute' that
often works much faster (than the commonly-used Van Jacobson method) and
goes through many configurations of packet-filter based firewalls. More
importantly, LFT implements numerous other features including AS number
lookups, loose source routing, netblock name lookups, et al.

WhoB is a likable whois client (see whois(1)) designed to provide
everything a network engineer needs to know about a routed IP
address by typing one line and reading one line. But even so,
it's worth typing a few more lines because WhoB can do lots of
other cool things for you!

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std
install -pDm755 %SOURCE1 %buildroot%_controldir/%name

%pre
%_sbindir/groupadd -r -f netadmin >/dev/null 2>&1
%pre_control %name

%post
%post_control -s netadmin %name

%files
%_bindir/*
%_man8dir/*
%config %_controldir/%name
%doc CHANGELOG COPYING README TODO

%changelog
* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 1:3.33-alt1
- 3.33

* Tue Apr 12 2011 Michael Shigorin <mike@altlinux.org> 1:3.32-alt1
- 3.32

* Wed Mar 09 2011 Michael Shigorin <mike@altlinux.org> 1:3.31-alt1
- 3.31

* Sat Feb 19 2011 Michael Shigorin <mike@altlinux.org> 1:3.3-alt1
- 3.3

* Thu May 14 2009 Michael Shigorin <mike@altlinux.org> 1:3.1-alt2
- better Group:

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 1:3.1-alt1
- 3.1, finally

* Mon Dec 11 2006 Michael Shigorin <mike@altlinux.org> 1:2.5-alt2
- thanks Damir Shayhutdinov (damir@) for looking into this,
  I somehow (mis)remembered there were problems inside...
- spec cleanup (macro abuse and hand-written control scripts instead
  of macro versions, how funny)
- updated Url:
- had to add Serial: as 2.5 is less than 2.31 for RPM
  (but that's the way upstream version numbering goes)
- NB: 2.5 introduces a new packaged tool, "whob"; worth looking at
  for those considering whois output overly noisy

* Mon Dec 11 2006 Damir Shayhutdinov <damir@altlinux.ru> 2.5-alt1
- NMU
- Updated to 2.5 version

* Mon Jan 17 2005 Michael Shigorin <mike@altlinux.ru> 2.31-alt1
- 2.31 (#5883)
- updated project URL

* Sun Feb 01 2004 Michael Shigorin <mike@altlinux.ru> 2.2-alt2
- rebuilt with libpcap-0.8.x

* Sat Aug 16 2003 Michael Shigorin <mike@altlinux.ru> 2.2-alt1
- built for ALT Linux
- control(8) support

* Sun Apr 20 2003 Nils McCarthy <nils@shkoo.com>
- Incorporated changes from Dag Wieers <dag@wieers.com> cleaning up
- a lot of the build process.

* Thu Mar 06 2003 Nils McCarthy <nils@shkoo.com>
- revised to work with autoconf

* Mon Oct 28 2002 Florin Andrei <florin@sgi.com>
- first version
- v2.0-1
