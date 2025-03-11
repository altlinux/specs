%def_with docs

%define pkg_name alex
%define pkgid %pkg_name-%version

Name: alex
Version: 3.5.2.0
Release: alt1
License: BSD-3-Clause

Group: Development/Haskell
Url: http://hackage.haskell.org/package/alex

Source: %name-%version.tar

Summary: Alex is a tool for generating lexical analysers in Haskell

BuildRequires(Pre): ghc-devel
BuildRequires(Pre): rpm-build-haskell

%description
Alex is a tool for generating lexical analysers in Haskell. It takes a
description of tokens based on regular expressions and generates a Haskell
module containing code for scanning text efficiently. It is similar to the
tool lex or flex for C/C++.

%prep
%setup

%build
%ghc_bin_build

%install
%ghc_bin_install
%ghc_gen_filelist %pkg_name %version

%files -f %pkgid-files.all
%_bindir/alex

%changelog
* Fri Feb 21 2025 Leonid Znamenok <respublica@altlinux.org> 3.5.2.0-alt1
Initial build for Sisyphus

