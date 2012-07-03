%define _bigfontsdir %_datadir/fonts/ttf/chinese-big5
%define _gbfontsdir %_datadir/fonts/ttf/chinese-gb2312

Name: fonts-ttf-chinese
Version: 1.0
Release: alt8

Summary: Free Chinese TrueType fonts
Summary (ru_RU.UTF-8): Китайские TrueType шрифты
License: GPL-like (see arphicpl.txt)
Group: System/Fonts/True type
Url: ftp://linux.tmtc.edu.tw/pub/arphic
Source: fonts-ttf-chinese.tar.bz2

BuildArch: noarch
BuildRequires: mkfontscale

%description
This Package provides free Chinese TrueType fonts.

%description -l ru_RU.UTF-8
В пакете находятся китайские TrueType шрифты.

%package big5
Summary: Chinese (Big5) TrueType fonts
Summary (ru_RU.UTF-8): Китайские (Big5) TrueType шрифты
License: GPL-like (see arphicpl.txt)
Group: System/Fonts/True type
PreReq: fontconfig >= 2.4.2
Obsoletes: chinese-fonts-ttf-big5
Provides: chinese-fonts-ttf-big5 = %version

%description big5
Chinese (Big5 encoded) TrueType Fonts donated by Arphic company.

%description big5 -l ru_RU.UTF-8
Китайские TrueType шрифты (кодировка Big5), от фирмы Arphic

%package gb2312
Summary: Chinese (GB2312) TrueType fonts
Summary (ru_RU.UTF-8): Китайские (GB2312) TrueType шрифты
License: GPL-like (see arphicpl.txt)
Group: System/Fonts/True type
PreReq: fontconfig >= 2.4.2
Obsoletes: chinese-fonts-ttf-gb2312
Provides: chinese-fonts-ttf-gb2312 = %version

%description gb2312
Chinese (GuoBiao 2312 encoded) TrueType Fonts donated by Arphic company.

%description gb2312 -l ru_RU.UTF-8
Китайские TrueType шрифты (кодировка GuoBiao 2312), от фирмы Arphic

%prep
%setup -q -n fonts-ttf-chinese

%build
%install
mkdir -p %buildroot%_bigfontsdir
install -m644 b*.ttf %buildroot%_bigfontsdir
mkfontscale %buildroot%_bigfontsdir
ln -s fonts.scale %buildroot%_bigfontsdir/fonts.dir

mkdir -p %buildroot%_gbfontsdir
install -m644 g*.ttf %buildroot%_gbfontsdir
mkfontscale %buildroot%_gbfontsdir
ln -s fonts.scale %buildroot%_gbfontsdir/fonts.dir

mkdir -p %buildroot%_sysconfdir/X11/fontpath.d
ln -s ../../..%_bigfontsdir %buildroot%_sysconfdir/X11/fontpath.d/ttf-chinese-big5:pri=50
ln -s ../../..%_gbfontsdir %buildroot%_sysconfdir/X11/fontpath.d/ttf-chinese-gb2312:pri=50

%post big5
%_bindir/fc-cache %_bigfontsdir ||:

%post gb2312
%_bindir/fc-cache %_gbfontsdir ||:

%files big5
%doc arphicpl.txt
%_sysconfdir/X11/fontpath.d/ttf-chinese-big5:pri=50
%_bigfontsdir

%files gb2312
%doc arphicpl.txt
%_sysconfdir/X11/fontpath.d/ttf-chinese-gb2312:pri=50
%_gbfontsdir

%changelog
* Thu Aug 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt8
- rebuild with fonts policy
- used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Mon Jul 11 2005 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt7
- link to encodings.dir removed, no longer requires freetype

* Thu Dec 16 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt6
- link to encodings.dir fixed

* Sat Jun 26 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt5
- %postun script fix

* Wed Feb 18 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt4
- %postun script fix

* Mon Sep 01 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt3
- Changed dir
- Cleanups

* Mon Jan 20 2003 Rider <rider@altlinux.ru> 1.0-alt2
- build requires fix (freetype)

* Wed Nov 27 2002 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- ALTLinux build
