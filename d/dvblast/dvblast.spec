Name: dvblast
Version: 2.2
Release: alt3

Summary: Video/Audio streaming application based on the linux-dvb API
License: GPLv2+
Group: Video
Url: http://www.videolan.org/projects/dvblast.html
Packager: Alexei Takaseev <taf@altlinux.ru>

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: bitstream-headers

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
