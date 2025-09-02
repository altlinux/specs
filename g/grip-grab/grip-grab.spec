%define _unpackaged_files_terminate_build 1

Name: grip-grab
Version: 0.6.7
Release: alt2
Url: https://github.com/alexpasmantier/grip-grab
Vcs: https://github.com/alexpasmantier/grip-grab.git
Summary: A fast lightweight ripgrep alternative
License: Apache-2.0
Group: File tools
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-rust

%description
A fast, more lightweight ripgrep alternative for daily use cases.

%prep
%setup
%rust_prep
%patch0 -p1

%build
export RUSTFLAGS="-Copt-level=3"
%rust_build

%install
%rust_install -- gg

%files
%_bindir/gg

%changelog
* Thu Aug 28 2025 Artyom Sinyugin <writers@altlinux.org> 0.6.7-alt2
- Optimized build.

* Fri Feb 28 2025 Artyom Sinyugin <writers@altlinux.org> 0.6.7-alt1
- Initial build.
