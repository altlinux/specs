%define _unpackaged_files_terminate_build 1

Name: bugstalker
Version: 0.4.5
Release: alt1
Url: https://godzie44.github.io/BugStalker/
Vcs: https://github.com/godzie44/BugStalker.git
Summary: Modern debugger for Linux x86-64. Written in Rust for Rust programs
License: MIT
Group: Development/Debuggers
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

ExclusiveArch: x86_64

BuildRequires(pre): rpm-build-rust
BuildRequires: libunwind-devel

%description
%summary.

%prep
%setup
%rust_prep
%patch -P 0 -p1

%build
export RUSTFLAGS="-Copt-level=3"
%rust_build

%install
%rust_install -- bs

%check
export RUSTFLAGS="-Copt-level=3"
%rust_test --lib

%files
%doc LICENSE README.md CHANGELOG.md doc
%_bindir/bs

%changelog
* Tue May 12 2026 Artyom Sinyugin <writers@altlinux.org> 0.4.5-alt1
- New version 0.4.5.

* Fri Jan 23 2026 Artyom Sinyugin <writers@altlinux.org> 0.4.1-alt1
- New version 0.4.1.

* Tue Sep 03 2025 Artyom Sinyugin <writers@altlinux.org> 0.3.3-alt1
- Initial build.
