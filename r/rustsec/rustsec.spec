%define _unpackaged_files_terminate_build 1

%ifarch %ix86
%define _smp_mflags -j32
%endif

Name: rustsec
Version: 0.32.0
Release: alt2

Summary: RustSec API & Tooling
License: Apache-2.0 or MIT
Group: Development/Other
Url: https://rustsec.org/
Vcs: https://github.com/rustsec/rustsec.git

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust

%description
The package contains a set of utilities maintained by RustSec to detect
vulnerabilities in crates.

Vulnerability database itself can be found at:
https://rustsec.org/

%package -n cargo-audit
Version: 0.22.1
Summary: Audit your dependencies for crates with security vulnerabilities
Group: Development/Tools
Url: https://crates.io/crates/cargo-audit

%description -n cargo-audit
Audit your dependencies for crates with security vulnerabilities
reported to the RustSec Advisory Database.

The advisory database itself can be found at:
https://github.com/RustSec/advisory-db

%package -n cargo-lock
Version: 11.0.1
Summary: Self-contained serde-powered Cargo.lock parser/serializer
Group: Development/Tools
Url: https://crates.io/crates/cargo-lock

%description -n cargo-lock
Self-contained serde-powered Cargo.lock parser/serializer with support
for the V1/V2/V3/V4 formats, as well as optional dependency tree
analysis features. Used by RustSec.

%prep
%setup -a 1
%rust_prep
%ifarch %ix86
cat >> .cargo/config.toml <<EOF
lto = "thin"
codegen-units = 16
EOF
%endif

%build
%rust_build --all-features -p cargo-audit -p cargo-lock

%install
%rust_install cargo-audit cargo-lock

%check
# Tests for cargo-audit require fetching database.
%rust_test --all-features -p cargo-lock

%files -n cargo-audit
%doc cargo-audit/LICENSE-*
%_bindir/cargo-audit

%files -n cargo-lock
%doc cargo-lock/LICENSE-*
%_bindir/cargo-lock

%changelog
* Tue Apr 07 2026 Sergey Zhidkih <rx1513@altlinux.org> 0.32.0-alt2
- Fix FTBFS on i586.

* Tue Feb 10 2026 Sergey Zhidkih <rx1513@altlinux.org> 0.32.0-alt1
- New rustsec version (0.32.0).
- New cargo-audit version (0.22.1).
- New cargo-lock version (11.0.1).

* Tue Aug 05 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.30.4-alt1
- Initial build.
