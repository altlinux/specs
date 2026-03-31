Name: shellcheck

Version: 0.11.0
Release: alt1.1
License: GPL-3.0-or-later
Url: https://github.com/koalaman/shellcheck
Group: Development/Tools

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): ghc-devel
BuildRequires(pre): rpm-build-haskell-vendored

BuildRequires: pandoc

Summary: Shell script analysis tool

%description
The goals of ShellCheck are:
* To point out and clarify typical beginner's syntax issues, that causes
a shell to give cryptic error messages;
* To point out and clarify typical intermediate level semantic problems,
that causes a shell to behave strangely and counter-intuitively;
* To point out subtle caveats, corner cases and pitfalls, that may cause
an advanced user's otherwise working script to fail under future
circumstances.

%prep
%setup -a 1

%build
%cabal_vendor_build exe:shellcheck

pandoc -s -f markdown-smart -t man shellcheck.1.md -o shellcheck.1

%install
%cabal_vendor_install exe:shellcheck

mkdir -p %buildroot%_man1dir
cp shellcheck.1 %buildroot%_man1dir

%check
%cabal_vendor_test

%files
%_bindir/shellcheck
%_man1dir/shellcheck.1*

%changelog
* Tue Mar 31 2026 Leonid Znamenok <respublica@altlinux.org> 0.11.0-alt1.1
- Fixed FTBFS with ghc-1:9.6.7-alt2.

* Mon Aug 04 2025 Leonid Znamenok <respublica@altlinux.org> 0.11.0-alt1
- Updated to 0.11.0.

* Mon May 05 2025 Leonid Znamenok <respublica@altlinux.org> 0.10.0-alt2
- Rebuilt with rpm-build-haskell-vendored.

* Wed Jul 03 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.10.0-alt1
- Updated to 0.10.0.

* Thu Apr 13 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.0-alt1
- Updated to 0.9.0.

* Thu Jan 20 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.0-alt1
- Updated to 0.8.0.

* Mon Oct 18 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.2-alt1
- Updated to 0.7.2.

* Sat Mar 27 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.1-alt1
- Updated to 0.7.1.

* Fri Aug 23 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.0-alt1
- Updated to 0.7.0.

* Thu May 25 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.6-alt1
- Updated to 0.4.6.

* Tue Nov 22 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.5-alt1
- Initial build.
