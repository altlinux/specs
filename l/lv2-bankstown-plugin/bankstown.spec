Name: lv2-bankstown-plugin
Version: 1.1.0
Release: alt1

Summary: Bass enhancer as LV2 plugin
License: MIT
Group: Sound
Url: https://github.com/chadmed/bankstown

ExclusiveArch: aarch64 x86_64

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: rust-cargo /proc

%description
Halfway-decent three-stage psychoacoustic bass approximation.

%prep
%setup
%ifdef bootstrap
cargo vendor crates
tar cf %SOURCE1 crates
%else
tar xf %SOURCE1
%endif

%build
export CARGO_HOME=${PWD}/cargo
cargo build --release

%install
install -pm0644 -D target/release/libbankstown.so \
	%buildroot%_libdir/lv2/bankstown.lv2/bankstown.so
install -pm0644 *ttl %buildroot%_libdir/lv2/bankstown.lv2

%files
%_libdir/lv2/*

%changelog
* Tue Dec 03 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.0-alt1
- 1.1.0 released
