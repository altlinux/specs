%define _unpackaged_files_terminate_build 1
%define bin_name kondo

Name: kondo
Version: 0.9
Release: alt1
Summary: Kondo cleans dependencies and build artifacts from various projects

License: MIT
Group: Development/Tools
Url: https://github.com/tbillington/kondo
Vcs: https://github.com/tbillington/kondo.git
Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo

%description
Kondo is a CLI and GUI tool to remove unneeded dependencies and build artifacts
like node_modules or target from projects. It supports 20+ project types
including Rust, Python, and JavaScript, saving disk space. Use cautiously, as it
acts like rm -rf, and always back up projects.

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
%doc README.md CHANGELOG.md
%_bindir/%bin_name

%changelog
* Thu Jun 25 2026 Aleksandr A. Voyt <sobue@altlinux.org> 0.9-alt1
- 0.8 -> 0.9

* Wed Aug 13 2025 Aleksandr A. Voyt <sobue@altlinux.org> 0.8-alt1
- Initial build.
