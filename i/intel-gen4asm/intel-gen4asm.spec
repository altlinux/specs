Name: intel-gen4asm
Version: 1.2
Release: alt1
Summary: intel-gen4asm
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: flex

%description
intel-gen4asm is a program to compile an assembly language for the Intel 965
Express Chipset.  It has been used to construct programs for textured video in
the 2d driver.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_pkgconfigdir/*.pc

%changelog
* Mon Jul 16 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.2-alt1
- 1.2

* Tue Jan 25 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt1
- 1.1

* Fri Jul 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt1
- 1.0

* Tue Aug 26 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.1-alt1
- initial release
