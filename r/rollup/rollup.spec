%define _unpackaged_files_terminate_build 1

%define rollup_arch %nodejs_native_arch

Name: rollup
Version: 4.60.2
Release: alt2
Summary: Rollup JavaScript bundler
License: MIT
Group: Development/Other
Url: https://rollupjs.org
VCS: https://github.com/rollup/rollup

Source: %name-%version.tar
Source1: node-modules-%version.tar
Source2: vendor.tar

BuildRequires(pre): rpm-macros-nodejs >= 0.20.7-alt4
BuildRequires(pre): rpm-macros-rust
BuildRequires: npm
BuildRequires: rust-cargo
BuildRequires: gcc-c++
BuildRequires: cmake

%description
Rollup is a JavaScript module bundler for Node.js.

%package native
Summary: Native bindings for Rollup
Group: Development/Other
Requires: %name = %EVR
ExcludeArch: %ix86

%description native
Native N-API bindings for Rollup.

%prep
%setup -a1 -a2

%rust_prep

%build
export PATH="$PATH:$PWD/node_modules/.bin"
export CARGO_BUILD_JOBS=${NPROCS:-4}
export RUSTC_BOOTSTRAP=1

%ifarch aarch64
export CARGO_TARGET_AARCH64_UNKNOWN_LINUX_GNU_LINKER=gcc
%endif
%ifarch loongarch64
export CARGO_TARGET_LOONGARCH64_UNKNOWN_LINUX_GNU_LINKER=gcc
%endif
%ifarch riscv64
export CARGO_TARGET_RISCV64GC_UNKNOWN_LINUX_GNU_LINKER=gcc
%endif

npm run build:napi -- --release
cp %name.linux-%rollup_arch-gnu.node node_modules/%name/dist
npm run build:js:node
npm run build:copy-native

%install
mkdir -p %buildroot%nodejs_sitelib/%name
cp -a package.json README.md %buildroot%nodejs_sitelib/%name
cp -a dist %buildroot%nodejs_sitelib/%name

mkdir -p %buildroot%_bindir
cat > %buildroot%_bindir/%name <<'EOF'
#!/usr/bin/env node
require('/usr/lib/node_modules/%name/dist/bin/%name')
EOF
chmod 755 %buildroot%_bindir/%name

mkdir -p %buildroot%nodejs_sitelib/@%name/%name-linux-%rollup_arch-gnu

install -m 755 \
  %name.linux-%rollup_arch-gnu.node \
  %buildroot%nodejs_sitelib/@%name/%name-linux-%rollup_arch-gnu/

cp -a \
  npm/linux-%rollup_arch-gnu/package.json \
  npm/linux-%rollup_arch-gnu/README.md \
  %buildroot%nodejs_sitelib/@%name/%name-linux-%rollup_arch-gnu/

%files
%doc README.md
%_bindir/%name
%dir %nodejs_sitelib/%name
%nodejs_sitelib/%name

%files native
%dir %nodejs_sitelib/@%name
%dir %nodejs_sitelib/@%name/%name-linux-%rollup_arch-gnu
%nodejs_sitelib/@%name/%name-linux-%rollup_arch-gnu/*

%changelog
* Tue Apr 21 2026 Ivan A. Melnikov <iv@altlinux.org> 4.60.2-alt2
- NMU: build on riscv64 and loongarch64.

* Mon Apr 20 2026 Aleksandr Gamzin <gamzin@altlinux.org> 4.60.2-alt1
- 4.60.2.

* Thu Jan 22 2026 Aleksandr Gamzin <gamzin@altlinux.org> 4.56.0-alt1
- Initial build for Sisyphus.
