Summary: A tool to replay captured network traffic
Name: tcpreplay
Version: 3.4.4
Release: alt1
License: BSD
Group: Networking/Other
Url: http://tcpreplay.synfin.net/trac/
Packager: Boris Savelev <boris@altlinux.org>

Source: %name-%version.tar.gz
Patch: 0001-fix-buffer_overflow.patch

# Automatically added by buildreq on Sat Mar 24 2012
# optimized out: guile18 libstdc++-devel
BuildRequires: autogen gcc-c++ groff-base libdnet-devel libpcap-devel tcpdump

%description
Tcpreplay is a tool to replay captured network traffic. Currently, tcpreplay
supports pcap (tcpdump) and snoop capture formats. Also included, is tcpprep a
tool to pre-process capture files to allow increased performance under certain
conditions as well as capinfo which provides basic information about capture
files.

%prep
%setup
%patch -p2

%build
%undefine __libtoolize
%configure \
    --enable-dynamic-link \
    --enable-tcpreplay-edit \
    --with-testnic=eth0 \
    --with-testnic2=eth1

%make_build

%install
%makeinstall_std

%files
%doc README docs/CHANGELOG docs/CREDIT docs/HACKING docs/INSTALL docs/LICENSE docs/TODO
%_bindir/tcpbridge
%_bindir/tcpprep
%_bindir/tcpreplay*
%_bindir/tcprewrite
%_man1dir/*

%changelog
* Sat Mar 24 2012 Fr. Br. George <george@altlinux.ru> 3.4.4-alt1
- Autobuild version bump to 3.4.4
- libdnet and tcpdump dependency

* Mon Jul 20 2009 Boris Savelev <boris@altlinux.org> 3.4.1-alt2
- fix build

* Tue Mar 10 2009 Boris Savelev <boris@altlinux.org> 3.4.1-alt1
- initial build

* Sun Jun 22 2008 Oden Eriksson <oeriksson@mandriva.com> 3.3.2-1mdv2009.0
+ Revision: 227869
- 3.3.2
- fix deps

* Sun May 18 2008 Oden Eriksson <oeriksson@mandriva.com> 3.3.1-1mdv2009.0
+ Revision: 208629
- 3.3.1

* Tue May 06 2008 Oden Eriksson <oeriksson@mandriva.com> 3.3.0-0mdv2009.0
+ Revision: 201829
- 3.3.0

* Fri Jan 25 2008 Oden Eriksson <oeriksson@mandriva.com> 3.2.5-1mdv2008.1
+ Revision: 157843
- 3.2.5

* Thu Jan 17 2008 Oden Eriksson <oeriksson@mandriva.com> 3.2.4-1mdv2008.1
+ Revision: 154131
- 3.2.4

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 26 2007 Oden Eriksson <oeriksson@mandriva.com> 3.2.1-1mdv2008.1
+ Revision: 102320
- 3.2.1

* Tue Aug 28 2007 Oden Eriksson <oeriksson@mandriva.com> 3.2.0-1mdv2008.0
+ Revision: 72646
- 3.2.0

* Fri Jul 20 2007 Oden Eriksson <oeriksson@mandriva.com> 3.1.1-1mdv2008.0
+ Revision: 53879
- 3.1.1

* Wed May 02 2007 Oden Eriksson <oeriksson@mandriva.com> 3.0.1-1mdv2008.0
+ Revision: 20475
- 3.0.1

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-1mdv2008.0
+ Revision: 16072
- fix deps
- 3.0.0

* Tue Jul 18 2006 Stefan van der Eijk <stefan@mandriva.org> 2.3.5-4
- rebuild
- %%mkrel

* Fri Mar 17 2006 Oden Eriksson <oeriksson@mandriva.com> 2.3.5-3mdk
- rebuilt against libnet1.1.2

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 2.3.5-2mdk
- rebuilt against new libpcap-0.9.1 (aka. a "play safe" rebuild)

* Mon Jul 04 2005 Oden Eriksson <oeriksson@mandriva.com> 2.3.5-1mdk
- 2.3.5

* Fri Feb 11 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.3.3-1mdk
- 2.3.3
- fix deps

* Mon Nov 08 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.3.2-1mdk
- 2.3.2
- fix deps

* Mon Sep 27 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.3.1-1mdk
- 2.3.1

* Mon Sep 06 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.3.0-1mdk
- 2.3.0
- build against the new shared libnet2

* Tue Jun 22 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.2.2-1mdk
- 2.2.2

* Sun May 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.2.0-1mdk
- 2.2.0
- fix P0
- fix deps

* Sun Dec 07 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.4.6-1mdk
- 1.4.6

* Sat Aug 30 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.4.5-1mdk
- 1.4.5

* Wed Aug 13 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.4.4-1mdk
- 1.4.4

