%define _unpackaged_files_terminate_build 1

Name: qbootctl
Version: 0.2.2
Release: alt1

Summary: Qualcomm A/B boot slot control utility
License: GPL-3.0-only
Group: System/Configuration/Boot and Init
Url: https://github.com/linux-msm/qbootctl

Source: %name-%version.tar
Patch1: qbootctl-alt-systemd-unit.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson

%description
qbootctl is a port of the Qualcomm bootctrl HAL to Linux. It manages the
A/B boot slot metadata (active, successful and bootable flags and the slot
retry counters) kept in the GPT partition attributes on Qualcomm devices,
letting the running system mark its current boot slot successful so the
bootloader stops decrementing the slot retry counter.

The bundled qbootctl-mark-successful.service marks the current slot
successful on every boot that reaches multi-user.target.

%prep
%setup
%patch1 -p1

%build
%add_optflags -I%_includedir/linux-default/include
%meson
%meson_build

%install
%meson_install
install -Dpm644 altlinux/qbootctl-mark-successful.service \
    %buildroot%_unitdir/qbootctl-mark-successful.service
install -Dpm644 altlinux/qbootctl-mark-successful.preset \
    %buildroot%_presetdir/85-qbootctl-mark-successful.preset

%post
%post_service qbootctl-mark-successful

%preun
%preun_service qbootctl-mark-successful

%files
%doc README.md
%_bindir/qbootctl
%_unitdir/qbootctl-mark-successful.service
%_presetdir/85-qbootctl-mark-successful.preset

%changelog
* Thu Jul 16 2026 Anton Politov <ampernic@altlinux.org> 0.2.2-alt1
- Initial build.
