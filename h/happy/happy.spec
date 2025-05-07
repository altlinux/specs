%define pkg_name happy
%define pkgid %pkg_name-%version

%def_with docs

Name: happy
Version: 1.20.1.1
Release: alt2
License: BSD-2-Clause

Group: Development/Haskell
Url: http://hackage.haskell.org/package/happy

Source: %name-%version.tar

Summary: Happy is a parser generator for Haskell

BuildRequires(Pre): ghc-devel
BuildRequires(Pre): rpm-build-haskell

%description
Happy is a parser generator for Haskell. Given a grammar specification in
BNF, Happy generates Haskell code to parse the grammar. Happy works in a
similar way to the @yacc@ tool for C.

%prep
%setup

%build
%ghc_bin_build

pushd doc > /dev/null
    autoconf
    ./configure
popd > /dev/null

%install
%ghc_bin_install
%ghc_gen_filelist %pkg_name %version

mkdir -p %buildroot%_man1dir
cp doc/happy.1 %buildroot%_man1dir

%files -f %pkgid-files.all
%_bindir/happy
%_man1dir/happy.1*

%changelog
* Tue May 06 2025 Leonid Znamenok <respublica@altlinux.org> 1.20.1.1-alt2
- Packaged man

* Tue Feb 25 2025 Leonid Znamenok <respublica@altlinux.org> 1.20.1.1-alt1
- Initial build for Sisyphus

