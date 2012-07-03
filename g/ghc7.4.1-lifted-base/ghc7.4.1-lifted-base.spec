%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name lifted-base
%define f_pkg_name lifted-base
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.1.0.3
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: https://github.com/basvandijk/lifted-base
Source: %name-%version.tar
Summary: lifted IO operations from the base library



# Automatically added by buildreq on Mon Mar 19 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-base-unicode-symbols ghc7.4.1-common ghc7.4.1-transformers ghc7.4.1-transformers-base libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1-doc ghc7.4.1-monad-control

%description
@lifted-base@ exports IO operations from the base library lifted to any
instance of 'MonadBase' or 'MonadBaseControl'.

Note that not all modules from @base@ are converted yet. If you need a
lifted version of a function from @base@, just ask me to add it or send me
a patch.

The package includes a copy of the @monad-peel@ testsuite written by Anders
Kaseorg The tests can be performed using @cabal test@. 

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
* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 0.1.0.3-alt1
- Spec created by cabal2rpm 0.20_08
