%define _altdata_dir %_datadir/alterator

Name: alterator-bacula-client
Version: 0.3
Release: alt1

Packager: Alexandra Panyukova <mex3@altlinux.ru>

BuildArch: noarch

Source:%name-%version.tar

Summary: Alterator module for Bacula client configuration
License: GPL
Group: System/Configuration/Other

Conflicts: alterator-fbi < 2.8-alt1
Conflicts: alterator-lookout < 1.2-alt1
Requires: alterator >= 3.1-alt6
Requires: alterator-sh-functions >= 0.6-alt3

BuildPreReq: alterator >= 3.3-alt5

BuildRequires: alterator

Requires: bacula-client

%description
Alterator module for Bacula client configuration

%prep
%setup -q

%build
%make_build libdir=%_libdir

%install
%makeinstall

%files
%_altdata_dir/ui/*/
%_altdata_dir/applications/*
%_alterator_backend3dir/*

%changelog
* Mon Dec 16 2013 Andrey Kolotov <qwest@altlinux.org> 0.3-alt1
- client password not displayed

* Fri Sep 27 2013 Andrey Cherepanov <cas@altlinux.org> 0.2-alt2
- Do not condrestart Alterator services
- Fix summary and dectription
- Require bacula-client for work

* Fri Jun 28 2013 Andrey Kolotov <qwest@altlinux.org> 0.2-alt1
- add turn on/off File Daemon
- not require alterator-bacula-functions
- add auto condrestart file daemon

* Mon Feb 21 2010 Alexandra Panyukova <mex3@altlinux.ru> 0.1-alt1
- Initial release

