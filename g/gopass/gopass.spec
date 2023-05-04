%define with_check

%global import_path github.com/gopasspw/gopass

Name:    gopass
Version: 1.15.5
Release: alt1

Summary: The slightly more awesome standard unix password manager for teams
License: MIT
Group:   Text tools
Url:     https://github.com/gopasspw/gopass

Source: %name-%version.tar

# Fixes a unit test for the vendored build
Patch0: gopass-1.15.5-alt-fix-tests-for-vendored-build.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

BuildRequires: git gnupg gnupg2

%description
Manage your credentials with ease. In a globally distributed team, on multiple
devices or fully offline on an air gapped machine.

Works everywhere - The same user experience on Linux, MacOS, *BSD or Windows.
Built for teams - Built from our experience working in distributed
development teams.
Full autonomy - No network connectivity required, unless you want it.

%prep
%setup
%patch0 -p0

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%make_build all

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

cd .build/src/%import_path
%make DESTDIR=%buildroot PREFIX=%prefix install

%check
git config --global user.name "nobody"
git config --global user.email "foo.bar@example.org"
cd .build/src/%import_path
%make DESTDIR=%buildroot PREFIX=%prefix test
%make DESTDIR=%buildroot PREFIX=%prefix test-integration

%files
%doc *.md
%_man1dir/*
%_bindir/%name
%dir %_datadir/bash-completion/
%dir %_datadir/bash-completion/completions/
%_datadir/bash-completion/completions/%name
%dir %_datadir/zsh/
%dir %_datadir/zsh/site-functions/
%_datadir/zsh/site-functions/_%name
%dir %_datadir/fish/
%dir %_datadir/fish/vendor_completions.d/
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Thu Apr 27 2023 Alexander Stepchenko <geochip@altlinux.org> 1.15.5-alt1
- Initial build for ALT
