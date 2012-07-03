%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name ghc-mod
%define f_pkg_name ghc-mod
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.10.11
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://www.mew.org/~kazu/proj/ghc-mod/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Happy Haskell programming on Emacs/Vim



# Automatically added by buildreq on Fri Mar 23 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-base-unicode-symbols ghc7.4.1-common ghc7.4.1-cpphs ghc7.4.1-hashable ghc7.4.1-haskell-src-exts ghc7.4.1-hscolour ghc7.4.1-lifted-base ghc7.4.1-monad-control ghc7.4.1-mtl ghc7.4.1-regex-base ghc7.4.1-syb ghc7.4.1-text ghc7.4.1-transformers ghc7.4.1-transformers-base ghc7.4.1-uniplate ghc7.4.1-unordered-containers libgmp-devel pkg-config python-base
BuildRequires: ghc7.4.1-alex ghc7.4.1-c2hs ghc7.4.1-ghc-paths ghc7.4.1-ghc-syb-utils ghc7.4.1-happy ghc7.4.1-hlint ghc7.4.1-io-choice ghc7.4.1-regex-posix

%description
This packages includes Elisp files and a Haskell command, "ghc-mod".
"ghc*.el" enable completion of Haskell symbols on Emacs. Flymake is also
integrated. "ghc-mod" is a backend of "ghc*.el". It lists up all installed
modules or extracts names of functions, classes, and data declarations. To
use "ghc-mod" on Vim, see <https://github.com/eagletmt/ghcmod-vim> or
<https://github.com/scrooloose/syntastic>

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

cd %buildroot%_datadir/doc/%name-%version
rm -rf doc LICENSE examples

%files -f %name-files.nonprof
%_bindir/*
%_datadir/%name-%version

%changelog
* Fri Mar 23 2012 Denis Smirnov <mithraen@altlinux.ru> 1.10.11-alt1
- Spec created by cabal2rpm 0.20_08
