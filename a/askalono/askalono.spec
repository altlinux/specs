Name:    askalono
Version: 0.5.0
Release: alt1

Summary: A tool & library to detect open source licenses from texts
License: Apache-2.0
Group:   Other
Url:     https://github.com/jpeddicord/askalono

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source: %name-%version.tar
Source1: spdx-license-list-data.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

%description
It is a library and command-line tool to help detect license texts. It's
designed to be fast, accurate, and to support a wide variety of license texts.

%prep
%setup -a 1
mv spdx-license-list-data -T datasets/modules/spdx-license-list-data
mkdir -p cli/.cargo
cat >> cli/.cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cd cli
%rust_build

%install
cd cli
%rust_install

%check
cd cli
%rust_test

%files
%doc *.md
%_bindir/*

%changelog
* Fri Jan 10 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus
