%define _unpackaged_files_terminate_build 1

Name: dtop
Version: 0.7.0
Release: alt1
Summary: Terminal dashboard for Docker monitoring across multiple hosts with Dozzle integration.
License: MIT
Group: System/Configuration/Other
Url: https://github.com/amir20/dtop

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo

%description
%summary

%prep
%setup -a 1
%patch -p1

%build
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
%rust_build

%install
%rust_install

%files
%doc README.md
%_bindir/%name

%changelog
* Thu Mar 19 2026 Pavel Shilov <zerospirit@altlinux.org> 0.7.0-alt1
- 0.6.13 -> 0.7.0

* Thu Mar 12 2026 Pavel Shilov <zerospirit@altlinux.org> 0.6.13-alt1
- 0.6.12 -> 0.6.13

* Fri Feb 20 2026 Pavel Shilov <zerospirit@altlinux.org> 0.6.12-alt1
- 0.6.7 -> 0.6.12

* Tue Dec 23 2025 Pavel Shilov <zerospirit@altlinux.org> 0.6.7-alt1
- 0.5.0 -> 0.6.7

* Thu Nov 27 2025 Pavel Shilov <zerospirit@altlinux.org> 0.5.0-alt1
- 0.4.5 -> 0.5.0

* Thu Nov 20 2025 Pavel Shilov <zerospirit@altlinux.org> 0.4.5-alt1
- 0.2.0 -> 0.4.5

* Tue Oct 21 2025 Pavel Shilov <zerospirit@altlinux.org> 0.2.0-alt1
- 0.2.0 -> 0.0.43

* Wed Sep 03 2025 Pavel Shilov <zerospirit@altlinux.org> 0.0.43-alt1
- 0.0.40 -> 0.0.43

* Wed Aug 27 2025 Pavel Shilov <zerospirit@altlinux.org> 0.0.40-alt1
- 0.0.38 -> 0.0.40

* Mon Aug 18 2025 Pavel Shilov <zerospirit@altlinux.org> 0.0.38-alt1
- 0.0.36 -> 0.0.38

* Mon Jul 21 2025 Pavel Shilov <zerospirit@altlinux.org> 0.0.36-alt1
- Initial build for Sisyphys.
