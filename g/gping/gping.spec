Name: gping
Version: 1.4.0
Release: alt1
Summary: Ping, but with a graph
License: MIT
Group: Networking/Other
Url: https://github.com/orf/gping
Source: %name-%version.tar

BuildRequires: rust-cargo

%description
%summary.

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cargo build --offline --release

%install
mkdir -p %buildroot%_bindir
install -m 0755 target/release/%name %buildroot%_bindir

%files
%_bindir/%name
%doc readme.md LICENSE

%changelog
* Fri Oct 07 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.4.0-alt1
- Updated to version 1.4.0

* Mon Jun 27 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.3.2-alt1
- Updated to version 1.3.2

* Mon May 16 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.3.1-alt1
- Updated to version 1.3.1

* Sat Nov 20 2021 Alexander Makeenkov <amakeenk@altlinux.org> 1.2.6-alt1
- Updated to version 1.2.6

* Sun Jun 06 2021 Alexander Makeenkov <amakeenk@altlinux.org> 1.2.1-alt1
 - Initial build for ALT

