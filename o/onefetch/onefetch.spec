%define _unpackaged_files_terminate_build 1

Name: onefetch
Version: 2.22.0
Release: alt1

Summary: Command-line Git information tool
License: MIT
Group: Monitoring
Url: https://onefetch.dev
Vcs: https://github.com/o2sh/onefetch

Source0: %name-%version.tar
Source1: vendor.tar
Source2: config.toml
BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: rust
BuildRequires: /proc
# error: failed to run custom build command for `libz-ng-sys v1.1.9` (cmake required)
BuildRequires: cmake

%description
Onefetch is a command-line Git information tool written in Rust that displays
project information and code statistics for a local Git repository directly
to your terminal. The tool is completely offline - no network access is required.

%prep
%setup -a 1
install -Dm 644 %SOURCE2 .cargo/config.toml

%build
%rust_build

%install
%rust_install
install -Dm 644  docs/onefetch.1 %buildroot%_man1dir/onefetch.1

%files
%_bindir/%name
%doc README.md docs/README.ru.md LICENSE.md
%_man1dir/*

%changelog
* Wed Sep 25 2024 Vladislav Glinkin <smasher@altlinux.org> 2.22.0-alt1
- Update to 2.22.0

* Sat Jul 06 2024 Vladislav Glinkin <smasher@altlinux.org> 2.21.0-alt1
- Update to 2.21.0

* Wed Mar 27 2024 Vladislav Glinkin <smasher@altlinux.org> 2.20.0-alt1
- Update to 2.20.0

* Tue Oct 10 2023 Vladislav Glinkin <smasher@altlinux.org> 2.18.1-alt1
- Initial build for ALT

