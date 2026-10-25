%global _unpackaged_files_terminate_build 1

Name: sgrep
Version: 0.3.0
Release: alt1
Summary: Search code and text with ripgrep and local static embeddings
License: MIT
Group: Development/Tools
URL: https://github.com/context-dot-dev/sgrep
VCS: https://github.com/context-dot-dev/sgrep

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

Requires: ripgrep

%description
sgrep finds files that match your query, then ranks relevant passages by
meaning using local static embeddings. It runs on your machine and reads
fresh source on every search, so there is no index to build or keep in
sync. The executable needs ripgrep on your PATH.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install

%files
%_bindir/%name

%changelog
* Sun Oct 25 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.3.0-alt1
- Initial build for ALT.
