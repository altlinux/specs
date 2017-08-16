Name: alterator-service-functions
Version: 3.0.0
Release: alt3

Packager: Paul Wolneykien <manowar@altlinux.ru>

BuildArch: noarch

Source: %name-%version.tar.gz

Summary: Helper functions for common service management
License: GPLv3
Group: System/Base

Conflicts: systemd < 1:234-alt3

%description
Helpers for common service management

%prep
%setup -q

%install
%makeinstall

%files
%_bindir/*

%changelog
* Wed Aug 16 2017 Paul Wolneykien <manowar@altlinux.org> 3.0.0-alt3
- Fixed typo in systemd version.

* Tue Aug 15 2017 Paul Wolneykien <manowar@altlinux.org> 3.0.0-alt2
- Added 'is_chrooted' function which tests if the program is executed
  inside a chroot.
- Updated README.

* Fri Aug 11 2017 Paul Wolneykien <manowar@altlinux.org> 3.0.0-alt1
- Systemd-first edition.
- Fixed chrooted operation (ALTERATOR_DESTDIR or process chroot).

* Thu Aug 10 2017 Paul Wolneykien <manowar@altlinux.org> 2.0.5-alt1
- Support installer mode (ALTERATOR_DESTDIR env. var.).

* Thu Aug 03 2017 Paul Wolneykien <manowar@altlinux.org> 2.0.4-alt1
- Enable and disable services in all available subsystems.
- Get rid of eval.

* Tue Apr 25 2017 Paul Wolneykien <manowar@altlinux.org> 2.0.3-alt2
- Fix: Do not call SysV by accident when 'systemctl' fails.

* Fri Jul 11 2014 Mikhail Efremov <sem@altlinux.org> 2.0.3-alt1
- sd_service_control: Fix condreload.

* Fri Jul 12 2013 Paul Wolneykien <manowar@altlinux.org> 2.0.2-alt1
- Use </dev/null with eval (safer for the message handler).
- Fix output redirection in debug mode.

* Mon Jun 03 2013 Mikhail Efremov <sem@altlinux.org> 2.0.1-alt1
- Don\'t use absolute paths for commands (closes: #28977).
- Use inittab if runlevel is unknown (closes: #28891).

* Thu Mar 21 2013 Paul Wolneykien <manowar@altlinux.org> 2.0.0-alt1
- Make service_control() support some combined status options
  (on/start, stop/off).
- sd_service_control: Handle condstop. (thx Mikhail Efremov).
- Implement systemd-related functions. (thx Mikhail Efremov).
- Rewrite service_control() and update related functions.
  (thx Mikhail Efremov).

* Sun Oct 31 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt5
- Add and use functions for service existance testing.

* Tue Oct 20 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt4
- Function to restart a service.

* Mon Oct 12 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt3
- Add function to reload a service.

* Thu Oct 08 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt2
- Wait for locked subsystem unlock prior to read service status.
- Remove garbage dependencies.

* Wed Oct 07 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt1
- Initial release
