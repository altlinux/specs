Name: acpi
Version: 1.6
Release: alt1

Summary: Command-line ACPI Client
License: GPLv2+
Group: Monitoring

URL: http://sourceforge.net/projects/acpiclient/
Source: http://download.sourceforge.net/acpiclient/acpi-%version.tar.gz

%description
Attempts to replicate the functionality of the 'old' apm command on ACPI
systems, including battery and thermal information. Does not support ACPI
suspending, only displays information about ACPI devices.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*

%changelog
* Sun Jan 15 2012 Victor Forsiuk <force@altlinux.org> 1.6-alt1
- 1.6

* Mon Dec 20 2010 Victor Forsiuk <force@altlinux.org> 1.5-alt1
- 1.5
- Oops... author mistakenly transposed memset parameters. Fixed.

* Fri Jul 03 2009 Victor Forsyuk <force@altlinux.org> 1.4-alt1
- New version (forked/took over as upstream by Debian maintainer).
- Fixed floating point exception when voltage_now is 0.

* Thu Sep 27 2007 Victor Forsyuk <force@altlinux.org> 0.09-alt2
- Add better manpage.
- Remove translations from spec.

* Sat Sep 03 2005 Vitaly Lipatov <lav@altlinux.ru> 0.09-alt1.1
- NMU: fix bug #4945

* Fri Apr 15 2005 Victor Forsyuk <force@altlinux.ru> 0.09-alt1
- New version.
- Fix URL.
- Apply %%optflags.

* Tue Nov 11 2003 Egor S. Orlov <oes@altlinux.ru> 0.07-alt1
- New version 
- Added old man-file

* Tue Jul 08 2003 Egor S. Orlov <oes@altlinux.ru> 0.0.6-alt1
- Build for sisyphus 

* Tue Jul 08 2003 Egor S. Orlov <oes@altlinux.ru> 0.0.6-alt0.1
- Initial build for ALT
- clenaup spec acording to the policy

* Fri Mar 14 2003 Mike Gerber <mike@sprachgewalt.de> 0.0.6
- Initial spec file
