%global _unpackaged_files_terminate_build 1
%global import_path github.com/gopasspw/gopass

%define git_commit_short 56e4bad6

%def_with check

Name: gopass
Version: 1.15.17
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

BuildRequires: rpm-build-golang golang >= 1.24.1

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
# don't strip debuginfo
sed -i 's/-s -w//' Makefile
# used by Makefile to set main.commit variable
echo %git_commit_short > COMMIT

%build
%make_build all

%install
%make DESTDIR=%buildroot PREFIX=%prefix install

%check
git config --global user.name "nobody"
git config --global user.email "foo.bar@example.org"
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
* Thu Sep 18 2025 Alexander Stepchenko <geochip@altlinux.org> 1.15.17-alt1
- 1.15.15 -> 1.15.17

* Wed Apr 09 2025 Alexander Stepchenko <geochip@altlinux.org> 1.15.15-alt1
- 1.15.14 -> 1.15.15

* Tue Aug 06 2024 Alexander Stepchenko <geochip@altlinux.org> 1.15.14-alt1
- 1.15.13 -> 1.15.14

* Wed May 29 2024 Alexander Stepchenko <geochip@altlinux.org> 1.15.13-alt1
- 1.15.11 -> 1.15.13

* Mon Dec 04 2023 Alexander Stepchenko <geochip@altlinux.org> 1.15.11-alt1
- 1.15.8 -> 1.15.11

* Wed Oct 04 2023 Alexander Stepchenko <geochip@altlinux.org> 1.15.8-alt1
- 1.15.5 -> 1.15.8
- Drop ownership of system-wide autocompletion directories.

* Thu Apr 27 2023 Alexander Stepchenko <geochip@altlinux.org> 1.15.5-alt1
- Initial build for ALT
