%global _unpackaged_files_terminate_build 1
%global import_path github.com/gopasspw/gopass

%def_with check

Name: gopass
Version: 1.15.13
Release: alt1

Summary: The slightly more awesome standard unix password manager for teams
License: MIT
Group: Text tools
Url: https://www.gopass.pw
Vcs: https://github.com/gopasspw/gopass

Source: %name-%version.tar
Source1: vendor.tar

# Fixes a unit test for the vendored build
Patch0: gopass-1.15.5-alt-fix-tests-for-vendored-build.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%if_with check
BuildRequires: git gnupg gnupg2
%endif

%description
Manage your credentials with ease. In a globally distributed team, on multiple
devices or fully offline on an air gapped machine.

Works everywhere - The same user experience on Linux, MacOS, *BSD or Windows.
Built for teams - Built from our experience working in distributed
development teams.
Full autonomy - No network connectivity required, unless you want it.

%prep
%setup -a 1
%patch0 -p0
# -buildmode=pie requires external (cgo) linking
sed -i 's/CGO_ENABLED=0/CGO_ENABLED=1/' Makefile

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
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Wed May 29 2024 Alexander Stepchenko <geochip@altlinux.org> 1.15.13-alt1
- 1.15.11 -> 1.15.13

* Mon Dec 04 2023 Alexander Stepchenko <geochip@altlinux.org> 1.15.11-alt1
- 1.15.8 -> 1.15.11

* Wed Oct 04 2023 Alexander Stepchenko <geochip@altlinux.org> 1.15.8-alt1
- 1.15.5 -> 1.15.8
- Drop ownership of system-wide autocompletion directories.

* Thu Apr 27 2023 Alexander Stepchenko <geochip@altlinux.org> 1.15.5-alt1
- Initial build for ALT
