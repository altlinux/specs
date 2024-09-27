%def_without check

Name: miniserve
Version: 0.28.0
Release: alt1
Summary: A CLI tool to serve files and dirs over HTTP
License: MIT
Group: System/Servers
Url: https://github.com/svenstaro/miniserve
Source: %name-%version.tar

Source1: vendor.tar

ExcludeArch: ppc64le

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo

%description
miniserve is a small, self-contained cross-platform CLI tool
that allows you to just grab the binary and serve some file(s)
via HTTP.

%prep
%setup -a 1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build
./target/release/%name --print-manpage > %name.1

%install
%rust_install
mkdir -p %buildroot%_man1dir
install -m 0644 %name.1 %buildroot%_man1dir

%check
%rust_test

%files
%_bindir/%name
%_man1dir/%name.1.*
%doc LICENSE README.md

%changelog
* Fri Sep 27 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.28.0-alt1
- Updated to version 0.28.0.

* Wed Jan 17 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.26.0-alt1
- Updated to version 0.26.0.

* Sun Jan 07 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.25.0-alt1
- Updated to version 0.25.0.

* Sun Oct 02 2022 Alexander Makeenkov <amakeenk@altlinux.org> 0.22.0-alt1
- Initial build for ALT.
