Name: sdlaplay
Version: 0.0.4
Release: alt1
Summary: SDL audio player
License: GPLv2
Group: Sound
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar

BuildRequires: libSDL-devel libSDL_mixer-devel

%description
SDL audio player

%prep
%setup -q

%build
%autoreconf
%configure

%make

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*

%changelog
* Mon Jul 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.0.4-alt1
- 0.0.4

* Mon Jul 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.0.3-alt1
- 0.0.3

* Wed Nov 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.0.2-alt1
- 0.0.2

* Tue Nov 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.0.1-alt1
- initial release

