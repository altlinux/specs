%define _unpackaged_files_terminate_build 1

Name: rtk
Version: 0.42.1
Release: alt1

Summary: CLI proxy that reduces LLM token consumption on common dev commands
License: Apache-2.0
Group: Development/Tools
Url: https://www.rtk-ai.app
Vcs: https://github.com/rtk-ai/rtk

Source0: %name-%version.tar
Source1: vendor.tar
Source2: config.toml
BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: rust

%description
High-performance CLI proxy that reduces LLM token consumption.
rtk filters and compresses command outputs before they reach your LLM context.

%prep
%setup -a 1
install -Dm 644 %SOURCE2 .cargo/config.toml

%build
%rust_build

%install
%rust_install

%files
%doc README.md
%_bindir/%name

%changelog
* Fri Jun 05 2026 Vladislav Glinkin <smasher@altlinux.org> 0.42.1-alt1
- New version

* Tue Mar 31 2026 Vladislav Glinkin <smasher@altlinux.org> 0.34.2-alt1
- New version

* Thu Mar 26 2026 Vladislav Glinkin <smasher@altlinux.org> 0.33.1-alt1
- Initial build for ALT

