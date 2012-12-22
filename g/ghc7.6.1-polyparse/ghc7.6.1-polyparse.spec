%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name polyparse
%define f_pkg_name polyparse
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.8
Release: alt1
License: LGPL
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://code.haskell.org/~malcolm/polyparse/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A variety of alternative parser combinator libraries.



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.6.1 ghc7.6.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-alex ghc7.6.1-c2hs ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-happy ghc7.6.1-hscolour ghc7.6.1-text

%description
A variety of alternative parser combinator libraries, including the
original HuttonMeijer set. The Poly sets have features like good error
reporting, arbitrary token type, running state, lazy parsing, and so on.
Finally, Text.Parse is a proposed replacement for the standard Read class,
for better deserialisation of Haskell values from Strings.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 1.8-alt1
- Spec created by cabal2rpm 0.20_08
