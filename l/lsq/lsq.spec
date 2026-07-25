%global _unpackaged_files_terminate_build 1
%def_with check

Name: lsq
Version: 0.1.0
Release: alt1
Summary: Command-line client for LocalSend
License: Apache-2.0
Group: Networking/File transfer
URL: https://github.com/AlexDevFlow/lsq
VCS: https://github.com/AlexDevFlow/lsq

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
A command-line client for LocalSend. Send and receive files between
devices on the same network from a terminal. It speaks to the normal
LocalSend apps, so you can push a file from your phone to a headless
server, or the other way around.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/%name

%changelog
* Sat Jul 25 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.1.0-alt1
- Initial build for ALT.
