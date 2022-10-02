%def_without check

Name: miniserve
Version: 0.22.0
Release: alt1
Summary: A CLI tool to serve files and dirs over HTTP
License: MIT
Group: System/Servers
Url: https://github.com/svenstaro/miniserve
Source: %name-%version.tar

ExcludeArch: ppc64le

BuildRequires: rust-cargo

%description
miniserve is a small, self-contained cross-platform CLI tool
that allows you to just grab the binary and serve some file(s)
via HTTP.

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

%if_with check
%check
cargo test
%endif

%install
install -D -m755 target/release/%name %buildroot%_bindir/%name

%files
%_bindir/%name
%doc LICENSE README.md

%changelog
* Sun Oct 02 2022 Alexander Makeenkov <amakeenk@altlinux.org> 0.22.0-alt1
- Initial build for ALT
