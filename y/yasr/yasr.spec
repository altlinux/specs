Name: yasr
Version: 0.6.7
Release: alt7
Packager: Michael Pozhidaev <msp@altlinux.ru>

Summary: %name - yet another screen reader
License: %gpl2only
Group: Accessibility
Url: http://yasr.sourceforge.net
Requires: voiceman
BuildRequires: rpm-build-licenses 

Source: %name-%version.tar.gz
Source1: voiceman-emacspeak-yasr
Patch0: %name-%version-alt-config.patch
Patch1: %name-%version-alt-voiceman.patch
Patch2: %name-%version-alt-pty.patch

%description
YASR ("Yet Another Screen Reader") is the attempt at a lightweight,
portable screen reader. It works by opening a shell in a pty and
intercepting all user input/output, maintaining a window of what
should be on the screen by looking at the codes and text sent to the
screen. It thus uses no Linuxisms such as /dev/vcsa0 and does not 
necessarily need to be setuid root (the only requirement being that 
the user be able to access the tts device).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure
make

%install
%__install -pD -m775 ./yasr/yasr %buildroot%_bindir/yasr
%__install -pD -m664 ./yasr.conf %buildroot%_sysconfdir/yasr.conf
%__install -pD -m664 ./yasr/yasr.1 %buildroot%_man1dir/yasr.1
%__install -pD -m755 %SOURCE1 %buildroot%_bindir/voiceman-emacspeak-yasr

%files
%_bindir/*
%_sysconfdir/*
%_man1dir/*
%doc ChangeLog BUGS CREDITS NEWS README TODO

%changelog
* Fri Dec 17 2010 Michael Pozhidaev <msp@altlinux.ru> 0.6.7-alt7
- Added voiceman-emacspeak-yasr script to adjust speech attributes for voiceman-1.5.0

* Sun Nov 21 2010 Michael Pozhidaev <msp@altlinux.ru> 0.6.7-alt6
- voiceman-espeak speech server specification changed to voiceman-emacspeak

* Wed Nov 12 2008 Michael Pozhidaev <msp@altlinux.ru> 0.6.7-alt5
- Fixed *pty call declarations

* Wed Oct 15 2008 Michael Pozhidaev <msp@altlinux.ru> 0.6.7-alt4
- Fixed man directory specification

* Sat Aug 30 2008 Michael Pozhidaev <msp@altlinux.ru> 0.6.7-alt3
- Modified voiceman client name

* Sun Aug 26 2007 Michael Pozhidaev <msp@altlinux.ru> 0.6.7-alt2
- Moved from group "Sound".

* Sat Aug 18 2007 Michael Pozhidaev <msp@altlinux.ru> 0.6.7-alt1
- Initial rpm
