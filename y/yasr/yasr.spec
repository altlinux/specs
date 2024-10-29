%define _unpackaged_files_terminate_build 1

Name: yasr
Version: 0.6.9
Release: alt1

Summary: %name - yet another screen reader
License: GPL-2.0-only
Group: Accessibility
Url: https://sourceforge.net/projects/yasr/
VCS: https://git.code.sf.net/p/yasr/git

Source: %name-%version.tar

BuildRequires(pre): rpm-build
BuildRequires: libtool
BuildRequires: gettext
BuildRequires: automake
BuildRequires: make
BuildRequires: gcc-c++

%description
YASR ("Yet Another Screen Reader") is the attempt at a lightweight,
portable screen reader. It works by opening a shell in a pty and
intercepting all user input/output, maintaining a window of what
should be on the screen by looking at the codes and text sent to the
screen. It thus uses no Linuxisms such as /dev/vcsa0 and does not 
necessarily need to be setuid root (the only requirement being that 
the user be able to access the tts device).

%prep
%setup

%build
%autoreconf
%configure
%make

%install
%makeinstall_std

mv %buildroot%_datadir/%name %buildroot%_sysconfdir
rm -rv %buildroot%_datadir/locale

%files
%_bindir/%name
%_sysconfdir/%name.conf
%_man1dir/%name.1.xz
%doc ChangeLog BUGS CREDITS NEWS README TODO

%changelog
* Tue Oct 29 2024 Artem Semenov <savoptik@altlinux.org> 0.6.9-alt1
- Build new version 0.6.9 (ALT bug: 51705)

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.6.7-alt7.qa1
- NMU: rebuilt for debuginfo.

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
