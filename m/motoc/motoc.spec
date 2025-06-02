Name:    motoc
Version: 0.3.4
Release: alt1

Summary: Monado Tracking Origin Calibrator
License: GPL-3.0
Group:   Other
Url:     https://github.com/galister/motoc

Source: %name-%version.tar
Source1: %name-vendor-%version.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: openxr-devel

ExclusiveArch: x86_64

%description
This tool allows users to calibrate devices of different tracking origins
(tracking technologies) to work together.

%prep
%setup -a1

mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/Ralith/openxrs.git?rev=6c7747aee678048642dc16aad8bab3d6961dce03"]
git = "https://github.com/Ralith/openxrs.git"
rev = "6c7747aee678048642dc16aad8bab3d6961dce03"
replace-with = "vendored-sources"

[source."git+https://github.com/technobaboo/libmonado-rs.git?rev=8982759c936ddf3d0fffc96ec404bfe53971276d"]
git = "https://github.com/technobaboo/libmonado-rs.git"
rev = "8982759c936ddf3d0fffc96ec404bfe53971276d"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

sed -i -e 's/"files":{[^}]*}/"files":{}/' \
    ./vendor/openxr-sys/.cargo-checksum.json

%build
%rust_build

%install
%rust_install

%files
%doc LICENSE README.md
%_bindir/%name

%changelog
* Mon Feb 17 2025 Sergey Palcheh <minergenon@altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus
