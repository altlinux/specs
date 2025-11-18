%define _unpackaged_files_terminate_build 1

%def_with check

Name: ripgrep-all
Version: 0.10.10
Release: alt1
Summary: Extended ripgrep with support for archives and more

License: AGPL-3.0
Group: File tools
Url: https://github.com/phiresky/ripgrep-all
Vcs: https://github.com/phiresky/ripgrep-all.git
Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust

%if_with check
BuildRequires: pandoc
BuildRequires: poppler
%endif

Requires: fzf
Requires: pandoc
Requires: ffprobe
Requires: ripgrep
Requires: poppler

%description
Ripgrep-all (rga) is an enhanced version of ripgrep, a fast
line-oriented search tool. It extends ripgrep's capabilities
to search within archives, PDFs, SQLite databases, and other
file types, making it a versatile tool for advanced searches.

%prep
%setup -a 1
%rust_prep

%build
%rust_build

%install
%rust_install rga rga-preproc rga-fzf rga-fzf-open

%check
%rust_test

%files
%doc README.md CHANGELOG.md
%_bindir/rga
%_bindir/rga-preproc
%_bindir/rga-fzf
%_bindir/rga-fzf-open

%changelog
* Tue Nov 11 2025 Aleksandr A. Voyt <sobue@altlinux.org> 0.10.10-alt1
- 0.10.9 -> 0.10.10

* Mon May 26 2025 Aleksandr A. Voyt <sobue@altlinux.org> 0.10.9-alt1
- Initial build.
