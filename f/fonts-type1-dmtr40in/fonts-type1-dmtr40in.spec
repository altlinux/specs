%define fname dmtr40in

Name: fonts-type1-dmtr40in
Version: 1.0
Release: alt4

Summary: Free sans serif font from Dmitry Sorokin
License: GPL
Group: System/Fonts/Type1

Url: ftp://ftp.ice.ru/pub/fonts/type1
Source: dmtr40in-fonts-1.0.tar.bz2
Packager: Michael Shigorin <mike@altlinux.org>

PreReq: fontconfig >= 2.4.2
Obsoletes: %fname-fonts <= 1.0-alt2
Provides: %fname-fonts = %version-%release
Conflicts: cyrillic-Type1-fonts

BuildArch: noarch
BuildRequires: mkfontscale
BuildRequires: rpm-build-fonts >= 0.3

Summary(ru_RU.UTF-8): Свободные шрифты без засечек от Дмитрия Сорокина

%description
Free versions of Bitstream Type1 fonts with cyrillic glyphs
from Dmitry Sorokin

%description -l ru_RU.UTF-8
Свободные версии шрифтов Bitstream Type 1 с кириллическими глифами
от Дмитрия Сорокина

%prep
%setup -n %fname-fonts-1.0

%install
%type1_fonts_install %fname

%post
%post_fonts

%postun
%postun_fonts

%files -f %fname.files
%doc COPYING

%changelog
* Mon Jul 20 2009 Michael Shigorin <mike@altlinux.org> 1.0-alt4
- added Conflicts: cyrillic-Type1-fonts (closes: #15040)
- fixed glyph attribution in (copied) package description
- spec cleanup according to fonts policy advice

* Fri Aug 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt3
- rebuild with fonts policy

* Tue Sep 02 2003 AEN <aen@altlinux.ru> 1.0-alt2
- Summary fixed (bug #2929)

* Tue Sep 02 2003 AEN <aen@altlinux.ru> 1.0-alt1
- new release from Dmitry Sorokin

* Wed Feb 05 2003 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.99-alt2
- Fixed typo in Summary.
- Added Summary and %%description translated in Russian.
- Added Packager tag.

* Tue Oct 15 2002 AEN <aen@altlinux.ru> 0.99-alt1
- new package in Sisyphus

