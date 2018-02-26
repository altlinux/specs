Name: appliance-base-admin-hn
Summary: Virtual package that require utilites for admins
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: System/Base

Obsoletes: appliance-base-admin < %version-%release

Requires: appliance-base-admin-common = %version-%release
Requires: appliance-base-admin-disk = %version-%release

%description
%summary

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

