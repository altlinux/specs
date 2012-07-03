Name: gtuxnes
Version: 0.75
Release: alt3

Packager: Ilya Mashkin <oddity@altlinux.ru>

Summary: GUI for TuxNES Emulator 
Summary(ru_RU.KOI8-R): Интрефейс для эмулятора Nintendo (Денди) TuxNES
License: GPL
Group: Emulators
Url: http://www.scottweber.com/projects/gtuxnes 

Source0: gtuxnes-0.75.tar.gz
Source1: %name-16.xpm
Source2: %name-32.xpm
Source3: %name-48.xpm
Requires: tuxnes


# Automatically added by buildreq on Sun Jan 08 2006
BuildRequires: glib-devel gtk+-devel
ExclusiveArch: i586

%description
GUI for Emulator for the 8-bit Nintendo Entertainment System (a.k.a. Dendy) - TuxNES

%description -l ru_RU.KOI8-R
Интерфейс для эмулятора игровой консоли Nintendo (так же известной как Денди) - TuxNES


%prep
%setup -q


%build
%make

%install
install -D -pm 755 gtuxnes %buildroot%_bindir/%name
install -D -pm 644 %SOURCE1 %buildroot%_miconsdir/%name.xpm
install -D -pm 644 %SOURCE2 %buildroot%_niconsdir/%name.xpm
install -D -pm 644 %SOURCE3 %buildroot%_liconsdir/%name.xpm



mkdir -p %buildroot/%_menudir
cat << EOF > %buildroot/%_menudir/%name
?package(%name):needs="x11" section="Emulators" \
title="GTuxNES" command="%name" \
longtitle="GUI for Nintendo (Dendy) Emulator." \
icon="%name.xpm"
EOF




%files
%doc COPYING AUTHORS TODO README CHANGES 
%_menudir/*
%_bindir/*
#_iconsdir/*.xpm
#_iconsdir/mini/*.xpm
#_iconsdir/large/*.xpm

%_miconsdir/%name.xpm
%_niconsdir/%name.xpm
%_liconsdir/%name.xpm


%changelog
* Thu Sep 03 2009 Ilya Mashkin <oddity@altlinux.ru> 0.75-alt3
- build for i586 only
- remove old macros
- fix icons locations

* Mon Mar 27 2006 Ilya Mashkin <oddity at altlinux.ru> 0.75-alt2
- fix icons

* Sun Jan 08 2006 Ilya Mashkin <oddity at altlinux.ru> 0.75-alt1
- Initial Christmas build (so far from past)
