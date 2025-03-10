%define _unpackaged_files_terminate_build 1

Name: grip-grab
Version: 0.6.7
Release: alt1
Url: https://github.com/alexpasmantier/grip-grab
Vcs: https://github.com/alexpasmantier/grip-grab.git
Summary: A fast lightweight ripgrep alternative
License: Apache-2.0
Group: File tools
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: /proc
BuildRequires: rust-cargo

%description
A fast, more lightweight ripgrep alternative for daily use cases.

%prep
%setup
%patch0 -p1 

%build
cargo build --offline --release

%install
install -Dp target/release/gg -t %buildroot%_bindir

%files
%_bindir/gg

%changelog
* Fri Feb 28 2025 Artyom Sinyugin <writers@altlinux.org> 0.6.7-alt1
- Initial build.
