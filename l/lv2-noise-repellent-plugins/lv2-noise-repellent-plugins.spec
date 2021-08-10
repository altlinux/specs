
%define _unpackaged_files_terminate_build 1
%define oname noise-repellent

Name: lv2-%oname-plugins
Version: 0.1.5
Release: alt2

Summary: An lv2 plug-in for broadband noise reduction
License: GPLv3+
Group: Sound

Url: https://github.com/lucianodato/noise-repellent
Source0: %name-%version.tar
Source1: Home.md

BuildRequires(pre): meson
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(fftw3f)

# meson.build have x86-specific options that require a patch
# to override; let's just rest restrict the targets for now
# (e2k is fine with 'em though).
ExclusiveArch: %ix86 x86_64 aarch64 %e2k

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

%build
%meson
%meson_build

%install
# NOTE: the build system installs to some strange location,
# let's just install the files manually
%define odir %_libdir/lv2/nrepel.lv2
mkdir -p %buildroot%odir
install -p -m644 -t %buildroot%odir/ */*.ttl */*.so

%files
%odir
%doc Home.md

%changelog
* Tue Aug 10 2021 Michael Shigorin <mike@altlinux.org> 0.1.5-alt2
- E2K builds fine

* Sat Jun 05 2021 Ivan A. Melnikov <iv@altlinux.org> 0.1.5-alt1
- Initial build for Sisyphus
