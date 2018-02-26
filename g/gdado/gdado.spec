Name: gdado
Version: 2.2
Release: alt5

Summary: Very simple application that simulates dice rolling
License: GPL
Group: Games/Other
Url: http://gdado.sourceforge.net

Source0: %name-%version.tar.gz
Source1: gdado-48x48.png
Source2: gdado-32x32.png
Source3: gdado-16x16.png

Patch0: gdado-2.2-alt-desktop-file.patch

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Thu Apr 10 2008
BuildRequires: libgnomeui-devel

%description
Gdado is a very simple application that simulates dice rolling. It is
intended to help roleplayers.

%prep
%setup -q
%patch0 -p1

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

mkdir -p %buildroot%_liconsdir/
mkdir -p %buildroot%_niconsdir/
mkdir -p %buildroot%_miconsdir/

install -m644 %SOURCE1 %buildroot%_liconsdir/gdado.png
install -m644 %SOURCE2 %buildroot%_niconsdir/gdado.png
install -m644 %SOURCE3 %buildroot%_miconsdir/gdado.png
install -m644 %SOURCE1 %buildroot%_datadir/pixmaps/gdado.png

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog README TODO
%_bindir/gdado
%_datadir/applications/gdado.desktop
%dir %_datadir/pixmaps/gdado
%_datadir/pixmaps/gdado/*
%_liconsdir/gdado.png
%_niconsdir/gdado.png
%_miconsdir/gdado.png
%_datadir/pixmaps/gdado.png

%changelog
* Wed Dec 03 2008 Igor Zubkov <icesik@altlinux.org> 2.2-alt5
- apply patch from repocop

* Thu Jul 10 2008 Igor Zubkov <icesik@altlinux.org> 2.2-alt4
- fix desktop file and icons for desktop file (thanks to repocop)

* Thu Apr 10 2008 Igor Zubkov <icesik@altlinux.org> 2.2-alt3
- run %%update_menus after install and %%clean_menus after uninstall
  (thanks repocop!)
- buildreq

* Mon Jun 25 2007 Igor Zubkov <icesik@altlinux.org> 2.2-alt2
- buildreq

* Sat May 05 2007 Igor Zubkov <icesik@altlinux.org> 2.2-alt1
- build for Sisyphus

