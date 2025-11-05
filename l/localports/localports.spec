%define _unpackage_files_terminate_build 1

Name: localports
Version: 0.1.0
Release: alt1

Summary: List network ports with their associated binaries
License: MIT
Group: Networking/Other
URL: https://github.com/diegoholiveira/localports

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
Requires: lsof

%description
A simple command-line tool to list network ports and their associated
binaries. Perfect for developers who need to quickly identify what's
using a specific port.

%prep
%setup -a 1
%rust_prep

%build 
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/%name
%doc LICENSE

%changelog
* Mon Sep 15 2025 Vladislav Eliseev <general@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus.
