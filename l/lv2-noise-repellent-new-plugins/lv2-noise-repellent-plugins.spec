
%define _unpackaged_files_terminate_build 1

Name: lv2-noise-repellent-new-plugins
Version: 0.2.5
Release: alt1

Summary: An lv2 plug-in for broadband noise reduction
License: GPLv3+
Group: Sound

Url: https://github.com/lucianodato/noise-repellent
Source0: %name-%version.tar
Source1: Home.md

Patch0:  %name-%version-%release.patch

BuildRequires(pre): meson
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(libspecbleach)

%description
noise-repellent is an lv2 plug-in for broadband noise
reduction, featuring:
* spectral gating and spectral subtraction suppression rule
* adaptive and manual noise thresholds estimation
* adjustable noise floor
* adjustable offset of thresholds to perform over-subtraction
* time smoothing and a masking estimation to reduce artifacts
* basic onset detector to avoid transients suppression
* whitening of the noise floor to mask artifacts and
  to recover higher frequencies
* option to listen to the residual signal
* soft bypass
* noise profile saved with the session

%prep
%setup
cp -a %SOURCE1 .

%autopatch -p1

%build
%meson
%meson_build -v

%install
%meson_install

%files
%_libdir/lv2/*
%doc Home.md

%changelog
* Thu Jan 29 2026 Ivan A. Melnikov <iv@altlinux.org> 0.2.5-alt1
- 0.2.5
- rename to lv2-noise-repellent-new-plugins

* Mon Sep 12 2022 Ivan A. Melnikov <iv@altlinux.org> 0.2.3-alt1
- 0.2.3

* Tue Aug 10 2021 Michael Shigorin <mike@altlinux.org> 0.1.5-alt2
- E2K builds fine

* Sat Jun 05 2021 Ivan A. Melnikov <iv@altlinux.org> 0.1.5-alt1
- Initial build for Sisyphus
