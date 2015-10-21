Name: haskell-filetrigger
Summary: auto recache ghc package list
Version: 0.0.5
Release: alt2
License: GPL
Group: Development/Haskell
BuildArch: noarch
Packager: Denis Smirnov <mithraen@altlinux.ru>

Conflicts: ghc < 7.6.1

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%install
install -m755 -D haskell.filetrigger %buildroot/usr/lib/rpm/haskell.filetrigger

%files
/usr/lib/rpm/haskell.filetrigger

%changelog
* Wed Oct 21 2015 Ivan Zakharyaschev <imz@altlinux.org> 0.0.5-alt2
- fix this package's conflicts range
  (not to conflict with the current ghc7.6.1-common package)

* Fri Nov 30 2012 Denis Smirnov <mithraen@altlinux.ru> 0.0.5-alt1
- fix work with ghc-pkg from ghc 7.6.1

* Sun Mar 18 2012 Denis Smirnov <mithraen@altlinux.ru> 0.0.4-alt1
- check packages integrity after install

* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 0.0.3-alt1
- add multiple ghc versions support

* Fri Sep 10 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.2-alt1
- cleanup

* Thu Sep 09 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- first build for Sisyphus
