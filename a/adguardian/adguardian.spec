Name: adguardian
Version: 1.6.0
Release: alt1
Summary: Terminal-based, real-time traffic monitoring and statistics for AdGuardHome
License: MIT
Group: Monitoring
Url: https://github.com/Lissy93/AdGuardian-Term
Source: %name-%version.tar
Source1: vendor.tar
# https://github.com/Lissy93/AdGuardian-Term/issues/21
Patch1: alt-fix-upstream-issue-21.patch
Patch2: alt-disable-updates-check.patch

ExcludeArch: ppc64le

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo

%description
AdGuardian Terminal Eddition - Keep an eye on your traffic,
with this (unofficial) buddy for your AdGuard Home instance.

%prep
%setup -a 1
%patch1 -p1
%patch2 -p1
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
%_bindir/%name

%changelog
* Thu Mar 07 2024 Alexander Makeenkov <amakeenk@altlinux.org> 1.6.0-alt1
- Initial build for ALT.
