Name: dvblast
Version: 3.0
Release: alt1.git19092016

Summary: Video/Audio streaming application based on the linux-dvb API
License: GPLv2+
Group: Video
Url: http://www.videolan.org/projects/dvblast.html
Packager: Alexei Takaseev <taf@altlinux.ru>

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: bitstream-headers libev-devel

%description 
DVBlast is a simple and powerful streaming application based on the
linux-dvb API. It opens a DVB device, tunes it, places PID filters,
configures a CAM module, and demultiplexes the packets to several RTP
outputs.

DVBlast is designed to be the core of a custom IRD or CID, based on
a PC with Linux-supported DVB cards.

DVBlast does not do any kind of processing on the elementary streams,
such as transcoding, PID remapping or remultiplexing. It does not
stream from plain files, only DVB devices. If you were looking for
these features, switch to VLC.

%prep
%setup
%patch0 -p1

%build
%make

%install
mkdir -p %buildroot%_bindir
install -pm755 dvblast %buildroot%_bindir/dvblast
install -pm755 dvblastctl %buildroot%_bindir/dvblastctl
install -pm755 dvblast_mmi.sh %buildroot%_bindir/dvblast_mmi.sh
install -pm0644 -D dvblast.1 %buildroot%_man1dir/dvblast.1

%files 
%doc COPYING README INSTALL TODO AUTHORS NEWS
%_bindir/*
%_man1dir/dvblast.1*

%changelog
* Tue Sep 20 2016 Alexei Takaseev <taf@altlinux.org> 3.0-alt1.git19092016
- update to git:f4b1a8e15f0514d80f729c876c6a960639ecf9b9

* Tue Oct 06 2015 Alexei Takaseev <taf@altlinux.org> 3.0-alt1
- 3.0

* Sat Jan 31 2015 Alexei Takaseev <taf@altlinux.org> 2.2-alt9
- Rebuild with new bitstream

* Thu Oct 30 2014 Alexei Takaseev <taf@altlinux.org> 2.2-alt8
- udp: fix /ifaddr= argument parsing

* Tue Oct 07 2014 Alexei Takaseev <taf@altlinux.org> 2.2-alt7
- update to git:71736aae24aad273874f86fdf13a802532e6475d

* Sun Jun 29 2014 Alexei Takaseev <taf@altlinux.org> 2.2-alt6
- update to git:9a2ea9ffb2141e1b4f29a181d97a4efbcb8fbc61

* Tue Oct 02 2012 Alexei Takaseev <taf@altlinux.org> 2.2-alt5
- Fix build
- Merge with upstream (git: 45d0fa69350915a099796e7eb6b6b0bd1041ecce)
- Add missing patch to spec

* Sat Aug 11 2012 Alexei Takaseev <taf@altlinux.org> 2.2-alt4
- Add support for uncommitted diseqc switch. (git: 05381442b9956fb280d5f4770e710df44b55cf26)

* Tue Jun 26 2012 Alexei Takaseev <taf@altlinux.org> 2.2-alt3
- Rebuild with bitstream-headers-1.0-alt2

* Sat Jun 16 2012 Alexei Takaseev <taf@altlinux.org> 2.2-alt2
- demux: Fix ECM pid selection. (Georgi Chorbadzhiyski gf_AT_unixsol.org)

* Sat May 19 2012 Alexei Takaseev <taf@altlinux.org> 2.2-alt1
- 2.2 release.
- build with bitstream

* Mon Oct 31 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2-alt2
- rebuilt with recent dvbpsi

* Mon Mar 01 2010 Konstantin Pavlov <thresh@altlinux.org> 1.2-alt1
- 1.2 release.

* Sun Aug 02 2009 Konstantin Pavlov <thresh@altlinux.ru> 1.0-alt1
- Initial build for ALT Linux Sisyphus.
