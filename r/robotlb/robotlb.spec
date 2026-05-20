%global _unpackaged_files_terminate_build 1

Name:    robotlb
Version: 0.0.6
Release: alt1

Summary: Hetzner LoadBalancer for bare-metal robot clusters
License: unknown
Group:   Other
Url:     https://github.com/Intreecom/robotlb

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires(pre): rpm-build-rust
BuildRequires: libssl-devel
BuildRequires: libjemalloc-devel
BuildRequires: /proc

%description
%summary.

%prep
%setup
%patch -p1
%rust_prep

%build
export JEMALLOC_SYS_WITH_MALLOC_CONF="background_thread:true,tcache:false,dirty_decay_ms:100,muzzy_decay_ms:100,abort_conf:true"
%rust_build

%install
%rust_install

%files
%doc README.md
%_bindir/%name

%changelog
* Tue May 05 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.0.6-alt1
- New version 0.0.6

* Tue Mar 24 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.0.5-alt1
- Initial build for ALT.
