Name: cabal-install

Version: 3.14.2.0
Release: alt2
License: BSD-3-Clause

Group: Development/Haskell
Url: https://hackage.haskell.org/package/cabal-install
VCS: https://github.com/haskell/cabal

Source: %name-%version.tar

# ghc_version arrives from ghc-devel package
Source1: bootstrap-sources-%ghc_version.tar.gz

Patch0: cabal_install-alt-multithread_build.patch

Summary: The command-line interface for Cabal and Hackage

BuildRequires(Pre): rpm-build-haskell
BuildRequires(Pre): ghc-devel

BuildRequires: python3

# 'zlib' haskell package dependancy
BuildRequires: zlib-devel

%description
The 'cabal' command-line program simplifies the process
of managing Haskell software by automating the fetching,
configuration, compilation and installation of Haskell
libraries and programs.

%prep
%setup

%patch0 -p1

%build
python3 ./bootstrap/bootstrap.py --bootstrap-sources %SOURCE1 %ghc_smp_mflags

%install
install -pm 755 -D -t %buildroot/%_bindir ./_build/bin/cabal
install -pm 644 -D -t %buildroot/%_datadir/bash-completion/completions \
                      ./cabal-install/bash-completion/cabal

%files
%doc LICENSE AUTHORS
%_bindir/cabal
%_datadir/bash-completion/completions/cabal

%changelog
* Wed Apr 23 2025 Leonid Znamenok <respublica@altlinux.org> 3.14.2.0-alt2
- Rebuild with -no-fdlocking flag for lukko
  + See: (https://github.com/haskellari/lukko/issues/15)

* Tue Apr 15 2025 Leonid Znamenok <respublica@altlinux.org> 3.14.2.0-alt1
- Initial build for Sisyphus
