Summary:        Berusky, 2D logic game
Name:           berusky
Version:        1.1
Release:        alt1.2
License:        GPL
Group:     Games/Other
Source:         http://www.anakreon.cz/download/berusky/tar.gz/%{name}-%{version}.tar.gz
URL:            http://www.anakreon.cz/
Packager:  Dmitriy Kulik <lnkvisitor@altlinux.org>
Requires:  	berusky-data
Requires:  	SDL

# Automatically added by buildreq on Mon Mar 02 2009 (-bi)
BuildRequires: gcc-c++ gcc-fortran libSDL-devel libncurses-devel

%description
Berusky is a 2D logic game based on an ancient puzzle named Sokoban.

An old idea of moving boxes in a maze has been expanded with new logic
items such as explosives, stones, special gates and so on.
In addition, up to five bugs can cooperate and be controlled by the player.

This package contains a binary for the game.

%prep
%setup -q -n %name-%version

%build
%configure \
    CFLAGS="$RPM_OPT_FLAGS"

%make

%install
rm -rf %buildroot
make DESTDIR=%buildroot install

mkdir -p %buildroot/%_datadir/%name
mkdir -p %buildroot/%_docdir/%name-%version

pushd %buildroot/usr/doc
mv * %buildroot%_docdir/%name-%version
popd

%files
%dir %_docdir/%name-%version
%doc %_docdir/%name-%version/*
%_bindir/berusky
%_datadir/%name/*

%changelog
* Thu Jan 07 2010 Dmitriy Kulik <lnkvisitor at altlinux.org> 1.1-alt1.2
- NMU (by repocop): the following fixes applied:
  * docdir-is-not-owned for berusky
  * postclean-05-filetriggers for spec file

* Tue Jan 05 2010 Dmitriy Kulik <lnkvisitor at altlinux.org> 1.1-alt1.1
- fix overflow destination buffer

* Mon Mar 02 2009 Dmitriy Kulik  <lnkvisitor@altlinux.org> 1.1-alt1
- Build for Alt Linux Sisyphus

* Mon Apr 23 2007 Martin Stransky <stransky@redhat.com> 1.1-1
- initial build

* Fri Apr 20 2007 Martin Stransky <stransky@redhat.com> 1.0-1
- initial build
