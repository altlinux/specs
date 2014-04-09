Name:		netinst-overlays
Version:	0.01
Release:	alt1
License:	BSD
Summary:	Managing ALT Linux netinst-style ISO patches
Group:		System/Configuration/Networking
BuildArch:	noarch
Source:		%name-%version.tar

%description
Set of server and client scripts for managing
ALT Linux netinst-style ISO patches.

%prep
%setup

%install
install -d %buildroot%_bindir
install overlays-* %buildroot%_bindir/

%files
%_bindir/*

%changelog
* Thu Mar 20 2014 Fr. Br. George <george@altlinux.ru> 0.01-alt1
- Initial build as RPM
