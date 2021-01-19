Name:     hyperfine
Version:  1.11.0
Release:  alt2

Summary:  A command-line benchmarking tool
License:  Apache-2.0
Group:    Development/Tools
Url:      https://github.com/sharkdp/hyperfine

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: x86_64 aarch64

BuildRequires: rust-cargo
BuildRequires: /proc

%description
%summary

%prep
%setup
%patch -p1

%build
export RUSTFLAGS="-g"
cargo build \
    --release \
    %{?_smp_mflags} \
    --offline \
    --target %_arch-unknown-linux-gnu

%install
install -Dm 755 target/%_arch-unknown-linux-gnu/release/%name %buildroot%_bindir/%name

%check
cargo test \
    --release \
    --no-fail-fast \
    --target %_arch-unknown-linux-gnu

%files
%_bindir/*
%doc *.md

%changelog
* Tue Jan 19 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.11.0-alt2
- Add generation of debuginfo

* Mon Nov 09 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.11.0-alt1
- Initial build for Sisyphus
