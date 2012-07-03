Name: pbx-utils
Summary: Useful utilites for Asterisk and CallWeaver
Version: 0.0.12
Release: alt5
License: GPL
Group: System/Servers
BuildRequires: asterisk1.6.2-devel libmhash-devel libnewt-devel libpopt-devel
BuildPreReq: dahdi-linux-headers libtonezone-dahdi-devel
%define ast_ver %{get_version asterisk1.6.2-devel}
Url: http://sisyphus.ru/ru/srpm/Sisyphus/pbx-utils
%define agi_dir %_libexecdir/asterisk/agi-bin
Source: %name-%version.tar

%package -n pbx-agi-samples
Summary: AGI samples for Asterisk
Group: System/Servers
Requires: asterisk-base
%define agi_dir %_libexecdir/asterisk/agi-bin

%description -n pbx-agi-samples
AGI samples for Asterisk


%package -n pbx-astcanary
Summary: Mute daemon for Asterisk
Group: %group

%description -n pbx-astcanary
Mute daemon for Asterisk

%package -n pbx-astman
Summary: Text mode manager for Asterisk
Group: System/Servers
Obsoletes: asterisk1.4-astman
Obsoletes: asterisk1.6-astman

%description -n pbx-astman
Astman is a text mode manager for Asterisk.
Astman connects to Asterisk by TCP, so you can run Astman on a completely
different computer than your Asterisk computer.


%package -n pbx-muted
Summary: Mute daemon for Asterisk
Group: %group
Conflicts: muted
Obsoletes: muted
Conflicts: muted1.3
Obsoletes: muted1.3
Obsoletes: asterisk1.4-muted
Obsoletes: asterisk1.6-muted

%description -n pbx-muted
Mute daemon for Asterisk

%package -n pbx-rawplayer
Summary: simple raw file stdout player
Group: System/Servers

%description -n pbx-rawplayer
simple raw file stdout player

%package -n pbx-smsq
Summary: SMS queuing application for Asterisk and CallWeaver
Group: System/Servers

%description -n pbx-smsq
SMS queuing application for Asterisk and CallWeaver

%package -n pbx-stereorize
Summary: Merge two mono WAV-files to one stereo WAV-file
Group: System/Servers

%description -n pbx-stereorize
Merge two mono WAV-files to one stereo WAV-file

%package -n pbx-streamplayer
Summary: A utility for reading from a raw TCP stream
Group: System/Servers

%description -n pbx-streamplayer
This application is intended for use when a raw TCP stream is desired to be
used as a music on hold source for Asterisk.  Some devices are capable of
taking some kind of audio input and provide it as a raw TCP stream over the
network, which is what inspired someone to fund this to be written.
However, it would certainly be possible to write your own server application
to provide music over a TCP stream from a centralized location.
This application is quite simple.  It just reads the data from the TCP
stream and dumps it straight to stdout.  Due to the way Asterisk handles
music on hold sources, this application checks to make sure writing
to stdout will not be a blocking operation before doing so.  If so, the data
is just thrown away.  This ensures that the stream will continue to be
serviced, even if Asterisk is not currently using the source.


%package all
Summary: This virtual package requires all pbx-utils subpackages
Group: System/Servers
Requires: pbx-astman pbx-muted pbx-rawplayer pbx-smsq pbx-stereorize pbx-streamplayer zones2indications
Requires: pbx-astcanary

%description all
This virtual package requires all pbx-utils subpackages

%package -n zones2indications
Summary: print libtonozone data as Asterisk indications.conf
Group: System/Servers

%description -n zones2indications
print libtonozone data as Asterisk indications.conf

%description
Useful utilites for Asterisk and CallWeaver


%prep
%setup

%build
export CFLAGS=-I/usr/include/asterisk-%ast_ver
%make_build

%install
%makeinstall install DESTDIR=%buildroot AGI_DIR=%agi_dir

%files -n pbx-agi-samples
%agi_dir/*

%files -n pbx-astcanary
%attr(0755,root,root) %_sbindir/astcanary

%files -n pbx-astman
%attr(0755,root,root) %_sbindir/astman

%files -n pbx-muted
%attr(0755,root,root) %_sbindir/muted
%attr(0600,root,root) %_sysconfdir/muted.conf

%files -n pbx-rawplayer
%_sbindir/rawplayer

%files -n pbx-smsq
%_sbindir/smsq

%files -n pbx-stereorize
%_sbindir/stereorize

%files -n pbx-streamplayer
%_sbindir/streamplayer

%files all

%files -n zones2indications
%attr(0755,root,root) %_sbindir/zones2indications

%changelog
* Wed Nov 17 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.12-alt5
- add requires from pbx-agi-samples to asterisk-base

* Tue Oct 19 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.12-alt4
- auto rebuild

* Mon Oct 11 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.12-alt3
- auto rebuild

* Wed Mar 03 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.12-alt2
- rebuild with new Asterisk

* Tue Jan 19 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.12-alt1
- rebuild with new Asterisk

* Mon Dec 21 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.11-alt1
- rebuild

* Sat Oct 31 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.10-alt1
- update from Asterisk 1.6.2

* Wed Sep 30 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.9-alt1
- rebuild

* Mon Sep 28 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.8-alt2
- add Url tag

* Mon Sep 28 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.8-alt1
- import pbx-agi-samples

* Fri Aug 21 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.7-alt1
- add pbx-astcanary

* Mon Aug 03 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.6-alt1
- add zones2indications
- add pbx-utils-all

* Sun Aug 02 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.5-alt1
- add pbx-astman

* Sun Aug 02 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.4-alt1
- add pbx-muted

* Sat Aug 01 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.3-alt2
- fix rawplayer install

* Sat Aug 01 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.3-alt1
- add pbx-rawplayer

* Fri Jul 31 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.2-alt1
- small fixes

* Fri Jul 31 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- first build for Sisyphus

