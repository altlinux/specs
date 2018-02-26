%define _fontsdir %_datadir/fonts/ttf/gw

Name: fonts-ttf-gw
Version: 1.0
Release: alt6

Summary: Free unicode TrueType fonts by George Williams
Summary (ru_RU.UTF-8): Свободные Unicode шрифты от Джорджа Вильямса в формате TrueType
License: BSD
Group: System/Fonts/True type
Url: http://bibliofile.mc.duke.edu/gww/fonts

Source0: CasUni.zip
Source1: MonospaceTTF.zip
Source2: CupUniTTF.zip
Source3: Caliban.ttf.gz
Source4: README
Source5: COPYING

PreReq: fontconfig >= 2.4.2
Obsoletes: gww-ttf gw-fonts-ttf
Provides: gww-ttf gw-fonts-ttf = %version

BuildArch: noarch
BuildRequires: unzip mkfontscale

%description
A set of Free unicode True Type fonts made by Gerge Williams.

%description -l ru_RU.UTF-8
Набор Unicode шрифтов формата TrueType от Джорджа Вильямса.

%prep
%install
unzip -u -L %SOURCE0 -d %name
unzip -u -L %SOURCE1 -d %name
unzip -u -L %SOURCE2 -d %name 
gunzip -c %SOURCE3 > %name/caliban_.ttf
cp %SOURCE4 %name/README
cp %SOURCE5 %name/COPYING

mkdir -p %buildroot%_fontsdir
install -m644 %name/*.ttf %buildroot%_fontsdir

mkfontscale %buildroot%_fontsdir
ln -s fonts.scale %buildroot%_fontsdir/fonts.dir

mkdir -p %buildroot%_sysconfdir/X11/fontpath.d
ln -s ../../..%_fontsdir %buildroot%_sysconfdir/X11/fontpath.d/ttf-gw:pri=50

%post
%_bindir/fc-cache %_fontsdir ||:

%files
%doc %name/README %name/COPYING
%_sysconfdir/X11/fontpath.d/*
%_fontsdir

%changelog
* Fri Aug 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt6
- rebuild with fonts policy
- used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Mon Jul 11 2005 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt5
- link to encodings.dir removed, no longer requires freetype
- updates

* Thu Dec 16 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt4
- link to encodings.dir fixed

* Wed Feb 18 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt3
- %postun script fix

* Sun Aug 24 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt2
- New version + Caliban, Cupola, Monospace
- Changed dir
- Cleanups

* Mon Nov 25 2002 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- 1st build
