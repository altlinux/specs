%define _unpackaged_files_terminate_build 1

Name:    linbit-losetup-container
Version: 1.1.0
Release: alt1

Summary: LINBIT-specific losetup-container
License: None
Group:   Other
Url:     https://github.com/LINBIT/losetup-container

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
Normal losetup, with one modification. If, and only if it is called
with losetup -l -O NAME,BACK-FILE, the output is slightly different,
in all other cases the normal losetup output is used.

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
export BUILDDIR="/usr/src/RPM/BUILD/%name-%version/target/release"
mv $BUILDDIR/losetup-container $BUILDDIR/%name
%rust_install

%check
%rust_test

%files
%doc *.md
%_bindir/*

%changelog
* Thu Mar 19 2026 Nadezhda Fedorova <fedor@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.
