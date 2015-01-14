%define _altdata_dir %_datadir/alterator

Name: alterator-net-bond
Version: 0.1.2
Release: alt1

Source:%name-%version.tar

Summary: alterator module for bonding interfaces
License: GPL
Group: System/Configuration/Other
Requires: alterator >= 4.24 libshell >= 0.0.1-alt4
Requires: alterator-l10n
Requires: alterator-sh-functions >= 0.12-alt1
Requires: alterator-hw-functions >= 0.7-alt2
Requires: alterator-net-functions >= 1.3.3
Requires: alterator-net-eth >= 4.20.0
Requires: etcnet

BuildPreReq: alterator >= 4.7-alt3

BuildArch: noarch

BuildRequires: alterator

%description
alterator module for bonding network interfaces

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%_altdata_dir/applications/*
%_altdata_dir/ui/*/
%_alterator_backend3dir/*

%changelog
* Wed Jan 14 2015 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1
- Prepend arp_ip_target value with '+' in the etcnet's config.

* Tue Jan 13 2015 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- build: Fix module name.

* Thu Dec 25 2014 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- Initial build.

