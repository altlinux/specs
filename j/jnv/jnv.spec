%define _unpackaged_files_terminate_build 1

Name: jnv
Version: 0.7.1
Release: alt1
Summary: JSON filter using jq with interactive features
License: MIT
Group: Text tools
URL: https://github.com/ynqa/jnv
VCS: https://github.com/ynqa/jnv

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires: rpm-macros-rust
BuildRequires: rust-cargo

%description
Interactive JSON filter built on jq, offering a terminal interface for exploring
and editing JSON.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install

%files
%doc README.md LICENSE
%_bindir/jnv

%changelog
* Tue May 05 2026 Alexey Rodygin <alehandro@altlinux.org> 0.7.1-alt1
- Updated to new version 0.7.1

* Tue Mar 17 2026 Alexey Rodygin <alehandro@altlinux.org> 0.6.2-alt1
- Initial build for ALT Linux
