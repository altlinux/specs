%define _unpackage_files_terminate_build 1

Name: diskonaut
Version: 0.11.0
Release: alt1

Summary: Terminal disk space navigator
License: MIT
Group: Terminals
URL: https://github.com/imsnif/diskonaut

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
%summary.

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
* Fri Sep 12 2025 Vladislav Eliseev <general@altlinux.org> 0.11.0-alt1
- Initial build for Sisyphus. 

