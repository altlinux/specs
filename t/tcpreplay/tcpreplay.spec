Summary: A tool to replay captured network traffic
Name: tcpreplay
Version: 4.4.3
Release: alt1
License: GPLv3
Group: Networking/Other
Url: https://github.com/appneta/tcpreplay
Source: %name-%version.tar
BuildRequires: autogen gcc-c++ groff-base libdnet-devel libpcap-devel tcpdump libopts-devel

%description
Tcpreplay is a tool to replay captured network traffic. Currently, tcpreplay
supports pcap (tcpdump) and snoop capture formats. Also included, is tcpprep a
tool to pre-process capture files to allow increased performance under certain
conditions as well as capinfo which provides basic information about capture
files.

%prep
%setup

%build
%autoreconf
%configure \
    --enable-dynamic-link \
    --disable-local-libopts \
    --disable-libopts-install \
    --with-testnic=eth0 \
    --with-testnic2=eth1

%make_build

%install
%makeinstall_std

%files
%doc README.md docs/CHANGELOG docs/CREDIT docs/HACKING docs/INSTALL docs/LICENSE docs/TODO
%_bindir/tcpbridge
%_bindir/tcpprep
%_bindir/tcpreplay*
%_bindir/tcprewrite
%_bindir/tcpliveplay
%_bindir/tcpcapinfo
%_man1dir/*

%changelog
* Wed Jan 18 2023 Anton Farygin <rider@altlinux.ru> 4.4.3-alt1
- 4.4.3

* Mon Nov 28 2022 Anton Farygin <rider@altlinux.ru> 4.4.2-alt1
- 4.4.2 (Fixes: CVE-2022-28487, CVE-2022-27942, CVE-2022-27940, CVE-2022-37047, CVE-2022-37049,
     CVE-2022-27939, CVE-2022-25484, CVE-2022-27941)

* Wed Feb 23 2022 Anton Farygin <rider@altlinux.ru> 4.4.1-alt1
- 4.4.1 (Fixes: CVE-2021-45387, CVE-2021-45386)

* Tue May 11 2021 Anton Farygin <rider@altlinux.ru> 4.3.4-alt1
- 4.3.4 (Fixes: CVE-2020-24266, CVE-2020-24265)

* Sat Jun 27 2020 Anton Farygin <rider@altlinux.ru> 4.3.3-alt1
- 4.3.3

* Sun Mar 17 2019 Anton Farygin <rider@altlinux.ru> 4.3.2-alt1
- 4.3.2

* Tue Jan 22 2019 Anton Farygin <rider@altlinux.ru> 4.3.1-alt1
- 4.2.6 -> 4.3.1

* Mon Oct 09 2017 Anton Farygin <rider@altlinux.ru> 4.2.6-alt1
- new version

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

