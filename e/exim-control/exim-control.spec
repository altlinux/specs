Name: exim-control
Version: 1.0
Release: alt1

Summary: Exim Mail Transport Agent facility control
License: GPL
Group: System/Servers
BuildArch: noarch

Source0: exim.control

%description
This package contains control rules for the Exim MTA facility.
See control(8) for details.

%install
install -pD -m755 %SOURCE0 $RPM_BUILD_ROOT%_controldir/exim

%files
%config %_controldir/*

%changelog
* Thu Jan 18 2007 Victor Forsyuk <force@altlinux.org> 1.0-alt1
- Initial build.
