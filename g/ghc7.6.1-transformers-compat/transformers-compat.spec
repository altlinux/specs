%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name transformers-compat
%define f_pkg_name transformers-compat
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.5.0.3
Release: alt1

Summary: A small compatibility shim for the transformers library

License: BSD3
Group: Development/Haskell
Url: https://hackage.haskell.org/package/transformers-compat

Packager: Grigory Ustinov <grenka@altlinux.org>
Source: %name-%version.tar
ExclusiveArch: %ix86 x86_64

BuildRequires: ghc7.6.1-generic-deriving
BuildRequires: ghc7.6.1-mtl ghc7.6.1-transformers

%description
This package includes backported versions of types that were added to
transformers in transformers 0.3, 0.4, and 0.5 for users who need strict
transformers 0.2 or 0.3 compatibility to run on old versions of the
platform, but also need those types.

Those users should be able to just depend on @transformers >= 0.2@ and
@transformers-compat >= 0.3@.

Note: missing methods are not supplied, but this at least permits the types
to be used.

%prep
%setup

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Wed Oct 31 2018 Grigory Ustinov <grenka@altlinux.org> 0.5.0.3-alt1
- Initial build for Sisyphus.
