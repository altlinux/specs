%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name darcs
%define f_pkg_name darcs
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: darcs
Version: 2.5.2
Release: alt1
License: GPL
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>
Group: Development/Haskell
URL: http://darcs.net/
Source: %name-%version.tar
Summary: A distributed, interactive, smart revision control system
BuildRequires: ghc ghc-hscolour ghc-zlib ghc-text ghc-regex-compat ghc-parsec ghc-mtl ghc-html ghc-haskeline ghc-tar ghc-hashed-storage libcurl-devel
BuildRequires(pre): rpm-build-haskell

%description
Darcs is a free, open source revision control system. It is:

* Distributed: Every user has access to the full command set, removing
boundaries between server and client or committer and non-committers.

* Interactive: Darcs is easy to learn and efficient to use because it asks
you questions in response to simple commands, giving you choices in your
work flow. You can choose to record one change in a file, while ignoring
another. As you update from upstream, you can review each patch name, even
the full "diff" for interesting patches.

* Smart: Originally developed by physicist David Roundy, darcs is based on
a unique algebra of patches.

This smartness lets you respond to changing demands in ways that would
otherwise not be possible. Learn more about spontaneous branches with
darcs.

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
%_bindir/darcs
%_man1dir/darcs.*
%hs_pkgconfdir/%f_pkg_name-%version.conf
%doc dist/doc/html
#%%doc LICENSE examples

%changelog
* Wed Nov 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.2-alt1
- Spec created by cabal2rpm 0.20_08
