Name: installer-feature-serial
Version: 0.6
Release: alt1

Summary: serial console support
License: public domain
Group: System/Kernel and hardware

Url: http://altlinux.org/serial
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

%description
Setup %summary.

%package stage2
Summary: serial console support for installer
Group: System/Configuration/Other
Requires: installer-common-stage2
Requires: agetty

%description stage2
Setup %summary:
get what's provided for the boot
and set it for the installer
so that serial shell is available.

%package stage3
Summary: serial console support for installed system
Group: System/Configuration/Other
Requires: agetty

%description stage3
Setup %summary:
get what's provided for the boot
and set it for the installed system
so that serial login is available.

%prep
%setup

%install
%makeinstall

%files stage2
%_datadir/install2/initinstall.d/*

%files stage3
%_datadir/install2/postinstall.d/*

%changelog
* Wed May 03 2023 Anton Midyukov <antohami@altlinux.org> 0.6-alt1
- postinstall.d/65-serial.sh: clear 'quiet' bootargs
- postinstall.d/65-serial.sh: do'nt clear 'splash' bootargs,
  add serial console for 'failsafe' mode also

* Wed Oct 17 2018 Michael Shigorin <mike@altlinux.org> 0.5-alt1
- rework stage3 into classic shape as well
  (to make sure systemd gets handled _if_ it's installed at all)

* Thu Sep 27 2018 Michael Shigorin <mike@altlinux.org> 0.4-alt1
- rework into classic i-f package (adding stage2 bits)

* Thu Sep 27 2018 Michael Shigorin <mike@altlinux.org> 0.3-alt1
- E2K: fix serial-getty@.service (if any) to just do 115200

* Tue Mar 21 2017 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- get authoritative serial port/speed from kernel cmdline

* Mon Mar 20 2017 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release
