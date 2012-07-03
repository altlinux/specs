
Name: nvram-wakeup
Version: 0.99b
Release: alt1

Summary: a tool to read/write the WakeUp time from/to the BIOS
License: GPL
Group: System/Configuration/Boot and Init
Url: http://sourceforge.net/projects/nvram-wakeup/
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source0: nvram-wakup-%version.tar.gz

Patch0: %name-0.97-alt-mb.patch
Patch1: %name-0.97-alt-makefile.patch
Patch2: %name-0.97-alt-rename-time.patch

%description
nvram-wakeup can read and write the wake up time in the BIOS                                                                            
(via /dev/nvram on recent 2.4.x kernels or direct I/O port access).                                                                     
On this wake up time the computer will be powered on automatically from                                                                 
the soft-off state. For the video disc recorder VDR, nvram-wakeup installs                                                              
a hook script, that allows VDR to set a wake up time, when it powers down.                                                              

%prep
%setup -q -n nvram-wakup-%version
#patch0 -p1
#patch1 -p0
#patch2 -p1

%__mkdir_p examples
%__cp nvram-wakeup.conf examples

%build
%make

%install
%__mkdir_p $RPM_BUILD_ROOT{%_sbindir,%_sysconfdir,%_man5dir,%_man8dir,%_docdir/%name-%version/examples}
%__install -m644 nvram-wakeup.conf $RPM_BUILD_ROOT%_sysconfdir
%__install {biosinfo,cat_nvram,guess,guess-helper,nvram-wakeup,rtc,set_timer} $RPM_BUILD_ROOT%_sbindir
%__install nvram-wakeup.conf.5 $RPM_BUILD_ROOT/%_man5dir
%__install {biosinfo,cat_nvram,guess,guess-helper,nvram-wakeup,rtc,set_timer}.8 $RPM_BUILD_ROOT%_man8dir

%files
%_sbindir/*
%config(noreplace) %_sysconfdir/nvram-wakeup.conf
%doc README README.mb README.reboot HISTORY examples
%_mandir/man?/*

%changelog
* Sat Jan 10 2009 Ilya Mashkin <oddity@altlinux.ru> 0.99b-alt1
- new version 0.99b
- droped old patches

* Mon Jun 06 2005 Alex Yustasov <yust@altlinux.ru> 0.97-alt2
- renamed /usr/sbin/time to /usr/sbin/nvtime

* Sat Dec 11 2004 Alex Yustasov <yust@altlinux.ru> 0.97-alt1
- initial release 
