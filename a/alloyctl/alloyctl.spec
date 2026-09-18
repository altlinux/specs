Name:    alloyctl
Version: 0.3.2
Release: alt1

Summary: Linux CLI to control SteelSeries devices
License: GPL-2.0-only
Group:   System/Configuration/Hardware
URL:     https://alloy.szymon-wilczek.me
VCS:     https://github.com/szymonwilczek/alloyctl

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-systemd
BuildRequires: gcc make libncursesw-devel pkg-config

%description
Full-screen terminal replacement for SteelSeries Engine on Linux.
Panes, modals, live preview, and every setting the hardware really has.

%prep
%setup

%build
%make_build CFLAGS="%optflags"

%install
%makeinstall_std PREFIX=%_prefix UDEVDIR=%_udevrulesdir

%files
%doc LICENSE README.rst
%_bindir/alloyctl
%_mandir/man1/alloyctl.1*
%_udevrulesdir/70-alloyctl-uinput.rules
%_udevrulesdir/71-alloyctl-hidraw.rules

%post
%udev_rules_update

%postun
%udev_rules_update

%changelog
* Fri Sep 18 2026 Sergey Palcheh <minergenon@altlinux.org> 0.3.2-alt1
- Initial build for Sisyphus
