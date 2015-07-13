%define _altdata_dir %_datadir/alterator

Name: alterator-drweb
Version: 0.99.4
Release: alt1

Packager: Dmitriy Kruglikov <gkr@altlinux.org>

BuildArch: noarch

Source:%name-%version.tar.gz

Summary: Dr. Web antivirus system configuration and administration module
License: GPL
Group: System/Configuration/Other
Requires: alterator >= 4.8-alt1
Requires: alterator-fbi >= 5.11-alt2
Conflicts: alterator >= 5.0
Conflicts: alterator-fbi >= 6.0

# Automatically added by buildreq on Wed Apr 08 2009
BuildRequires: alterator rpm-macros-fillup

%description
Dr. WEB antivirus system configuration and administration module

%prep
%setup -q

%build
%make_build

%install
%makeinstall


%files
%_alterator_datadir/applications/*
%_alterator_datadir/ui/drweb/
%_alterator_backend3dir/drweb

%changelog
* Fri Sep 18 2015 Andrey Cherepanov <cas@altlinux.org> 0.99.4-alt1
- Drop empty help page.

* Mon Dec 15 2014 Mikhail Efremov <sem@altlinux.org> 0.99.3-alt1
- Workaround for drweb-qcontrol bug.

* Mon Nov 10 2014 Mikhail Efremov <sem@altlinux.org> 0.99.2-alt1
- Add support for Dr.Web(R) Samba VFS SpIDer.

* Wed Aug 06 2014 Mikhail Efremov <sem@altlinux.org> 0.99.1-alt1
- Don't require drweb-qcontrol and drwebdc.
- Don't require alterator-service-functions.

* Sun May 16 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.99-alt1
- Full functionality.

* Sun May 10 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.5-alt1
- Initial release.
