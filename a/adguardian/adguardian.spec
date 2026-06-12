%def_with check

Name: adguardian
Version: 1.7.0
Release: alt1
Summary: Terminal-based, real-time traffic monitoring and statistics for AdGuardHome
License: MIT
Group: Monitoring
URL: https://adguardian.as93.net
VCS: https://github.com/Lissy93/AdGuardian-Term

Source: %name-%version.tar
Source1: vendor.tar
Patch: alt-disable-updates-check.patch

ExcludeArch: ppc64le

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
AdGuardian Terminal Eddition - Keep an eye on your traffic,
with this (unofficial) buddy for your AdGuard Home instance.

%prep
%setup -a 1
%patch -p1
%rust_prep

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/%name

%changelog
* Fri Jun 12 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.7.0-alt1
- Updated to version 1.7.0.

* Thu Mar 07 2024 Alexander Makeenkov <amakeenk@altlinux.org> 1.6.0-alt1
- Initial build for ALT.
