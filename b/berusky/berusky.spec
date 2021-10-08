Name:           berusky
Version:        1.7.2
Release:        alt2
Summary:        Berusky, 2D logic game
License:        GPLv2
Group:          Games/Other
Source:         http://www.anakreon.cz/download/berusky/tar.gz/%{name}-%{version}.tar.gz
URL:            http://www.anakreon.cz/
Requires:       berusky-data
Requires:       SDL

# Automatically added by buildreq on Mon Mar 02 2009 (-bi)
BuildRequires: gcc-c++ gcc-fortran libgtk+2-devel libSDL_image-devel libncursesw-devel

%description
Berusky is a 2D logic game based on an ancient puzzle named Sokoban.

An old idea of moving boxes in a maze has been expanded with new logic
items such as explosives, stones, special gates and so on.
In addition, up to five bugs can cooperate and be controlled by the player.

This package contains a binary for the game.

%prep
%setup

%build
%autoreconf
%add_optflags -std=gnu++14
%configure
%make

%install
%makeinstall_std

# Need for starting the game
install -D data/berusky.ini %buildroot/var/games/berusky/berusky.ini

pushd %buildroot/usr/doc
mkdir -p %buildroot%_defaultdocdir/%name
mv * %buildroot%_defaultdocdir/%name
popd

%files
%doc %_defaultdocdir/%name
%_bindir/%name
%_datadir/%name
%dir /var/games/%name
/var/games/%name/berusky.ini

%changelog
* Fri Oct 08 2021 Grigory Ustinov <grenka@altlinux.org> 1.7.2-alt2
- Fixed FTBFS.

* Fri Jul 03 2020 Grigory Ustinov <grenka@altlinux.org> 1.7.2-alt1
- Build new version.

* Thu Aug 16 2018 Grigory Ustinov <grenka@altlinux.org> 1.7.1.0.8.gitc5f0c88-alt1
- Build from last commit.
- Fix program crash at start, adding the config file.

* Tue Jun 05 2018 Grigory Ustinov <grenka@altlinux.org> 1.7.1-alt1
- Build new version (Closes: #29541).

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.1-alt1.2.qa1
- NMU: rebuilt for debuginfo.

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
