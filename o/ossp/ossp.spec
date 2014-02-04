Name: ossp
Version: 1.3.2
Release: alt10

Summary: OSS Proxy - emulate OSS device using CUSE
Group: System/Kernel and hardware
License: GPLv2
Url: http://osspd.sourceforge.net/

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar
Patch: ossp-1.3.2-alt-DSO.patch
Source1: osspd.service
Source2: ossp.tmpfiles.conf
Source3: ossp.modprobe.conf
Source4: ossp.rules

# Automatically added by buildreq on Sun Apr 10 2011 (-bb)
# optimized out: elfutils pkg-config
BuildRequires: libalsa-devel libfuse-devel libpulseaudio-devel

Requires(pre): fuse >= 2.8.5-alt2

%description
%summary

%prep
%setup
%patch -p2

%build
%make CFLAGS="%optflags"
%install
%make install DESTDIR=%buildroot prefix=/usr
install -D -m755 osspd.init %buildroot%_initdir/osspd
install -D -m644 modprobe %buildroot%_sysconfdir/modprobe.d/osspd.conf
install -D -m644 osspd.config %buildroot%_sysconfdir/sysconfig/osspd
install -D -m644 %SOURCE1 %buildroot%_unitdir/osspd.service
# sysconf/udev policy - /etc is for user
mkdir -p %buildroot%_udevrulesdir/
mkdir -p %buildroot/lib/tmpfiles.d
mv %buildroot%_sysconfdir/udev/rules.d/* %buildroot%_udevrulesdir/

install -D -m644 %SOURCE2 %buildroot/lib/tmpfiles.d/ossp.conf
install -D -m644 %SOURCE3 %buildroot/etc/modprobe.d/ossp.conf
cat %SOURCE4 >> %buildroot%_udevrulesdir/98-osscuse.rules

%preun
%preun_service osspd
%post
%post_service osspd

%files
/etc/modprobe.d/%name.conf
/lib/tmpfiles.d/%name.conf
%_udevrulesdir/98-osscuse.rules
%_sbindir/ossp-alsap
%_sbindir/ossp-padsp
%attr(2711,root,cuse) %_sbindir/osspd
%_initdir/osspd
%_sysconfdir/modprobe.d/osspd.conf
%config(noreplace) %_sysconfdir/sysconfig/osspd
%_unitdir/osspd.service

%changelog
* Tue Feb 04 2014 Denis Smirnov <mithraen@altlinux.ru> 1.3.2-alt10
- auto-start when needed (thanks to led@)

* Wed Apr 24 2013 Denis Smirnov <mithraen@altlinux.ru> 1.3.2-alt9
- repocop fixes

* Thu Jan 31 2013 Denis Smirnov <mithraen@altlinux.ru> 1.3.2-alt8
- add systemd service file

* Sun Dec 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt7.1
- Completed linking

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
