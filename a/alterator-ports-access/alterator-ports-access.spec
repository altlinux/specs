%define _altdata_dir %_datadir/alterator

Name: alterator-ports-access
Version: 0.5.3
Release: alt1.1
BuildArch: noarch
Source:%name-%version.tar
Summary: alterator module to control ports access
License: %gpl2plus
Group: System/Configuration/Other
Requires: alterator >= 4.10-alt8 alterator-sh-functions >= 0.6-alt5 libshell >= 0.0.1-alt4 gettext
Requires: alterator-l10n >= 2.9.110
Requires: %name-cmdline = %version-%release
BuildPreReq: rpm-build-licenses
BuildPreReq: rpm-macros-alterator
BuildRequires: alterator
BuildArch: noarch

%description
Alterator module to control serial/USB ports access

%package cmdline
Summary: alterator ports access control module command line part
Group: System/Configuration/Other

%description cmdline
Command line part of alterator module to control serial/USB ports access

%prep
%setup -q

%build
%make_build

%install
%makeinstall
#find_lang %name

mkdir -p %buildroot%_sysconfdir/udev/rules.d
touch %buildroot%_sysconfdir/udev/rules.d/40-alterator-ports-access.rules
touch %buildroot%_sysconfdir/udev/rules.d/40-alterator-ports-access-serial.rules
touch %buildroot%_sysconfdir/udev/rules.d/99-alterator-ports-access-usbdevs.rules

#files -f %name.lang
%files
%_altdata_dir/applications/*
%_altdata_dir/ui/*/*
%_alterator_backend3dir/*
%_altdata_dir/help/*/*

%files cmdline
%_bindir/%name
%_bindir/%name-lib.sh
/lib/udev/alterator-ports-access
%config(noreplace) %_sysconfdir/alterator-ports-access.conf
%ghost %_sysconfdir/udev/rules.d/40-alterator-ports-access.rules
%ghost %_sysconfdir/udev/rules.d/40-alterator-ports-access-serial.rules
%ghost %_sysconfdir/udev/rules.d/99-alterator-ports-access-usbdevs.rules

%changelog
* Fri Dec 09 2022 Paul Wolneykien <manowar@altlinux.org> 0.5.3-alt1.1
- Fixes:
  + OVE-20221208-0002 Applying port access changes needs system restart.

* Thu Mar 17 2022 Paul Wolneykien <manowar@altlinux.org> 0.5.3-alt1
- Added -v option to turn on verbose mode.
- Fixed help info output (closes: 42142).

* Thu Mar 03 2022 Paul Wolneykien <manowar@altlinux.org> 0.5.2-alt1
- UI improved: Turn the widgets on and off according with a list
  entry selection.

* Thu Mar 03 2022 Paul Wolneykien <manowar@altlinux.org> 0.5.1-alt1
- Fix: Enable UART on all serial ports when control is disabled.

* Mon Feb 28 2022 Paul Wolneykien <manowar@altlinux.org> 0.5-alt1
- Update the captions and messages for better translation.
- Expand the main tables to full width.
- Specify the width of 100% for all inputs inside the tables.
- Include into the package the paths of the generated rule files
  as %%ghost files.
- Apply access mode options to block, input and other USB device
  nodes.
- Fix: Don't use bash for the unauthorized device access message.
- FIX: Run 'udevadm control -R' to update the rules before triggering
  them!
- Disable verbose mode for udevadm invocations.
- Allow to edit the USB device rules.
- Remove the rc.serial script: run 'setserial' from the serial udev
  rules (40-alterator-ports-access-serial.rules).
- Use alterator-service-functions to cotnrol udev and udisks2
  services.
- Allow to specify owner, group and access mode for serial and USB
  devices.

* Mon Jan 11 2021 Ivan Razzhivin <underwit@altlinux.org> 0.4-alt1
- enforce changes to udisks2 and udevd

* Mon Oct 26 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.3-alt2
- -x removed from alterator-ports-access script

* Mon Oct 26 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.3-alt1
- divided to subpackages to allow use without alterator
- packed configuration file

* Sun Feb 26 2017 Denis Medvedev <nbr@altlinux.org> 0.2-alt1
- Emits alarm to system log via systemd.

* Thu Dec 15 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.1-alt1
- sub-device interfaces support added

* Thu Oct 20 2016 Andrey Cherepanov <cas@altlinux.org> 0.0.3-alt9
- Do not show this html module in alterator-browser-qt (ALT #32626)

* Fri Oct 02 2015 Michael Shigorin <mike@altlinux.org> 0.0.3-alt8
- Translations moved to alterator-l10n as of 2.9-alt49

* Tue Sep 25 2012 Michael Shigorin <mike@altlinux.org> 0.0.3-alt7
- Add logging (serial port enabled/disabled) as requested

* Mon Sep 24 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.3-alt6
- Fix serial available ports list 2

* Mon Sep 24 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.3-alt5
- Fix serial available ports list

* Wed Sep 19 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.3-alt4
- Accepts bad words

* Wed Sep 19 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.3-alt3
- Add BuildRequires to alterator

* Wed Sep 19 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.3-alt2
- Fix spec, add rpm-macros-alterator

* Wed Sep 19 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.3-alt1
- Add serial field in known USB devices, add patch from ua2fgb.

* Fri Aug 31 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.2-alt1
- List devices, USB HID

* Tue Jul 31 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt1
- Initial build
