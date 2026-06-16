%define _unpackaged_files_terminate_build 1

Name: bfs
Version: 4.1.3
Release: alt1

Summary: A breadth-first version of the UNIX find command
License: 0BSD
Group: File tools
Url: https://github.com/tavianator/bfs

Source: %name-%version.tar

BuildRequires: pkgconfig(libacl)
BuildRequires: pkgconfig(libcap)
BuildRequires: pkgconfig(libselinux)
BuildRequires: pkgconfig(liburing)
BuildRequires: pkgconfig(oniguruma)

%description
bfs is a variant of the UNIX `find` command that operates breadth-first
rather than depth-first.

It tries to be easier to use than `find`, while remaining compatible
with find(1). For example, bfs is less picky about where you put its
arguments. bfs also adds some extra options that make some common tasks
easier.

When bfs detects that its output is a terminal, it automatically colors
its output with the same colors ls uses.

%prep
%setup

%build
./configure \
  --enable-release \
  V=1
%make_build

%install
%makeinstall_std

%files
%doc LICENSE README.md docs/{CHANGELOG,CONTRIBUTING,RELATED,SECURITY,USAGE}.md
%_bindir/%name
%_man1dir/%{name}.1*
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%{name}.fish
%_datadir/zsh/site-functions/_%{name}

%changelog
* Tue Jun 16 2026 Nikolay Strelkov <snk@altlinux.org> 4.1.3-alt1
- New version 4.1.3.

* Thu May 07 2026 Nikolay Strelkov <snk@altlinux.org> 4.1.2-alt1
- New version 4.1.2.

* Fri May 01 2026 Nikolay Strelkov <snk@altlinux.org> 4.1.1-alt1
- New version 4.1.1.

* Mon Aug 18 2025 Nikolay Strelkov <snk@altlinux.org> 4.1-alt1
- New version 4.1.

* Sat Jun 21 2025 Nikolay Strelkov <snk@altlinux.org> 4.0.8-alt1
- New version 4.0.8.

* Fri Jun 20 2025 Nikolay Strelkov <snk@altlinux.org> 4.0.7-alt1
- Initial build for Sisyphus
