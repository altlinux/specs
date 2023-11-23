Name: LibreOffice-unmet-holder
Version: 7.6.3.1
Release: alt1

Summary: Empty LibreOffice dependency holder on platforms that don't have one
License: MPL-2.0
Group: Office
ExclusiveArch: armh

Provides: LibreOffice, LibreOffice-gnome, LibreOffice-langpack-ru, /usr/bin/libreoffice

%description
%summary. Usefull for arches that are not supported by LibreOffice, but there are packages that require it.

%files

%changelog
* Wed Nov 22 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 7.6.3.1-alt1
- New release 7.6.3.1

* Fri Sep 29 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 7.6.2.1-alt1
- Initial build for Sisyphus.
