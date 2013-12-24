Name: xorg-conf-synaptics
Version: 0.2
Release: alt1
Summary: Config file for Synaptics touchpads
License: %pubdomain
Group: System/Configuration/Hardware
Source0: synaptics.conf
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

Requires: xorg-drv-synaptics

%description
This package contains configuratin file for Synaptics touchpads
with some frequently used options.
Left mouse button by tapping is enabled by default.

%install
install -Dm0644 %SOURCE0 %buildroot/%_sysconfdir/X11/xorg.conf.d/20-synaptics.conf

%files
%config(noreplace) %_sysconfdir/X11/xorg.conf.d/20-synaptics.conf

%changelog
* Tue Dec 24 2013 Mikhail Efremov <sem@altlinux.org> 0.2-alt1
- added elantech soft-button example (by Michael Shigorin).

* Wed Dec 11 2013 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build.

