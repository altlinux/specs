Name:    ccsum
Version: 0.2.3
Release: alt1

Summary: Convenient Checksum Utility
License: MIT
Group:   Other
Url:     https://github.com/sevenc-nanashi/ccsum
VCS:     https://github.com/sevenc-nanashi/ccsum.git

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires: rpm-build-rust
BuildRequires: gcc-c++

%description
Convenient Checksum Utility - a CLI tool for computing and verifying
file checksums with support for multiple hash algorithms.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install

%files
%doc LICENSE README.*
%_bindir/%name

%changelog
* Thu Jun 25 2026 Sergey Palcheh <minergenon@altlinux.org> 0.2.3-alt1
- new version 0.2.3

* Wed May 27 2026 Sergey Palcheh <minergenon@altlinux.org> 0.2.2-alt1
- new version 0.2.2
- switched to predownloaded-development (cargo vendor) packaging

* Sun Jan 26 2025 Sergey Palcheh <minergenon@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
