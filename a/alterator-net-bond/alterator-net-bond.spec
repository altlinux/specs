Name: alterator-net-bond
Version: 1.1.0
Release: alt1.1.1

Source:%name-%version.tar

Summary: alterator module for bonding interfaces
License: GPL
Group: System/Configuration/Other
Requires: alterator >= 5.0 libshell >= 0.0.1-alt4
Requires: alterator-l10n
Requires: alterator-sh-functions >= 0.12-alt1
Requires: alterator-net-functions >= 2.0.0
Requires: alterator-net-eth >= 5.0.0
Requires: etcnet

BuildPreReq: alterator >= 5.0
BuildRequires: alterator-fbi

%ifarch %e2k
BuildRequires: guile20-devel libguile20-devel
%else
BuildRequires: guile22-devel
%endif

%define _unpackaged_files_terminate_build 1

%description
alterator module for bonding network interfaces

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%_alterator_datadir/applications/*
%_alterator_datadir/ui/*/
%_alterator_libdir/ui/*
%_alterator_backend3dir/*

%changelog
* Fri Apr 13 2018 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1.1.1
- NMU: Replace BuildRequires for guile on e2k arch.

* Tue Apr 18 2017 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1
- Changes for guile22.
- Add Qt UI.

* Wed Mar 23 2016 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Use functions from new alterator-net-functions.

* Wed Jan 14 2015 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1
- Prepend arp_ip_target value with '+' in the etcnet's config.

* Tue Jan 13 2015 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- build: Fix module name.

* Thu Dec 25 2014 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- Initial build.

