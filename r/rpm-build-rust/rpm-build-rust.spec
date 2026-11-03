Name:      rpm-build-rust
Version:   0.2.0
Release:   alt1
Summary:   RPM build enviroment to build rust packages
Group:     Development/Other
License:   GPLv2
BuildArch: noarch
Packager:  Mikhail Gordeev <obirvalger@altlinux.ru>

Source0:   rust.macros

Requires:  rust
Requires:  rust-cargo-c
Requires:  rpm-macros-rust

%description
RPM build enviroment to build rust packages

%package -n rpm-macros-rust
Summary: RPM helper macros to build rust packages
Group: Development/Other
BuildArch:      noarch

%description -n rpm-macros-rust
These helper macros provide possibility to create rust packages.

%install
mkdir -p %buildroot/%_rpmmacrosdir

cp %SOURCE0 %buildroot%_rpmmacrosdir/rust

%files

%files -n rpm-macros-rust
%_rpmmacrosdir/rust

%changelog
* Tue Oct 27 2026 Sergey Zhidkih <rx1513@altlinux.org> 0.2.0-alt1
- Switch the rust-cargo requirement to rust
- Add a vendoring option to %%rust_prep (Closes: 48459)
- Remove RUSTFLAGS from the environment (Closes: 48459)
- Synchronize rustflags between stages (Closes: 48459)
- Allow %%rust_prep to be specified for an arbitrary path
- Lower macro's debuginfo priority
- Add options to configure optimizations, debuginfo and stripping
- Add rust-cargo-c macros: %%rust_cbuild, %%rust_cinstall and %%rust_ctest
- Add dependency on rust-cargo-c macros: %%rust_cbuild, %%rust_cinstall and %%rust_ctest
- Add support for overriding upstream build profiles
- Add %%rust_resolve_target_dir to determine the target directory from Cargo configuration
- Add %%rust_build_dir, containing the default path where Cargo places build artifacts
- Prepend empty line to config.toml in %%rust_prep (Closes: 60438)
- Rename %%__cargo macro to %%cargo and make use of it
- Add %%rust_run macro for building intermidiate artifacts

* Tue Jul 29 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.4-alt1
- Fix %%rust_prep ending (Closes: 55406)

* Tue Jun 22 2025 Artyom Sinyugin <writers@altlinux.org> 0.1.3-alt1
- (NMU) New macro %%rust_prep was added
- (NMU) smp_mflags and --no-fail-fast params were added in %%rust_test
- (NMU) RUSTFLAGS env variable was added into %%rust_test to match %%rust_build

* Fri Aug 20 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.2-alt1
- Add parameters to macros

* Tue Aug 03 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.1-alt1
- Remove target specifiaction

* Tue Jun 22 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.0-alt1
- Initila build
