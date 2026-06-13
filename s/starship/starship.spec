%ifarch i586 armh ppc64le
%def_without check
%else
%def_with check
%endif

Name: starship
Version: 1.25.1
Release: alt1
Summary: The minimal, blazing-fast, and infinitely customizable prompt for any shell
License: ISC
Group: Shells
Url: https://starship.rs
VCS: https://github.com/starship/starship

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: cargo-vendor-checksum
BuildRequires: cmake

%if_with check
BuildRequires: git
%endif

%description
%summary.

%prep
%setup -a 1
%rust_prep
sed -i 's/strip = true/strip = false/' Cargo.toml
%ifarch armh i586
# build failed with lto
sed -i 's/lto = true/lto = false/' Cargo.toml
%endif

%build
cargo-vendor-checksum --all
%rust_build

%install
%rust_install

%check
%buildroot%_bindir/%name print-config > %name.toml
export STARSHIP_CONFIG=%name.toml
export TERM=xterm
# skip randomly failing test
cargo test -- --skip expiration_date_set

%files
%_bindir/%name
%doc LICENSE

%changelog
* Sat Jun 13 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.25.1-alt1
- Updated to version 1.25.1.

* Fri Nov 28 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.24.1-alt2
- Removed illegal content from README files.

* Sat Nov 22 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.24.1-alt1
- Updated to version 1.24.1.

* Fri Oct 31 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.24.0-alt1
- Updated to version 1.24.0.

* Wed May 28 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.23.0-alt1
- Updated to version 1.23.0.

* Sat Dec 14 2024 Alexander Makeenkov <amakeenk@altlinux.org> 1.21.1-alt1
- Updated to version 1.21.1.

* Tue Aug 27 2024 Alexander Makeenkov <amakeenk@altlinux.org> 1.20.1-alt1
- Updated to version 1.20.1.

* Sun Jan 07 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.17.1-alt2
- NMU: fixed FTBFS on LoongArch

* Fri Jan 05 2024 Alexander Makeenkov <amakeenk@altlinux.org> 1.17.1-alt1
- Updated to version 1.17.1.

* Wed Sep 13 2023 Alexander Makeenkov <amakeenk@altlinux.org> 1.16.0-alt1
- Updated to version 1.16.0.

* Thu Apr 06 2023 Alexander Makeenkov <amakeenk@altlinux.org> 1.13.1-alt1
- Updated to version 1.13.1

* Sun Dec 18 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.12.0-alt1
- Updated to version 1.12.0
- Enabled check

* Sun Nov 20 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.11.0-alt1
- Initial build for ALT
