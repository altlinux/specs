Summary: ttyrec - A tty recorder
Name: ttyrec
Version: 1.0.8
Release: alt2
Group: Terminals
License: BSD
Source0: %name-%version.tar.gz

Patch0: 01_Makefile.diff
Patch1: 02_minor_cleanup.diff
Patch2: 03_io_h.diff
Patch3: 04_64-bit.diff
Patch4: 05_WINSZ.diff
Patch5: 06_pause.diff
Patch6: 07_ttyrec_man.diff
Patch7: 08_sigchld.diff
Patch8: 09_sigwinch.diff
Patch9: 10_control_tty.diff
Patch10: 11_sigaction.diff
Patch11: 12_ttyplay_fix_select.diff
Patch12: 13_ttyplay_fread.diff
Patch13: 14_ttyplay_man.diff
Patch14: 15_ttyrec_dont_record_query.diff
Patch15: 16_ttyrec_XCASE.diff
Patch50: 50_openpty_ALT.patch

Url: http://0xcc.net/ttyrec/
%define PLAYterm You can yse PLAYterm service (http://www.playterm.org/) to share records.

%description
ttyrec is a tty recorder. Recorded data can be played back with the
included ttyplay command. It can record emacs -nw, vi, lynx, or any
programs running on tty.

%PLAYterm

%prep
%setup

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
# Don't know how it works in Debian!
%patch50 -p1

echo "%PLAYterm" >> README

%build
%make_build

%install
mkdir -p %buildroot%_bindir %buildroot%_man1dir
%makeinstall DESTDIR=%buildroot
install *.1 %buildroot%_man1dir/
#install -d %buildroot%_mandir/man1
#install -m 755 ttyrec  %buildroot%_bindir
#install -m 755 ttyplay %buildroot%_bindir
#install -m 755 ttytime %buildroot%_bindir
#install -m 644 *.1     %buildroot%_mandir/man1

%files
%doc README
%_bindir/*
%_man1dir/*

%changelog
* Tue Sep 27 2011 Fr. Br. George <george@altlinux.ru> 1.0.8-alt2
- Debian patches applied
- Fix stoneage openpty use

* Tue Sep 27 2011 Fr. Br. George <george@altlinux.ru> 1.0.8-alt1
- Autobuild version bump to 1.0.8

* Sun Sep 25 2011 Fr. Br. George <george@altlinux.ru> 1.0.7-alt1
- Initial (resurrect?) build from TurboLinux

* Fri Jan 13 2006 Bob Lee <bobl@turbolinux.com>
- update to 1.0.7
- add copyright

* Fri Jun 13 2003 Noriyuki Suzuki <noriyuki@turbolinux.co.jp>
- update to 1.0.6

* Tue Feb 26 2002 Toshihiro Yamagishi<toshihiro@turbolinux.co.jp>
- updated to 1.0.5

* Thu Jun 14 2001 Hirofumi Takeda <takepin@turbolinux.co.jp>
- Initial release. (1.0.4)
