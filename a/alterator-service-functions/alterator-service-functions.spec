Name: alterator-service-functions
Version: 1.0
Release: alt5

Packager: Paul Wolneykien <manowar@altlinux.ru>

BuildArch: noarch

Source: %name-%version.tar.gz

Summary: Helpers for common service management
License: GPLv3
Group: System/Base

%description
Helpers for common service management

%prep
%setup -q

%install
%makeinstall

%files
%_bindir/*

%changelog
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
