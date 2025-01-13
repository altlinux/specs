%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name:    askalono
Version: 0.5.0
Release: alt2

Summary: A tool to detect open source licenses from texts
License: Apache-2.0
Group:   Development/Tools
Url:     https://github.com/jpeddicord/askalono

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source: %name-%version.tar
Source1: spdx-license-list-data.tar

BuildRequires(pre): rpm-build-rust

%description
It is a command-line tool to help detect license texts. It's designed to be
fast, accurate, and to support a wide variety of license texts.

%prep
%setup -b 1 -n %name-%version/cli
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%doc LICENSE NOTICE *.md
%_bindir/%name

%changelog
* Sun Jan 12 2025 Vitaly Chikunov <vt@altlinux.org> 0.5.0-alt2
- Improve stans super humeros gigantum.

* Fri Jan 10 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus
