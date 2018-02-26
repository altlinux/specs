%define _fontsdir %_datadir/fonts/bitmap/tamil

Name: fonts-bitmap-tamil
Version: 1.0
Release: alt2

Summary: Tamil bitmap fonts
Summary (ru_RU.UTF-8): Тамильские растровые шрифты 
License: Free
Group: System/Fonts/X11 bitmap
Url: http://groups.yahoo.com/group/tamilinix/files

Source: tscii-bitmap.tar.bz2

PreReq: fontconfig >= 2.4.2
Obsoletes: tamil-fonts-bitmap
Provides: tamil-fonts-bitmap = %version

BuildArch: noarch
BuildRequires: xorg-x11-font-utils

%description
This Package provides free Tamil bitmap fonts.

%description -l ru_RU.UTF-8
В этом пакете находятся тамильские растровые шрифты.

%prep
%setup -q -n tscii-bitmap

%build
for i in $( ls *.bdf ); do
    bdftopcf "$i" | gzip > "$(echo $i | sed -e "s/.bdf//")".pcf.gz
done

%install
mkdir -p %buildroot%_fontsdir
install -m644 *.pcf.gz %buildroot%_fontsdir
install -m644 fonts.dir %buildroot%_fontsdir/fonts.dir

mkdir -p %buildroot%_sysconfdir/X11/fontpath.d
ln -s ../../..%_fontsdir %buildroot%_sysconfdir/X11/fontpath.d/bitmap-tamil:unscaled:pri=20

%post
%_bindir/fc-cache %_fontsdir

%files
%doc README
%_sysconfdir/X11/fontpath.d/*
%_fontsdir

%changelog
* Fri Aug 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt2
- rebuild with fonts policy
- used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Thu Nov 28 2002 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- ALTLinux build
