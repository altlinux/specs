Name: cdrtools-control
Version: 1.1
Release: alt4

Summary: Facilities control for CD/DVD media tools
License: GPL
Group: System/Servers
BuildArch: noarch

Requires(pre): control
Conflicts: cdrecord < 5:2.01-alt1a37

Source: cdrtools.control

%description
This package contains control rules for CD/DVD media tools.
See control(8) for details.

%package -n rscsi-control
Summary: Facilities control for rscsi protocol
Group: System/Servers
Requires: cdrtools-control > 1.1-alt2, rscsi
Conflicts: cdrtools-control <= 1.1-alt2

%description -n rscsi-control
This package contains control rules for rscsi protocol.
See control(8) for details.

%package -n readcd-control
Summary: Facilities control for readcd
Group: System/Servers
Requires: cdrtools-control > 1.1-alt2, readcd
Conflicts: cdrtools-control <= 1.1-alt2

%description -n readcd-control
This package contains control rules for readcd.
See control(8) for details.

%install
for n in cdrecord-classic readcd-classic rscsi; do
	install -pD -m755 %SOURCE0 "$RPM_BUILD_ROOT%_controldir/$n"
	subst -p "s/@NAME@/$n/" "$RPM_BUILD_ROOT%_controldir/$n"
done
# rscsi lives in sbin
perl -pi -e "s/\/bin(?=\/rscsi)/\/sbin/" "$RPM_BUILD_ROOT%_controldir/rscsi"

%files
%config %_controldir/*
%exclude %_controldir/rscsi
%exclude %_controldir/readcd-classic

%files -n rscsi-control
%config %_controldir/rscsi

%files -n readcd-control
%config %_controldir/readcd-classic

%changelog
* Wed Oct 02 2024 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt4
- Remove dvdrecord-control (superseded by cdrecord-classic).

* Thu Mar 12 2009 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt3
- split to many *-control cause they depends on separate packages.

* Sat Jan 07 2006 LAKostis <lakostis at altlinux.ru> 1.1-alt2
- Added dvdrecord and renamed cdrecord->cdrecord-classic.

* Mon Dec 13 2004 LAKostis <lakostis at altlinux.ru> 1.1-alt1.1
- Added rscsi control.

* Sat Oct 02 2004 Dmitry V. Levin <ldv@altlinux.org> 1.1-alt1
- Added help.

* Tue Aug 24 2004 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt1
- Initial revision.
