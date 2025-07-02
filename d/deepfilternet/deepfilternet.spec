%def_disable snapshot
%define _name deepfilternet
%define __name DeepFilterNet
%define ver_major 0.5

%def_disable bootstrap

Name: %_name
Version: %ver_major.6
Release: alt0.1

Summary: A Low Complexity Speech Enhancement Framework for Full-Band Audio using on Deep Filtering
License: MIT OR Apache-2.0
Group: Sound
Url: https://github.com/Rikorose/DeepFilterNet

Vcs: https://github.com/Rikorose/DeepFilterNet.git

%if_disabled snapshot
Source: https://github.com/Rikorose/DeepFilterNet/archive/v%version/%__name-%version.tar.gz
%else
Source: %__name-%version.tar
%endif
Source1: %__name-%version-cargo.tar

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-rust
BuildRequires: rust-cargo rust-cargo-c python3 /proc
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(hdf5)
BuildRequires: ladspa_sdk

# for df-demo ui
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(expat)
# ...

%description
%{summary}.

%package -n ladspa-%name-plugins
Summary: %__name LADSPA plugin
Group: Sound

%description -n ladspa-%name-plugins
This package provides %__name LADSPA plugin library.

%package -n df-demo
Summary: %__name demo package
Group: Sound

%description -n df-demo
This package provides df-demo from %__name package.

%prep
%setup -n %__name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ -d .cargo ] || mkdir .cargo
# this is an inference error on crate `time` caused by an API change in Rust 1.80.0; update `time` to version `>=0.3.35`
cargo update -p time &&
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%__name-%version-cargo.tar Cargo.lock .cargo/ vendor/}

%build
# for --features

%rust_build \
%ifarch %ix86
    --config 'profile.release.lto=false'
%endif
# error[E0554]: `#![feature]` may not be used on the stable release channel
%if 0
export RUSTUP_TOOLCHAIN=nightly
-p deep-filter-ladspa \
-p df-demo \
--features df-demo/ui \
--bin df-demo \
--lib
%endif
%nil

%install
# ladspa plugin
install -Dm 755 target/release/libdeep_filter_ladspa.so -t %buildroot%_ladspa_path
# df-demo-c
install -Dm 755 target/release/df-demo-c -t %buildroot%_bindir

%files -n ladspa-%name-plugins
%_ladspa_path/libdeep_filter_ladspa.so
%doc ladspa/README*

%files -n df-demo
%_bindir/df-demo-c
%doc README*

%changelog
* Wed Jul 02 2025 Yuri N. Sedunov <aris@altlinux.org> 0.5.6-alt0.1
- first build for Sisyphus

