%define ghc_version 7.4.1
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
URL: http://gorgias.mine.nu/repos/citeproc-hs/
Source: %name-%version.tar
Summary: A Citation Style Language implementation in Haskell 



# Automatically added by buildreq on Mon Mar 19 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-common ghc7.4.1-mtl ghc7.4.1-syb ghc7.4.1-text ghc7.4.1-transformers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1-hs-bibutils ghc7.4.1-json ghc7.4.1-pandoc-types ghc7.4.1-parsec ghc7.4.1-utf8-string ghc7.4.1-xml

%description
citeproc-hs is a library for rendering bibliographic reference citations
into a variety of styles using a macro language called Citation Style
Language (CSL). More details on CSL can be found here:
<http://citationstyles.org/>.

For the API documentation please see "Text.CSL". 

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
* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 0.3.4-alt1
- Spec created by cabal2rpm 0.20_08
