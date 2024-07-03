# shellcheck requires newer modules then we have in Sisyphus
# So... We build static shellcheck with bundled new modules.
%def_disable getsource

Name: shellcheck
Version: 0.10.0
Release: alt1
License: GPL-3.0-or-later
Url: https://github.com/koalaman/shellcheck
Group: Development/Tools

BuildRequires: /proc ghc8.6.4 ghc8.6.4-cabal-install pandoc

%if_disabled getsource
Source: %name-%version.tar
%endif

Source1: shellcheck.1.md

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
%if_enabled getsource
%setup -c -T
%else
%setup
%endif

%build
%if_enabled getsource
rm -rf $HOME/.cabal
mkdir shellcheck-%version
ln -s -r -f shellcheck-%version $HOME/.cabal
cabal new-update
cabal fetch ShellCheck-%version
echo '' | cabal new-repl -w ghc-8.6.4 --build-dep fail
tar -cf shellcheck-%version.tar shellcheck-%version
exit 1
%else
rm -rf $HOME/.cabal
ln -s -r -f . $HOME/.cabal
cabal new-install %_smp_mflags ShellCheck-%version
%endif

pandoc -s -f markdown-smart -t man %SOURCE1 -o shellcheck.1

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_man1dir
cp bin/shellcheck %buildroot%_bindir
cp shellcheck.1 %buildroot%_man1dir

%files
%_bindir/shellcheck
%_man1dir/shellcheck.1*

%changelog
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
