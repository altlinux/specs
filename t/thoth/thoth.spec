Name:    thoth
Version: 0.1.84
Release: alt1

Summary: Terminal scratchpad inspired by the Heynote app
License: MIT
Group:   Other
Url:     https://github.com/jooaf/thoth
VCS:     https://github.com/jooaf/thoth.git

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: gcc-c++

%description
%summary

%prep
%setup -a1

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

%files
%doc CHANGELOG.* CONTRIBUTING.* LICENSE README.*
%_bindir/%name

%changelog
* Mon Jul 14 2025 Sergey Palcheh <minergenon@altlinux.org> 0.1.84-alt1
- Initial build for Sisyphus

