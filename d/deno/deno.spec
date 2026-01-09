%def_enable snapshot
%define ver_major 2.6

%def_disable bootstrap
# online tests failed
%def_disable check

Name: deno
Version: %ver_major.4
Release: alt1

Summary: A modern runtime for JavaScript and TypeScript
License: MIT
Group: Development/Other
Url: https://github.com/denoland/deno

Vcs: https://github.com/denoland/deno.git

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define v8_ver 142.2.0
Source2: https://github.com/denoland/rusty_v8/releases/download/v%v8_ver/librusty_v8_release_x86_64-unknown-linux-gnu.a.gz
Source3: https://github.com/denoland/rusty_v8/releases/download/v%v8_ver/librusty_v8_release_aarch64-unknown-linux-gnu.a.gz

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-build-rust
BuildRequires: cmake clang-devel protobuf-compiler
BuildRequires: glib2-devel
BuildRequires: pkgconfig(sqlite3)

%description
Deno is a JavaScript, TypeScript, and WebAssembly runtime with secure
defaults and a great developer experience.

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%define v8name librusty_v8_release_%_arch-unknown-linux-gnu.a
cp %_sourcedir/%v8name.gz ./
gunzip %v8name.gz

%build
export RUSTY_V8_ARCHIVE=$PWD/%v8name
%rust_build

%install
%rust_install %name %{name}rt

%check
export RUSTY_V8_ARCHIVE=$PWD/%v8name
%rust_test
# --no-remote --unstable-net aspecially for hasher
target/release/deno test -A --unstable --no-remote --unstable-net \
    --lock=tools/deno.lock.json --config tests/config/deno.json tests/unit

%files
%_bindir/%name
%doc README* Releases* CLAUDE* .github/CONTRIBUTING*

#%files runtime
#%_bindir/%{name}rt

%changelog
* Fri Jan 09 2026 Yuri N. Sedunov <aris@altlinux.org> 2.6.4-alt1
- first build for Sisyphus (v2.6.4-18-g30d1a9567)


