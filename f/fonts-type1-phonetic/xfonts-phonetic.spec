%define type1dir %_datadir/fonts/type1/phonetic
%define vdate 19980806
Name: fonts-type1-phonetic
Version: 0.%vdate
Release: alt1.1

Summary: Phonetic fonts for X Window System
Summary(ru_RU.UTF-8): Фонетические шрифты для X Window System
License: distributable
Group: System/Fonts/Type1
URL: http://www.ctan.org/tex-archive/fonts/tipa/

Packager: Igor Vlasenko <viy@altlinux.ru>

Source0: tipa-type1-%vdate.tar.bz2
Source1: silipa-1.enc
Source2: fonts.dir
# TODO: for migration to 1.3
Source3: gen-fonts-alias-alt.pl

BuildArch: noarch
PreReq: fontconfig >= 2.4.2

Provides: xfonts-phonetic
Obsoletes: xfonts-phonetic
Provides: phonetic-fonts-type1
Obsoletes: phonetic-fonts-type1

%description
Collection of phonetic Type1 fonts for X Window System from TeX Live
CD distribution.
This package contains type 1 version of the Phonetic fonts of the TIPA
 (Tokyo International Phonetic Alphabet) for the X Window system.  It
 contains the pfb and afm files.  The installed X font has the silipa
 encoding (see http://www.sil.org/computing/fonts/encore-ipa.html).

%description -l ru_RU.UTF-8
Набор фонетических шрифтов в формате Type1 для X Window System из 
дистрибутива TeX Live CD.

%prep
%setup -q -n tipa-type1-%vdate
mkdir rpmdoc
cp README rpmdoc

%install
mkdir -p $RPM_BUILD_ROOT%type1dir
install -p -m644 *.pfb afm/*.afm %SOURCE1 %SOURCE2 $RPM_BUILD_ROOT%type1dir
cat > $RPM_BUILD_ROOT%type1dir/encodings.dir <<EOF
1
silipa-1 %type1dir/silipa-1.enc
EOF

ln -s fonts.dir %buildroot%type1dir/fonts.scale

mkdir -p %buildroot%_sysconfdir/X11/fontpath.d
ln -s ../../..%type1dir %buildroot%_sysconfdir/X11/fontpath.d/type1-phonetic:pri=40

%post
%_bindir/fc-cache %type1dir ||:

%triggerun -- %name <= 0.19980806-alt1
if [ -x %_sbindir/chkfontpath -a -f %_sysconfdir/X11/fs/config ]; then
	%_sbindir/chkfontpath -q -r %type1dir ||:
fi

%postun
if [ "$1" = "0" ]; then
        %_bindir/fc-cache --system-only ||:
fi

%files
%_sysconfdir/X11/fontpath.d/*
%type1dir
%doc rpmdoc/*

%changelog
* Tue Sep 04 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.19980806-alt1.1
- NMU:
  + used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Tue Jan 23 2007 Igor Vlasenko <viy@altlinux.ru> 0.19980806-alt1
- fixed typo in silipa.enc;
- changed name and install dir to follow ALT font policy;
- changed version to make future migration to tipa-1.3 easy;
- TODO: migrate to tipa-1.3 (hint: use debian);

* Sat Apr 22 2006 Igor Vlasenko <viy@altlinux.ru> 19980806-alt2
- NMU: fixed bug: path to silipa.enc

* Mon Aug 23 2004 Vyacheslav Dikonov <slava@altlinux.ru> 19980806-alt1
- moved to /usr/share/fonts, changed name to follow general policy

* Mon Nov 11 2002 Stanislav Ievlev <inger@altlinux.ru> 19980806-ipl4
- rebuild

* Sat Jun 9 2001 AEN <aen@logic.ru> 19980806-ipl3
- silipa.enc fixed (thnx to Vladimir Byrganov)

* Tue May 22 2001 Stanislav Ievlev <inger@altlinux.ru> 19980806-ipl2
- Remove XFree86 requirement from spec. We need only XFree86-libs

* Wed Feb 21 2001 Peter 'Nidd' Novodvorsky <petya@logic.ru> ipl1
- Initial release
