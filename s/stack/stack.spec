Name: stack

Version: 3.5.1
Release: alt1.1
License: BSD-3-Clause
Url: https://github.com/commercialhaskell/stack
Group: Development/Haskell

Source: %name-%version.tar
Source1: vendor.tar

Patch1: vendored_basement-github-fix_i586.patch
Patch2: vendored_cborg-github-fix_i586.patch
Patch3: vendored_memory-github-fix_i586.patch

BuildRequires(pre): ghc-devel
BuildRequires(pre): rpm-build-haskell-vendored

# for autocompletion
BuildRequires: /proc

BuildRequires: zlib-devel
BuildRequires: gcc-c++

# stack is searching certs in /etc/ssl
Requires: ca-trust-directory-hash

Summary: The Haskell Tool Stack

%description
Stack is a tool to build projects and manage their dependencies for the
programming language Haskell. It uses the Cabal library but with a curated
version of the Hackage software repository named Stackage.

Stack competes against Cabal's binary file cabal-install and has been created
as a result of the overall criticism about dependency problems. However, it
does not provide its own package format, but uses extant *.cabal files and
complements projects with an added stack.yaml file.

%prep
%setup -a 1

%ifarch i586
%patch1 -p1
%patch2 -p1
%patch3 -p1
%endif

%build
%cabal_vendor_build

%install
%cabal_vendor_install

mkdir -p %buildroot%_datadir/zsh/site-functions
mkdir -p %buildroot%_datadir/bash-completion/completions
mkdir -p %buildroot%_datadir/fish/vendor_completions.d

%buildroot%_bindir/%name --zsh-completion-script '%_bindir/%name' > \
                                %buildroot%_datadir/zsh/site-functions/_%name

%buildroot%_bindir/%name --bash-completion-script '%_bindir/%name' > \
                                %buildroot%_datadir/bash-completion/completions/%name

%buildroot%_bindir/%name --fish-completion-script '%_bindir/%name' > \
                                %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%files
%doc doc/*
%_bindir/%name
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Tue Mar 31 2026 Leonid Znamenok <respublica@altlinux.org> 3.5.1-alt1.1
- Fixed FTBFS with ghc-1:9.6.7-alt2.

* Tue May 06 2025 Leonid Znamenok <respublica@altlinux.org> 3.5.1-alt1
- Initial build for Sisyphus

