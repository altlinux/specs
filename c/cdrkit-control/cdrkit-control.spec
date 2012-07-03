Name: cdrkit-control
Version: 1.0
Release: alt1

Summary: Facilities control for CD/DVD media tools
License: GPL
Group: System/Servers
BuildArch: noarch

PreReq: control

Source: cdrkit.control

%description
This package contains control rules for CD/DVD media tools.
See control(8) for details.

%install
for n in readom wodim; do
	%__install -pD -m755 %SOURCE0 "%buildroot%_controldir/$n"
	%__subst -p "s/@NAME@/$n/" "%buildroot%_controldir/$n"
done

%files
%config %_controldir/*

%changelog
* Sun Feb 10 2008 Hihin Ruslan <ruslandh@altlinux.ru> 1.0-alt1
- Initial revision.


