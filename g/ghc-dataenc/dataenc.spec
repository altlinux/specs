%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name dataenc
%define f_pkg_name dataenc
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.13.0.5
Release: alt2.1
License: BSD
Group: Development/Haskell
URL: http://hackage.haskell.org/cgi-bin/hackage-scripts/package/%h_pkg_name
Source: %f_pkg_name-%version.tar
Summary: Data encoding library
# Automatically added by buildreq on Tue Apr 14 2009
BuildRequires: ghc-binary ghc(mtl) ghc-network ghc-regex-compat ghc-stm ghc(time) ghc-utf8-string

BuildRequires: ghc haddock %hs_package_dependencies
BuildRequires(pre): rpm-build-haskell


%description
Data encoding library currently providing Uuencode, Base64,
Base64Url, Base32, Base32Hex, Base16, Base85, and yEncoding.

%prep
%setup -n %h_pkg_name-%version


%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

cd %buildroot%_datadir/doc/%hsc_namever-%f_pkg_name-%version
rm -rf doc LICENSE

%files -f %name-files.nonprof
%hs_pkgconfdir/%f_pkg_name-%version.conf
%doc dist/doc/html
%doc LICENSE

%changelog
* Sat Aug 13 2011 Denis Smirnov <mithraen@altlinux.ru> 0.13.0.5-alt2.1
- rebuild with shared objects support

* Wed Mar 09 2011 Denis Smirnov <mithraen@altlinux.ru> 0.13.0.5-alt2
- rebuild

* Thu Mar 03 2011 Denis Smirnov <mithraen@altlinux.ru> 0.13.0.5-alt1
- 0.13.0.5

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.12-alt6
- auto rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.12-alt5
- auto rebuild

* Thu Sep 09 2010 Denis Smirnov <mithraen@altlinux.ru> 0.12-alt2
- ghc 6.12.3

* Thu Sep 09 2010 Denis Smirnov <mithraen@altlinux.ru> 0.12-alt1.1.1
- rebuild with new haskell

* Wed Mar 17 2010 Denis Smirnov <mithraen@altlinux.ru> 0.12-alt1.1
- rebuild with new haskell

* Tue Apr 14 2009 Anton Farygin <rider@altlinux.ru> 0.12-alt1
- first buiild for Sisyphus
