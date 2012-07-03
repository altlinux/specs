%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name uniplate
%define f_pkg_name uniplate
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.6.3
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://community.haskell.org/~ndm/uniplate/
Source: %name-%version.tar
Summary: Help writing simple, concise and fast generic operations.
# Automatically added by buildreq on Tue Oct 25 2011 (-bb)
# optimized out: elfutils ghc libgmp-devel pkg-config python-base
BuildRequires: ghc-alex ghc-c2hs ghc-cpphs ghc-happy ghc-hscolour ghc-prof ghc-syb rpm-build-haskell

BuildRequires: ghc 
BuildRequires(pre): rpm-build-haskell



%description
Uniplate is library for writing simple and concise generic operations.
Uniplate has similar goals to the original Scrap Your Boilerplate work, but
is substantially simpler and faster.

To get started with Uniplate you should import one of the three following
modules:

* "Data.Generics.Uniplate.Data" - to quickly start writing generic
functions. Most users should start by importing this module.

* "Data.Generics.Uniplate.Direct" - a replacement for
"Data.Generics.Uniplate.Data" with substantially higher performance (around
5 times), but requires writing instance declarations.

* "Data.Generics.Uniplate.Operations" - definitions of all the operations
defined by Uniplate. Both the above two modules re-export this module.

In addition, some users may want to make use of the following modules:

* "Data.Generics.Uniplate.Zipper" - a zipper built on top of Uniplate
instances.

* "Data.Generics.SYB" - users transitioning from the Scrap Your Boilerplate
library.

* "Data.Generics.Compos" - users transitioning from the Compos library.

* "Data.Generics.Uniplate.DataOnly" - users making use of both @Data@ and
@Direct@ to avoid getting instance conflicts. 

%prep
%setup

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

cd %buildroot%_datadir/doc/%name-%version
rm -rf doc LICENSE examples

%files -f %name-files.nonprof
%hs_pkgconfdir/%f_pkg_name-%version.conf
%doc dist/doc/html
#%%doc LICENSE examples

%changelog
* Mon Oct 24 2011 Denis Smirnov <mithraen@altlinux.ru> 1.6.3-alt1
- Spec created by cabal2rpm 0.20_08
