%define cname xtermg

Name: fonts-bitmap-%cname
Version: 3.3
Release: alt2
Summary: XTermG fonts - a fixed width English/Cyrillic fonts with some additional characters
License: MIT
Group: System/Fonts/X11 bitmap
BuildArch: noarch

Source0: %name-%version.tar.gz

BuildPreReq: rpm-build-fonts

# Automatically added by buildreq on Wed Apr 04 2018
BuildRequires: bdftopcf python3-dev python3-module-tpg

%description
XTermG fonts is an English/Cyrillic (ISO10646-1 and KOI7/8)
fixed size font familly with some commonly useful characters added.
Sizes: 12x20 12x20 8x14 8x16 8x16 8x8

# TODO package -n fonts-console-%cname

%prep
%setup -n george.fonts

%build
%make pcf

%install
%bitmap_fonts_install %cname

%files -f %cname.files
%doc TODO

%changelog
* Sun Jan 09 2022 Fr. Br. George <george@altlinux.ru> 3.3-alt2
- Initial new symbols

* Sat Oct 09 2021 Fr. Br. George <george@altlinux.ru> 3.3-alt1
- New symbols

* Fri Mar 12 2021 Fr. Br. George <george@altlinux.ru> 3.2-alt2
- Fix charset

* Fri Apr 10 2020 Fr. Br. George <george@altlinux.ru> 3.2-alt1
- Black circle

* Sat May 25 2019 Fr. Br. George <george@altlinux.ru> 3.1-alt1
- Linedraw endings

* Wed Apr 04 2018 Fr. Br. George <george@altlinux.ru> 3.0-alt1
- ALT build at least


