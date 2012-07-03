Name: cabal2rpm
Version: 0.20.08
Release: alt9
License: GPL2+
Group: Development/Haskell
Source: %name-%version.tar
Summary: converts Haskell Cabal descriptions into RPM specs
Url: http://community.moertel.com/ss/space/Cabal2rpm

BuildArch: noarch

%description
This tool converts Haskell Cabal package-descriptions (.cabal files)
into RPM spec files.  It makes reasonable guesses at what should go
in the specs, but because "Cabalized" tarballs presently do not have a
standardized layout and naming conventions, you may need to make some
adjustments.

%prep
%setup

%build
%install
install -D -m755 cabal2rpm %buildroot%_bindir/cabal2rpm
install -D -m755 cabal2gear %buildroot%_bindir/cabal2gear

%files
%_bindir/cabal2rpm
%_bindir/cabal2gear

%changelog
* Sun Jul 01 2012 Denis Smirnov <mithraen@altlinux.ru> 0.20.08-alt9
- fix spec creation for packages with executables

* Sat Jun 30 2012 Denis Smirnov <mithraen@altlinux.ru> 0.20.08-alt8
- cabal2gear -- ghc version autodetect
- haddock fix

* Tue Mar 27 2012 Denis Smirnov <mithraen@altlinux.ru> 0.20.08-alt7
- fix working in non-english locales
- change gear repo structure

* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 0.20.08-alt6
- ghc 7.4.1 support

* Sun Sep 19 2010 Denis Smirnov <mithraen@altlinux.ru> 0.20.08-alt5
- add Url tag

* Tue Sep 14 2010 Denis Smirnov <mithraen@altlinux.ru> 0.20.08-alt4
- use new macro from rpm-build-haskell

* Fri Sep 10 2010 Denis Smirnov <mithraen@altlinux.ru> 0.20.08-alt3
- fix changelog
- add cabal2gear utility

* Thu Sep 09 2010 Denis Smirnov <mithraen@altlinux.ru> 0.20.08-alt2
- fix for ghc 6.12

* Wed Sep 08 2010 Denis Smirnov <mithraen@altlinux.ru> 0.20.08-alt1
- first build for Sisyphus
