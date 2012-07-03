%define ghc_version 7.4.2
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name ghc-mod
%define f_pkg_name ghc-mod
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.11.0
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://www.mew.org/~kazu/proj/ghc-mod/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Happy Haskell programming on Emacs/Vim



# Automatically added by buildreq on Sun Jul 01 2012 (-bb)
# optimized out: elfutils ghc7.4.2 ghc7.4.2-base-unicode-symbols ghc7.4.2-common ghc7.4.2-cpphs ghc7.4.2-hashable ghc7.4.2-haskell-src-exts ghc7.4.2-hscolour ghc7.4.2-lifted-base ghc7.4.2-monad-control ghc7.4.2-mtl ghc7.4.2-regex-base ghc7.4.2-syb ghc7.4.2-text ghc7.4.2-transformers ghc7.4.2-transformers-base ghc7.4.2-uniplate ghc7.4.2-unordered-containers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.2-alex ghc7.4.2-c2hs ghc7.4.2-ghc-paths ghc7.4.2-ghc-syb-utils ghc7.4.2-happy ghc7.4.2-hlint ghc7.4.2-io-choice ghc7.4.2-regex-posix

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

%files -f %name-files.all

%changelog
* Sun Jul 01 2012 Denis Smirnov <mithraen@altlinux.ru> 1.11.0-alt1
- Spec created by cabal2rpm 0.20_08
