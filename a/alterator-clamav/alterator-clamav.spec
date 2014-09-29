%define _altdata_dir %_datadir/alterator

Name: alterator-clamav
Version: 1.1.1
Release: alt1

Packager:  Dmitriy Kruglikov <dkr@altlinux.ru>

BuildArch: noarch

Source:%name-%version.tar.gz

Summary: Clamav antivirus system configuration module
License: GPL
Group: System/Configuration/Other
Requires: alterator >= 4.8-alt1
Requires: alterator-fbi >= 5.11-alt2
Requires: clamav >= 0.95.3
Conflicts: alterator >= 5.0
Conflicts: alterator-fbi >= 6.0
Conflicts: clamav >= 1.0.0

# Automatically added by buildreq on Wed Apr 08 2009
BuildRequires: alterator rpm-macros-fillup

%description
Clamav antivirus system configuration module

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_alterator_datadir/applications/*
%_alterator_datadir/ui/clamav
%_alterator_backend3dir/clamav


%changelog
* Mon Sep 29 2014 Mikhail Efremov <sem@altlinux.org> 1.1.1-alt1
-  Fix services start/stop (by "Valery V. Inozemtsev").

* Mon Aug 25 2014 Mikhail Efremov <sem@altlinux.org> 1.1-alt2
- Drop alterator-service-functions from conflicts/requires.

* Tue May 25 2010 Dmitriy Kruglikov <dkr@altlinux.ru> 1.1-alt1
- Released.

* Tue Apr 27 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt1
- Initial release.
