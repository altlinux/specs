%define _unpackaged_files_terminate_build 1

Name: nvidia-legacy-nouveau
Version: 0.1.0
Release: alt1

Summary: Use nouveau for NVIDIA GPUs older than Maxwell
License: GPL-2.0-or-later
Group: System/Configuration/Hardware
Url: https://altlinux.space/rauty/nvidia-legacy-nouveau
VCS: https://altlinux.space/rauty/nvidia-legacy-nouveau.git
BuildArch: noarch

Source: %name-%version.tar

Requires: make-initrd

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-setuptools

# End-to-end tests in %check: the packages whose behaviour the tool relies on.
# A change in any of them must fail the build.
BuildRequires: /proc
BuildRequires: fakeroot
BuildRequires: make-initrd kmod
BuildRequires: blacklist-nouveau
BuildRequires: installer-common-functions
BuildRequires: hwdata

%description
Proprietary NVIDIA branches available in the repository either do not
support GPUs older than Maxwell or work badly with them. This package
provides the nvidia-legacy-nouveau tool: if every NVIDIA GPU in the
system is older than Maxwell, it lifts the nouveau blacklist and keeps
the proprietary driver from loading; otherwise it keeps the proprietary
driver.

%package -n installer-feature-nvidia-legacy-nouveau-stage2
Summary: Installer hook to use nouveau for NVIDIA GPUs older than Maxwell
Group: System/Configuration/Other
Requires: %name = %EVR

%description -n installer-feature-nvidia-legacy-nouveau-stage2
This package contains the installer stage2 hook that runs
nvidia-legacy-nouveau for the system being installed.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
mkdir -p %buildroot%_sbindir
mv %buildroot%_bindir/nvidia-legacy-nouveau %buildroot%_sbindir/
install -pDm755 installer/preinstall.d/40-nvidia-legacy-nouveau.sh \
	%buildroot%_datadir/install2/preinstall.d/40-nvidia-legacy-nouveau.sh

%check
# Fail instead of skipping the end-to-end tests, run the installed entry point.
export NVIDIA_LEGACY_NOUVEAU_E2E=required
export NVIDIA_LEGACY_NOUVEAU_PROG=nvidia-legacy-nouveau
%pyproject_run_unittest discover -s tests -v

%files
%doc README.md
%_sbindir/nvidia-legacy-nouveau
%python3_sitelibdir/nvidia_legacy_nouveau/
%python3_sitelibdir/%{pyproject_distinfo %name}

%files -n installer-feature-nvidia-legacy-nouveau-stage2
%_datadir/install2/preinstall.d/40-nvidia-legacy-nouveau.sh

%changelog
* Mon Oct 26 2026 Ajrat Makhmutov <rauty@altlinux.org> 0.1.0-alt1
- Initial build.
- Use nouveau for NVIDIA GPUs older than Maxwell (Closes: 56688).
