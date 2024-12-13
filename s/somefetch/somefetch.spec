Name:    somefetch
Version: 0.2.0
Release: alt1

Summary: Simple fetch for unix-like
License: BSD-3-Clause
Group:   Other
Url:     https://github.com/UnixAwesomes/somefetch
VCS:     https://github.com/UnixAwesomes/somefetch

Source0: %name-%version.tar
Source1: vendor.tar
 
Patch: somefetch-0.2.0-alt-fixes.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

%description
Simple fetch for unix-like systems

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

tar -xf %SOURCE1 -C %_builddir/%name-%version/

%patch -p0

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%doc *.md
%_bindir/%name

%changelog
* Sat Dec 14 2024 Aleksandr Shamaraev <shad@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus
