%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name citeproc-hs
%define f_pkg_name citeproc-hs
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.3.6
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://gorgias.mine.nu/repos/citeproc-hs/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A Citation Style Language implementation in Haskell



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.6.1 ghc7.6.1-common ghc7.6.1-extensible-exceptions ghc7.6.1-list ghc7.6.1-mtl ghc7.6.1-network ghc7.6.1-parsec ghc7.6.1-syb ghc7.6.1-text ghc7.6.1-transformers ghc7.6.1-utf8-string libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-happy ghc7.6.1-hexpat ghc7.6.1-hs-bibutils ghc7.6.1-hscolour ghc7.6.1-http ghc7.6.1-json ghc7.6.1-pandoc-types

%description
citeproc-hs is a library for rendering bibliographic reference citations
into a variety of styles using a macro language called Citation Style
Language (CSL). More details on CSL can be found here:
<http://citationstyles.org/>.

For the API documentation please see "Text.CSL".

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.3.6-alt1
- Spec created by cabal2rpm 0.20_08
