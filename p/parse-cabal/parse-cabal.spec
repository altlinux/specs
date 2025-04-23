Name: parse-cabal

Version: 1.0.0
Release: alt1
License: BSD-3-Clause

Group: Development/Haskell
Url: https://hackage.haskell.org/package/parse-cabal

Source: %name-%version.tar
Source1: local-repo.tar

Summary: A simple utility for retrieving information from a .cabal file

BuildRequires(Pre): ghc-devel
BuildRequires(Pre): rpm-build-haskell-vendored

%description
The parse-cabal utility is a tool designed to retrieve
information from .cabal files.

It is primarily intended for use in shell scripts.

The available output formats are plain text, TOML, and JSON.

%prep
%setup
%setup -a 1

%build
%cabal_vendor_build

%install
%cabal_vendor_install

mkdir -p %buildroot%_datadir/zsh/site-functions
mkdir -p %buildroot%_datadir/bash-completion/completions
mkdir -p %buildroot%_datadir/fish/vendor_completions.d

%buildroot%_bindir/parse-cabal --zsh-completion-script '%_bindir/%name' > \
                                %buildroot%_datadir/zsh/site-functions/_%name

%buildroot%_bindir/parse-cabal --bash-completion-script '%_bindir/%name' > \
                                %buildroot%_datadir/bash-completion/completions/%name

%buildroot%_bindir/parse-cabal --fish-completion-script '%_bindir/%name' > \
                                %buildroot%_datadir/fish/vendor_completions.d/%name.fish


%files
%doc LICENSE
%_bindir/%name
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Tue Apr 22 2025 Leonid Znamenok <respublica@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

