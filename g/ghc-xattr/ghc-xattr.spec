%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name xattr
%define f_pkg_name xattr
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.5.2
Release: alt5.1.1
License: BSD3
Packager: Alex V. Myltsev <avm@altlinux.ru>
Group: Development/Haskell
URL: ???
Source: %name-%version.tar
Summary: Haskell bindings to libattr
BuildRequires: ghc
BuildRequires: libattr-devel
BuildRequires(pre): rpm-build-haskell


%description
Relatively low-level interface to work with extended attributes on Unix
systems. This is a fairly straightforward port of the API exposed by SGI's
libattr. Build-Type: Configure

%prep
%setup

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

cd %buildroot%_datadir/doc/%hsc_namever-%f_pkg_name-%version
rm -rf doc LICENSE examples

%files -f %name-files.nonprof
%hs_pkgconfdir/%f_pkg_name-%version.conf
%doc dist/doc/html
#%%doc LICENSE examples

%changelog
* Sat Aug 13 2011 Denis Smirnov <mithraen@altlinux.ru> 0.5.2-alt5.1.1
- rebuild with shared objects support

* Tue Dec 07 2010 Denis Smirnov <mithraen@altlinux.ru> 0.5.2-alt5.1
- rebuild with ghc 7.0/var/lib/altlinux/sisyphus/files/SRPMS/ghc-ansi-terminal-0.5.3-alt1.src.rpm

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.5.2-alt5
- auto rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.5.2-alt4
- auto rebuild

* Fri Sep 10 2010 Denis Smirnov <mithraen@altlinux.ru> 0.5.2-alt1
- Spec created by cabal2rpm 0.20_08
