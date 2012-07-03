Name: alterator-bacula-functions
Version: 0.2
Release: alt1

Packager: Alexandra Panyukova <mex3@altlinux.ru>

Source:%name-%version.tar

%add_findreq_skiplist %_libexecdir/alterator/backend3/bacula-restore

%define backupadmin_group backupadmin

Summary: helper functions for alterator Bacula backup system
License: GPL
Group: System/Configuration/Other
Requires(pre): shadow-utils
# require console timeout feature
Requires: alterator >= 4.10-alt5
Requires: alterator-sh-functions alterator-net-functions alterator-hw-functions >= 0.6-alt1
Conflicts: alterator-lookout < 2.1-alt1
Conflicts: alterator-fbi < 5.20-alt1
Conflicts: alterator-bacula < 0.7-alt14

BuildArch: noarch

BuildPreReq: alterator >= 4.10-alt5

%description
helper functions for alterator Bacula backup system

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_bindir/*

%changelog
* Mon Apr 18 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- try /dev/mapper/device after /dev/device while probing

* Wed Mar 09 2011 Alexandra Panyukova <mex3@altlinux.ru> 0.1-alt1
- separation functions from modules
