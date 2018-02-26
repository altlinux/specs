Name: lufis
Version: 0.3
Release: alt2

Summary: Wrapper to use lufs modules with fuse kernel support
License: GPL
Group: System/Kernel and hardware
Url: http://sourceforge.net/projects/fuse

Summary(ru_RU.KOI8-R): Обертка для использования модулей lufs с ядерными модулями от fuse

Source: %name-%version.tar.bz2
#Patch: PLD-lufis-no_lufs.patch
#Patch2: gentoo-lufis-allow-uid-and-gid.patch
Requires: fuse >= 2.3-alt1

# Automatically added by buildreq on Thu Feb 10 2005
BuildRequires: glib2 libfuse-devel pkgconfig

%description
Wrapper to use lufs modules with fuse kernel support

%description -l ru_RU.KOI8-R
Обертка для использования модулей lufs с ядерными модулями от fuse

%prep
%setup -q
#%patch -p1
#%patch2 -p1

%build
%make_build

%install
install -d %buildroot%_bindir/
install lufis %buildroot%_bindir/

%files
%_bindir/lufis

%doc ChangeLog README

%changelog
* Wed Sep 07 2005 Serge Pavlovsky <pal@altlinux.ru> 0.3-alt2
- built with new libfuse

* Thu Feb 10 2005 Serge Pavlovsky <pal@altlinux.ru> 0.3-alt1
- new version

* Sat Jan 15 2005 Serge Pavlovsky <pal@altlinux.ru> 0.2-alt1
- converted from PLD

