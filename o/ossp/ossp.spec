Name: ossp
Version: 1.3.2
Release: alt7

Summary: OSS Proxy - emulate OSS device using CUSE
Group: System/Kernel and hardware
License: GPLv2
Url: http://osspd.sourceforge.net/

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

# Automatically added by buildreq on Sun Apr 10 2011 (-bb)
# optimized out: elfutils pkg-config
BuildRequires: libalsa-devel libfuse-devel libpulseaudio-devel

Requires(pre): fuse >= 2.8.5-alt2

%description
%summary

%prep
%setup

%build
%make CFLAGS="%optflags"
%install
%make install DESTDIR=%buildroot prefix=/usr
install -D -m755 osspd.init %buildroot%_initdir/osspd
install -D -m644 modprobe %buildroot%_sysconfdir/modprobe.d/osspd.conf
install -D -m644 osspd.config %buildroot%_sysconfdir/sysconfig/osspd

%preun
%preun_service osspd
%post
%post_service osspd

%files
%_sysconfdir/udev/rules.d/98-osscuse.rules
%_sbindir/ossp-alsap
%_sbindir/ossp-padsp
%attr(2711,root,cuse) %_sbindir/osspd
%_initdir/osspd
%_sysconfdir/modprobe.d/osspd.conf
%config(noreplace) %_sysconfdir/sysconfig/osspd

%changelog
* Tue May 10 2011 Denis Smirnov <mithraen@altlinux.ru> 1.3.2-alt7
- cleanup unneeded hacks for run as unpriviledged user, osspd
  backends change uid to user that try access to /dev/dsp

* Fri May 06 2011 Denis Smirnov <mithraen@altlinux.ru> 1.3.2-alt6
- and one else fix for pid-file creation

* Thu May 05 2011 Denis Smirnov <mithraen@altlinux.ru> 1.3.2-alt5
- multiple fixes by led@
  - correctly create pid-files
  - use alsa backend by default
  - alsa/pulseaudio backend configurable in /etc/sysconfig/osspd

* Sat Apr 30 2011 Denis Smirnov <mithraen@altlinux.ru> 1.3.2-alt4
- fix modprobe (ALT #25537) thanks to vsu@
- start from root (starting with _osspd user not work correctly now)
- update from upstream

* Fri Apr 29 2011 Denis Smirnov <mithraen@altlinux.ru> 1.3.2-alt3
- fix initscript

* Thu Apr 28 2011 Denis Smirnov <mithraen@altlinux.ru> 1.3.2-alt2
- add initscript
- set preclaim_oss=0 in soundcore

* Sun Apr 10 2011 Denis Smirnov <mithraen@altlinux.ru> 1.3.2-alt1
- initial build for ALT Linux Sisyphus
