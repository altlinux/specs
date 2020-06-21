%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name blaze-builder
%define f_pkg_name blaze-builder
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.4.1.0
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://github.com/lpsmith/blaze-builder
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Efficient buffered output.

BuildPreReq: haskell(abi) = %ghc_version


%description
This library provides an implementation of the older blaze-builder
interface in terms of the new builder that shipped with bytestring-0.10.4.0

This implementation is mostly intended as a bridge to the new builder, so
that code that uses the old interface can interoperate with code that uses
the new implementation. Note that no attempt has been made to preserve the
old internal modules, so code that has these dependencies cannot use this
interface.

New code should, for the most part, use the new interface. However, this
module does implement a chunked HTTP encoding, which is not otherwise
implemented (yet?) with the new builder.

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
* Sun Jun 21 2020 Denis Smirnov <mithraen@altlinux.ru> 0.4.1.0-alt1
- Spec created by cabal2rpm 0.20_10
