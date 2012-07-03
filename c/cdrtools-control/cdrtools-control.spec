Name: cdrtools-control
Version: 1.1
Release: alt2

Summary: Facilities control for CD/DVD media tools
License: GPL
Group: System/Servers
BuildArch: noarch

PreReq: control
Conflicts: cdrecord < 5:2.01-alt1a37

Source: cdrtools.control

%description
This package contains control rules for CD/DVD media tools.
See control(8) for details.

%install
for n in cdrecord-classic dvdrecord readcd rscsi; do
	%__install -pD -m755 %SOURCE0 "$RPM_BUILD_ROOT%_controldir/$n"
	%__subst -p "s/@NAME@/$n/" "$RPM_BUILD_ROOT%_controldir/$n"
done
# rscsi lives in sbin
%__perl -pi -e "s/\/bin(?=\/rscsi)/\/sbin/" "$RPM_BUILD_ROOT%_controldir/rscsi"

%files
%config %_controldir/*

%changelog
* Sat Jan 07 2006 LAKostis <lakostis at altlinux.ru> 1.1-alt2
- Added dvdrecord and renamed cdrecord->cdrecord-classic.

* Mon Dec 13 2004 LAKostis <lakostis at altlinux.ru> 1.1-alt1.1
- Added rscsi control.

* Sat Oct 02 2004 Dmitry V. Levin <ldv@altlinux.org> 1.1-alt1
- Added help.

* Tue Aug 24 2004 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt1
- Initial revision.
