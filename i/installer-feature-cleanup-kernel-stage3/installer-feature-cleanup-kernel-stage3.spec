Name: installer-feature-cleanup-kernel-stage3
Version: 0.3
Release: alt1

Summary: Purge kernels except running
License: GPL-2.0-or-later
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar

BuildArch: noarch

%define hookdir %_datadir/install2/preinstall.d

%description
%summary

%prep
%setup

%install
mkdir -p %buildroot%hookdir
install -pm755 40-cleanup-kernel.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Tue May 17 2022 Anton Midyukov <antohami@altlinux.org> 0.3-alt1
- Replace postinstall.d/98-cleanup-kernel.sh to
  preinstall.d/40-cleanup-kernel.sh

* Tue Jun 23 2020 Anton Midyukov <antohami@altlinux.org> 0.2-alt1
- Use 'rpm -e' instead 'apt-get remove'

* Sun Jun 07 2020 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build
