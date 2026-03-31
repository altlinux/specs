%define pkg_name happy
%define pkgid %pkg_name-%version

Name: happy
Version: 2.1.5
Release: alt1.1
License: BSD-2-Clause

Group: Development/Haskell
Url: http://hackage.haskell.org/package/happy

Source: %name-%version.tar
Source1: vendor.tar

Summary: Happy is a parser generator for Haskell

BuildRequires(pre): ghc-devel
BuildRequires(pre): rpm-build-haskell-vendored

%description
Happy is a parser generator for Haskell. Given a grammar specification in
BNF, Happy generates Haskell code to parse the grammar. Happy works in a
similar way to the @yacc@ tool for C.

%prep
%setup -a 1

%build
%cabal_vendor_build

%install
%cabal_vendor_install
%ghc_gen_filelist %pkg_name %version

%files -f %pkgid-files.all
%_bindir/happy

%changelog
* Tue Mar 31 2026 Leonid Znamenok <respublica@altlinux.org> 2.1.5-alt1.1
- Fixed FTBFS with ghc-1:9.6.7-alt2.

* Mon Jun 09 2025 Leonid Znamenok <respublica@altlinux.org> 2.1.5-alt1
- 2.1.5

* Tue May 06 2025 Leonid Znamenok <respublica@altlinux.org> 1.20.1.1-alt2
- Packaged man

* Tue Feb 25 2025 Leonid Znamenok <respublica@altlinux.org> 1.20.1.1-alt1
- Initial build for Sisyphus

