%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name network-uri
%define f_pkg_name network-uri
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 2.6.1.0
Release: alt1
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: https://github.com/haskell/network-uri
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: URI manipulation

BuildPreReq: haskell(abi) = %ghc_version


%description
This package provides facilities for parsing and unparsing URIs, and
creating and resolving relative URI references, closely following the URI
spec, <http://www.ietf.org/rfc/rfc3986.txt IETF RFC 3986>.

== Backward-compatibility

In @network-2.6@ the "Network.URI" module was split off from the @network@
package into this package. If you're using the "Network.URI" module you can
be backward compatible and automatically get it from the right package by
using the </package/network-uri-flag network-uri-flag pseudo-package> in
your @.cabal@ file's build-depends (along with dependencies for both
@network-uri@ and @network@):

> build-depends: > network-uri-flag == 0.1.*

Or you can do the same manually by adding this boilerplate to your @.cabal@
file:

> flag network-uri > description: Get Network.URI from the network-uri
package > default: True > > library > -- ... > if flag(network-uri) >
build-depends: network-uri >= 2.6, network >= 2.6 > else > build-depends:
network-uri < 2.6, network < 2.6

That is, get the module from either @network < 2.6@ or from @network-uri >=
2.6@.

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
* Wed Apr 17 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.6.1.0-alt1
- Spec created by cabal2rpm 0.20_11
