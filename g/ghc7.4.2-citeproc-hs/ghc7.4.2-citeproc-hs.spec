%define ghc_version 7.4.2
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name citeproc-hs
%define f_pkg_name citeproc-hs
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.3.4
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://gorgias.mine.nu/repos/citeproc-hs/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A Citation Style Language implementation in Haskell



# Automatically added by buildreq on Sun Jul 01 2012 (-bb)
# optimized out: elfutils ghc7.4.2 ghc7.4.2-common ghc7.4.2-mtl ghc7.4.2-syb ghc7.4.2-text ghc7.4.2-transformers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.2-alex ghc7.4.2-cpphs ghc7.4.2-doc ghc7.4.2-happy ghc7.4.2-hs-bibutils ghc7.4.2-json ghc7.4.2-pandoc-types ghc7.4.2-parsec ghc7.4.2-utf8-string ghc7.4.2-xml

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
%hs_pkgconfdir/%f_pkg_name-%version.conf
%_docdir/%name-%version

%changelog
* Sat Jun 30 2012 Denis Smirnov <mithraen@altlinux.ru> 0.3.4-alt1
- Spec created by cabal2rpm 0.20_08
