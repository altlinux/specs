Name: hadolint
Version: 2.12.0
Release: alt1

Summary: Dockerfile Linter JavaScript API
License: GPL-3.0-only
Group: Development/Tools
Url: http://hackage.haskell.org/package/hadolint
Vcs: https://github.com/hadolint/hadolint

Source0: %name-%version.tar
Source1: vendor.tar
Patch1: vendored_basement-github-fix_i586.patch
Patch2: vendored_memory-github-fix_i586.patch

BuildRequires: ghc-devel
BuildRequires: rpm-build-haskell-vendored

%description
A smarter Dockerfile linter that helps you build best practice Docker images.

%prep
%setup -a1
%patch1 -p1
%patch2 -p1

%build
%cabal_vendor_build -f -static

%install
%cabal_vendor_install -f -static

%files
%_bindir/hadolint

%changelog
* Fri Oct 30 2026 Anton Zhukharev <ancieg@altlinux.org> 2.12.0-alt1
- Packaged for ALT Sisyphus.
