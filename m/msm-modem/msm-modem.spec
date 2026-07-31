%define _unpackaged_files_terminate_build 1

%def_enable uim_selection
%def_enable wwan_port

Name: msm-modem
Version: 13
Release: alt1
Summary: Common support for Qualcomm MSM modems
License: GPLv3
Group: System/Kernel and hardware
Url: https://gitlab.postmarketos.org/postmarketOS/msm-modem/
VCS: https://gitlab.postmarketos.org/postmarketOS/msm-modem.git

ExclusiveArch: aarch64

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson

%description
Tools and utilities for controlling Qualcomm MSM (Mobile Station Modem)
devices on ARM64 systems. Provides systemd service units for UIM selection and
WWAN port configuration.

%prep
%setup

%build
%meson \
    %{subst_enable_meson_bool uim_selection uim-selection} \
    %{subst_enable_meson_bool wwan_port wwan-port} \
    -Ddownstream=false \
    -Dopenrc=false \
    -Dsystemd=true 

%meson_build -v

%install
%meson_install

%files
%_libexecdir/*
%_unitdir/*.service

%changelog
* Sun Jul 26 2026 Vasiliy Doylov <neko@altlinux.org> 13-alt1
- Initial build for ALT.
