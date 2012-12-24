%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name libnotify
%define f_pkg_name libnotify
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.0.2.1
Release: alt1
License: MIT
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://hackage.haskell.org/package/libnotify
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Haskell binding for Libnotify



# Automatically added by buildreq on Mon Dec 24 2012 (-bb)
# optimized out: elfutils fontconfig fontconfig-devel ghc7.6.1 ghc7.6.1-cairo ghc7.6.1-common ghc7.6.1-glib ghc7.6.1-mtl ghc7.6.1-pango ghc7.6.1-transformers glib2-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgmp-devel libpango-devel pkg-config python-base rpm-build-haskell zlib-devel
BuildRequires: ghc7.6.1-alex ghc7.6.1-c2hs ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-gtk ghc7.6.1-happy ghc7.6.1-hscolour libgtk+2-devel libnotify-devel

%description
Usable binding to libnotify library.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.0.2.1-alt1
- Spec created by cabal2rpm 0.20_08
