%global _unpackaged_files_terminate_build 1

Name: netwatch
Version: 0.25.0
Release: alt1

Summary: Real-time network diagnostics in your terminal

Group: Monitoring
License: MIT
Url: https://netwatchlabs.com/
Vcs: https://github.com/matthart1983/netwatch.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# upstream only supports these architectures
ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libpcap-devel

%description
%summary.

%prep
%setup
%patch -p1
%rust_prep

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%doc *.md
%_bindir/netwatch

%changelog
* Mon Jun 01 2026 Nikita Stavtsev <nst@altlinux.org> 0.25.0-alt1
- Initial build
