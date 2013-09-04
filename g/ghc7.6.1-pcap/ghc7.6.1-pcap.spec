%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name pcap
%define f_pkg_name pcap
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.4.5.2
Release: alt1
License: BSD3
Packager: Igor Zubkov <icesik@altlinux.org>
Group: Development/Haskell
Url: https://github.com/bos/pcap
Source0: pcap-%version.tar.gz
Summary: A system-independent interface for user-level packet capture

# Automatically added by buildreq on Wed Sep 04 2013 (-bi)
# optimized out: elfutils ghc7.6.1 ghc7.6.1-common ghc7.6.1-mtl ghc7.6.1-parsec ghc7.6.1-text ghc7.6.1-transformers libffi-devel libgmp-devel pkg-config python-base rpm-build-haskell
#WTF?? python-module-distribute python-module-zope
BuildRequires: ghc7.6.1-network libpcap-devel

%description
A system-independent interface for user-level packet capture

%prep
%setup -q -n pcap-%version

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all
#doc README.markdown LICENSE

%changelog
* Wed Sep 04 2013 Igor Zubkov <icesik@altlinux.org> 0.4.5.2-alt1
- Spec created by cabal2rpm 0.20_08
