%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name darcs
%define f_pkg_name darcs
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 2.8.4
Release: alt1
License: GPL
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://darcs.net/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: a distributed, interactive, smart revision control system



# Automatically added by buildreq on Sat Feb 16 2013
# optimized out: ghc7.6.1 ghc7.6.1-common ghc7.6.1-dataenc ghc7.6.1-extensible-exceptions ghc7.6.1-mmap ghc7.6.1-mtl ghc7.6.1-network ghc7.6.1-parsec ghc7.6.1-primitive ghc7.6.1-regex-base ghc7.6.1-regex-posix ghc7.6.1-terminfo ghc7.6.1-text ghc7.6.1-transformers ghc7.6.1-zlib libgmp-devel libtinfo-devel pkg-config
BuildRequires: ghc7.6.1-alex ghc7.6.1-c2hs ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-happy ghc7.6.1-hashed-storage ghc7.6.1-haskeline ghc7.6.1-hscolour ghc7.6.1-html ghc7.6.1-http ghc7.6.1-random ghc7.6.1-regex-compat ghc7.6.1-tar ghc7.6.1-utf8-string ghc7.6.1-vector libcurl-devel libncurses-devel zlib-devel

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
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Sat Feb 16 2013 Denis Smirnov <mithraen@altlinux.ru> 2.8.4-alt1
- Spec created by cabal2rpm 0.20_08
