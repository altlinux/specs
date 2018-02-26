%define ttfdir %_datadir/fonts/ttf/TrueType-vera
%define origname ttf-bitstream-vera

Name: fonts-ttf-vera
Version: 1.10
Release: alt3

Summary: Bitstream Vera Fonts
License: Freely distributable
Group: System/Fonts/True type

Url: http://www.gnome.org/fonts
Source: ftp://ftp.gnome.org/pub/GNOME/sources/%origname/%origname-%version.tar.bz2

BuildArch: noarch

PreReq: fontconfig >= 2.4.2
Obsoletes: vera-fonts-ttf
Provides: vera-fonts-ttf = %version

BuildRequires: mkfontscale

Summary(ru_RU.KOI8-R): Шрифты Bitstream Vera
Summary(uk_UA.KOI8-U): Шрифти Bitstream Vera

%description
This package contains Bitstream Vera fonts.

%description -l ru_RU.KOI8-R
Этот пакет содержит свободно распространяемые шрифты Bitstream Vera.

%description -l uk_UA.KOI8-U
Цей пакунок м╕стить в╕льно розповсюджуван╕ шрифти Bitstream Vera.

%prep
%setup -q -n %origname-%version

%build
%install
%__mkdir_p %buildroot%ttfdir/
%__install -p -m644 *.ttf %buildroot%ttfdir/
mkfontscale %buildroot%ttfdir
%__ln_s fonts.scale %buildroot%ttfdir/fonts.dir

%__mkdir_p %buildroot%_sysconfdir/X11/fontpath.d
%__ln_s ../../..%ttfdir %buildroot%_sysconfdir/X11/fontpath.d/ttf-TrueType-vera:pri=50

%post
%_bindir/fc-cache %ttfdir ||:

%files
%doc COPYRIGHT.TXT local.conf README.TXT RELEASENOTES.TXT
%_sysconfdir/X11/fontpath.d/*
%ttfdir

%changelog
* Thu Aug 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.10-alt3
- rebuild with fonts policy
- used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Thu Feb 12 2004 Michael Shigorin <mike@altlinux.ru> 1.10-alt2
- fixed #3691

* Sun Jan 04 2004 Michael Shigorin <mike@altlinux.ru> 1.10-alt1
- built for ALT Linux
  (looking at thai-fonts-ttf-0.1-alt2 spec by Vyacheslav Dikonov <slava@>)

* Thu Apr 17 2003 GЖtz Waschk <waschk linux-mandrake com> 1.10-2mdk
- add fonts.dir and fonts.scale for chkfontpath

* Thu Apr 17 2003 Frederic Crozat <fcrozat mandrakesoft com> - 1.10-1mdk
- Initial build.

