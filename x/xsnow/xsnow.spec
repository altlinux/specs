Name: xsnow
Version: 1.42
Release: alt4

Summary: An X Window System based dose of Christmas cheer
License: MIT
Group: Toys

Url: http://dropmix.xs4all.nl/rick/Xsnow/
Source0: %url/xsnow-%version.tar.gz
Source1: xsnow.png
Patch: xsnow-1.42-misc.patch
Packager: Michael Shigorin <mike@altlinux.org>

Summary(ru_RU.KOI8-R): Рождественская игрушка для X Window
Summary(uk_UA.KOI8-U): Р╕здвяна цяцька для X Window

# Automatically added by buildreq on Fri Oct 30 2009
BuildRequires: gccmakedep imake libXext-devel libXpm-devel libXt-devel xorg-cf-files

%description
The Xsnow toy provides a continual gentle snowfall, trees, and Santa
Claus flying his sleigh around the screen.  Xsnow is only for the X
Window System, though; consoles just get coal.

%description -l ru_RU.KOI8-R
Xsnow добавляет снегопад, елки и оленей к новогоднему фону экрана.

%description -l uk_UA.KOI8-U
Xsnow дода╓ хуртовину, смереки та олен╕в до новор╕чного тла екрану.

%prep
%setup
%patch -p1

%build
xmkmf -a
%make

%install
%makeinstall_std install.man
install -pDm644 %SOURCE1 %buildroot%_liconsdir/%name.png

%files
%doc README
%_bindir/*
%_man1dir/*
%_liconsdir/*

%changelog
* Sun Dec 13 2009 Michael Shigorin <mike@altlinux.org> 1.42-alt4
- an icon is now correctly placed 48x48 one (thx repocop)

* Fri Oct 30 2009 Michael Shigorin <mike@altlinux.org> 1.42-alt3
- buildreq per repocop proposal
- updated an Url:
- minor spec cleanup

* Tue Jun 20 2006 Michael Shigorin <mike@altlinux.org> 1.42-alt2.1
- rebuild (x86_64)

* Mon Feb 28 2005 Victor Forsyuk <force@altlinux.ru> 1.42-alt2
- Updated build deps and patch.

* Thu Dec 26 2002 Michael Shigorin <mike@altlinux.ru> 1.42-alt1
- built for ALT Linux
- based on Red Hat spec; credits:
  Donnie Barnes <djb@redhat.com>
  Erik Troan <ewt@redhat.com>
  Michael Maher <mike@redhat.com>
  Than Ngo <than@redhat.com>
  Tim Powers <timp@redhat.com>
