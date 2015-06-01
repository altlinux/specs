Name: livecd-admin-cups
Version: 0.1
Release: alt1

Summary: allow user to configure local CUPS print server
License: Public domain
Group: System/Configuration/Printing

BuildArch: noarch
AutoReqProv: no
Requires: cups

%description
%summary
(there are some LiveCD use cases when root access
shouldn't be readily available but printing should).

%prep

%post
sed -i 's,Require user @SYSTEM,#&,' /etc/cups/cupsd.conf ||:

%files

%changelog
* Fri Apr 17 2015 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

