Name: fillets-ng-data
Version: 1.0.0
Release: alt1

Summary: docs, graphics, music and international sounds for fillets-ng
License: GPL
Group: Games/Puzzles
Url: http://fillets.sourceforge.net/
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Source0: %name-%version.tar.gz

BuildArch: noarch

%description
Fish Fillets is strictly a puzzle game. The goal in every of the seventy
levels is always the same: find a safe way out. The fish utter witty remarks
about their surroundings, the various inhabitants of their underwater realm
quarrel among themselves or comment on the efforts of your fish. The whole
game is accompanied by quiet, comforting music.

This package contains the data needed for the game.

%prep
%setup -q

%build

%install
mkdir -p %buildroot%_datadir/fillets-ng/
cp -pr font images music script sound %buildroot%_datadir/fillets-ng/

%files
%doc doc/html/*
%_datadir/fillets-ng

%changelog
* Sat Dec 25 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt1
- New version

* Mon Dec 28 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.2-alt1
- New version

* Wed Mar 25 2009 Igor Zubkov <icesik@altlinux.org> 0.8.1-alt1
- 0.8.0 -> 0.8.1

* Wed Mar 05 2008 Igor Zubkov <icesik@altlinux.org> 0.8.0-alt1
- build for Sisyphus

