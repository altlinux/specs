# shellcheck requires newer modules then we have in Sisyphus
# So... We build static shellcheck with bundled new modules.
%def_disable getsource

Name: shellcheck
Version: 0.7.1
Release: alt1
License: %gpl3only
Url: https://github.com/koalaman/shellcheck
Group: Development/Tools

BuildRequires(pre): rpm-build-licenses
BuildRequires: /proc ghc8.6.4 ghc8.6.4-cabal-install

%if_disabled getsource
Source: %name-%version.tar
%endif

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

%install
mkdir -p %buildroot%_bindir
cp bin/shellcheck %buildroot%_bindir

%files
%_bindir/shellcheck

%changelog
* Sat Mar 27 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.1-alt1
- Updated to 0.7.1.

* Fri Aug 23 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.0-alt1
- Updated to 0.7.0.

* Thu May 25 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.6-alt1
- Updated to 0.4.6.

* Tue Nov 22 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.5-alt1
- Initial build.
