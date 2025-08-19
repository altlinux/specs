%define _unpackaged_files_terminate_build 1

Name: tukai
Version: 0.2.3
Release: alt1
Summary: Terminal based touch typing application.
License: MIT
Group: Games/Educational
Url: https://github.com/hlsxx/tukai

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo

%description
The app provides an interactive typing experience with switchable templates,
designed to help users improve their typing speed and accuracy.

%prep
%setup -a 1
%autopatch -p1

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
%doc *.md 
%_bindir/%name

%changelog
* Tue Aug 19 2025 Pavel Shilov <zerospirit@altlinux.org> 0.2.3-alt1
- 0.2.2 -> 0.2.3

* Thu Jul 31 2025 Pavel Shilov <zerospirit@altlinux.org> 0.2.2-alt1
- Initial build for Alt.
