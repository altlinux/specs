%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name blaze-builder
%define f_pkg_name blaze-builder
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.3.1.0
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://github.com/meiersi/blaze-builder
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Efficient buffered output.



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1 ghc7.6.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-hscolour ghc7.6.1-text

%description
This library provides an abstraction of buffered output of byte streams and
several convenience functions to exploit it. For example, it allows to
efficiently serialize Haskell values to lazy bytestrings with a large
average chunk size. The large average chunk size allows to make good use of
cache prefetching in later processing steps (e.g. compression) and reduces
the sytem call overhead when writing the resulting lazy bytestring to a
file or sending it over the network.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.3.1.0-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.3.1.0-alt1
- Spec created by cabal2rpm 0.20_08
