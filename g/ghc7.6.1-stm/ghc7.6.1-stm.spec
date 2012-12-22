%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name stm
%define f_pkg_name stm
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 2.4.2
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://hackage.haskell.org/package/stm
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Software Transactional Memory



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1 ghc7.6.1-doc

%description
A modular composable concurrency abstraction.

Changes in version 2.4.2

* Added "Control.Concurrent.STM.TSem" (transactional semaphore)

Changes in version 2.4.1

* Added Applicative/Alternative instances of STM for GHC <7.0

Changes in version 2.4

* Added "Control.Concurrent.STM.TQueue" (a faster @TChan@)

* Added "Control.Concurrent.STM.TBQueue" (a bounded channel based on
@TQueue@)

* @TChan@ has an @Eq@ instances

* Added @newBroadcastTChan@ and @newBroadcastTChanIO@

* Some performance improvements for @TChan@

* Added @cloneTChan@

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 2.4.2-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 2.4.2-alt1
- Spec created by cabal2rpm 0.20_08
