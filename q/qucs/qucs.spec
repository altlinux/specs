Name: qucs
Version: 0.0.16
Release: alt1
Summary: Circuit simulator
License: GPL
Group: Education
Url: http://qucs.sourceforge.net/

Source0: http://ovh.dl.sourceforge.net/sourceforge/qucs/%name-%version.tar.gz
Source1: %name.desktop
Source2: qucs-tango-icons.tar.bz2
Source3: qucs-icons.tar.bz2

# Automatically added by buildreq on Thu May 05 2011
# optimized out: fontconfig libICE-devel libSM-devel libX11-devel libstdc++-devel xorg-xproto-devel
BuildRequires: flex gperf imake libqt3-devel xorg-cf-files

BuildRequires: gcc3.4-c++

%description
Qucs is a circuit simulator with graphical user interface.  The
software aims to support all kinds of circuit simulation types,
e.g. DC, AC, S-parameter and harmonic balance analysis.

%prep
%setup
tar -xjf %SOURCE2 -C qucs

%build
#autoreconf
export CC=gcc-3.4 CXX=g++-3.4
%configure
%make_build

%install
%make DESTDIR=%buildroot install

install -pD -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
mkdir -p %buildroot%_iconsdir
tar -xjf %SOURCE3 -C %buildroot%_iconsdir

for l in $(find %buildroot%_datadir/%name/lang -name \*.qm); do
    echo -n $l | sed 's,.*_\(.*\)\.qm,%lang\(\1\) ,' >> %name.lang
    echo $l | sed "s,%buildroot,," >> %name.lang
done

%files -f %name.lang
%doc AUTHORS NEWS README TODO
%_bindir/*
%dir %_datadir/%name
%dir %_datadir/%name/lang
%_datadir/%name/bitmaps
%_datadir/%name/library
%_datadir/%name/tline
%_datadir/%name/octave
%dir %_datadir/%name/docs
%_datadir/%name/docs/en
%lang(de) %_datadir/%name/docs/de
%lang(es) %_datadir/%name/docs/es
%lang(fr) %_datadir/%name/docs/fr
%lang(ru) %_datadir/%name/docs/ru
%lang(uk) %_datadir/%name/docs/uk
%lang(cs) %_datadir/%name/docs/cs
%lang(pt) %_datadir/%name/docs/pt
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*.png
%_man1dir/*

%changelog
* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 0.0.16-alt1
- Autobuild version bump to 0.0.16
- Switch to gcc3.4 to avoid C++ error messages

* Thu Jul 01 2010 Fr. Br. George <george@altlinux.ru> 0.0.15-alt1.1
- Rebuild for Sisyphus

* Sun May 31 2009 Ilya Mashkin <oddity@altlinux.ru> 0.0.15-alt1
- 0.0.15

* Wed Jan 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.0.13-alt1
- 0.0.13

* Tue Jun 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.0.12-alt1
- 0.0.12

* Wed Jun 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.0.11-alt1
- initial build
