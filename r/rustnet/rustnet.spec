%define _unpackaged_files_terminate_build 1

Name:           rustnet
Version:        1.4.0
Release:        alt1

Summary:        A cross-platform network monitoring terminal UI tool
License:        Apache-2.0
Group:          Monitoring
URL:            https://github.com/domcyrus/rustnet

Source:         %name-%version.tar
# Prepare using:
# cargo-vendor-alt --exclude-crate-path libbpf-sys#elfutils \
#                  --exclude-crate-path libbpf-sys#libbpf
Source1:        vendor.tar

Patch:          %name-%version-%release.patch

BuildRequires(pre): rpm-build-rust
BuildRequires:      pkgconfig(libbpf)
BuildRequires:      pkgconfig(libelf)
BuildRequires:      pkgconfig(zlib)
BuildRequires:      pkgconfig(libpcap)
BuildRequires:      clang

%description
A cross-platform network monitoring tool built with Rust.
RustNet provides real-time visibility into network connections
with detailed state information, connection lifecycle management,
deep packet inspection, and a terminal user interface.

%prep
%setup -a 1 -q
%patch -p1
%rust_prep
# Disabling vendor build of libbpf and elfutils dependencies:
sed -i \
  's/libbpf-rs.*optional = true/&, default-features = false/' \
  crates/rustnet-host/Cargo.toml
sed -i \
  's/libbpf-cargo.*optional = true/&, default-features = false/' \
  crates/rustnet-host/Cargo.toml

%build
%rust_build

%install
%rust_install

# The tests are disabled because their results are unstable
# and depend on system time, and the build may crash due to them.
# The test_get_all_stats and test_get_all_stats tests
# do not work correctly in an isolated environment.
%check
%rust_test -- --skip test_rate_tracker_steady_traffic \
    --skip test_rate_tracker_multiple_updates \
    --skip test_rate_tracker_window_sliding \
    --skip test_list_interfaces \
    --skip test_get_all_stats

%files
%_bindir/*
%doc README.md CHANGELOG.md

%changelog
* Thu Jun 25 2026 Sergey Savelev <medovi@altlinux.org> 1.4.0-alt1
- New version 1.4.0.

* Tue May 19 2026 Sergey Savelev <medovi@altlinux.org> 1.3.0-alt1
- New version 1.3.0.

* Mon Apr 13 2026 Sergey Savelev <medovi@altlinux.org> 1.2.0-alt1
- New version 1.2.0.

* Wed Mar 18 2026 Sergey Savelev <medovi@altlinux.org> 1.1.0-alt1
- New version 1.1.0.

* Thu Feb 12 2026 Sergey Savelev <medovi@altlinux.org> 1.0.0-alt1
- New version 1.0.0.
- The system libraries libbpf and elfutils are used.

* Mon Jan 12 2026 Sergey Savelev <medovi@altlinux.org> 0.18.0-alt1
- New version 0.18.0.

* Mon Dec 08 2025 Sergey Savelev <medovi@altlinux.org> 0.17.0-alt1
- New version 0.17.0.

* Tue Nov 25 2025 Sergey Savelev <medovi@altlinux.org> 0.16.1-alt1
- Initial build for Sisyphus.
