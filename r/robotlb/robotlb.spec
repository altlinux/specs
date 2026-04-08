%global _unpackaged_files_terminate_build 1

Name:    robotlb
Version: 0.0.5
Release: alt1

Summary: Hetzner LoadBalancer for bare-metal robot clusters
License: unknown
Group:   Other
Url:     https://github.com/Intreecom/robotlb

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: libssl-devel
BuildRequires: libjemalloc-devel
BuildRequires: /proc

%description
%summary.

%prep
%setup
%patch -p1
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
# from Dockerfile
export JEMALLOC_SYS_WITH_MALLOC_CONF="background_thread:true,tcache:false,dirty_decay_ms:100,muzzy_decay_ms:100,abort_conf:true"
%rust_build

%install
%rust_install

%files
%doc README.md
%_bindir/%name

%changelog
* Tue Mar 24 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.0.5-alt1
- Initial build for ALT.
