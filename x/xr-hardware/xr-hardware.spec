Name: xr-hardware
Version: 1.1.1
Release: alt1

Summary: Udev rules files for normal user access to XR input devices
License: BSL-1.0
Group: System/Configuration/Hardware
URL: https://gitlab.freedesktop.org/monado/utilities/xr-hardware

Source: %name-%version.tar

BuildRequires: make
BuildRequires: python3
BuildRequires: python3-module-attrs
BuildRequires: python3-module-black
BuildRequires: python3-module-flake8

BuildArch: noarch

%description
This package contains a udev rules file to permit access to virtual reality
(VR) and augmented reality (AR), collectively "XR", interaction devices as a
normal user.

%prep
%setup

%build
%make_build all

%install
%make_install RULES_DIR="%_udevrulesdir" DESTDIR="%buildroot" install

%check
make test

%files
%doc LICENSE.txt README.md CHANGELOG.md
%_udevrulesdir/70-xrhardware.rules

%changelog
* Tue Jan 14 2025 Sergey Palcheh <minergenon@altlinux.org> 1.1.1-alt1
- initial build for ALT Sisyphus

