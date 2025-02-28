%define _unpackaged_files_terminate_build 1

Name:           hexyl
Version:        0.16.0
Release:        alt1

Summary:        A command-line hex viewer.
License:        MIT
Group:          File tools
URL:            https://github.com/sharkdp/hexyl

Source:         %name-%version.tar
Source1:        vendor.tar

Patch:          %name-%version-%release.patch

BuildRequires(pre): rpm-build-rust

%description
Hexyl is a hex viewer for the terminal.
It uses a colored output to distinguish different categories
of bytes (NULL bytes, printable ASCII characters,
ASCII whitespace characters, other ASCII characters and non-ASCII).

%prep
%setup -q
%patch -p1
tar -xf %SOURCE1

mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/*
%doc README.md CHANGELOG.md

%changelog
* Wed Feb 26 2025 Sergey Savelev <medovi@altlinux.org> 0.16.0-alt1
- Initial build for Sisyphus.
