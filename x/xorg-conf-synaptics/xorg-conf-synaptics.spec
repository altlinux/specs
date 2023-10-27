Name: xorg-conf-synaptics
Version: 1.0
Release: alt2
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
install -Dm0644 %SOURCE0 %buildroot/%_sysconfdir/X11/xorg.conf.d/75-synaptics-extra.conf

%files
%config(noreplace) %_sysconfdir/X11/xorg.conf.d/75-synaptics-extra.conf

%changelog
* Wed Oct 25 2023 Dmitry Terekhin <jqt4@altlinux.org> 1.0-alt2
- Add an additional setting for touchpads with ID 0911:5288

* Mon Jul 03 2017 Mikhail Efremov <sem@altlinux.org> 1.0-alt1
- Rename config and move it to 75 position (closes: #33611).
- Drop MaxTapTime option.

* Sat Nov 14 2015 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt1
- added an example how to disable the tap.

* Tue Dec 24 2013 Mikhail Efremov <sem@altlinux.org> 0.2-alt1
- added elantech soft-button example (by Michael Shigorin).

* Wed Dec 11 2013 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build.

