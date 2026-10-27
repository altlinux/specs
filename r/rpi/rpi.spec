%global _unpackaged_files_terminate_build 1
%def_with check

Name: rpi
Version: 0.11.0
Release: alt1
Summary: Coding-agent runtime and terminal CLI inspired by Pi
License: MIT
Group: Development/Tools
URL: https://rpi.laofu.online
VCS: https://github.com/bigfish1913/pi-rust

Source: %name-%version.tar
Source1: vendor.tar
Patch: alt-disable-self-update.patch

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
Rust-native, library-first coding-agent runtime and terminal CLI
inspired by Pi, with composable LLM providers, tools, sessions,
and plugin ABI.
Ready-to-install extensions live in the online catalog
https://rpi.bigfisharc.cn/packages.html.

%prep
%setup -a1
%patch -p1
%rust_prep

%build
%rust_build -p rpi-cli

%install
%rust_install rpi

%check
%rust_test -p rpi-cli -- --test-threads=1

%files
%_bindir/rpi

%changelog
* Tue Oct 27 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.11.0-alt1
- Initial build for ALT.
