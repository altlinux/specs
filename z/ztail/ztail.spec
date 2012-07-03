%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name ztail
%define f_pkg_name ztail
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: ztail
Version: 1.0.1
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: ???
Source: %name-%version.tar
Summary: Multi-file, colored, filtered log tailer.

Patch: %name-%version-%release.patch

# Automatically added by buildreq on Fri Mar 23 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-common ghc7.4.1-mtl ghc7.4.1-regex-base ghc7.4.1-regex-posix ghc7.4.1-transformers libgmp-devel pkg-config python-base
BuildRequires: ghc7.4.1-alex ghc7.4.1-c2hs ghc7.4.1-cpphs ghc7.4.1-happy ghc7.4.1-hinotify ghc7.4.1-regex-compat

%description
An even more improved version of xtail/tail -f, including inotify support,
full regex-based filtering, substitution, and colorization.

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
runghc Setup copy --destdir=%buildroot

%files
%_bindir/ztail

%changelog
* Fri Mar 23 2012 Denis Smirnov <mithraen@altlinux.ru> 1.0.1-alt2
- fix build with new ghc + hinotify

* Tue Mar 08 2011 Denis Smirnov <mithraen@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt3
- rebuild

* Tue Oct 19 2010 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt2
- rebuild

* Fri Sep 10 2010 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt1
- Spec created by cabal2rpm 0.20_08
