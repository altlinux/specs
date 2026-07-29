Name:    motoc
Version: 0.4.0
Release: alt1

Summary: Monado Tracking Origin Calibrator
License: GPL-3.0-only
Group:   Other
URL:     https://github.com/galister/motoc

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: openxr-devel

ExclusiveArch: x86_64

%description
This tool allows users to calibrate devices of different tracking origins
(tracking technologies) to work together.

%prep
%setup -a1
%rust_prep

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
* Wed Jul 29 2026 Sergey Palcheh <minergenon@altlinux.org> 0.4.0-alt1
- new version 0.4.0

* Sun Jun 07 2026 Sergey Palcheh <minergenon@altlinux.org> 0.3.6-alt1
- new version 0.3.6

* Mon Feb 17 2025 Sergey Palcheh <minergenon@altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus
