%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name monad-control
%define f_pkg_name monad-control
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.3.1.4
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: https://github.com/basvandijk/monad-control
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Lift control operations, like exception catching, through monad transformers



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1 ghc7.6.1-common ghc7.6.1-transformers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-base-unicode-symbols ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-hscolour ghc7.6.1-transformers-base

%description
This package defines the type class @MonadBaseControl@, a subset of
@MonadBase@ into which generic control operations such as @catch@ can be
lifted from @IO@ or any other base monad. Instances are based on monad
transformers in @MonadTransControl@, which includes all standard monad
transformers in the @transformers@ library except @ContT@.

See the @lifted-base@ package which uses @monad-control@ to lift @IO@
operations from the @base@ library (like @catch@ or @bracket@) into any
monad that is an instance of @MonadBase@ or @MonadBaseControl@.

Note that this package is a rewrite of Anders Kaseorg's @monad-peel@
library. The main difference is that this package provides CPS style
operators and exploits the @RankNTypes@ and @TypeFamilies@ language
extensions to simplify and speedup most definitions.

The following @criterion@ based benchmark shows that @monad-control@ is on
average about 99% faster than @monad-peel@:

@git clone <https://github.com/basvandijk/bench-monad-peel-control>@

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.3.1.4-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.3.1.4-alt1
- Spec created by cabal2rpm 0.20_08
